---
name: topy-growth-experiments
description: 'Run growth experiments end to end in TOPY: a falsifiable hypothesis tied to a KPI and a journey stage, target fixed before launch, one owner, an honest read-out recorded as a KPI value, and a ship, kill or iterate call. Use when the user says things like "let''s test a referral offer"; "set up an experiment for the new onboarding email"; "which experiments are running?"; "the pricing test finished, what do we do?"; "is the experiment working yet?"; "what have our experiments taught us?". Needs the TOPY MCP server.'
license: MIT
metadata:
  category: core
  tier: core
  version: 0.2.0
  docs: https://github.com/TOPY-AI-LTD/TOPY-AI-CEO-Skills/blob/main/plugins/topy-ai/skills/topy-growth-experiments/SKILL.md
---
# Growth experiments

Most startup "experiments" are launches with a hopeful look at a dashboard afterwards. This skill makes each one a real test: the hypothesis, metric, target and duration are written into TOPY before anything starts, one person owns it, and the read-out compares the result with what was promised, not with what looks good on the day. Every test is tied to a KPI (and, where journeys exist, to the stage of the customer journey it targets), its result is recorded on that KPI, and every test ends in a decision whose lesson stays on record.

## When to use
- The founder has a growth idea to try, or wants to plan a batch of tests.
- An experiment reached its end date or sample size.
- A check on what is running and what was learned.
- Not for: the overall channel strategy (`topy-gtm-plan`); a pricing decision without a test (`topy-pricing-decisions`).

## Before you start
- Know the project (`projects_list`; can be left out with one project).
- `growth_experiments_list` first: avoid re-running a test that already failed, and avoid two tests on the same audience at once.
- `kpis_list`: the KPI the test should move (an input metric or a KR). No KPI yet → create it first with `topy-kpi-dashboard`; a test with no KPI cannot be read.
- `journeys_list`: if journeys exist, the stage the test targets (e.g. "Trial → first value"). Prefer the stage with the biggest drop.
- `owner_user_id` takes a TOPY user id (`account_get` → `id`); a non-user owner goes in `success_criteria.owner_name`.
- If TOPY tools are missing, run `topy-connect`.

## Workflow

### 1. Write the hypothesis
`hypothesis` (required): "If we [change] for [audience], then [metric] will [move by X], because [reason]." If it cannot be wrong, it is not a hypothesis. Set `channel` (e.g. `email`, `seo`, `paid_social`, `referral`, `product`) and `experiment_type` (`a_b`, `before_after`, `fake_door`, `pilot`).

### 2. Fix the success criteria before launch
Put them in `success_criteria`, all set before `started_at`:
`{"metric": "trial-to-paid rate", "kpi_key": "custom.trial_to_paid", "baseline": 0.08, "target": 0.10, "minimum_sample": 400, "duration_days": 21, "guardrail": "refund rate stays under 3%", "decision_rule": "ship if target met at full sample; iterate if between baseline and target; kill if at or below baseline"}`.
- Link it in `metadata_json`: `{"kpi_id": "<id>", "journey_id": "<id>", "journey_stage": "Trial", "objective_id": "<id if it serves a KR>"}`.
- Baseline from the KPI's recorded values or the founder's real data; if unknown, the first step is measuring it.
- Duration: at least one full business cycle (usually 2 weeks) so weekdays and weekends both count.
- Sample: if the founder cannot reach the minimum sample within 6 weeks, test something bigger or use a qualitative pilot instead.

### 3. Prioritise (when planning several)
Score each idea 1-10 on impact, confidence and ease (ICE), favour tests on KPIs of at-risk objectives and the worst journey stage, run the top ones (rarely more than 3-5 at once), and never more than the founder can watch. One owner per experiment.

### 4. Save and start
Preview `growth_experiment_create` (`status` defaults to `planned`), show it, confirm with `confirm: true` and the `confirmation` only after the founder agrees. When it launches, preview `growth_experiment_update` with `status: "running"` and `started_at`. A scheduled agent's key with a standing permission may add experiments without a preview up to its daily cap; it can never start, update or close one.

### 5. While it runs: avoid peeking bias
- Do not call a winner before `duration_days` and `minimum_sample` are both reached. Early leads often vanish.
- The only reason to stop early is a guardrail breach (refunds, complaints, a broken flow). Record it.
- If asked "is it working yet?", give the current numbers with the remaining days and say no call is possible yet.

### 6. Read out and decide
1. Read the record with `growth_experiment_get` to get the pre-set `success_criteria`. Ask for the observed numbers; store them in `result_data`, e.g. `{"observed": 0.094, "sample": 431, "guardrail_ok": true, "decision": "iterate"}`.
2. Apply the pre-set `decision_rule`, not a new one:

| Result | Decision | Next |
|---|---|---|
| Target met at full sample, guardrail held | `ship` | roll out; log it with `decision_create` if it changes how the business runs |
| Between baseline and target | `iterate` | one change, new experiment record |
| At or below baseline, or guardrail broken | `kill` | write down why; do not quietly re-run |
| Sample not reached | `inconclusive` | extend once or stop; do not round up |

3. Record the result on the KPI: preview `kpi_value_record` with `period_date` (the test's end date), `actual_value` (the observed value), `note` ("experiment <title>"), `metadata_json.source` (`ga4`, `stripe`… or `founder` when they reported it) and `evidence_ref` (the experiment id). If the KPI already has a value for that period from its own source, say so rather than overwrite it.
4. `result_summary`: two or three sentences with the lesson. Preview `growth_experiment_update` with `status: "completed"`, `ended_at`, `result_data`, `result_summary`; confirm on a yes.
5. Killed and inconclusive tests stay on record with the lesson; do not delete them.

## Output
- New test: hypothesis, success criteria table, owner, start and end dates.
- Review: `Experiment | KPI | Journey stage | Status | Baseline → Target | Observed (source) | Decision | Lesson`.

## Example
Founder of Fernhollow Fitness (a fictional online yoga studio): "Test a 'bring a friend free' week."
- `growth_experiments_list` shows a referral discount test killed in June ("discount drew one-off sign-ups").
- Hypothesis: "If members can invite one friend for a free week, new paid members from referrals will rise from 12 to 20 a month, because a friend is a stronger reason than a discount." Metric: paid members from referrals; 28 days; guardrail: member churn unchanged.
- Created after a yes, started on 1 Nov. On day 9 the founder sees 11 sign-ups and asks if it worked: the agent says 19 days remain and no call is possible yet. At day 28: 17 paid referrals → `iterate` (add a reminder email), recorded and confirmed.

## Quality bar
- [ ] Hypothesis is falsifiable and names audience, change, metric and reason.
- [ ] Metric, baseline, target, sample, duration and decision rule written before `started_at`.
- [ ] One owner; linked to a KPI (and a journey stage where journeys exist).
- [ ] The observed result is recorded on the KPI with a source.
- [ ] Decision follows the pre-set rule; no target moved after the fact.
- [ ] Lesson written for every finished test, including kills.
- [ ] Every write was previewed and confirmed only after a yes.

## Guardrails
- Changes in TOPY take two calls: a preview first, shown to the user, then `confirm: true` with the `confirmation` only after they agree. Never confirm for the user.
- Never invent baselines, results or sample sizes; if the founder has no number, say the test cannot be read yet. KPI values always carry a `source` (`founder` when they said it).
- Never change `success_criteria` after launch; if the test was badly designed, end it and start a new record.
- Tests on customers must respect consent and the law (no dark patterns, honest pricing, email consent). Say when a lawyer should look.

## Related skills
- `topy-decision-log` — log ship decisions that change the business.
- `topy-gtm-plan` — the channels these tests feed.
- `topy-kpi-dashboard` — the KPIs the tests move.
- `topy-user-journey` — the stage with the biggest drop.
- `topy-pricing-decisions` — pricing tests and their decision.
- `topy-daily` — flags experiments needing a call.
