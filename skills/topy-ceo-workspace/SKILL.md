---
name: topy-ceo-workspace
description: The founder's CEO records in TOPY.AI — decisions, risks, founder journal, go-to-market plans, growth experiments, research sources and project memory — and a weekly CEO review. Use when the user wants to log or review a decision, risk, experiment, GTM plan or research, remember something about the company, or run a weekly review.
---

# The CEO's workspace

Follow the shared rules in `topy-ai-ceo`. Every record kind has the same five tools:

| Records | List | Read | Add | Change | Delete (permanent) |
|---|---|---|---|---|---|
| decisions | `decisions_list` | `decision_get` | `decision_create` | `decision_update` | `decision_delete` |
| risks | `risks_list` | `risk_get` | `risk_create` | `risk_update` | `risk_delete` |
| founder journal | `journal_entries_list` | `journal_entry_get` | `journal_entry_create` | `journal_entry_update` | `journal_entry_delete` |
| GTM plans | `gtm_plans_list` | `gtm_plan_get` | `gtm_plan_create` | `gtm_plan_update` | `gtm_plan_delete` |
| growth experiments | `growth_experiments_list` | `growth_experiment_get` | `growth_experiment_create` | `growth_experiment_update` | `growth_experiment_delete` |
| research sources | `research_sources_list` | `research_source_get` | `research_source_create` | `research_source_update` | `research_source_delete` |
| project memory | `memories_list` | `memory_get` | `memory_create` | `memory_update` | `memory_delete` |
| investor contacts / updates | see `topy-fundraising` | | | | |

`topy help <tool>` (or the tool's schema) lists each record's fields.

- **Record what the user said**, in their words; don't pad. A decision has its context, the options
  considered and the reasoning; a risk its likelihood, impact and mitigation; an experiment its
  hypothesis, metric and result.
- Deletes can't be undone — prefer `_update` (e.g. a status) unless the user wants it gone.

## Weekly CEO review

1. Read `decisions_list`, `risks_list`, `growth_experiments_list` and `journal_entries_list`.
2. Summarise what was decided, what moved, which risks grew and which experiments need a call.
3. Propose the three priorities for next week. Offer to record a decision or a journal entry; save
   nothing until the user agrees.
