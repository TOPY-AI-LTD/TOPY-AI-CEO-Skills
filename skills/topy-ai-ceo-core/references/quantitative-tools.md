# Quantitative Tools

Use this reference when the decision needs a calculation rather than a paragraph.

## Available helper functions

- `decision_matrix(criteria, options)`
- `ice_scoring(initiatives)`
- `expected_value(options)`
- `monte_carlo_simulation(scenarios, num_simulations, seed)`
- `npv(cash_flows, discount_rate)`
- `irr(cash_flows, precision, max_iterations)`
- `bayesian_update(prior_probability, evidence_list, dependency_discount)`
- `sensitivity_analysis(base_prior, evidence_list, prior_shift, lr_multiplier)`

## When to use which

- Decision matrix: compare a small number of strategic options
- ICE: prioritize a backlog quickly
- Expected value: compare probabilistic upside and downside
- Monte Carlo: understand outcome spread and tail risk
- NPV / IRR: model capital allocation or fundraising choices
- Bayesian update: combine evidence into a posterior belief

## Output checklist

1. Show the assumptions.
2. Show the formula or method.
3. Show the sensitivity.
4. Convert the math back into a recommendation.
