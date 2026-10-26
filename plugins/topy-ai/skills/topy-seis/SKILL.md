---
name: topy-seis
description: Draft the answers for a UK SEIS Advance Assurance application from a TOPY.AI business plan, choose the right qualifying route, and list the documents HMRC expects. Use when the user says things like "help me apply for SEIS advance assurance"; "draft my SEIS application"; "is my company SEIS eligible?"; "what does HMRC need for SEIS?"; "SEIS answers from my business plan". Needs the TOPY MCP server.
license: MIT
metadata:
  category: core
  tier: core
  version: 0.1.0
  docs: https://github.com/TOPY-AI-LTD/TOPY-AI-CEO-Skills/blob/main/plugins/topy-ai/skills/topy-seis/SKILL.md
---
# SEIS Advance Assurance

UK startups raising from angels usually ask HMRC for SEIS Advance Assurance first, so investors know they'll get
the tax relief. The application asks the same questions a good plan answers — trade, risk to capital, use of money,
growth intentions. TOPY drafts those answers from the founder's plan; this skill picks the route, checks the
eligibility facts the plan can't show, and lists what to attach.

## When to use
- A UK company preparing an SEIS (or SEIS then EIS) raise.
- Not for: non-UK companies; whether an individual investor qualifies; final tax advice.

## Before you start
- A finished plan (`plans_list` → `status: success`), read in full with `plan_get`. If none, `topy-business-plan` first.
- Ask the eligibility facts one at a time, because the plan rarely states them: when the company started trading; total assets; number of employees; whether it has raised SEIS/EIS/VCT before; who holds the shares. Present the thresholds as "HMRC's published limits — check gov.uk for the current figures"; don't quote numbers from memory as certain.

## Workflow
1. **Choose the route** with the founder (`activity_type`):
   | Route | When |
   |---|---|
   | `qualifying_trade` | the company trades (sells products/services) in a qualifying trade |
   | `rd_intended_to_lead_to_qualifying_trade` | R&D now that is meant to lead to a qualifying trade |
   | `rd_existing_qualifying_trade` | R&D within a trade the company already carries on |
2. **Draft.** `plan_seis_assurance` with `plan_id` and `activity_type`. It returns answers per question (risk to capital, the trade, use of funds, growth and development, the supporting documents checklist).
3. **Check the draft against the plan and the facts.** For each answer: is the risk-to-capital case explicit (growth and development intentions, employees, revenue goals, real risk of loss)? Does the use of money match the plan's use-of-funds section? Flag anything the founder must confirm or that contradicts the plan.
4. **Close gaps in the plan if needed.** A thin use-of-funds or growth section weakens the application: offer `plan_section_suggest` → show → `plan_update`, or `topy-plan-revision` if figures change.
5. **Documents checklist.** From the draft's checklist, mark what the founder has and what's missing (typically: business plan, financial forecasts, latest accounts if any, articles, shareholder list, the investor list or a statement that investors are not yet identified, any existing investment documents).

## Output
```
**Route:** <activity_type> — why
**Draft answers:** <question> — <answer> (needs confirming: …)
**Gaps to close:** …
**Documents:** ✓ … / ✗ …
**Next:** submit through HMRC's online form; have an accountant check it.
```

## Quality bar
- [ ] The route was chosen with the founder, not assumed.
- [ ] Every answer was checked against the plan; contradictions flagged.
- [ ] Limits are presented as "check the current HMRC guidance", not quoted as certain.

## Guardrails
- Changes in TOPY take two calls: a preview, shown to the user, then `confirm: true` with the `confirmation` only after they agree. Never confirm for the user.
- Not tax or legal advice: an accountant or SEIS adviser should review the application before it's submitted.
- Never state eligibility as certain; HMRC decides.
- Don't invent investors, revenue or employees to strengthen the case.

## Related skills
- `topy-investor-ready` — strengthen the plan first.
- `topy-cap-table` — the share structure and dilution.
- `topy-fundraising-strategy` — the raise around the assurance.
