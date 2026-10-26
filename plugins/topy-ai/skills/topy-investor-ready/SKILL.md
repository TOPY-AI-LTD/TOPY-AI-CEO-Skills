---
name: topy-investor-ready
description: Review a TOPY.AI business plan the way a seed investor would and list the five fixes that matter most, each with its section — then fix the ones the founder picks. Use when the user says things like "is my plan investor-ready?"; "review my business plan like an investor"; "what would a VC pick apart in this plan?"; "before I send the plan to angels"; "find the weak points in my plan". Needs the TOPY MCP server.
license: MIT
metadata:
  category: core
  tier: core
  version: 0.1.0
  docs: https://github.com/TOPY-AI-LTD/TOPY-AI-CEO-Skills/blob/main/plugins/topy-ai/skills/topy-investor-ready/SKILL.md
---
# Investor-ready check

Investors skim a plan for a handful of things and stop at the first that's missing. This skill reads the whole
plan, scores it the way a seed investor would, and turns the gaps into five concrete fixes — without changing
anything until the founder picks one.

## When to use
- Before sending a plan to investors, a bank or a grant body; after a revision.
- Not for: writing the plan (`topy-business-plan`); the pitch deck itself (`topy-pitch-deck`).

## Before you start
- The plan: `plans_list` → newest with `status: success`, unless named. Read it with `plan_get` `full: true`.
- The audience (angels and SEIS investors weigh founder and tax relief; funds weigh market size and scalability; banks weigh cash flow and security).

## Workflow
1. **Score eight areas** 0–2 each (0 missing, 1 weak, 2 convincing), quoting the line that earns the score:
   | Area | Convincing looks like |
   |---|---|
   | Problem & customer | a specific customer with a costly, frequent problem; evidence (interviews, pilots) |
   | Solution & why now | what changes for the customer; why this is possible or urgent now |
   | Market | bottom-up sizing (customers × price) with stated sources; not only a top-down "1% of $X bn" |
   | Traction & validation | numbers with dates: users, revenue, pilots, LOIs, retention |
   | Business model | price, margin, CAC/LTV or payback, how revenue scales |
   | Financials | assumptions stated; the same figures in every section; break-even and runway follow from them |
   | Use of funds & milestones | the raise tied to milestones that de-risk the next round |
   | Team & risks | why this team; honest risks with mitigations |
2. **Check consistency.** The same raise, prices, headcount and dates must appear in every section; list any mismatch with both locations — these are the most damaging gaps.
3. **Check sources.** Market and benchmark figures without a source: if `research_sources_list` has one, point to it; otherwise flag "needs a source" (never supply one yourself).
4. **Pick the five fixes**, ordered by investor impact: consistency errors first, then any area scored 0, then 1s in Market, Traction, Financials, Use of funds. For each: the section, what's wrong (quote), the fix, and the tool.
5. **Offer to fix** one at a time:
   - wording or depth in one section → `plan_section_suggest` with the instruction → show → if kept `plan_update`;
   - a figure that must change everywhere → `topy-plan-revision`;
   - missing evidence → ask the founder for it; don't fabricate.

## Output
```
**Investor-ready: <score>/16** for <audience>
| Area | Score | Why (quote) |
**Inconsistencies:** <figure> says X in <section> and Y in <section>
**Five fixes**
1. <section> — <problem> → <fix> (<tool>)
…
```

## Quality bar
- [ ] Every score quotes the plan.
- [ ] Inconsistencies list both locations.
- [ ] No figure, source or traction was invented.
- [ ] Nothing changed without the founder picking the fix and agreeing to the preview.

## Guardrails
- Changes in TOPY take two calls: a preview, shown to the user, then `confirm: true` with the `confirmation` only after they agree. Never confirm for the user.
- This is a review, not investment advice and not a promise that anyone will invest.
- Be direct about weaknesses; don't soften a 0 into a 1.

## Related skills
- `topy-plan-revision` — fix a figure everywhere.
- `topy-pitch-deck` — the deck from the improved plan.
- `topy-fundraising-strategy` — who to raise from and when.
