# Quantitative Tools

Use this reference when the decision needs a calculation rather than a paragraph.

## Available helper functions

- `decision_matrix(criteria, options)`
- `ice_scoring(initiatives)`
- `expected_value(probability_success, value_if_success, cost_if_failure)`
- `monte_carlo_simulation(scenarios, num_simulations, seed)`
- `npv(cash_flows, discount_rate)`
- `irr(cash_flows, precision, max_iterations)`
- `bayesian_update(prior_probability, evidence_list, dependency_discount)`
- `sensitivity_analysis(base_prior, evidence_list, prior_range, lr_multiplier_range)`
- `beta_binomial_update(prior_alpha, prior_beta, successes, trials)`
- `format_bayesian_report(...)`

## When to use which

### Decision matrix

Use when:

- you have a small number of strategic options
- criteria are known in advance
- you need transparent weighting

Inputs:

- criteria list with weights summing to 1.0
- options with score maps

Watch out for:

- bad weights
- too many criteria
- scores that are just disguised preference

### ICE scoring

Use when:

- the problem is a queue or backlog
- you need a quick first ranking
- you can refine later

Watch out for:

- overfitting the confidence score
- ignoring dependencies
- treating a backlog rank as a final strategy

### Expected value

Use when:

- outcomes are discrete and probabilistic
- upside and downside can be priced or approximated

Watch out for:

- missing tail risk
- mixing revenue with profit
- pretending probabilities are more certain than they are

### Monte Carlo

Use when:

- the spread of outcomes matters
- a single EV number hides too much
- you need a distribution rather than a point estimate

Inputs:

- scenarios
- scenario probabilities that sum to 1.0
- outcome ranges for each scenario

Watch out for:

- invalid probability totals
- unrealistic ranges
- false confidence from too few simulations

### NPV and IRR

Use when:

- you are comparing capital uses
- the timing of cash flows matters
- you need to compare alternatives on a time-adjusted basis

Watch out for:

- ignoring the discount rate assumption
- using IRR when the cash flow pattern is ambiguous
- letting a big return hide an ugly downside

### Bayesian update

Use when:

- new evidence arrives over time
- you want to combine multiple clues into one updated belief
- the decision is naturally probabilistic

Watch out for:

- correlated evidence
- fake precision
- forgetting the prior

### Beta-binomial update

Use when:

- the data is success/failure over repeated trials
- you want a simple posterior mean and updated parameters

## Typical input shapes

### Decision matrix

```json
{
  "criteria": [{"name": "risk", "weight": 0.4}, {"name": "speed", "weight": 0.6}],
  "options": [{"name": "A", "scores": {"risk": 7, "speed": 5}}]
}
```

### ICE

```json
[
  {"name": "project X", "impact": 8, "confidence": 6, "ease": 4}
]
```

### Bayesian update

```json
{
  "hypothesis": "feature reaches 10k users in 12 months",
  "prior_probability": 0.3,
  "prior_source": "base rate",
  "evidence": [
    {"description": "beta engagement is high", "quality_grade": "B", "likelihood_ratio": 3.0, "supports": true}
  ],
  "value_if_success": 5000000,
  "cost_if_failure": 500000
}
```

## Reading the output

- rank order is not the same as certainty
- a positive EV can still be a bad idea if the downside is unacceptable
- a strong posterior can still be fragile if the evidence is correlated
- sensitivity results tell you whether to act now or collect more evidence

## Output checklist

1. Show the assumptions.
2. Show the formula or method.
3. Show the sensitivity.
4. Convert the math back into a recommendation.
