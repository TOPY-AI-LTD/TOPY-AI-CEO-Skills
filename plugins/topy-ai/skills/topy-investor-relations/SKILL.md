---
name: topy-investor-relations
description: Keep a founder's investor pipeline and follow-ups in TOPY, and draft, approve and save the periodic investor update from the project's own records. Use when the user says things like "who do I need to follow up with?"; "add this investor to my pipeline"; "move Northgate to meeting stage"; "write this month's investor update"; "where does my raise stand?"; "an investor passed, log it". Needs the TOPY MCP server.
license: MIT
metadata:
  category: core
  tier: core
  version: 0.1.0
  docs: https://github.com/TOPY-AI-LTD/TOPY-AI-CEO-Skills/blob/main/plugins/topy-ai/skills/topy-investor-relations/SKILL.md
---
# Investor relations

A raise is won on follow-through: the right next step with each investor on the right day, and a steady monthly update that makes existing and prospective investors feel the company moving. This skill keeps the pipeline in TOPY's investor contacts, surfaces who is overdue, and turns the project's decisions, experiments, journal and risks into an update the founder approves before it is saved.

## When to use
- The founder asks who to chase, adds or moves an investor, or logs a pass.
- Month end (or quarter end): time for the investor update.
- Before a partner meeting, to read back everything recorded about one fund.
- Not for: deciding how much to raise and from whom (`topy-fundraising-strategy`); the board pack and minutes (`topy-board-meetings`); the pitch narrative (`topy-pitch-deck`).

## Before you start
- Know the project. Call `projects_list` if the founder has several; with one project `project_id` can be left out.
- Read before writing: `investor_contacts_list` for the pipeline, `investor_updates_list` for the last update sent.
- If TOPY tools are missing, run `topy-connect` first.
- Ask one question at a time. Never ask for passwords or keys, and never ask for investor data the founder does not need (home address, personal phone, family details).

## Workflow

### 1. Agree the stage vocabulary
`status` is free text; keep it consistent so the pipeline can be counted. Use these unless the founder already has their own (check existing records first):

| status | Meaning | Typical next step |
|---|---|---|
| `lead` (default) | On the list, no contact yet | find a warm intro |
| `intro_requested` | Someone asked to introduce | chase the introducer in 5 working days |
| `contacted` | First email or call done | book the first meeting |
| `meeting` | In conversation | send follow-up material within 24 hours |
| `diligence` | Asked for the data room or a deep dive | answer open questions; agree a decision date |
| `term_sheet` | Terms on the table | lawyer review; `topy-term-sheet` |
| `committed` / `closed` | Verbal yes / money in | paperwork; add to the update list |
| `passed` / `not_now` | No, or not this round | log the reason; ask permission to keep them updated |

### 2. Keep each contact lean
Fields: `name`, `fund_name`, `email`, `stage_focus`, `thesis_tags`, `status`, `notes`, `metadata_json`. Put follow-up tracking in `metadata_json`, for example `{"next_step": "send cohort data", "follow_up_on": "2026-11-04", "last_contact_on": "2026-10-28", "intro_via": "Priya (angel)", "pass_reason": null}`.
- `notes` hold what helps the raise: what they asked, what they care about, their objection. Not gossip, not personal life.
- `metadata_json` is replaced as a whole on update: read the contact with `investor_contact_get`, merge your change, send the full object.

### 3. Pipeline review
`investor_contacts_list`, then show:
1. Overdue: `follow_up_on` before today, oldest first, with the exact next step.
2. Due this week.
3. Count by stage, and any contact stuck in one stage for more than 21 days (by `updated_at`).
Propose updates (new status, new `follow_up_on`) as a short list; preview each with `investor_contact_update` and confirm only the ones the founder approves.

### 4. Add or move a contact
Preview `investor_contact_create` / `investor_contact_update`, show the preview, wait for a yes, then call again with `confirm: true` and the `confirmation`. The confirmation runs exactly what was previewed: if the founder edits anything, get a new preview.

### 5. Draft the investor update
1. Find the last sent update (`investor_updates_list`, newest `sent_at`) and read it with `investor_update_get` for its numbers and asks; then read what happened since: `decisions_list`, `growth_experiments_list`, `journal_entries_list`, `risks_list`.
2. Ask the founder for the headline numbers for the period (revenue or MRR, users, burn, runway). TOPY records do not hold verified financials: never infer them.
3. Draft in this order: headline (one sentence) · numbers (with change vs last period) · highlights · lowlights and what is being done · key decisions · what experiments taught us · top risks · asks (specific: "intro to a head of ops at a UK clinic group") · thanks.
4. Leave out anything from the journal the founder has not cleared for investors.
5. Show the full draft. After the founder approves the text, preview `investor_update_create` with `update_type` (`monthly` default, or `quarterly`), `subject`, `content`, `payload_json` (e.g. `{"period": "2026-10", "metrics": {...}, "asks": [...]}`) and `status: "draft"`; confirm on a yes.
6. TOPY does not send email. Once the founder has sent it, preview `investor_update_update` with `status: "sent"` and `sent_at`.

### 6. Removing someone
Prefer `investor_contact_update` with `status: "passed"` or `"not_now"`: the history stays. Use `investor_contact_delete` only when the investor asks to be removed or the founder wants their personal data gone. Say plainly that delete is permanent and cannot be undone, then follow the two-call rule.

## Output
- Pipeline: table `Investor | Fund | Stage | Last contact | Next step | Due`, overdue first, then stage counts.
- Update: the full text under its subject line, then "Saved as draft in TOPY" only when the tool result says so.

## Example
Founder of Brindle Loop (a fictional UK B2B scheduling startup): "Who do I chase, and draft October's update."
- `investor_contacts_list` → 14 contacts. Overdue: Dana Reyes (Halden Ventures, `meeting`, follow-up 2026-10-21, "send pilot retention numbers"). Stage counts: 6 lead, 3 contacted, 3 meeting, 1 diligence, 1 passed.
- Agent proposes moving Halden's follow-up to 2026-10-29 once the numbers are sent; founder agrees; preview → confirm.
- For the update, the agent reads 3 decisions, 2 finished experiments and 1 new high risk, asks for the numbers (MRR £8.4k, up from £7.1k; runway 11 months), drafts, and saves it as a draft after the founder approves the text.

## Quality bar
- [ ] Every figure in the update came from the founder or a TOPY record, and is labelled with its period.
- [ ] Overdue follow-ups listed first, each with a concrete next step and date.
- [ ] Stage names match the existing records.
- [ ] Asks are specific enough that an investor can act on them in one reply.
- [ ] No journal content in the update without the founder's say-so.
- [ ] Every write was previewed and confirmed only after a yes; the close lists only writes the tools confirmed.

## Guardrails
- Changes in TOPY take two calls: a preview first, shown to the user, then `confirm: true` with the `confirmation` only after they agree. Never confirm for the user.
- Investor tools are not covered by standing permissions: a scheduled agent's key cannot add or change contacts or updates. Leave those for the founder.
- Never invent investors, funds, commitments, valuations or figures. A rumour of interest is not `committed`.
- Investor contacts hold third-party personal data: keep work email, fund and what the raise needs. No personal phone, address, social profiles or private remarks.
- Never describe a deal as closed, or an amount as raised, before the founder confirms it.
- Not legal or investment advice: term sheets and securities rules go to a lawyer.
- Deletes are permanent (risk W4). Prefer a status change.

## Related skills
- `topy-fundraising-strategy` — the raise plan this pipeline executes.
- `topy-board-meetings` — board packs reuse the update's numbers and decisions.
- `topy-decision-log` — log the key decisions the update reports.
- `topy-risk-register` — the risks section of the update.
