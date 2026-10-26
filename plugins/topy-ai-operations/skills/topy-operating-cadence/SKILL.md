---
name: topy-operating-cadence
description: Set the company's rhythm of weekly, monthly, quarterly and annual meetings, each with an owner, inputs, a timed agenda and the decisions it exists to make. Use when the user says things like "we have too many meetings and still nothing gets decided"; "set up a weekly leadership meeting"; "what meetings should a 10-person startup have?"; "design our monthly business review"; "how do we run quarterly planning?"; "we keep finding out about problems too late". Uses TOPY when it is connected.
license: MIT
metadata:
  category: operations
  tier: connected
  version: 0.2.0
  docs: https://github.com/TOPY-AI-LTD/TOPY-AI-CEO-Skills/blob/main/plugins/topy-ai-operations/skills/topy-operating-cadence/SKILL.md
---
# Operating cadence

Designs the small set of recurring forums a startup runs on, so information arrives while it can still be
acted on and decisions have a regular home. Each forum gets one owner, a fixed timed agenda, an input pack
prepared beforehand and a short list of the decisions it exists to make. Meetings that do none of that are
cut. With TOPY connected each forum becomes a meeting record in TOPY, the rules go into project memory, and
the recurring CEO work (daily brief, weekly review, monthly close) is suggested as scheduled routines.

## When to use
- Too many meetings, or the wrong ones; problems surface late; priorities change every week; a new
  leadership team is forming; the company passes a size where hallway updates stop working.
- Not for: running a single week's review (use `topy-weekly-review`) or daily check-in (use `topy-daily`);
  choosing the metrics on the scorecard (use `topy-kpi-dashboard`); the board meeting itself (use
  `topy-board-meetings`).

## Before you start
- Ask one question at a time: team size and leadership; meetings today with length and attendees; what
  metrics and plans exist; fixed external dates.
- With TOPY connected, call `memories_list` first to see whether a cadence or meeting rules were saved
  before; build on them instead of starting over. `tasks_list` (status `todo`) shows how many follow-ups
  meetings already generate and how many are overdue: a sign of forums that decide without closing the loop.
- Without TOPY, ask the founder to paste the current calendar of recurring meetings.

## Workflow
1. **Audit what exists.** For every recurring meeting list: owner, frequency, length, attendees, person-hours
   per month (length × attendees × occurrences), and the last decision it made. A meeting with no decision in
   its last four occurrences is a candidate to cut or turn into a written update.
2. **Pick the forums by stage** (rule of thumb):
   | Team size | Minimum cadence |
   |---|---|
   | 2-5 | Weekly founders' meeting; monthly metrics and cash check; quarterly priorities |
   | 6-25 | Above, plus weekly all-hands (short), weekly 1:1s, monthly business review, quarterly planning |
   | 25+ | Above, plus team-level weeklies feeding leadership, quarterly board/strategy offsite, annual plan |
3. **Write each forum's contract:** purpose in one line, decisions it owns, owner, attendees (deciders and
   needed contributors only), input pack and its deadline, output and where it is recorded.
4. **Use these default agendas** and adjust lengths to team size.
   **Weekly leadership (60 min)**
   - 0-10 · Scorecard: each metric owner reports only reds and changes (no reading of greens).
   - 10-20 · Priorities: last week's commitments done / not done, one line each.
   - 20-50 · Issues: the 2-3 items pre-submitted, highest impact first; each ends in a decision, an owner
     and a date, or an explicit "parked until <date>".
   - 50-60 · Commitments and messages: who does what by next week; what is cascaded to teams.
   **Monthly business review (90 min)**
   - 0-20 · Financials and runway vs plan (finance owner).
   - 20-50 · Each function: outcome vs target, cause of the largest gap, what changes next month.
   - 50-75 · One deep dive chosen a week ahead (a cohort, a channel, a process).
   - 75-90 · Decisions, risks to add or close, update of the forecast.
   **Quarterly planning (half day to a day)**
   - Review: last quarter's goals scored honestly, what was learned.
   - Context: market, customers, cash, risks.
   - Choose 3-5 company priorities and their owners; explicitly list what will not be done.
   - Translate into team goals and capacity; agree how progress shows on the scorecard.
   **Weekly 1:1 (30 min)**, report's agenda first: their topics, then priorities, blockers, feedback both ways.
   **All-hands (30 min)**: wins, numbers, priorities, one decision explained, open questions.
5. **Fix the inputs.** The pack is due before the meeting (rule of thumb: 24 hours for weeklies, 2-3 working
   days for monthly and quarterly). No pack, no agenda slot. Pre-reads are read before, not during.
6. **Keep the time budget honest.** Total the person-hours per month of the new cadence against the old.
   Leadership time in recurring meetings above roughly a fifth of the week is worth questioning (rule of thumb).
7. **Lay out the calendar.** Weeklies early in the week so the week can still change; monthly review after
   the books close; quarterly planning finished before the quarter starts; board meetings after a monthly review.
8. **Set the review.** After 6 weeks ask each attendee: which forum produced decisions, which was theatre.
   Adjust once, then hold the rhythm for a quarter.
9. **Save it** (connected; each write a preview, confirmed only after the founder agrees):
   - The rules (forums, owners, days, agenda rules) with `memory_create` (`memory_type: preference`) so
     `topy-weekly-review` and later sessions follow it.
   - The next occurrence of each forum with `meeting_create`: `meeting_type` (`team` for internal forums,
     `board` or `investor` for those), `title`, `scheduled_at`, `attendees`, `agenda` (the timed items),
     `status: "planned"`. Put the recurrence ("weekly, Monday 09:30") in the title or agenda notes.
10. **Suggest routines, the AI CEO's side of the rhythm** (01 §4): daily brief at 07:30 (`topy-daily`),
    weekly review on Friday (`topy-weekly-review`), monthly close on the first working day
    (`topy-monthly-close`), quarterly planning two weeks before quarter end (`topy-okrs`). Each is a scheduled
    agent with its own standing permission, set up with `topy-scheduled-agent`; this skill only proposes them.

## Output
```
Operating cadence: <company> · <team size> · <date>
| Forum | Purpose | Decisions it owns | Owner | When | Length | Attendees | Input pack (due) | Output recorded in |
Agendas: one timed agenda per forum
Cut or merged: <meeting> → <cut | merged into X | async update>, hours saved/month
Time budget: before <h>/month · after <h>/month
Review: <date>, questions to ask
```

## Quality bar
- Every forum owns at least one named decision; none exists only to share status that could be written.
- Each agenda is timed and ends with owners and dates.
- Inputs have deadlines and owners; the calendar order lets one forum feed the next.
- The cadence costs no more leadership time than before, or the increase is justified.
- At least one existing meeting was cut, merged or made asynchronous, or the audit shows why not.

## Guardrails
- Changes in TOPY take two calls: a preview first, shown to the user, then `confirm: true` with the
  `confirmation` only after they agree. Never confirm for the user.
- Calendar invitations are not sent from TOPY: the founder sends them. Never set up a standing permission
  for the founder; that happens in the dashboard (`topy-scheduled-agent`).
- Never invent research on meeting productivity; time thresholds are rules of thumb.
- Respect time zones and working-time rules; for statutory works councils, union consultation or board
  procedures, say that a lawyer or company secretary should confirm requirements.
- Do not store personal or sensitive information about individuals in project memory.

## Related skills
- `topy-weekly-review` — runs the weekly review inside this cadence.
- `topy-daily` — the founder's daily check-in.
- `topy-kpi-dashboard` — the scorecard the weekly forum reads.
- `topy-okrs` — the quarterly goals the planning forum sets.
- `topy-board-meetings` — the board forum and its pack.
- `topy-monthly-close` — the monthly finance forum's input.
- `topy-scheduled-agent` — run the CEO routines on a schedule.
