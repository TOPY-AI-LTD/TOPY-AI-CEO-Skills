---
name: topy-decision-memo
description: Turns a hard founder call into a one-page decision memo with real options (including doing nothing), weighed trade-offs, a recommendation and the signals that would reverse it. Use when the user says things like "help me decide whether to ..."; "write a decision memo"; "should we build it, buy it or partner?"; "I keep going back and forth on this"; "lay out the options for me"; "what's the case for and against?". Uses TOPY when it is connected.
license: MIT
metadata:
  category: strategy
  tier: connected
  version: 0.1.0
  docs: https://github.com/TOPY-AI-LTD/TOPY-AI-CEO-Skills/blob/main/plugins/topy-ai-strategy/skills/topy-decision-memo/SKILL.md
---
# Decision memo

Helps a founder make one consequential choice well and leave a record of why. The agent frames the real question, builds a set of options that someone would genuinely defend (always including doing nothing), compares them on a few weighted criteria, stress-tests the front-runner and ends with a recommendation, a stated confidence and the specific evidence that would change it. When TOPY is connected, the agreed decision can be saved to the project's decision log.

## When to use
- A single choice with trade-offs: hire vs contract, build vs buy vs partner, raise now vs later, pivot vs persist, kill a product line, change pricing model, take a large customer's custom request.
- The founder is stuck, the team disagrees, or the decision will need explaining to a co-founder, board or investor later.
- Phrases like "help me decide", "pros and cons", "which option", "I need to make this call".
- Not for: ranking a backlog of many initiatives (use `topy-prioritization`), a full bias review of a very large bet (add `topy-debiasing`), or simply recording a decision already made (use `topy-decision-log`).

## Before you start
- Ask one question at a time. First: "What exactly are you deciding, and by when?"
- With TOPY connected:
  - If you do not know the project, call `projects_list` and ask which one.
  - Call `project_get` for what the company does, its market and stage.
  - Call `decisions_list` and scan titles for anything related. If a past decision covers the same ground, read it out and ask whether this is a reversal; a reversal should say what changed.
- Without TOPY, ask: what the company does and its stage, months of runway, team size, and any earlier decision on this topic.
- Then collect: who decides (one name), who must be consulted, hard constraints (cash, contracts, legal), and what the founder is already leaning towards. Note the lean; do not let it steer the options.

## Workflow
1. **Frame the question.** Write it as one sentence that ends in a choice: "Should we [action] by [date], given [constraint]?" If the question is really a fact ("what does a contractor cost?"), answer the fact and stop; no memo needed. If two decisions are tangled ("hire a CTO and move to enterprise"), split them and handle the one that unlocks the other first.
2. **Size the decision.** Classify on two axes and set the effort accordingly:
   | | Easy to reverse | Hard to reverse |
   |---|---|---|
   | Small stakes | decide today, half-page memo | short memo, one risk check |
   | Large stakes | short memo, decide fast, set a review date | full memo with pre-mortem and sensitivity |
   As a rule of thumb, treat it as large stakes if it commits more than about a month of runway, a quarter of the team's time for a quarter, or a public promise to customers or investors. Use the founder's own threshold if they have one.
3. **Price the delay.** State what waiting a week or a month costs (lost deals, burn, a closing window) and what waiting buys (new data due on a known date). If waiting buys nothing, say "decide now".
4. **Build the options.** At least three plus do-nothing:
   - *Do nothing* is the current path projected forward, not a frozen present. Describe where it leads in six months.
   - Include a *staged or partial* option (pilot, contract-to-hire, one region first) when one exists; it is often the best answer to a hard-to-reverse choice.
   - No straw men: each option must be one a smart person would argue for. If you cannot write its best case in two sentences, drop it.
5. **Choose criteria and weights.** Three to five criteria tied to the company's goal for the next 6-12 months (growth, runway, focus, customer trust, learning speed). Weights add to 100. Write the weights down before scoring, so scores cannot bend them.
6. **Score honestly.** Score each option 1-5 per criterion with a one-line reason. Weighted score = sum of (weight × score) ÷ 100. Mark any score that rests on a guess with "(assumption)".
7. **Check sensitivity.** Move the top weight 10 points up and down, and swap the two highest weights. If the winner changes, call it a close call and say which single assumption decides it. Do not present a close call as firm.
8. **Weigh uncertain payoffs.** For options with a wide outcome range, write three states (good, expected, bad) with rough probabilities that sum to 1 and a value for each. Expected value = sum of probability × value. Report the bad case beside it. Rule: an option whose bad case would leave the company unable to make payroll or finish its plan is out unless the bad case can be capped, however good its expected value.
9. **Name the opportunity cost.** For the leading option list the two or three concrete things that will not happen because of it (the feature that slips, the hire that waits). Ask: "If we had not already spent anything on this, would we still choose it today?"
10. **Pre-mortem the front-runner.** "It is a year from now and this went badly. What happened?" Take the three most plausible causes, give each a mitigation or an early warning sign.
11. **Quick bias scan.** Check four things in writing: anchoring (which number came first and is it doing the work?), sunk cost (is past spend in the argument?), confirmation (what evidence would change the founder's mind, and has anyone looked for it?), and the lean noted earlier (did the scores drift towards it?).
12. **Recommend.** Name the option, explain why it beats the runner-up specifically (not why it is good in general), state confidence (low / medium / high, with the reason), the assumptions it depends on, and two or three tripwires: measurable signals with a date that would trigger a re-think ("if fewer than N pilots convert by [date], revisit"). Set a review date.
13. **Hand the call back.** The founder decides. Ask what they chose and why, in their words.
14. **Save it (TOPY connected).** Offer to record the founder's decision with `decision_create`:
    - `title`: the question in a few words; `context`: the frame, constraints and deadline.
    - `options_considered`: each option with its one-line case and weighted score.
    - `decision`: what the founder chose (their words); `rationale`: why it beat the runner-up, plus assumptions.
    - `confidence`: low / medium / high; `impact_scope`: the areas affected (e.g. hiring, runway, product).
    - `metadata_json`: tripwires and the review date.
    Call it once without `confirm` to get the preview, show it, and only after the founder agrees call it again with `confirm: true` and the `confirmation`. If the founder has not decided yet, do not save a recommendation as a decision.

## Output
```
Decision: [question in one sentence]
Decider · deadline · cost of waiting · reversibility and stakes
1. Options              table: option | best case | main risk | reversible?
2. Criteria and scores  table: criterion | weight | score per option, with reasons | weighted total
3. Sensitivity          firm / close call, and the assumption that decides it
4. Risks                pre-mortem: cause | mitigation or warning sign
5. Recommendation       option, why it beats the runner-up, confidence, assumptions
6. Tripwires and review signal | threshold | date; review date
7. What we give up      opportunity cost
```
Keep the memo to about one page for small decisions and two for large ones.

## Quality bar
- The question is one sentence and ends in a choice.
- Do-nothing is an option and is described as a trajectory.
- Weights were set before scores; every score has a reason; guesses are marked.
- The sensitivity result is stated, and a close call is called a close call.
- The recommendation says why it beats the runner-up, not only why it is good.
- Tripwires are measurable and dated; there is a review date.
- Nothing is saved in TOPY until the founder has decided and approved the preview.

## Guardrails
- Changes in TOPY take two calls: a preview first, shown to the user, then `confirm: true` with the `confirmation` only after they agree. Never confirm for the user.
- Never invent figures, customers, quotes, market data or sources; label assumptions as assumptions and use ranges where the number is unknown.
- Not legal, tax or investment advice. Decisions touching contracts, employment, equity, tax or regulation should be checked by a lawyer or accountant; say so in the memo.
- Recommend, do not decide. The founder owns the call, and the record holds their words.
- If the decision affects people (layoffs, a co-founder's role), keep names out of saved records unless the founder asks, and suggest how and in what order to tell those affected.

## Related skills
- `topy-decision-log` — record, review and revisit decisions over time.
- `topy-debiasing` — a deeper pre-mortem and red team for the biggest bets.
- `topy-scenario-planning` — when the answer depends on which future arrives.
- `topy-prioritization` — when the choice is among many initiatives, not a few options.
- `topy-ceo-advisor` — open-ended CEO questions that are not yet a decision.
