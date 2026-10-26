---
name: topy-founder-journal
description: 'Keep the founder''s dated journal and the AI CEO''s durable project memory in TOPY, and put each note in the right place so the CEO remembers facts without cluttering them with feelings. Use when the user says things like "journal today: rough day, lost the Acme deal"; "remember that we never offer discounts over 20%"; "what was I worried about last month?"; "what do you remember about this project?"; "forget what I said about the Berlin office"; "log my wins and blockers for the week". Needs the TOPY MCP server.'
license: MIT
metadata:
  category: core
  tier: core
  version: 0.1.0
  docs: https://github.com/TOPY-AI-LTD/TOPY-AI-CEO-Skills/blob/main/plugins/topy-ai/skills/topy-founder-journal/SKILL.md
---
# Founder journal and project memory

Two different stores, often confused. The journal is the founder's dated record of what happened and how it felt: private, reflective, never rewritten. Project memory is what the AI CEO should carry into every future conversation: short, current facts and preferences. This skill writes each note to the right store, keeps memory accurate as things change, and reads both back when the founder wants patterns or context.

## When to use
- The founder wants to write down a day, a week, a setback or a win.
- The founder says "remember", "always", "never", "from now on", or corrects something the CEO believes.
- Looking back: "what was I stuck on in September?", "what do you know about us?".
- Not for: a decision with options and rationale (`topy-decision-log`); a threat to the business (`topy-risk-register`); a source behind a claim (`topy-research-library`).

## Before you start
- Know the project (`projects_list`; can be left out with one project).
- `account_get` → `id`: `journal_entry_create` requires it as `author_user_id`; memory can take it as `created_by_user_id`.
- Before a memory write, `memories_list` to find an existing entry on the same subject: update it instead of adding a second, conflicting one.
- If TOPY tools are missing, run `topy-connect`.

## Workflow

### 1. Route the note

| The note is… | Goes to | Example |
|---|---|---|
| What happened, how it felt, what's next (dated) | journal | "Demo went badly; customer wants SSO" |
| A stable fact about the company | memory, `long_term` | "Sells to UK dental clinics, 1-10 chairs" |
| A standing preference or rule for the CEO | memory, `preference` | "Write in British English; amounts in GBP" |
| True for a while only | memory, `short_term` with `expires_at` | "Founder on leave until 15 Nov" |
| A choice between options | `topy-decision-log` | "Chose annual billing" |
| A threat | `topy-risk-register` | "Lead engineer may leave" |

If a note mixes several, split it and say where each part went.

### 2. Journal entry
Fields: `author_user_id`, `entry_type` (`daily_log` default; also `weekly_review`, `reflection`, `milestone`), `title`, `content` (required, the founder's words, lightly tidied only if asked), `mood_signal` (the founder's own word, or 1-5 if they use a scale), `wins`, `blockers`, `next_actions` (short lists), `happened_at` (when it happened, if not now).
- Draw out wins, blockers and next actions from what the founder said; do not add any they did not say.
- Preview `journal_entry_create`, show it, confirm with `confirm: true` and the `confirmation` only after a yes.

### 3. Memory entry
Fields: `memory_type`, `title` (the subject, e.g. "Pricing rule"), `content` (one fact, one or two sentences), `importance_score` (1-5: 5 = shapes every answer, 1 = nice to know), `source` (where it came from, e.g. `{"from": "founder", "said_on": "2026-10-26"}`), `expires_at` for temporary facts.
- One fact per entry, so it can be corrected or forgotten on its own.
- Existing entry on the subject: preview `memory_update` instead of creating a duplicate.
- Preview `memory_create`, show it, confirm after a yes.

### 4. Correct and forget
- "That's out of date": `memory_get`, then preview `memory_update` with the corrected `content` (and `metadata_json` sent whole if you change it).
- "Forget X": find the entry with `memories_list`, show it, say `memory_delete` is permanent and cannot be undone, preview, confirm on a yes. If the founder only wants it parked, set `expires_at` instead.
- Journal entries are the founder's history: read the entry with `journal_entry_get`, then fix a typo or add a line with `journal_entry_update` if asked, but do not rewrite the substance. `journal_entry_delete` only at the founder's explicit request, with the same permanence warning.

### 5. Read back
- Patterns: `journal_entries_list` for the period; group blockers that recur three or more times, wins, and how the mood signal moved. Quote the founder's own words.
- Memory: `memories_list`, grouped by type, highest importance first; flag expired entries and pairs that contradict each other, and offer to fix them.

### 6. Scheduled agents
A scheduled agent's key with a standing permission may add journal entries and memory without a preview, up to its daily cap. It can never update or delete either, and cannot confirm anything: corrections wait for the founder.

## Output
- Saved: "Journal (daily_log, 26 Oct): …" and/or "Remembered (preference, importance 4): …", only after the tool result confirms it.
- Read-back: `Theme | Times | First seen | Last seen | Founder's words`, or memory as `Type | Title | Content | Importance | Expires`.

## Example
Founder of Marrowbone Labs (a fictional pet-health app): "Long day. Vet chain pilot slipped to January because their IT wants a security review. Also, from now on never suggest Facebook ads, they never worked for us."
- Split: the pilot news → journal (`daily_log`, blocker "security review for vet chain", next action "send security questionnaire by Friday", mood "tired"); the ad rule → memory (`preference`, title "Channel rule", content "Do not suggest Facebook ads; the founder found they never worked", importance 4).
- `memories_list` shows no channel rule yet. Both previews shown; the founder approves; both confirmed. Agent also asks whether the slipped pilot is worth adding to the risk register.

## Quality bar
- [ ] Each note went to the right store; mixed notes were split and the split explained.
- [ ] Journal content is the founder's words; no invented wins, blockers or moods.
- [ ] Memory entries hold one fact each, with importance, source and expiry where it applies.
- [ ] No duplicate or contradicting memory left behind.
- [ ] Every write was previewed and confirmed only after a yes.

## Guardrails
- Changes in TOPY take two calls: a preview first, shown to the user, then `confirm: true` with the `confirmation` only after they agree. Never confirm for the user.
- The journal is private: never quote it into investor updates, plans or anything shared without the founder's permission.
- Do not store secrets (passwords, keys, card numbers) or sensitive personal data about other people in either store.
- Never invent facts for memory; a guess is not a memory.
- Deletes are permanent (risk W4): only on the founder's explicit request.
- If the journal shows signs of serious distress, respond as a person first and suggest talking to someone they trust or a professional.

## Related skills
- `topy-weekly-review` — turns the week's entries into next week's priorities.
- `topy-decision-log` — decisions that surface in the journal.
- `topy-scheduled-agent` — what an agent may write to the journal and memory on its own.
