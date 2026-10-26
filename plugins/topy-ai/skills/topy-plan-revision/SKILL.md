---
name: topy-plan-revision
description: Carry a change — a funding amount, price, milestone, KPI, hire or team change — through every affected section of a TOPY.AI business plan, consistently, as a new version. Use when the user says things like "we're raising £250k now, not £200k"; "push the launch to Q3 2027"; "add a CTO hire to the plan"; "change the target to 300 customers"; "update the plan, our pricing changed"; "the numbers in the plan are out of date". Needs the TOPY MCP server.
license: MIT
metadata:
  category: core
  tier: core
  version: 0.1.0
  docs: https://github.com/TOPY-AI-LTD/TOPY-AI-CEO-Skills/blob/main/plugins/topy-ai/skills/topy-plan-revision/SKILL.md
---
# Revise a plan for a change

When the company changes, the plan has to change everywhere at once: a bigger raise changes use of funds, runway,
dilution and SEIS headroom; a new hire changes payroll, the team section and the risk section. TOPY works out every
consequence first, lets the founder correct it, then writes a new version with the affected sections updated in
order and a final consistency check. The original plan is kept. No credits.

## When to use
- Any single change that touches several sections: money, dates, targets, prices, people.
- Not for: rewording one section (`topy-business-plan`, section edit); a brand-new plan.

## Before you start
- Which plan (`plans_list`, the newest finished one unless the founder names another).
- The change in the founder's own words. If several changes, do them in one request so the figures stay consistent.

## Workflow
1. **Analyse.** `plan_revise_analyze` with `plan_id` and `change_request`. Nothing changes and nothing is charged. Follow the returned job with `plan_status` (`job_id`) until `success` — usually under two minutes.
2. **Show the analysis** from the job's `result_json.analysis`:
   - `change_summary`;
   - each `fact_changes` item as **old → new** (old as written in the plan);
   - each `derived_figures` item with its `basis` — mark the ones that say they are assumptions;
   - sections by impact: **major** (rework), **minor** (a few figures or sentences), **none** (left untouched).
3. **Get corrections.** Ask: "Are these figures right? Anything to change or leave out?" Common fixes: a derived salary, a rounding, a section the founder wants left as it is. Note them in the founder's words.
4. **Apply.** `plan_revise_apply` with `plan_id`, `analysis_job_id`, `corrections` (their words — they override the analysis) and `selected` only if they removed sections. Preview: "Write a revised version of plan … (the current plan is kept)." Confirm after a yes.
5. **Follow.** `plan_status` (`job_id`), about 4 minutes. Report the sections revised, any consistency fixes, and `remaining_issues` it lists as worth a look. Give the new plan's id and title ("… (revised <date>)").
6. **Check.** Offer `plan_get` with `section` on the most important changed section (usually the financial plan) so the founder can read it.

## Output
```
**Change:** <summary>
| What | Was | Now |            (facts and derived figures; assumptions flagged)
**Sections:** major: … · minor: … · unchanged: …
→ after apply: new version "<title>", revised <n> sections, consistency fixes: …, worth a look: …
```

## Example
"We're raising £250k instead of £200k and hiring a CTO in Q2 2027." → analysis: SEIS raise £200,000 → £250,000; derived: post-money valuation, investor equity %, CTO salary (assumption, marked), FY payroll, use-of-funds split; 13 of 14 sections affected (3 major), Market Analysis untouched → founder corrects the CTO salary → apply → new version with 12 sections revised and one consistency fix.

## Quality bar
- [ ] The founder saw every old → new figure and every assumption before applying.
- [ ] Corrections were passed in their words.
- [ ] The new version's title and id were reported; the original was not modified.

## Guardrails
- Changes in TOPY take two calls: a preview, shown to the user, then `confirm: true` with the `confirmation` only after they agree. Never confirm for the user.
- Never edit sections one by one for a cross-cutting change; the revision keeps figures consistent.
- Don't present assumptions (e.g. a salary TOPY estimated) as facts; ask the founder to confirm them.
- If the analysis misread the change, re-run `plan_revise_analyze` with a clearer request instead of correcting everything.

## Related skills
- `topy-business-plan` — read the new version, edit one section, export.
- `topy-financial-model` — work the numbers out first when the change is financial.
- `topy-investor-ready` — re-check the revised plan before sending it.
