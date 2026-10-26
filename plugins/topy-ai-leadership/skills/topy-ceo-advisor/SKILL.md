---
name: topy-ceo-advisor
description: 'A general CEO decision advisor for cross-functional, ambiguous or board-level calls: frames the real question, compares options, checks bias, runs the numbers and ends in a recommendation, routing to narrower TOPY skills when one fits. Use when the user says things like "I need to make a big call and don''t know where to start"; "help me think this decision through like a CEO"; "should we do A, B or wait?"; "what would a good CEO do here?"; "run the numbers on these options"; "I''m torn between two strategies".'
license: MIT
metadata:
  category: leadership
  tier: standalone
  version: 0.1.0
  docs: https://github.com/TOPY-AI-LTD/TOPY-AI-CEO-Skills/blob/main/plugins/topy-ai-leadership/skills/topy-ceo-advisor/SKILL.md
---
# CEO advisor

The default executive reasoning skill for decisions that cut across functions, are ambiguous, or will be
taken to a board. It classifies the decision, finds the real question behind the stated one, picks the
smallest useful playbook from its references, compares at least three options (plus doing nothing), checks
for bias and uncertainty, and ends with a recommendation the founder can act on. When a narrower TOPY skill
fits, it hands over to it.

## When to use
- Strategic bets, resource allocation, build/buy/partner, M&A, exec transitions, capital decisions, or any
  hard call where the founder needs a recommendation rather than a list of considerations.
- Not for a problem that matches a narrower skill; route instead:
  | The question is about... | Use |
  |---|---|
  | One decision written up for the record | `topy-decision-memo` |
  | Ranking initiatives under limited capacity | `topy-prioritization` |
  | Entering a new market or segment | `topy-market-entry` |
  | Competitor moves and response | `topy-competitive-strategy` |
  | Uncertain futures | `topy-scenario-planning` |
  | Raising money | `topy-fundraising-strategy` |
  | Burn and runway | `topy-runway` |
  | Hires, structure, meetings, metrics, board | `topy-hiring-plan`, `topy-org-design`, `topy-operating-cadence`, `topy-kpi-dashboard`, `topy-board-meetings` |
  | An incident happening now | `topy-crisis-response` |
  | Getting people on board | `topy-stakeholder-alignment` |
  | Stress-testing a big call | `topy-debiasing` |
  | Doing something in the TOPY account (plans, revisions, records) | `topy-connect`, then the core skills |

## Before you start
- Ask one question at a time: what happened; what decision they think they face; the deadline; constraints
  and non-negotiables; who is affected. Ask for numbers only if the analysis needs them.
- This skill does not call TOPY. To save the outcome, hand over to `topy-decision-log`.

## Workflow
1. **Classify the decision:** Type 1 (hard to reverse), Type 2 (reversible experiment), crisis, strategic
   bet, operating design, capital, stakeholder, or competitive move. A crisis goes straight to
   `topy-crisis-response`: containment comes before analysis.
2. **State the real question** in one sentence. "Should we enter Japan?" may really be "where does the next
   year of growth come from with the team we have?"
3. **Surface constraints:** facts, deadlines, cash, people, non-negotiables, and who can block.
4. **Load only the reference that fits:**
   - Strategy and prioritization: [references/strategy-and-priority.md](references/strategy-and-priority.md)
   - Operating model, OKRs, KPIs, capital: [references/operating-and-capital.md](references/operating-and-capital.md)
   - Crisis and stakeholders: [references/crisis-and-stakeholders.md](references/crisis-and-stakeholders.md)
   - Competitive and market moves: [references/competitive-and-market.md](references/competitive-and-market.md)
   - Debiasing and uncertainty: [references/debiasing-and-uncertainty.md](references/debiasing-and-uncertainty.md)
   - Quantitative tools: [references/quantitative-tools.md](references/quantitative-tools.md)
5. **Generate at least three options plus do-nothing**, each with its trade-off and what it says no to.
6. **Run the numbers when the decision turns on them**, with [scripts/decision_tools.py](scripts/decision_tools.py)
   (Python 3, no dependencies) rather than mental arithmetic:
   ```
   python3 scripts/decision_tools.py matrix --json '{"criteria":[...],"options":[...]}'
   python3 scripts/decision_tools.py ice --json '[{"name":"X","impact":8,"confidence":6,"ease":4}]'
   python3 scripts/decision_tools.py ev --json '{"probability_success":0.3,"value_if_success":500000,"cost_if_failure":80000}'
   python3 scripts/decision_tools.py monte-carlo --json '[{"name":"base","probability":0.6,"outcome_range":[-50000,200000]}, ...]' --seed 1
   python3 scripts/decision_tools.py npv --rate 0.12 --json '[-100000,30000,40000,50000]'
   python3 scripts/decision_tools.py irr --json '[-100000,30000,40000,50000]'
   python3 scripts/decision_tools.py bayes --file evidence.json
   ```
   Input shapes and pitfalls are in the quantitative reference. Inputs come from the founder; label
   estimates as estimates and show the sensitivity.
7. **Check bias and uncertainty:** the quick scan for Type 2 decisions; the full scan and a pre-mortem for
   Type 1 (or hand over to `topy-debiasing`).
8. **Recommend:** what to do, why it beats the nearest alternative, what would change the answer, and the
   review point.

Worked prompt patterns with what a strong answer contains: [examples/](examples/) (market entry,
fundraising, crisis response, prioritization).

## Output
```
## Decision brief: <title>
Decision type: <type> · Urgency: <immediate | this week | can wait> · Confidence: <high | medium | low>
The question: <one sentence>
Context and constraints: <facts, deadlines, resources, non-negotiables>
Stakeholders: <who matters, who can block, who must be told>
Options: | Option | Upside | Downside | Reversible? | Says no to |   (3+ plus do-nothing)
Analysis: <method, inputs, result, sensitivity>   (when numbers were run)
Recommendation: <what and why, vs the nearest alternative>
What would change this: <evidence or event>
Risks to monitor: <failure mode → mitigation, owner>
Next steps: <action, owner, date> · Review: <date>
```

## Quality bar
- The real question is stated and differs from the surface one when it should.
- Three or more options plus do-nothing, each with a real trade-off.
- Numbers come from the script with visible inputs; ranges where uncertainty is real.
- A clear recommendation, not a list of considerations; what would change it is named.
- A narrower skill was used instead when one fitted.

## Guardrails
- Never invent figures, market data, sources or precedents; label assumptions as assumptions.
- No fake precision: a positive expected value with an unacceptable downside is not a "go".
- Not legal, tax or investment advice: say when a lawyer, accountant or regulated adviser should check,
  and flag employment-law questions (departures, dismissals, restructuring) for an HR adviser or lawyer.
- In a crisis, lead with containment, then stabilisation, then root cause.

## Related skills
- `topy-decision-memo` — write the chosen option up as a formal memo.
- `topy-debiasing` — full pre-mortem and red team for a Type 1 call.
- `topy-crisis-response` — when the situation is live.
- `topy-stakeholder-alignment` — bring the board and team along.
- `topy-prioritization` — when the decision is a ranking.
- `topy-decision-log` — record the decision in TOPY and review it later.
