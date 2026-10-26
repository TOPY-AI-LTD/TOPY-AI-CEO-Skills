---
name: topy-risk-register
description: 'Keep the project''s risk register in TOPY: score likelihood and impact, name an owner and a mitigation, review on a cadence, and close risks by status, never by deleting them. Use when the user says things like "what are our biggest risks?"; "add a risk: our only supplier might fold"; "review the risk register"; "this risk is gone now, close it"; "rescore the churn risk"; "which risks have no owner?". Needs the TOPY MCP server.'
license: MIT
metadata:
  category: core
  tier: core
  version: 0.1.0
  docs: https://github.com/TOPY-AI-LTD/TOPY-AI-CEO-Skills/blob/main/plugins/topy-ai/skills/topy-risk-register/SKILL.md
---
# Risk register

A risk register is useful only if it is honest, scored the same way every time, and looked at on a schedule. This skill keeps the project's risks in TOPY with a consistent likelihood × impact score, one owner and a concrete mitigation each, and a review date that matches how dangerous the risk is. Risks leave the register by changing status, so the history shows what the company faced and how it dealt with it.

## When to use
- The founder names a worry, a dependency or a threat, or a review surfaces one.
- A weekly or monthly risk review; before a board meeting or investor update.
- Something changed (a competitor raised, a key customer wobbled): rescore.
- Not for: a risk that has already happened (`topy-crisis-response`); a technical security audit (a security specialist); deciding a mitigation with big trade-offs (`topy-decision-memo`, then log it in `topy-decision-log`).

## Before you start
- Know the project (`projects_list`; can be left out with one project).
- `risks_list` first, so a new risk is not a duplicate and the scale matches what is already there.
- `owner_user_id` takes a TOPY user id only (`account_get` gives the founder's `id`). If the owner is someone without a TOPY account, put their name in `metadata_json.owner_name`.
- If TOPY tools are missing, run `topy-connect`.

## Workflow

### 1. Describe the risk
- `title`: cause → effect, e.g. "Single payment processor freezes payouts → 4 weeks without revenue".
- `category`: one of `market`, `product`, `execution`, `financial`, `fundraising`, `people`, `legal`, `technical`, `supplier` (keep what the register already uses).
- `description`: the trigger or early warning sign, and what is exposed.

### 2. Score
`likelihood_score` and `impact_score` are integers 1-5:

| Score | Likelihood (next 12 months) | Impact |
|---|---|---|
| 1 | under 5% | annoyance, under a week of lost work |
| 2 | 5-20% | a month's delay or under 5% of revenue |
| 3 | 20-50% | a quarter's delay, 5-15% of revenue, a key hire lost |
| 4 | 50-80% | runway cut by a third, the main customer lost |
| 5 | over 80% | the company may not survive |

Score = likelihood × impact. Set `risk_level` from it: 1-4 `low`, 5-9 `medium`, 10-15 `high`, 16-25 `critical`. Score as the founder judges it today, not the hoped-for state after mitigation; put that in `metadata_json.residual_score`.

### 3. Owner, mitigation, cadence
- One owner per risk (`owner_user_id` or `metadata_json.owner_name`). "Everyone" is no one.
- `mitigation_plan`: an action with a date ("sign a second processor by 30 Nov"), plus a contingency if it happens anyway.
- Review cadence by level, stored in `metadata_json`: critical weekly, high every 2 weeks, medium monthly, low quarterly. Example `{"next_review_on": "2026-11-09", "review_every_days": 14, "early_warning": "payout delay over 3 days", "residual_score": 6}`.

### 4. Save
Preview `risk_create` (`status` defaults to `open`), show it, confirm with `confirm: true` and the `confirmation` only after the founder agrees. A scheduled agent's key with a standing permission may add risks without a preview up to its daily cap; it can never update, close or delete one.

### 5. Review
1. `risks_list`; sort by score, then by `next_review_on`.
2. Flag: critical or high risks without a mitigation date; unowned risks; reviews overdue; scores unchanged for 3 reviews while the mitigation is "in progress".
3. For each risk reviewed, ask what changed. Rescore only with evidence the founder gives.
4. Changes: read with `risk_get`, merge into the existing `metadata_json` (it is replaced whole), preview `risk_update`, confirm on a yes.

### 6. Leaving the register
Change `status`, never delete:
- `mitigating`: work under way.
- `accepted`: the founder chose to live with it; record why in `metadata_json.accepted_reason`.
- `closed`: no longer applies; record why and the date.
- `occurred`: it happened; hand over to `topy-crisis-response`.
`risk_delete` is only for a duplicate or an entry made by mistake. Say it is permanent and cannot be undone, then follow the two-call rule.

## Output
Register table: `# | Risk | Category | L | I | Score | Level | Owner | Mitigation (due) | Next review | Status`, sorted by score; then "Needs attention" (overdue, unowned, no mitigation) and changes proposed.

## Example
Founder of Cobblestone Freight (a fictional same-day courier app): "Add a risk: our only van leasing partner might pull out."
- `risks_list` shows 6 risks, none about leasing. Agent asks how likely (founder: "they renegotiate yearly; maybe 1 in 4") and what it would cost (founder: "we'd lose half our capacity for a month").
- Scored likelihood 3, impact 4 → 12, `high`; category `supplier`; owner the founder; mitigation "quote from a second leasing firm by 20 Nov"; review every 14 days.
- Preview shown, founder agrees, confirmed. Three weeks later a second lease is signed: likelihood drops to 1, score 4, status `mitigating` → `closed` with the reason, previewed and confirmed.

## Quality bar
- [ ] Every risk has a cause → effect title, both scores, a level that matches the score, one owner and a dated mitigation.
- [ ] Scores use the same 1-5 scale as the rest of the register.
- [ ] Next review date set according to the level.
- [ ] No closed risk without a written reason.
- [ ] `metadata_json` sent whole on update.
- [ ] Every write was previewed and confirmed only after a yes.

## Guardrails
- Changes in TOPY take two calls: a preview first, shown to the user, then `confirm: true` with the `confirmation` only after they agree. Never confirm for the user.
- Never delete a risk to make the register look better, and never lower a score without new evidence. A register with no high risks in an early-stage company is a warning sign: say so.
- Never invent probabilities, amounts or events; label the founder's estimates as estimates.
- Deletes are permanent (risk W4): duplicates and mistakes only.
- Legal, regulatory and insurance risks: say when a lawyer or broker should look at them.

## Related skills
- `topy-crisis-response` — when a risk has occurred.
- `topy-decision-log` — record the choice to accept or mitigate a big risk.
- `topy-daily` — surfaces open risks needing a call.
- `topy-board-meetings` — the top risks go into the board pack.
