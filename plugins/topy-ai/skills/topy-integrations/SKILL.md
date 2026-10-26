---
name: topy-integrations
description: Connect data sources (Stripe, QuickFile) to TOPY through the founder's dashboard, bind KPIs to them, and sync so actuals arrive on their own with their source. Use when the user says things like "connect Stripe"; "update MRR automatically"; "which data sources are connected?"; "sync our numbers now"; "stop me typing in the KPIs every week"; "hook up Google Analytics to signups". Needs the TOPY MCP server.
license: MIT
metadata:
  category: core
  tier: core
  version: 0.1.0
  docs: https://github.com/TOPY-AI-LTD/TOPY-AI-CEO-Skills/blob/main/plugins/topy-ai/skills/topy-integrations/SKILL.md
---
# Data integrations

KPIs typed in by hand go stale, and stale KPIs turn the operating board grey. This skill connects the founder's
sources (Stripe, the accounting ledger, GA4…) to TOPY, binds each KPI to the source and query that produces it, and
runs a sync, so actuals arrive on their own with their source attached. Connecting happens on TOPY's own secure
page: the agent only hands over the link.

## When to use
- "Connect Stripe", "update MRR automatically", "sync now", "what's connected?"
- When `topy-operating-board` shows KPIs as stale, or `topy-monthly-close` keeps asking for the same figures.
- Not for: designing KPIs (`topy-kpi-dashboard`); connecting the agent itself to TOPY (`topy-connect`).

## Before you start
- The project (`projects_list`). `integrations_list`: what is already connected (credentials are never returned).
- `kpis_list`: which KPIs could come from the source; note each `metadata_json.key`.
- Never ask for API keys, passwords or OAuth codes in chat, and never accept them if pasted; tell the founder to revoke a key they pasted.

## Workflow
1. **Pick the source per KPI** (standard keys):

| KPI key | Usual provider | Query |
|---|---|---|
| `mrr`, `active_subscriptions`, `new_customers`, `churn_rate_monthly` | `stripe` | same name |
| `revenue_monthly` | `stripe` (card revenue) or `quickfile` (turnover in the books) | `revenue_monthly` |
| `cash_balance`, `net_burn`, `gross_margin` | `quickfile` (bank balances; the month's loss; margin after cost of sales) | same name |

   Those are the only providers and queries today (`integrations_list` shows them). Anything else (GA4 signups,
   NRR) stays founder-reported or comes from the cofounder who owns it.
2. **Connect.** `integration_connect_link` with the provider returns a link to TOPY's dashboard. Give the founder the link; they sign in or paste the key there. When they're back, `integrations_list` to confirm it shows as connected. Don't report it connected until it does.
3. **Bind KPIs.** `kpi_source_set` per KPI with `{provider, query}` (e.g. `{provider: "stripe", query: "mrr"}`). Preview the list of bindings, confirm after a yes. If a KPI was founder-reported, say that future values will come from the provider instead.
4. **Sync.** `integration_sync` with the provider (preview, then confirm). It runs as a job and records KPI values with `source` set to the provider. Then `kpi_values_list` for each bound KPI: show the new values.
5. **Check against what was there.** Where a synced value replaced a founder-reported one for the same period, show both; a difference over 5% gets a line of explanation (definition mismatch, timing) before anyone relies on it.
6. **Next.** Offer `topy-alerts` on the KPIs that now update themselves.

## Output
```
## Integrations — <project>
Connected: <providers>
| KPI | Provider | Query | Latest value (as of) |
Unbound KPIs (founder-reported): …
Differences to check: …
```

## Quality bar
- [ ] No credential requested or handled in chat.
- [ ] "Connected" only after `integrations_list` shows it.
- [ ] Every bound KPI shows a synced value or a reason it has none.
- [ ] Replaced founder figures are shown side by side.
- [ ] No binding or sync without a preview and a yes.

## Guardrails
- Changes in TOPY take two calls: a preview first, shown to the user, then `confirm: true` with the `confirmation` only after they agree. Never confirm for the user.
- Connecting is 🔒: the founder does it on TOPY's dashboard page. The agent never asks for, stores or repeats keys or passwords.
- Numbers only from tools; synced values carry `source` set to the provider and founder-given values `source: founder`. Never "correct" a synced figure by hand without saying so.
- Goal and target changes are D2: preview and the founder's yes, never under a standing permission.
- Records extracted from the plan carry an `origin`; say so before changing one the founder has edited.
- Anything sent outside TOPY is confirmed one send at a time; this skill only reads from sources and never moves money.

## Related skills
- `topy-kpi-dashboard` — create the KPIs to bind.
- `topy-monthly-close` — uses synced actuals.
- `topy-alerts` — rules on KPIs that now update themselves.
- `topy-operating-board` — where stale KPIs show up.
