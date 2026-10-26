---
name: topy-stakeholder-alignment
description: 'Bring the people who matter along on a decision or change: map their power, interests and likely objections, choose the order to talk to them, and prepare each conversation. Use when the user says things like "how do I get the board to agree to this?"; "my co-founder disagrees with the pivot"; "who do I need to talk to before announcing this?"; "I need buy-in for raising prices"; "the team is resisting the new direction"; "map the stakeholders for this decision".'
license: MIT
metadata:
  category: leadership
  tier: standalone
  version: 0.1.0
  docs: https://github.com/TOPY-AI-LTD/TOPY-AI-CEO-Skills/blob/main/plugins/topy-ai-leadership/skills/topy-stakeholder-alignment/SKILL.md
---
# Stakeholder alignment

Helps a founder take a decision or change from "I think this is right" to "the people who matter support
it, or at least will not block it". It maps everyone involved, finds what each actually cares about behind
their stated position, decides the order of conversations so nobody important is surprised, and prepares
each conversation. Alignment is not manipulation: the founder listens as well as persuades, and may change
the plan.

## When to use
- A pivot, price change, reorg, round, leadership change, partnership or any decision that needs approval
  or cooperation from people the founder does not control.
- Before a board meeting with a contentious item; when a co-founder disagrees; when a team resists.
- Not for: a live incident (use `topy-crisis-response`); structuring the org itself (use `topy-org-design`);
  the formal board meeting (use `topy-board-meetings`).

## Before you start
- Ask one question at a time: the decision and how settled it is; who is involved and what each controls;
  what the founder knows of each person's view; the deadline.
- If the decision is still open, say so to stakeholders; asking for input on a decision already made damages trust.
- This skill does not read or save TOPY data. To record the final decision, use `topy-decision-log`.

## Workflow
1. **Write the ask in one sentence** for each stakeholder group: what you need them to do (approve,
   support, accept, not block, carry out) by when.
2. **List the stakeholders.** Typical groups: co-founders, board directors, lead and other investors,
   leadership, affected employees, key customers, partners, regulators. Treat individuals separately when
   their views differ.
3. **Map each one:**
   | Stakeholder | Power over this (approve / block / influence / none) | Interest (high/low) | Stance now (champion / supporter / neutral / sceptic / opponent / unknown) | Stance needed | Stated position | Underlying interest or fear | Likely reaction if surprised |
   Positions are what they say ("no price rise"); interests are why ("I promised our first customers stability").
   Unknown is a valid stance: find out rather than guess.
4. **Find the gaps.** Prioritise people whose stance needed is higher than stance now, weighted by power.
   High power and high interest: engage personally and early. High power, low interest: brief concisely,
   avoid surprises. Low power, high interest: keep informed, listen for useful objections.
5. **Diagnose resistance before answering it.** Is the person: missing information; disagreeing with the
   analysis; afraid of personal impact (role, status, money, workload); protecting a commitment they made;
   or objecting on values? Each needs a different response: information, debate on the evidence, a concrete
   answer about impact, a way to keep face, or a real reconsideration.
6. **Sequence the conversations.** Rule of thumb order:
   1) a trusted ally who will test the idea honestly; 2) the most powerful approver or likely blocker;
   3) swing voices whose view others follow; 4) people directly affected; 5) the wider group; 6) outside
   parties. Nobody with power should hear it second-hand. Leave time between rounds to change the plan.
7. **Prepare each key conversation** with a one-page brief: goal of the conversation; what they care about;
   the case in their terms; the hardest question they will ask and an honest answer; what you can offer or
   change; what you will not change; the next step you will ask for.
8. **Run the conversation as a listening one.** Open with the problem, not the solution; ask for their view
   before defending yours; restate their concern until they agree you understood it; agree a next step.
9. **Track commitments** after every conversation: stance after, commitments made by either side, follow-up
   date. Update the map; if a powerful stakeholder moved to opponent for a good reason, revisit the decision.
10. **Announce** only when approvers have agreed and affected people have heard directly. Afterwards, thank
    the people who changed the plan for the better, by name where appropriate.

## Output
```
Stakeholder alignment: <decision> · status <decided | preferred | open> · announce by <date>
Ask: <one sentence per group>
Map
| Stakeholder | Power | Interest | Stance now → needed | Underlying interest | Resistance type | Approach |
Sequence
| # | Who | Messenger | Format (1:1, call, written) | By | Goal |
Conversation briefs (one per key stakeholder)
  Goal · What they care about · Our case in their terms · Hardest question + answer · Can offer · Won't change · Next step
Commitment tracker
| Who | Date | Stance after | Their commitment | Our commitment | Follow-up |
```

## Quality bar
- Each stakeholder has a stated position *and* an underlying interest, or "unknown" with a plan to find out.
- Every approver and potential blocker is met personally before any wide announcement.
- Each brief contains the hardest question and an honest answer, not a deflection.
- The plan says what the founder is willing to change; alignment that cannot change anything is just notification.
- Commitments on both sides are written down with dates.

## Guardrails
- Never invent what a stakeholder thinks; label guesses as guesses.
- No manipulation: no misleading framing, selective disclosure that would mislead, or playing people
  against each other. Honest disagreement is information.
- Not legal advice: shareholder consents, board approvals, consultation duties with employees or their
  representatives, and changes to anyone's terms of employment can carry legal requirements; check with a
  lawyer or HR adviser.
- Keep personal information about stakeholders to what is needed for the decision.

## Related skills
- `topy-board-meetings` — the formal meeting after the pre-wiring.
- `topy-decision-memo` — the written case to share with stakeholders.
- `topy-org-design` — when the change is a restructure.
- `topy-crisis-response` — when sequencing is urgent.
- `topy-ceo-advisor` — when the decision itself is still open.
