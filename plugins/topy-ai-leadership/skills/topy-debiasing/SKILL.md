---
name: topy-debiasing
description: 'Stress-test a big call before committing: independent estimates, base rates, a pre-mortem, a red team, a bias scan and pre-set kill criteria, ending in an adjusted confidence. Use when the user says things like "am I fooling myself on this?"; "run a pre-mortem on our plan"; "red team this decision"; "we''re about to commit a lot of money, sanity check it"; "everyone agrees, which worries me"; "how confident should I really be?".'
license: MIT
metadata:
  category: leadership
  tier: standalone
  version: 0.1.0
  docs: https://github.com/TOPY-AI-LTD/TOPY-AI-CEO-Skills/blob/main/plugins/topy-ai-leadership/skills/topy-debiasing/SKILL.md
---
# Debiasing a big decision

A structured stress test for an important, hard-to-reverse decision that already has a favourite. It does
not replace judgement; it makes the judgement harder to fool. The founder leaves knowing which assumptions
carry the case, how the outside view compares with the inside one, how the plan most plausibly fails, the
strongest argument against it, and the evidence that would make them stop.

## When to use
- Before signing, hiring, raising, launching or spending on something costly to undo; when a team agrees
  too quickly; when the founder senses they are attached to an option.
- Not for: small reversible choices (decide and learn; a two-minute bias scan is enough); structuring the
  decision from scratch (use `topy-ceo-advisor` or `topy-decision-memo`); mapping several futures (use
  `topy-scenario-planning`).

## Before you start
- Ask one question at a time: the decision and preferred option; the forecasts the case rests on; who
  decides and how the preference formed; history of similar efforts.
- If other people are involved, the method works best when they write estimates privately before any
  discussion: suggest the founder collects them first.
- This skill does not read or save TOPY data. To keep the decision, assumptions and kill criteria for later
  review, use `topy-decision-log`.

## Workflow
1. **Restate the decision neutrally.** Write it once as a gain and once as a loss ("gain a new segment" /
   "spend nine months not improving the core"). If the preference flips between framings, note it.
2. **Find the load-bearing assumptions.** List every assumption; mark the 3-5 that, if wrong, would change
   the decision. For each: the evidence, its quality (direct data / analogy / opinion), and what result
   would prove it wrong.
3. **Take the outside view.** Pick a reference class (similar launches, hires, markets, projects in this
   company or comparable ones). Ask the founder for real outcomes they know of; start the estimate from that
   base rate and adjust for genuine differences. If no reference class can be found, say so: the forecast
   is then a guess and should be a wide range.
4. **Estimate independently, then compare.** Have each decider write a low / likely / high for the key
   numbers before discussing. A wide spread means the group does not know; do not average it away.
5. **Run a pre-mortem (about 30 minutes):**
   - 0-5 · "It is <date + 12-18 months>. This decision failed badly. That is a fact."
   - 5-15 · Each person writes, silently, the reasons it failed. Specific, not "execution".
   - 15-25 · Go round one reason at a time until all are listed; group them.
   - 25-30 · Rank by likelihood × damage; take the top 3-5 to mitigations.
6. **Red team.** One person (or one separate pass by the agent) builds the strongest case for the best
   alternative, including do-nothing. The preferred option must answer it on the merits; "they just don't
   get it" is not an answer.
7. **Scan for bias** and note which apply, with the fix:
   | Bias | Question | Fix |
   |---|---|---|
   | Anchoring | Which number did we hear first? | Re-estimate from the base rate |
   | Confirmation | What evidence did we not look for? | Seek the disconfirming case |
   | Sunk cost | Would we start this today from zero? | Decide on future costs only |
   | Overconfidence | How often were our past forecasts right? | Widen ranges |
   | Planning fallacy | How long did similar work really take? | Use the reference class |
   | Availability | Is one vivid story driving this? | Count cases, not stories |
   | Groupthink | Has anyone senior dissented? | Private estimates, assigned red team |
   | Status quo | Are we avoiding change because it is uncomfortable? | Clean-sheet comparison |
   | Incentives | Who benefits personally from each option? | Name it, involve someone neutral |
8. **Test sensitivity.** Move each load-bearing assumption to its pessimistic value one at a time. If the
   decision flips on a single plausible change, it is fragile: reduce exposure (pilot, stage-gate, option to
   exit) or gather that evidence first. For calculations, `topy-ceo-advisor` includes decision tools
   (expected value, Monte Carlo, Bayesian update).
9. **Pre-commit kill criteria.** Before deciding, write the signals that would trigger stop or rethink:
   metric, threshold, date, who checks. Kill criteria set after starting tend to drift.
10. **Decide and record confidence.** Verdict: go / go with changes / pause for evidence / stop. State the
    confidence before and after the exercise, and the one piece of evidence that would most change it.

## Output
```
Debiasing review: <decision> · preferred <option> · <date>
Framing check: <gain frame> / <loss frame> → <changed preference? y/n>
Load-bearing assumptions
| Assumption | Evidence | Quality | Disproved if | Pessimistic value | Decision flips? |
Outside view: reference class <...> · base rate <from founder's data or "none found"> · inside estimate <...>
Independent estimates: | Person | Low | Likely | High |
Pre-mortem: top causes (likelihood × damage) → mitigation, owner
Red team: strongest case for <alternative> · response
Biases found: <bias → fix applied>
Kill criteria: | Signal | Threshold | Check date | Checker |
Verdict: <go | go with changes | pause | stop> · confidence <before → after> · evidence that would change it
```

## Quality bar
- The 3-5 load-bearing assumptions are named, each with a disproof condition.
- A base rate came from real cases the founder supplied, or its absence is stated.
- Pre-mortem reasons are specific and each top one has a mitigation and owner.
- The red-team case is strong enough that the founder found it uncomfortable.
- Kill criteria are measurable, dated and set before the decision.
- The verdict and an adjusted confidence are explicit.

## Guardrails
- Never invent base rates, studies or statistics; if the founder wants research, they supply or name a
  source and it is labelled as such. The bias list is a checklist, not a scientific diagnosis of anyone.
- Critique the decision, never the person; keep the red team on ideas.
- Not legal, tax or investment advice: say when a professional should review the decision itself.
- If the exercise reveals a hidden personal conflict of interest, say so plainly and suggest a neutral reviewer.

## Related skills
- `topy-ceo-advisor` — frame the decision and run the numbers.
- `topy-decision-memo` — write up the decision with the kill criteria.
- `topy-scenario-planning` — when several futures matter, not one forecast.
- `topy-decision-log` — store the assumptions and review them on the kill-criteria date.
- `topy-stakeholder-alignment` — when the main risk is others not accepting the call.
