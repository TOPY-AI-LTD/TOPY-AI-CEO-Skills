---
name: topy-org-design
description: 'Design a startup''s structure as it grows: who owns which outcomes (DRI and RACI), reporting lines, spans of control and decision rights, plus how to roll the change out. Use when the user says things like "everyone reports to me and it''s not working"; "who should own what now that we''re 15 people?"; "draw our org chart for the next stage"; "nobody owns onboarding, things fall through the cracks"; "do we need a VP or a team lead here?"; "make a RACI for our launch".'
license: MIT
metadata:
  category: operations
  tier: standalone
  version: 0.1.0
  docs: https://github.com/TOPY-AI-LTD/TOPY-AI-CEO-Skills/blob/main/plugins/topy-ai-operations/skills/topy-org-design/SKILL.md
---
# Org design

Helps a founder decide how the team is organised for the next stage: which outcomes each person is the
directly responsible individual (DRI) for, who reports to whom, how wide each manager's span is, and who
decides what. The aim is the simplest structure that makes the next quarter's important decisions fast and
leaves no critical outcome without an owner. Ends with a careful rollout plan, because a good structure
announced badly still fails.

## When to use
- The founder is the bottleneck for most decisions; work falls between people; two people think they own
  the same thing; a new layer of management is being considered; a reorg or new team is planned.
- Mapping a RACI for a launch, a recurring process (pricing changes, releases, hiring) or a crisis rota.
- Not for: which roles to hire and when (use `topy-hiring-plan`); meeting rhythm (use
  `topy-operating-cadence`); getting a contested change accepted (pair with `topy-stakeholder-alignment`).

## Before you start
- Ask one question at a time: the team list with reporting lines; the top 3-5 outcomes for the next two
  quarters; the symptoms the founder sees; hires planned.
- Ask for roles and work, not personal details. If a specific person's performance is the real issue, say
  so plainly: that is a management conversation, not a structure problem.
- This skill does not read or save TOPY data. To keep the outcome, record it with `topy-decision-log`.

## Workflow
1. **List the outcomes, then the work.** Write the company's outcomes for the period and, under each, the
   recurring activities that produce it (e.g. "pipeline" → outbound, demos, proposals, CRM hygiene).
2. **Map current ownership.** For each outcome and activity: who actually does it, who decides, who is
   blamed when it slips. Mark four failure types:
   - **Orphan**: no one owns it. **Duplicate**: two people believe they own it.
   - **Overload**: one person owns more than they can review weekly. **Shadow**: the founder still decides
     something they "delegated".
3. **Check spans of control.** Count direct reports per manager. Rule of thumb, not a law: managers of
   people doing similar work can often handle more reports than managers of very different specialists;
   founders who also run sales or product usually cope with fewer. Flag anyone whose 1:1s no longer happen
   weekly as overloaded, whatever the number.
4. **Choose the grouping.** Pick one primary axis and state the trade-off:
   | Grouping | Good when | Cost |
   |---|---|---|
   | Function (eng, sales, ops) | One product, early stage, depth matters | Hand-offs between functions |
   | Product / customer segment | Several products or segments with distinct goals | Duplicated specialists |
   | Mission team (cross-functional pod) | A goal needs tight eng-design-GTM loops | Harder career paths, more coordination at the top |
   Early-stage default: functional, with a temporary mission team for the single most important bet.
5. **Assign one DRI per outcome.** A DRI is one named person who can say "I own this, here is the status".
   Rules: one DRI per outcome; a DRI may own several outcomes but no more than they review weekly; the DRI
   has the authority or the budget to act, or the role is ceremonial.
6. **Write the RACI for cross-team processes only.** Use it where hand-offs fail (launches, pricing changes,
   incidents, hiring). Exactly one A per row; R may be several; keep C small, because every C is a meeting.
7. **Set decision rights.** For recurring decisions, state who decides, who must be consulted, and the
   threshold that escalates to the founder (e.g. spend above a set amount, any customer-facing price change,
   any hire). Reversible, low-cost decisions go as low as possible.
8. **Test the design against three scenarios:** a top customer escalates on a Friday night; a launch slips
   two weeks; the founder is away for a month. Walk each through the new structure. If any lands back on the
   founder by default, fix the ownership.
9. **Plan the rollout.**
   - Talk first, privately, to anyone whose scope, title, manager or pay changes, before any group announcement.
   - Announce once, in writing and live, with the why, the new chart, the DRI list and what does not change.
   - Set a review in 6-8 weeks (rule of thumb) to fix what the design got wrong.
   - Changes to someone's role, title, hours, location or contract can have legal and contractual
     implications: check with an HR adviser or employment lawyer before announcing.

## Output
```
Org design: <company> · <headcount> people · <date>
Diagnosis
| Outcome / activity | Owner today | Issue (orphan/duplicate/overload/shadow) | Evidence |
Proposed structure
  Grouping: <function | product | mission> because <reason>; trade-off <cost>
  Reporting lines: <manager> → <reports> (span n)
DRI list
| Outcome | DRI | Weekly measure | Escalates to |
RACI (cross-team processes)
| Process step | R | A | C | I |
Decision rights
| Decision | Decides | Consults | Escalate when |
Scenario test: 3 scenarios, who handles each
Rollout: private conversations (who, by when) · announcement date · review date
```

## Quality bar
- Every outcome has exactly one DRI; every RACI row has exactly one A.
- No manager's span is justified only by the org chart looking tidy; overloads are named.
- The founder's own scope is explicit and smaller than before, or the reason it is not is stated.
- The three scenarios were walked through and none defaults to the founder.
- The rollout puts private conversations before any announcement.
- Legal or contractual implications of role changes are flagged for an HR adviser.

## Guardrails
- Never invent benchmarks for ideal team sizes or ratios; present spans as rules of thumb.
- Not legal advice: redundancies, demotions, title or pay changes, relocations and contract changes go to an
  employment lawyer or HR adviser in the relevant country.
- Do not make judgements about individuals' performance or personal circumstances; describe roles and work.
- Do not recommend restructuring as a substitute for a direct performance conversation.

## Related skills
- `topy-hiring-plan` — the roles the new structure needs, timed and costed.
- `topy-operating-cadence` — the meetings where DRIs report.
- `topy-kpi-dashboard` — the weekly measure each DRI owns.
- `topy-stakeholder-alignment` — bringing co-founders, leads and the board along before announcing.
