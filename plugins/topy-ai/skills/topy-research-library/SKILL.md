---
name: topy-research-library
description: Keep the research sources behind a project's business plan in TOPY, matched to the claims they support, with clean citations and no invented sources. Use when the user says things like "save this report as a source"; "which claims in my plan have no source?"; "where did the market size figure come from?"; "add my customer interview notes"; "check my sources are still current"; "build the bibliography for the plan". Needs the TOPY MCP server.
license: MIT
metadata:
  category: core
  tier: core
  version: 0.1.0
  docs: https://github.com/TOPY-AI-LTD/TOPY-AI-CEO-Skills/blob/main/plugins/topy-ai/skills/topy-research-library/SKILL.md
---
# Research library

Every number in a business plan will be asked about by someone: an investor, an assessor, a bank. This skill keeps the evidence for each claim in TOPY's research sources, records exactly which claim each source backs and how, and finds the claims that have nothing behind them. The result is a plan the founder can defend line by line, and a reference list that holds up when checked.

## When to use
- The founder has a report, article, dataset or interview to keep.
- Before sending a plan to investors or for SEIS: which claims are unsupported?
- An investor asks where a figure came from.
- Every few months: are sources still current?
- Not for: changing a figure in the plan (`topy-plan-revision`); a full investor-style review (`topy-investor-ready`); competitor strategy (`topy-competitive-strategy`).

## Before you start
- Know the project (`projects_list`; can be left out with one project).
- `research_sources_list` first, to avoid duplicates and to match the existing citation style.
- For a plan check: `plans_list`, then `plan_get` with `full: true` (or one `section` at a time for a long plan).
- If TOPY tools are missing, run `topy-connect`.

## Workflow

### 1. Record a source
Fields:
- `source_type`: `web` (default), `report`, `dataset`, `academic`, `government`, `interview`, `survey`, `internal`.
- `title`, `url`, `publisher` (e.g. `{"name": "Office for National Statistics", "kind": "government"}`), `published_at`.
- `summary`: what the source says that matters here, in two or three sentences, with the exact figure, its year and geography.
- `relevance_score`: 1-5 (5 = directly supports a plan claim with the same market, geography and year).
- `citation`: the link to the plan, e.g. `{"claim": "UK independent dental clinics: about 9,000", "plan_section": "Market analysis", "quote": "...", "page": 14, "accessed_on": "2026-10-26", "style": "Harvard"}`.
- `metadata_json` for the rest: `{"verified": true, "paywalled": false, "method": "census"}`.
Preview `research_source_create`, show it, confirm with `confirm: true` and the `confirmation` after a yes. A scheduled agent's key with a standing permission may add sources without a preview up to its daily cap; it cannot change or delete them.

### 2. Verify before saving
- The URL or document must exist and say what the summary claims. If you can open it, check; if you cannot, save with `"verified": false` and tell the founder.
- Quote numbers exactly as published; give the unit, year and geography.
- Prefer the primary source (the statistics office, the original survey) over an article quoting it; if only the secondary is available, say so in `metadata_json`.

### 3. Map claims to sources
1. From the plan, list every factual claim: market sizes, growth rates, prices, competitor facts, regulations, customer behaviour.
2. Match each to sources; grade the match:

| Grade | Meaning | Action |
|---|---|---|
| Supported | same metric, geography and period within ~2 years | none |
| Weak | a proxy, different region, or a secondary source | find a better one or soften the wording |
| Stale | over 3 years old for market data, over 1 year for prices or competitors | refresh |
| Unsupported | no source | find one, mark as founder estimate, or remove |
| Contradicted | a source says otherwise | change the plan via `topy-plan-revision` |

3. Founder's own data (interviews, sales figures) is valid evidence: record it as `interview` or `internal` with the sample size and date.

### 4. Maintain
- Correct a field: `research_source_get`, then preview `research_source_update` (send `metadata_json` whole if you change it).
- Superseded by a newer edition: add the new source, and set the old one's `metadata_json.superseded_by` rather than deleting it, so the history of a plan figure stays traceable.
- `research_source_delete` only for duplicates or records made by mistake; say it is permanent and cannot be undone, then follow the two-call rule.

### 5. Reference list
One style throughout (the existing one, or Harvard by default): author or publisher, year, title, URL, accessed date.

## Output
- Claim map: `Claim | Plan section | Source | Grade | Action`, unsupported and contradicted first.
- Reference list in one style.

## Example
Founder of Tidewell Kitchens (a fictional meal-kit startup for care homes) before an SEIS application: "Which claims have no source?"
- `plan_get` (full) yields 11 factual claims. `research_sources_list` has 5 sources.
- Map: 4 supported, 2 weak (a US meal-kit growth figure used for a UK market), 1 stale (2021 care-home count), 4 unsupported (including "average spend per resident per day").
- The founder supplies a government care-home dataset link and the per-resident figure from their own pilot invoices (3 homes, Sept 2026). Both are saved after previews; the pilot figure as `internal` with its sample size. The US proxy is flagged for `topy-plan-revision` to reword.

## Quality bar
- [ ] Every saved source exists, says what its summary says, and has a date and publisher.
- [ ] Every citation names the claim and plan section it supports.
- [ ] Figures quoted exactly, with unit, year and geography.
- [ ] Unverified sources marked as such.
- [ ] Unsupported and contradicted claims listed, not hidden.
- [ ] Every write was previewed and confirmed only after a yes.

## Guardrails
- Changes in TOPY take two calls: a preview first, shown to the user, then `confirm: true` with the `confirmation` only after they agree. Never confirm for the user.
- Never fabricate a source, a URL, an author, a page number or a quote. If no source can be found, say so; "founder estimate" is an honest label.
- Never reword a source's figure to fit the plan.
- Interview records: no names or contact details of interviewees unless they agreed; use a role and organisation type.
- Respect copyright: summarise and quote briefly; do not store whole paywalled documents.
- Deletes are permanent (risk W4).

## Related skills
- `topy-plan-revision` — carry a corrected figure through the whole plan.
- `topy-investor-ready` — a full investor-style read of the plan.
- `topy-data-room` — sources feed the due-diligence folder.
- `topy-seis` — assessors check the market claims too.
