---
name: topy-weekly-review
description: A weekly CEO review on TOPY.AI — what was decided, what moved, which risks grew, which experiments need a call — ending in next week's three priorities, recorded only with the founder's yes. Use when the user says things like "run my weekly CEO review"; "weekly review"; "what should I focus on next week?"; "how did this week go?"; "Friday review"; "set my priorities for next week". Needs the TOPY MCP server.
license: MIT
metadata:
  category: core
  tier: core
  version: 0.1.0
  docs: https://github.com/TOPY-AI-LTD/TOPY-AI-CEO-Skills/blob/main/plugins/topy-ai/skills/topy-weekly-review/SKILL.md
---
# Weekly CEO review

Once a week the founder steps back: what did we decide, what moved, what got riskier, what did we learn — and
what are the three things that matter next week. This skill reads the week's records in TOPY, writes the review,
proposes priorities, and saves a decision or journal entry only when the founder agrees.

## When to use
- "Weekly review", "what should I focus on next week", a Friday or Monday ritual.
- Before a board or investor update (then hand off to `topy-investor-relations`).
- Not for: today's to-do (`topy-daily`); a single big decision (`topy-decision-memo`).

## Before you start
- The project (`projects_list` if unknown). The review window: the last 7 days unless the founder says otherwise.
- Ask one question first: "What was the most important thing that happened this week, in your words?" Use the answer as the review's frame.

## Workflow
1. **Read the week** (filter by dates inside the window):
   - `decisions_list` → decisions with `decided_at` in the window.
   - `journal_entries_list` → entries with `happened_at` in the window; collect `wins`, `blockers`, `next_actions`.
   - `growth_experiments_list` → started, running, ended; results in `result_summary`.
   - `risks_list` → open risks; note any whose `risk_level` rose or that are high.
   - `gtm_plans_list` and `plans_list` → anything that changed the plan of record (a new plan version, a revision).
2. **Find the signal.** Answer four questions in one or two lines each:
   - What moved the company forward? (evidence: a decision, a result, a win)
   - What stalled, and why? (blockers that appeared twice or more are a pattern)
   - What did we learn? (an experiment result or a surprise)
   - What got riskier? (a risk that rose, or a new one)
3. **Pick next week's three priorities.** Rules:
   - Each must trace to something above (a blocker, a risk, an experiment, a plan goal) — say which.
   - Each has one owner and one measurable outcome by the end of next week ("signed LOI from 2 pilots", not "work on sales").
   - At most one may be "keep doing"; at least one must reduce the biggest risk or unblock the biggest blocker.
   - Name what you are deliberately **not** doing next week.
4. **Show the review** (below) and ask the founder to confirm or edit the priorities.
5. **Record (only with a yes).**
   - The priorities as a decision: `decision_create` with `title` "Priorities for week of <date>", `context` (the four answers), `options_considered` (the candidates you dropped), `decision` (the three), `rationale`, `confidence`.
   - Or a journal entry: `journal_entry_create` with `entry_type` "weekly_review", `wins`, `blockers`, `next_actions`.
   Each is a preview first; confirm only after the founder agrees.

## Output
```
## Week of <date> — <project>
**Frame:** <founder's one line>
**Moved:** …   **Stalled:** …   **Learned:** …   **Riskier:** …
**Next week**
1. <priority> — owner <name>, done when <outcome> (because <trace>)
2. …
3. …
**Not doing:** …
```
Under 250 words.

## Example
> **Frame:** "We finally got a pilot customer to say yes."
> **Moved:** pilot verbally agreed (journal 24 Oct). **Stalled:** pricing page — blocked twice on legal copy. **Learned:** founder-led LinkedIn posts drove 3 of 4 demo requests. **Riskier:** key-person risk (only the founder can run demos).
> **Next week:** 1. Pilot contract signed — founder, done when signed (traces to the win). 2. Record a demo video and train Sam to run demos — Sam, done when Sam runs one demo alone (key-person risk). 3. Ship pricing page with interim terms — Alex (blocker ×2).
> **Not doing:** the partner programme.

## Quality bar
- [ ] Every claim in Moved/Stalled/Learned/Riskier points to a record from this week.
- [ ] Exactly three priorities, each with owner, outcome and trace.
- [ ] A "not doing" line.
- [ ] Nothing saved without a preview and a yes.

## Guardrails
- Changes in TOPY take two calls: a preview, shown to the user, then `confirm: true` with the `confirmation` only after they agree. Never confirm for the user.
- Never invent progress, numbers or people; if the records are thin, say so and ask the founder instead.
- Don't close risks or experiments here; hand off to their skills.

## Related skills
- `topy-daily` — the daily version.
- `topy-decision-log`, `topy-founder-journal` — where the outcome is kept.
- `topy-investor-relations` — turn the week into an investor update.
