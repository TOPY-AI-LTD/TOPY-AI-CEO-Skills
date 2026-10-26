---
name: topy-market-entry
description: 'Decides whether, where and how a startup should enter a new geography or customer segment: readiness, bottom-up sizing, entry mode, a beachhead, gated phases and kill criteria set in advance. Use when the user says things like "should we expand to the US?"; "which market should we go into next?"; "we want to sell to enterprise now"; "how do we enter a new country?"; "partner or open an office?"; "is this new segment worth it?". Uses TOPY when it is connected.'
license: MIT
metadata:
  category: strategy
  tier: connected
  version: 0.1.0
  docs: https://github.com/TOPY-AI-LTD/TOPY-AI-CEO-Skills/blob/main/plugins/topy-ai-strategy/skills/topy-market-entry/SKILL.md
---
# Market entry

Helps a founder make an expansion decision that is cheap to test and safe to reverse. The agent checks whether the home market is ready to leave, sizes each candidate from the bottom up, compares candidates (including staying focused at home), chooses the lightest entry mode that can work, picks a beachhead, and writes phases with pass gates and kill criteria before any money is spent. With TOPY connected, it reads the project, its research and past decisions, and can record the final call.

## When to use
- A new country or region, a new customer segment (SMB to enterprise, B2B to B2C), or a new vertical.
- Inbound demand from a market the company does not serve yet, or an investor pushing for expansion.
- Choosing between several candidate markets, or between partner, remote sales and a local team.
- Not for: reacting to a competitor in the current market (use `topy-competitive-strategy`), the detailed launch and channel plan once the market is chosen (use `topy-gtm-plan`), or a pure market-size estimate for a pitch deck (use `topy-pitch-deck`).

## Before you start
- With TOPY connected:
  - If you do not know the project, call `projects_list` and ask which one; then `project_get` for market, industry and current geography.
  - Call `research_sources_list` for any market data already gathered on the candidates; use those sources and note their dates.
  - Call `decisions_list` and look for earlier expansion or focus decisions; a reversal should state what changed.
- Without TOPY, ask: what you sell, where, to whom, and whether expansion was considered before.
- Then ask, one question at a time: which markets or segments, why now (the trigger), what evidence of demand exists there, and how much money and whose time can go into it over the next 12 months.

## Workflow
1. **Define the target and the trigger.** Write each candidate precisely ("mid-size accounting firms in Germany", not "Europe") and why it is on the table now: inbound customers, a partner offer, a competitor's absence, investor pressure. Pressure without demand is a warning sign; say so.
2. **Check home-market readiness.** Expansion often hides a core that is not yet working. Ask for evidence of: retention that stabilises rather than falling steadily, at least one acquisition channel that produces customers predictably, and unit economics the founder is comfortable with. Verdict: *ready*, *ready with one gap* (name it), or *not ready* (recommend going deeper at home first, unless there is a strong reason such as the home market being too small). Keep "go deeper at home" as an option through the rest of the analysis.
3. **Size bottom-up.** For each candidate:
   - Number of target customers you can name or count (from a registry, a directory, an association, or the founder's sources).
   - × share you could realistically reach with the planned channel in three years.
   - × expected annual revenue per customer (adjusted for local pricing and currency).
   Cross-check with a capacity view: sellers or partners × deals each can close per year × revenue per deal. Then cross-check top-down if a credible source exists. If bottom-up and top-down differ by more than about three times (rule of thumb), find which assumption is wrong before going on. Every number gets a source or "assumption".
4. **Score attractiveness against ability to win.** Weights to 100 for each side, scores 1-5 with one-line reasons:
   - Attractiveness: reachable size, growth, willingness to pay, competitive intensity, cost to serve, regulatory burden.
   - Ability to win: product fits without major change, access to a channel, need for local presence, brand or references there, language and localisation effort, payments and invoicing, legal and data requirements.
   Plot candidates on the two scores. Go first where both are high; a very attractive market where the company has little ability to win is usually a later move, not a first one.
5. **List the adaptations.** For the leading candidate, what must change: product, language, pricing and currency, contracts, legal entity, tax registration, data residency, payment methods, support hours, certifications. Mark each *before first customer* or *can wait*. A long "before" list raises the entry cost; add it to the budget.
6. **Choose the entry mode.** From least to most commitment:
   | Mode | Fits when | Reversible? |
   |---|---|---|
   | Remote / digital from home | self-serve or inside-sales product, buyers accept a foreign supplier | easily |
   | Partner, reseller or distributor | buyers rely on local relationships or installers; you need reach fast | fairly, check contract exits |
   | First local hire | relationships matter and the partner route failed or does not exist | moderately |
   | Local team or entity | proven demand, regulatory need for presence, volume to justify it | costly |
   | Acquisition or joint venture | time matters more than cash and a fitting target exists | hard |
   Decision rule: start with the lightest mode that can produce a real test of demand; step up only when a gate is passed.
7. **Pick the beachhead.** The first sub-segment or city where the company can win decisively: buyers with an urgent version of the problem, reachable through one channel, who talk to each other, and where the main local rival is weak. One beachhead, not three.
8. **Plan the phases and gates.**
   - *Phase 0 — test* (for example 8-12 weeks): a demand test such as targeted outreach to a fixed list, a localised landing page, or two or three pilot customers. Gate: numbers the founder sets now (e.g. qualified conversations, pilots signed, paid conversions).
   - *Phase 1 — beachhead*: first paying customers in the beachhead, the entry mode running. Gate: customers retained, acquisition cost within the founder's limit, one reference customer.
   - *Phase 2 — scale*: wider segment, step up the entry mode if needed.
   Each gate has an owner and a date. The founder writes the thresholds; the agent challenges any that would pass even if demand were weak.
9. **Budget and opportunity cost.** Cost per phase (people, travel, legal, localisation, partner margins), months until the market covers its own costs under the founder's assumptions, and what the home market loses (founder time is usually the biggest cost; name what slips).
10. **Set kill criteria and the exit path.** Before starting: "Stop if [measurable condition] by [date]" for each phase (e.g. fewer than [N] pilots from [M] qualified conversations by the end of Phase 0). Then the exit path: which contracts, hires, entities or commitments would need unwinding and at what cost. Prefer entry steps whose exit cost is known.
11. **Pre-mortem and incumbent response.** "A year from now this failed. Why?" Top three causes and their mitigations. Ask how the strongest local player will react; if the answer matters, run `topy-competitive-strategy` on it.
12. **Save the decision (TOPY connected).** Once the founder decides, offer `decision_create`: `title` (e.g. "Enter Germany via reseller pilot"), `context` (trigger, readiness verdict), `options_considered` (each candidate and mode, including going deeper at home, with scores), `decision` (the founder's choice in their words), `rationale`, `confidence`, `impact_scope`, and `metadata_json` with the gates, kill criteria and review dates. Preview first, show it, then `confirm: true` with the `confirmation` only after the founder agrees. If the move changes the business plan's figures, point to `topy-plan-revision`.

## Output
1. Recommendation in three lines: where, how, first step, and the date of the first gate.
2. Readiness verdict with the evidence.
3. Sizing per candidate (table: input | value | source or assumption), with cross-checks.
4. Attractiveness vs ability-to-win table and ranking, including "go deeper at home".
5. Adaptations: item | before first customer / can wait | cost.
6. Entry mode and why; the beachhead and why.
7. Phase plan: phase | goal | duration | budget | gate | owner.
8. Kill criteria and exit path.
9. Pre-mortem and likely incumbent response.

## Quality bar
- Home-market readiness was checked, and "go deeper at home" stayed an option to the end.
- Sizing is bottom-up from countable customers, cross-checked, with every input sourced or marked as an assumption.
- The entry mode is the lightest one that can test demand; heavier modes are tied to gates.
- There is exactly one beachhead.
- Gates and kill criteria are numeric, dated and set before spending, by the founder.
- The exit path and its cost are written down.

## Guardrails
- Changes in TOPY take two calls: a preview first, shown to the user, then `confirm: true` with the `confirmation` only after they agree. Never confirm for the user.
- Never invent market sizes, growth rates, local prices or competitor facts; label assumptions as assumptions and cite real sources.
- Not legal, tax or investment advice. Entity set-up, permanent-establishment tax risk, employment of local staff, distributor contracts, data-protection rules, export controls and sanctions all need a qualified local lawyer or accountant before commitments are made; say which ones apply.
- Do not recommend hiring locally or opening an entity before a passed gate, unless regulation requires local presence to sell at all.

## Related skills
- `topy-competitive-strategy` — how incumbents in the new market will respond.
- `topy-decision-memo` — a full memo for a large, hard-to-reverse entry.
- `topy-gtm-plan` — the go-to-market plan for the chosen market.
- `topy-plan-revision` — update the business plan once the decision is made.
- `topy-scenario-planning` — when entry depends on regulation or funding conditions.
