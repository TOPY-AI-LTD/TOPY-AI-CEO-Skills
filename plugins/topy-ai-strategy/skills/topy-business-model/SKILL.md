---
name: topy-business-model
description: Maps how a startup creates, delivers and captures value on a business model canvas, checks that the pieces add up, and turns the riskiest assumptions into cheap, pre-registered tests. Use when the user says things like "help me with my business model"; "fill in a business model canvas"; "how will we make money?"; "does this business model work?"; "what are our riskiest assumptions?"; "subscription or one-off pricing?". Uses TOPY when it is connected.
license: MIT
metadata:
  category: strategy
  tier: connected
  version: 0.1.0
  docs: https://github.com/TOPY-AI-LTD/TOPY-AI-CEO-Skills/blob/main/plugins/topy-ai-strategy/skills/topy-business-model/SKILL.md
---
# Business model

Lays out the whole business on one page so a founder can see whether the parts fit: who pays, for what, through which channels, at what cost. Every entry is tagged by how well it is known, the maths is checked, and the assumptions that would sink the business if wrong are turned into small tests with pass and fail lines set in advance. With TOPY connected, it reads the project and business plan first and can save each test as a growth experiment.

## When to use
- Pre-launch or early: the idea is clear, but how it makes money is not.
- Before a raise, when investors will ask "how does this make money and what have you proved?"
- When a pricing, channel or segment change might break the model.
- Phrases like "business model", "canvas", "how do we make money", "riskiest assumptions".
- Not for: detailed CAC/LTV and cohort analysis (use `topy-unit-economics`), setting a price (use `topy-pricing-decisions`), or building the financial model (use `topy-financial-model`).

## Before you start
- With TOPY connected:
  - If you do not know the project, call `projects_list` and ask which one; then `project_get`.
  - Call `plans_list`; if there is a plan, `plan_get` it and lift its customer, revenue, cost and channel sections as the first draft of the canvas.
  - Call `growth_experiments_list` so you do not propose tests that are already running.
- Without TOPY, ask one at a time: what you sell, who the first customer is, how they find you, what they pay and how often, and the biggest costs.
- Ask for evidence explicitly: "How many people have paid, signed something, or used it every week?" The answer decides how much of the canvas is a guess.

## Workflow
1. **One canvas per customer segment.** If the business serves several segments with different needs or prices, draw separate canvases. A marketplace or platform needs one for each side (buyers and sellers, users and advertisers), linked.
2. **Fill the nine blocks, specifically.**
   | Block | Write | Not acceptable |
   |---|---|---|
   | Customer segment | who, size of company or situation, the trigger that makes them look | "SMEs", "everyone" |
   | Value proposition | the job, the pain removed, the gain created, versus today's alternative | a feature list |
   | Channels | how they hear, evaluate, buy and receive it | "online" |
   | Relationships | self-serve, sales-assisted, account-managed, community | blank |
   | Revenue streams | who pays, for what, price model, frequency | "subscriptions" with no price |
   | Key resources | what you must own or have: data, people, licences, inventory | |
   | Key activities | what you must do well every week | |
   | Key partners | who you depend on, and what they get | |
   | Cost structure | the three biggest lines, fixed vs variable | |
3. **Tag every entry.** E = evidence (observed behaviour: payment, signature, retained usage, measured cost). B = belief (signals such as interviews or waitlists). G = guess. A canvas that is mostly G is a hypothesis, which is fine at the start; say so plainly.
4. **Name the model pattern and its known weak points.**
   | Pattern | Check first |
   |---|---|
   | Subscription | retention after the first months; what makes renewal automatic |
   | Usage-based | revenue swings; whether customers can predict their bill |
   | Transactional / one-off | repeat purchase rate; acquisition cost per sale |
   | Marketplace take rate | which side to seed first; whether buyers and sellers will go around you |
   | Freemium | share of free users who ever pay; cost of serving free users |
   | Productised service | gross margin as volume grows; founder time per customer |
   | Hardware plus consumables | upfront cost and working capital; attach rate |
5. **Check the maths.** Use the founder's numbers; mark any missing one as unknown rather than filling it.
   - Gross margin = (price − variable cost to serve) ÷ price.
   - Monthly gross profit per customer = monthly revenue per customer × gross margin.
   - Acquisition payback in months = acquisition cost per customer ÷ monthly gross profit per customer.
   - Break-even customers = monthly fixed costs ÷ monthly gross profit per customer.
   State what the payback and break-even numbers imply for cash. Compare them with the founder's own targets; any published benchmark is a loose rule of thumb that varies by sector.
6. **Check channel-price fit.** The channel must be affordable at the price. A low annual price cannot carry a field-sales process; a high-value, complex purchase rarely closes through self-serve alone. If the planned channel costs more per customer than a year or so of gross profit (rule of thumb; adjust to the founder's cash position), flag it.
7. **List the assumptions.** Turn every G and B into a sentence that could be false: "Clinic managers will pay monthly without a contract", "We can serve a customer for under X a month".
8. **Rank them.** Score each on impact if wrong (1-5: 5 = the model fails) and uncertainty (1-5: 5 = no evidence). Risk = impact × uncertainty. Break ties in this order: will customers want it, will they pay enough, can we deliver it. The top three are the riskiest assumptions.
9. **Design one test per top assumption.**
   - Hypothesis: "We believe [segment] will [do something observable] because [reason]."
   - Measure: one metric, the pass line, the fail line, and the deadline, written before the test starts.
   - Method: the cheapest test that produces behaviour, not opinion. Stronger evidence costs the customer more: a stated opinion < a sign-up < time given (pilot, onboarding call) < money or a signed commitment (pre-order, paid pilot, letter of intent). Use interviews to find problems, not to prove demand.
   - Budget and owner.
   Results between the pass and fail lines mean "inconclusive"; decide in advance what happens then (extend once, or change the test).
10. **Save the tests (TOPY connected).** For each test, offer `growth_experiment_create` with `hypothesis`, `channel` (where the test runs), `experiment_type` (e.g. pre-sale, fake door, concierge, pricing test), `status` "planned", and `success_criteria` holding the metric, pass line, fail line and deadline. One preview per experiment; show it and call again with `confirm: true` and the `confirmation` only after the founder agrees.
11. **Note what the plan should change.** If the canvas contradicts the business plan (a different segment, price or channel), list the differences and point to `topy-plan-revision` to carry them through the plan. Do not edit the plan from this skill.

## Output
1. Canvas table (block | entries | tag E/B/G), one per segment or side.
2. Model pattern and its checks.
3. Unit maths: inputs (with source or "assumption"), gross margin, payback, break-even.
4. Coherence findings: what does not add up, in order of severity.
5. Assumption ranking: assumption | impact | uncertainty | risk.
6. Test cards for the top three: hypothesis | metric | pass | fail | deadline | method | cost | owner.
7. Differences from the business plan, if any.

## Quality bar
- No block says "everyone", "online" or a feature list; each entry is specific enough to be wrong.
- Every entry carries an E, B or G tag, and the summary states how much is evidence.
- The maths uses the founder's numbers or shows "unknown"; nothing is filled from thin air.
- Each test has pass and fail lines and a deadline set before it runs, and measures behaviour.
- The three riskiest assumptions are tested before anything that depends on them is built.

## Guardrails
- Changes in TOPY take two calls: a preview first, shown to the user, then `confirm: true` with the `confirmation` only after they agree. Never confirm for the user.
- Never invent market sizes, conversion rates, prices or customer counts; label assumptions as assumptions.
- Not legal, tax or investment advice. Pre-sales, deposits, subscriptions and data-based revenue can carry consumer-protection, tax and privacy obligations; suggest a lawyer or accountant checks before taking money.
- Tests involving real customers must be honest: if a fake-door test shows something that does not exist yet, tell people promptly and refund any money taken.

## Related skills
- `topy-growth-experiments` — run and close the tests designed here.
- `topy-unit-economics` — deeper CAC, LTV, payback and cohorts once there is data.
- `topy-pricing-decisions` — when the riskiest assumption is the price.
- `topy-plan-revision` — carry a changed model through the business plan.
- `topy-financial-model` — turn the canvas into a driver-based forecast.
