#!/usr/bin/env python3
"""Decision-analysis helpers for the TOPY AI CEO Core skill.

This module keeps the quantitative utilities dependency-free and reusable from
agent runtimes that can execute Python.
"""

from __future__ import annotations

import argparse
import json
import math
import random
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence

DEFAULT_SIMULATIONS = 10_000


class ValidationError(ValueError):
    """Raised when a payload is structurally invalid."""


def _require_non_empty(items: Sequence, label: str) -> None:
    if not items:
        raise ValidationError(f"{label} must not be empty")


def _quantile(sorted_values: Sequence[float], q: float) -> float:
    if not sorted_values:
        raise ValidationError("cannot compute a quantile of empty data")
    if q <= 0:
        return float(sorted_values[0])
    if q >= 1:
        return float(sorted_values[-1])

    position = (len(sorted_values) - 1) * q
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return float(sorted_values[lower])

    weight = position - lower
    return float(sorted_values[lower] * (1 - weight) + sorted_values[upper] * weight)


def _load_payload(raw_json: str | None, file_path: str | None):
    if raw_json and file_path:
        raise ValidationError("use either --json or --file, not both")
    if raw_json:
        return json.loads(raw_json)
    if file_path:
        return json.loads(Path(file_path).read_text(encoding="utf-8"))
    raise ValidationError("either --json or --file is required")


def _normalize_probability(value: float) -> float:
    probability = float(value)
    if not 0 < probability < 1:
        raise ValidationError("probability must be between 0 and 1")
    return probability


@dataclass(frozen=True)
class Evidence:
    description: str
    quality_grade: str
    likelihood_ratio: float
    supports: bool


@dataclass(frozen=True)
class BayesianUpdate:
    prior_probability: float
    posterior_probability: float
    prior_odds: float
    posterior_odds: float
    evidence_count: int
    combined_lr: float
    confidence_change: str


def probability_to_odds(probability: float) -> float:
    probability = _normalize_probability(probability)
    return probability / (1 - probability)


def odds_to_probability(odds: float) -> float:
    odds = float(odds)
    if odds < 0:
        raise ValidationError("odds must be non-negative")
    return odds / (1 + odds)


def bayesian_update(
    prior_probability: float,
    evidence_list: Sequence[Evidence],
    *,
    dependency_discount: float = 1.0,
) -> BayesianUpdate:
    prior_probability = _normalize_probability(prior_probability)
    if not 0 < dependency_discount <= 1:
        raise ValidationError("dependency_discount must be between 0 and 1")

    prior_odds = probability_to_odds(prior_probability)
    combined_lr = 1.0
    for evidence in evidence_list:
        adjusted_lr = 1 + (float(evidence.likelihood_ratio) - 1) * dependency_discount
        combined_lr *= adjusted_lr

    posterior_odds = prior_odds * combined_lr
    posterior_probability = odds_to_probability(posterior_odds)

    if posterior_probability > prior_probability + 0.05:
        confidence_change = "Increased"
    elif posterior_probability < prior_probability - 0.05:
        confidence_change = "Decreased"
    else:
        confidence_change = "Stable"

    return BayesianUpdate(
        prior_probability=prior_probability,
        posterior_probability=posterior_probability,
        prior_odds=prior_odds,
        posterior_odds=posterior_odds,
        evidence_count=len(evidence_list),
        combined_lr=combined_lr,
        confidence_change=confidence_change,
    )


def beta_binomial_update(
    prior_alpha: float,
    prior_beta: float,
    successes: int,
    trials: int,
) -> tuple[float, float, float]:
    if trials < 0 or successes < 0 or successes > trials:
        raise ValidationError("invalid trial data")

    posterior_alpha = float(prior_alpha) + successes
    posterior_beta = float(prior_beta) + (trials - successes)
    posterior_mean = posterior_alpha / (posterior_alpha + posterior_beta)
    return posterior_mean, posterior_alpha, posterior_beta


def sensitivity_analysis(
    base_prior: float,
    evidence_list: Sequence[Evidence],
    *,
    prior_range: float = 0.1,
    lr_multiplier_range: tuple[float, float] = (0.5, 2.0),
) -> dict:
    if not 0 < prior_range < 1:
        raise ValidationError("prior_range must be between 0 and 1")
    low_multiplier, high_multiplier = lr_multiplier_range
    if not 0 < low_multiplier <= high_multiplier:
        raise ValidationError("invalid lr_multiplier_range")

    base_result = bayesian_update(base_prior, evidence_list)
    best_prior = min(base_prior + prior_range, 0.99)
    worst_prior = max(base_prior - prior_range, 0.01)

    best_evidence = [
        Evidence(e.description, e.quality_grade, e.likelihood_ratio * high_multiplier, e.supports)
        for e in evidence_list
    ]
    worst_evidence = [
        Evidence(e.description, e.quality_grade, e.likelihood_ratio * low_multiplier, e.supports)
        for e in evidence_list
    ]

    best_result = bayesian_update(best_prior, best_evidence)
    worst_result = bayesian_update(worst_prior, worst_evidence)

    return {
        "best_case": best_result.posterior_probability,
        "base_case": base_result.posterior_probability,
        "worst_case": worst_result.posterior_probability,
        "range": best_result.posterior_probability - worst_result.posterior_probability,
        "robust": (best_result.posterior_probability - worst_result.posterior_probability) < 0.2,
    }


def expected_value(probability_success: float, value_if_success: float, cost_if_failure: float) -> dict:
    probability_success = _normalize_probability(probability_success)
    probability_failure = 1 - probability_success
    ev = (probability_success * float(value_if_success)) - (
        probability_failure * float(cost_if_failure)
    )

    if float(value_if_success) + float(cost_if_failure) > 0:
        breakeven = float(cost_if_failure) / (float(value_if_success) + float(cost_if_failure))
    else:
        breakeven = None

    return {
        "expected_value": ev,
        "ev_success": probability_success * float(value_if_success),
        "ev_failure": probability_failure * float(cost_if_failure),
        "recommendation": "Go" if ev > 0 else "No-Go",
        "breakeven_probability": breakeven,
        "margin": probability_success - breakeven if breakeven is not None else None,
    }


def decision_matrix(criteria: Sequence[dict], options: Sequence[dict]) -> list[dict]:
    _require_non_empty(criteria, "criteria")
    _require_non_empty(options, "options")

    total_weight = sum(float(criterion["weight"]) for criterion in criteria)
    if not math.isclose(total_weight, 1.0, rel_tol=1e-9, abs_tol=1e-9):
        raise ValidationError(f"criteria weights must sum to 1.0, got {total_weight:.6f}")

    results = []
    for option in options:
        total_score = 0.0
        breakdown = {}
        for criterion in criteria:
            criterion_name = criterion["name"]
            score = float(option["scores"].get(criterion_name, 5))
            weighted = score * float(criterion["weight"])
            breakdown[criterion_name] = {"raw": score, "weighted": round(weighted, 4)}
            total_score += weighted
        results.append(
            {
                "option": option["name"],
                "total_score": round(total_score, 4),
                "breakdown": breakdown,
            }
        )

    return sorted(results, key=lambda item: item["total_score"], reverse=True)


def ice_scoring(initiatives: Sequence[dict]) -> list[dict]:
    _require_non_empty(initiatives, "initiatives")

    results = []
    for item in initiatives:
        impact = float(item["impact"])
        confidence = float(item["confidence"])
        ease = float(item["ease"])
        results.append(
            {
                "name": item["name"],
                "impact": impact,
                "confidence": confidence,
                "ease": ease,
                "ice_score": round(impact * confidence * ease, 4),
            }
        )

    return sorted(results, key=lambda item: item["ice_score"], reverse=True)


def monte_carlo_simulation(
    scenarios: Sequence[dict],
    num_simulations: int = DEFAULT_SIMULATIONS,
    *,
    seed: int | None = None,
) -> dict:
    _require_non_empty(scenarios, "scenarios")
    if num_simulations <= 0:
        raise ValidationError("num_simulations must be > 0")

    rng = random.Random(seed)
    total_probability = 0.0
    normalized_scenarios = []
    for scenario in scenarios:
        probability = float(scenario["probability"])
        outcome_range = scenario["outcome_range"]
        if len(outcome_range) != 2:
            raise ValidationError("outcome_range must contain exactly two values")
        low, high = float(outcome_range[0]), float(outcome_range[1])
        if probability <= 0:
            raise ValidationError("scenario probability must be > 0")
        if low > high:
            raise ValidationError("outcome_range min must be <= max")
        total_probability += probability
        normalized_scenarios.append(
            {
                "name": scenario["name"],
                "probability": probability,
                "outcome_range": (low, high),
            }
        )

    if not math.isclose(total_probability, 1.0, rel_tol=1e-9, abs_tol=1e-9):
        raise ValidationError(
            f"scenario probabilities must sum to 1.0, got {total_probability:.6f}"
        )

    cumulative = []
    running = 0.0
    for scenario in normalized_scenarios:
        running += scenario["probability"]
        cumulative.append((running, scenario))

    results: list[float] = []
    for _ in range(num_simulations):
        pick = rng.random()
        chosen = cumulative[-1][1]
        for threshold, candidate in cumulative:
            if pick <= threshold:
                chosen = candidate
                break
        low, high = chosen["outcome_range"]
        results.append(rng.uniform(low, high))

    results.sort()
    count = len(results)
    return {
        "num_simulations": count,
        "mean": round(sum(results) / count, 4),
        "median": round(_quantile(results, 0.5), 4),
        "p5": round(_quantile(results, 0.05), 4),
        "p25": round(_quantile(results, 0.25), 4),
        "p75": round(_quantile(results, 0.75), 4),
        "p95": round(_quantile(results, 0.95), 4),
        "min": round(results[0], 4),
        "max": round(results[-1], 4),
        "probability_of_loss": round(sum(1 for value in results if value < 0) / count, 4),
    }


def npv(cash_flows: Iterable[float], discount_rate: float) -> float:
    cash_flows = [float(cash_flow) for cash_flow in cash_flows]
    _require_non_empty(cash_flows, "cash_flows")
    if discount_rate <= -1:
        raise ValidationError("discount_rate must be greater than -1")
    return round(
        sum(cash_flow / (1 + discount_rate) ** period for period, cash_flow in enumerate(cash_flows)),
        4,
    )


def irr(cash_flows: Iterable[float], precision: float = 0.0001, max_iterations: int = 1000) -> float:
    cash_flows = [float(cash_flow) for cash_flow in cash_flows]
    _require_non_empty(cash_flows, "cash_flows")
    if precision <= 0:
        raise ValidationError("precision must be > 0")
    if not any(value < 0 for value in cash_flows) or not any(value > 0 for value in cash_flows):
        raise ValidationError("cash_flows must include at least one negative and one positive value")

    def _npv(rate: float) -> float:
        return sum(cash_flow / (1 + rate) ** period for period, cash_flow in enumerate(cash_flows))

    low, high = -0.9999, 10.0
    low_npv = _npv(low)
    high_npv = _npv(high)
    if low_npv == 0:
        return round(low, 4)
    if high_npv == 0:
        return round(high, 4)
    if low_npv * high_npv > 0:
        raise ValidationError("IRR not bracketed in search interval")

    mid = 0.0
    for _ in range(max_iterations):
        mid = (low + high) / 2
        mid_npv = _npv(mid)
        if abs(mid_npv) < precision:
            return round(mid, 4)
        if low_npv * mid_npv <= 0:
            high = mid
            high_npv = mid_npv
        else:
            low = mid
            low_npv = mid_npv

    return round(mid, 4)


def format_bayesian_report(
    hypothesis: str,
    prior_probability: float,
    prior_source: str,
    evidence_list: Sequence[Evidence],
    *,
    value_if_success: float | None = None,
    cost_if_failure: float | None = None,
) -> str:
    update = bayesian_update(prior_probability, evidence_list)
    sensitivity = sensitivity_analysis(prior_probability, evidence_list)

    report = [
        f"## Bayesian Decision Analysis: {hypothesis}",
        "",
        "### Hypothesis",
        hypothesis,
        "",
        "### Prior Belief",
        f"- **Probability:** {prior_probability:.1%}",
        f"- **Source:** {prior_source}",
        f"- **Prior Odds:** {update.prior_odds:.2f}:1",
        "",
        "### Evidence Summary",
    ]

    for index, evidence in enumerate(evidence_list, 1):
        direction = "Supports" if evidence.supports else "Contradicts"
        report.extend(
            [
                f"{index}. **{evidence.description}**",
                f"   - Quality Grade: {evidence.quality_grade}",
                f"   - Likelihood Ratio: {evidence.likelihood_ratio:.2f}",
                f"   - Direction: {direction}",
                "",
            ]
        )

    report.extend(
        [
            "### Updated Belief",
            f"- **Prior:** {update.prior_probability:.1%} → **Posterior:** {update.posterior_probability:.1%}",
            f"- **Posterior Odds:** {update.posterior_odds:.2f}:1",
            f"- **Combined LR:** {update.combined_lr:.2f}",
            f"- **Confidence Change:** {update.confidence_change}",
            "",
            "### Sensitivity Analysis",
            f"- **Best Case:** {sensitivity['best_case']:.1%}",
            f"- **Base Case:** {sensitivity['base_case']:.1%}",
            f"- **Worst Case:** {sensitivity['worst_case']:.1%}",
            f"- **Range:** {sensitivity['range']:.1%}",
            f"- **Decision Robust?** {'Yes' if sensitivity['robust'] else 'No - gather more evidence'}",
        ]
    )

    if value_if_success is not None and cost_if_failure is not None:
        ev_result = expected_value(update.posterior_probability, value_if_success, cost_if_failure)
        report.extend(
            [
                "",
                "### Expected Value Analysis",
                f"- **EV(Go):** ${ev_result['expected_value']:,.0f}",
                f"- **EV if Success:** ${ev_result['ev_success']:,.0f}",
                f"- **EV if Failure:** -${ev_result['ev_failure']:,.0f}",
                f"- **Break-even Probability:** {ev_result['breakeven_probability']:.1%}",
                f"- **Margin:** {ev_result['margin']:.1%}",
                f"- **Recommendation:** {ev_result['recommendation']}",
            ]
        )

    return "\n".join(report)


def _evidence_from_payload(payload: Sequence[dict]) -> list[Evidence]:
    return [
        Evidence(
            description=item["description"],
            quality_grade=item.get("quality_grade", "C"),
            likelihood_ratio=float(item["likelihood_ratio"]),
            supports=bool(item.get("supports", True)),
        )
        for item in payload
    ]


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Decision-analysis helpers for CEO reasoning")
    subparsers = parser.add_subparsers(dest="command", required=False)

    matrix = subparsers.add_parser("matrix", help="Run a weighted decision matrix")
    matrix.add_argument("--json")
    matrix.add_argument("--file")

    ice = subparsers.add_parser("ice", help="Run ICE scoring")
    ice.add_argument("--json")
    ice.add_argument("--file")

    ev = subparsers.add_parser("ev", help="Run expected value analysis")
    ev.add_argument("--json")
    ev.add_argument("--file")

    monte = subparsers.add_parser("monte-carlo", help="Run a Monte Carlo simulation")
    monte.add_argument("--json")
    monte.add_argument("--file")
    monte.add_argument("--simulations", type=int, default=DEFAULT_SIMULATIONS)
    monte.add_argument("--seed", type=int)

    npv_parser = subparsers.add_parser("npv", help="Calculate NPV")
    npv_parser.add_argument("--json")
    npv_parser.add_argument("--file")
    npv_parser.add_argument("--rate", required=True, type=float)

    irr_parser = subparsers.add_parser("irr", help="Calculate IRR")
    irr_parser.add_argument("--json")
    irr_parser.add_argument("--file")
    irr_parser.add_argument("--precision", type=float, default=0.0001)
    irr_parser.add_argument("--max-iterations", type=int, default=1000)

    bayes = subparsers.add_parser("bayes", help="Run Bayesian update and report")
    bayes.add_argument("--json")
    bayes.add_argument("--file")

    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    if not args.command:
        parser.print_help()
        return 0

    try:
        payload = _load_payload(getattr(args, "json", None), getattr(args, "file", None))

        if args.command == "matrix":
            result = decision_matrix(payload["criteria"], payload["options"])
        elif args.command == "ice":
            result = ice_scoring(payload)
        elif args.command == "ev":
            result = expected_value(payload["probability_success"], payload["value_if_success"], payload["cost_if_failure"])
        elif args.command == "monte-carlo":
            result = monte_carlo_simulation(payload, num_simulations=args.simulations, seed=args.seed)
        elif args.command == "npv":
            result = {"npv": npv(payload, args.rate)}
        elif args.command == "irr":
            result = {"irr": irr(payload, precision=args.precision, max_iterations=args.max_iterations)}
        elif args.command == "bayes":
            evidence = _evidence_from_payload(payload["evidence"])
            result = {
                "prior_probability": float(payload["prior_probability"]),
                "posterior_probability": bayesian_update(
                    float(payload["prior_probability"]),
                    evidence,
                    dependency_discount=float(payload.get("dependency_discount", 1.0)),
                ).posterior_probability,
                "report": format_bayesian_report(
                    payload["hypothesis"],
                    float(payload["prior_probability"]),
                    payload.get("prior_source", "unspecified"),
                    evidence,
                    value_if_success=payload.get("value_if_success"),
                    cost_if_failure=payload.get("cost_if_failure"),
                ),
            }
        else:
            parser.error(f"unknown command: {args.command}")
            return 2
    except (ValidationError, KeyError, json.JSONDecodeError, OSError, TypeError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
