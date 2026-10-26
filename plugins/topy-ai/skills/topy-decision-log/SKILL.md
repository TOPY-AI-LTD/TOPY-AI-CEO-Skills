---
name: topy-decision-log
description: Record a founder's decisions in TOPY with context, options, rationale, confidence and a review date, and later review them against what actually happened. Use when the user says things like "log this decision"; "we decided to drop the free plan, record it"; "why did we choose Stripe over Paddle?"; "which decisions are due for review?"; "did that decision work out?"; "show me what we decided this quarter". Needs the TOPY MCP server.
license: MIT
metadata:
  category: core
  tier: core
  version: 0.1.0
  docs: https://github.com/TOPY-AI-LTD/TOPY-AI-CEO-Skills/blob/main/plugins/topy-ai/skills/topy-decision-log/SKILL.md
---
# Decision log

Founders make dozens of consequential calls a month and remember the reasoning behind almost none of them. This skill writes each decision down while the reasoning is fresh, sets a date to look back, and on that date compares what was expected with what happened. The result is a searchable record of why the company is the way it is, and a founder who gets better at deciding.

## When to use
- The founder states a decision ("we're going annual-only"), or a conversation ends in one.
- Before revisiting an old choice: read the record first.
- Weekly or monthly: decisions whose review date has passed.
- Not for: working out what to decide (`topy-decision-memo`, `topy-debiasing`); a risk that is not yet a decision (`topy-risk-register`); a test with a metric (`topy-growth-experiments`).

## Before you start
- Know the project (`projects_list`; can be left out with one project).
- `decisions_list` first: the decision may already be logged, or contradict an earlier one.
- `account_get` gives the founder's user `id` for `decided_by_user_id`. That field takes a TOPY user id only; if someone else decided, name them in `metadata_json`.
- If TOPY tools are missing, run `topy-connect`.

## Workflow

### 1. Capture
Ask only for what is missing, one question at a time. Map to the fields:

| Field | What goes in | Good example |
|---|---|---|
| `title` | The decision as a short statement | "Annual-only billing for new customers" |
| `context` | The situation and constraint that forced the choice | "Monthly churn 6%; cash needs to last to the seed round" |
| `options_considered` | Every real option, including doing nothing, each with its main trade-off | `["Keep monthly: easy sales, high churn", "Annual-only: cash up front, slower close", "Discounted annual: middle"]` |
| `decision` | What was chosen, with scope and start date | "Annual-only for all new sign-ups from 1 Nov" |
| `rationale` | Why this option beat the others | "Cash matters more than speed this half" |
| `confidence` | `low`, `medium` or `high` (or a %), as the founder feels it | `medium` |
| `impact_scope` | What it touches | `["pricing", "sales", "cash"]` |
| `decided_at` | When it was decided | `2026-10-24T10:00:00Z` |
| `metadata_json` | Review fields (below) | |

Put the review fields in `metadata_json`: `{"review_on": "2027-01-24", "expected_outcome": "churn under 3%, close rate down no more than 20%", "change_my_mind_if": "close rate falls 40%", "reversibility": "two-way"}`.

### 2. Set the review date
- Two-way door (cheap to reverse): 4-6 weeks.
- One-way door (hiring, pricing public, a market exit): 3 months, and a mid-point check.
- No review date means the record cannot teach anything: always set one.

### 3. Save
Preview `decision_create`, show the preview with the full record, and confirm with `confirm: true` and the `confirmation` only after the founder agrees. A scheduled agent with a standing permission can add decisions without a preview up to its daily cap; that key can never confirm or change anything else.

### 4. Review
1. `decisions_list`; pick records whose `metadata_json.review_on` is today or earlier and that have no `verdict`.
2. For each, read it back and ask what happened. Use only the founder's account or other TOPY records as evidence.
3. Grade two things separately:

| | Good outcome | Bad outcome |
|---|---|---|
| Sound process (options, evidence, rationale held up) | earned it | bad luck: keep the method |
| Weak process | luck: do not repeat the method | learn: what was missing? |

4. Read the record with `decision_get`, merge `{"outcome": "...", "verdict": "sound/lucky/unlucky/weak", "reviewed_on": "...", "lesson": "..."}` into the existing `metadata_json`, and preview `decision_update` with the whole object (it replaces the old one).

### 5. Changing a decision
Log the new decision as its own record, then update the old one's `metadata_json` with `"superseded_by": "<new id>"`. Never rewrite the original reasoning after the fact.
`decision_delete` is only for a duplicate or a record made by mistake. Say it is permanent and cannot be undone, then use the two-call rule.

## Output
- New record: the table above filled in, then "Logged" only when the tool result confirms it.
- Review: `Decision | Decided | Expected | Happened | Verdict | Lesson`, then any decision to revisit.

## Example
Founder of Pellucid Tea Co. (a fictional subscription tea brand): "We're stopping wholesale to focus on direct subscriptions. Log it."
- `decisions_list` shows no earlier wholesale decision. Agent asks for the options considered, then the reason.
- Record: title "Stop wholesale; direct subscriptions only", context "Wholesale is 30% of revenue at 18% margin; ops time split", options keep both / wholesale only / direct only, rationale "margin and focus", confidence `medium`, `review_on` 2027-01-31, expected "direct revenue replaces wholesale within 3 months".
- Preview shown, founder says yes, confirmed. In January the review finds direct revenue replaced 70%: verdict "sound, partly met", lesson "allow 6 months for channel shifts".

## Quality bar
- [ ] At least two real options, including doing nothing when it was viable.
- [ ] Rationale says why the chosen option beat the others, not just why it is good.
- [ ] A review date and an expected outcome someone could check.
- [ ] Confidence is the founder's, not the agent's.
- [ ] Reviews keep decision quality and outcome apart.
- [ ] `metadata_json` sent whole on update; nothing previously stored lost.

## Guardrails
- Changes in TOPY take two calls: a preview first, shown to the user, then `confirm: true` with the `confirmation` only after they agree. Never confirm for the user.
- Never invent options, figures or outcomes the founder did not give; label assumptions as assumptions.
- Never edit an old record's context or rationale to fit hindsight; supersede it.
- Deletes are permanent (risk W4): only for duplicates or mistakes, and only after a clear yes.
- Not legal or tax advice: decisions with legal or tax effect should be checked by a professional.

## Related skills
- `topy-decision-memo` — structure a hard call before logging it.
- `topy-weekly-review` — reviews due decisions each week.
- `topy-debiasing` — pre-mortem for one-way-door decisions.
- `topy-risk-register` — risks a decision creates or closes.
