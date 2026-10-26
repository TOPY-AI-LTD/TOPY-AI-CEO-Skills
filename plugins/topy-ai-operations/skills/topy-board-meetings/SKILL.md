---
name: topy-board-meetings
description: 'Prepare and run a startup board meeting: the board pack, a timed agenda, the asks and decisions, and minutes with actions, built from TOPY''s decisions, risks and investor updates. Use when the user says things like "help me prepare for our board meeting"; "what goes in a board pack?"; "draft the agenda for next week''s board"; "how do I tell the board we missed the quarter?"; "write the board minutes from my notes"; "first board meeting after our seed round". Uses TOPY when it is connected.'
license: MIT
metadata:
  category: operations
  tier: connected
  version: 0.1.0
  docs: https://github.com/TOPY-AI-LTD/TOPY-AI-CEO-Skills/blob/main/plugins/topy-ai-operations/skills/topy-board-meetings/SKILL.md
---
# Board meetings

Turns a board meeting from a status recital into a working session. The founder sends a pack the board
reads beforehand, spends most of the meeting on the two or three questions that need the board's judgement
or approval, and leaves with clear decisions, owners and dates. With TOPY connected, the pack draws on the
decision log, the risk register and recent investor updates, so the story the board hears matches what
investors were already told.

## When to use
- Preparing a board pack or agenda, the first board after a round, delivering bad news, drafting minutes.
- Not for: the monthly or quarterly investor update email (use `topy-investor-relations`); building the
  metrics themselves (use `topy-kpi-dashboard`); winning over one difficult director before the meeting
  (pair with `topy-stakeholder-alignment`).

## Before you start
- Ask one question at a time: date and slot length; who attends and in what capacity; results since last
  meeting; what the founder needs from the board; anything that formally requires board approval.
- With TOPY connected, read first:
  - `investor_updates_list`: the most recent updates, so figures and narrative in the pack agree with them.
  - `decisions_list`: decisions since the last board, and any marked for board review.
  - `risks_list`: open risks, highest severity first; these feed the risk section.
- Without TOPY, ask for the last investor update, the decisions taken since the last board and the top
  risks the founder worries about.

## Workflow
1. **Decide the meeting's job first.** Write the 1-3 things the founder needs by the end: approvals
   (budget, option grants, financing), decisions (strategy choices), or advice (a specific question). If
   none exists, the meeting can be shorter or replaced by a written update.
2. **Build the pack** (send 3-5 working days before, as a rule of thumb; one document, numbered pages):
   1. *CEO letter* (one page): the period in five lines, what went well, what did not, what you need.
   2. *Scorecard*: north star and input metrics, target vs actual, trend; reds explained in one line each.
   3. *Financials*: cash, burn, runway, revenue vs plan and vs last forecast; changes to the forecast.
   4. *Progress against the company priorities* for the quarter, scored honestly.
   5. *Discussion topics*: for each, the question, context, options, the founder's recommendation.
   6. *Risks*: top 3-5 from the register with trend and mitigation owner.
   7. *Approvals*: the exact resolutions needed, with supporting papers.
   8. *Appendix*: team changes, hiring, product, pipeline, decisions log since last meeting.
3. **Deliver bad news early.** Anything materially worse than the last update goes to each director
   individually before the pack lands, with cause, impact and plan. The meeting is for the plan, not the surprise.
4. **Set the agenda** for a 2-hour slot (scale to the slot):
   - 0-10 · Opening, conflicts of interest declared, approval of last minutes.
   - 10-25 · CEO summary and questions on the pack (no page-by-page walk-through; it was pre-read).
   - 25-85 · Discussion topics, most important first, each with a stated question and the decision sought.
   - 85-100 · Approvals and resolutions.
   - 100-110 · Actions and owners read back; date of next meeting.
   - 110-120 · Directors-only session without management, if the board wants it.
5. **Frame each discussion topic** as: the question, what we know, options with trade-offs, recommendation,
   what we need from you (decide / advise / approve). Close each with: decision, owner, date, or "revisit on <date>".
6. **Write the minutes within 48 hours** (rule of thumb). Record: attendees and capacity, quorum, conflicts
   declared, a short summary of each discussion, resolutions in exact wording with how they were passed, and
   actions with owners and dates. Minutes record what was decided, not every opinion voiced.
7. **Close the loop.** Actions go into the next pack's first page with status. With TOPY connected, offer to
   save each board decision with `decision_create` (the question, options, decision, rationale, review date).

## Output
Pack outline:
```
Board pack: <company> · meeting <date> · sent <date>
1 CEO letter · 2 Scorecard · 3 Financials · 4 Priorities · 5 Discussion topics · 6 Risks · 7 Approvals · 8 Appendix
Asks of the board: 1) <decide/advise/approve> ... 2) ...
```
Agenda:
```
| Time | Item | Owner | Paper ref | Outcome sought (decide/advise/approve/note) |
```
Minutes:
```
Board meeting of <company> · <date> · <place/video>
Present: <directors> · In attendance: <observers, invitees> · Quorum: <yes/no>
Conflicts declared: ...
1 <item>: summary (2-4 lines) · Resolved: "<exact wording>"
Actions: | # | Action | Owner | Due |
```

## Quality bar
- The pack's figures match the latest investor update and TOPY records, or the difference is explained.
- Every discussion topic states the question and the decision sought; at least half the meeting is discussion.
- Bad news appears in the CEO letter, not on page 14.
- Resolutions are worded exactly and listed separately from discussion.
- Every action has one owner and a date.

## Guardrails
- Changes in TOPY take two calls: `decision_create` first returns a preview, shown to the user; call it
  again with `confirm: true` and the `confirmation` only after they agree. Never confirm for the user.
- Never invent figures, quotes from directors or approvals that did not happen; mark draft minutes as draft
  until the chair approves them.
- Not legal advice: what needs board or shareholder approval, quorum, notice periods, written resolutions,
  director duties and conflicts depend on the articles, shareholder agreement and local company law. Say so
  and recommend the company's lawyer or company secretary check resolutions and minutes.
- Treat board material as confidential; do not paste it into tools or records the founder did not choose.

## Related skills
- `topy-investor-relations` — investor updates that the board pack must agree with.
- `topy-decision-log` — the record of board decisions.
- `topy-risk-register` — the risks section.
- `topy-kpi-dashboard` — the scorecard page.
- `topy-stakeholder-alignment` — pre-wiring directors on a contentious item.
