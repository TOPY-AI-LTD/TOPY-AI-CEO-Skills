---
name: topy-alerts
description: Set early-warning rules on KPIs in TOPY, work through the alerts they raise, and turn the serious ones into a corrective action, a risk or an incident. Use when the user says things like "tell me if MRR drops more than 10%"; "set an alert on churn"; "any alerts?"; "what's firing right now?"; "warn me when runway goes under 9 months"; "close that alert, it's fixed". Needs the TOPY MCP server.
license: MIT
metadata:
  category: core
  tier: core
  version: 0.1.0
  docs: https://github.com/TOPY-AI-LTD/TOPY-AI-CEO-Skills/blob/main/plugins/topy-ai/skills/topy-alerts/SKILL.md
---
# Alerts

A founder can't watch every number every day. This skill puts tripwires on the KPIs that matter, so TOPY raises an
alert when one crosses a line, and then works each alert through to an end: a corrective action, an explicit
"accept", a risk, or an incident. Rules are checked every time a KPI value is recorded, and a daily check flags KPIs
that have gone stale.

## When to use
- "Tell me if X drops", "set an alert", "any alerts?", "close that alert".
- After KPIs exist (`topy-kpi-dashboard`), ideally with automatic values (`topy-integrations`).
- Not for: the overall status (`topy-operating-board`); a running crisis (`topy-crisis-response`); a slow-moving risk with no number (`topy-risk-register`).

## Before you start
- The project (`projects_list`). `kpis_list`: the KPI must exist; note its `unit`, `metadata_json.key` and `higher_is_better`.
- `alert_rules_list`: avoid a second rule doing the same job.
- `kpi_values_list` for the KPI: the recent range, so the threshold isn't one that fires every week.

## Workflow

### 1. Set a rule
Turn the founder's words into one rule:

| Field | Meaning | Example |
|---|---|---|
| `kpi_id` | the KPI watched | MRR |
| `below` / `above` | absolute floor or ceiling | `runway_months` below 9 |
| `delta_pct` + `direction` | change versus the previous value | `mrr` down 10% |
| `severity` | `info`, `warn` or `critical` | |
| `notify` | who hears and how | founder, in the daily brief |

Severity guide: `critical` = cash, security or revenue loss that needs action today (runway under 6 months, MRR down 20%, `critical_vulns_open` above 0); `warn` = act this week; `info` = note in the brief. Check the threshold against the recent values and say how often it would have fired. Preview `alert_rule_create`, confirm after a yes. Change a rule with `alert_rule_get` then `alert_rule_update`; `alert_rule_delete` is permanent (two calls).

### 2. Triage open alerts
`alerts_list` with `status: open`, critical first. For each:
1. **Scope.** Which KPI, how far past the line, which objectives depend on it (`topy-operating-board`).
2. **Acknowledge.** `alert_ack` (preview, then confirm) so it is not raised again while being worked.
3. **Decide**, one of:
   - **Corrective action**: name the owner and the action; record it with `topy-decision-log` or a task.
   - **Accept**: the founder decides the deviation is fine for now; record why.
   - **Escalate to a risk**: a lasting threat → `risk_create` with the alert as evidence.
   - **Escalate to an incident**: something broke (outage, breach, a key customer lost) → `incident_create` with `incident_type`, `severity`, `summary`, `impact`, then `topy-crisis-response`.
4. **Resolve** when the KPI is back inside the line or the decision is recorded: `alert_resolve` with `resolution` saying what was done. Never resolve to make the list shorter.

A critical alert needs a corrective action or an explicit accept within 24 hours.

## Output
```
## Alerts — <project>
Open: <n> (<c> critical)
| Severity | KPI | Value vs line | Since | Proposed handling |
Rules added/changed: …
```

## Quality bar
- [ ] Every rule names a KPI, a line and a severity; it was checked against recent values.
- [ ] Every critical alert has an owner and an action or an accept.
- [ ] Resolutions state what changed.
- [ ] Nothing written without a preview and a yes.

## Guardrails
- Changes in TOPY take two calls: a preview first, shown to the user, then `confirm: true` with the `confirmation` only after they agree. Never confirm for the user.
- Numbers only from tools; an alert's value comes from a KPI value with a `source`. Don't guess why a number moved; say what evidence is needed.
- Changing a goal or target because an alert fired is D2: preview and the founder's yes, never under a standing permission.
- Records extracted from the plan carry an `origin`; say so before changing one the founder has edited.
- Notifying anyone outside TOPY (customers, investors, the public) is approved one message at a time. A data breach may carry a legal reporting deadline: tell the founder to call a lawyer.

## Related skills
- `topy-kpi-dashboard` — the KPIs alerts watch.
- `topy-integrations` — values arriving on time so alerts fire on time.
- `topy-risk-register`, `topy-crisis-response` — where escalated alerts go.
- `topy-operating-board` — the full status around an alert.
