---
name: topy-term-sheet
description: 'Read a startup term sheet in plain language: the economic and control terms, what they cost at real exit values and on the cap table (simulated in TOPY, never written), and the few points worth pushing on. Not legal advice. Use when the user says things like "we got a term sheet, what does it mean?"; "is this liquidation preference normal?"; "what should we push back on?"; "explain the anti-dilution clause"; "how much do we actually get if we sell for 20 million?"; "the investor wants a board seat and veto rights, is that OK?". Uses TOPY when it is connected.'
license: MIT
metadata:
  category: fundraising
  tier: connected
  version: 0.2.0
  docs: https://github.com/TOPY-AI-LTD/TOPY-AI-CEO-Skills/blob/main/plugins/topy-ai-fundraising/skills/topy-term-sheet/SKILL.md
---
# Term sheet review

Helps a founder understand what a term sheet really says before talking to a lawyer and the investor. It
separates the terms that move money (price, pool, preferences, anti-dilution) from the terms that move
control (board, vetoes, drag, vesting), computes what each side receives at realistic exit values, and
picks the two or three points worth spending goodwill on. With TOPY connected it runs each offer and each
ask through `round_simulate` on the stored cap table, so the cost of a term shows up in founder points;
the simulation writes nothing. **This is not legal or tax advice. A lawyer
who acts for the company must review the term sheet and the final documents before anything is signed.**

## When to use
- "We have a term sheet", "is this normal?", "what do we push on?", "compare these offers".
- Also for a SAFE, ASA or convertible note side letter (pro-rata, MFN, information rights).
- Not for: deciding whether and how much to raise (use `topy-fundraising-strategy`); modelling ownership
  across several rounds (use `topy-cap-table`); preparing due diligence (use `topy-data-room`).

## Before you start
- Ask one question at a time: the term sheet text; the current cap table; which terms the founder already
  cares about; the deadline for signing; whether other offers exist.
- Ask the company's country and governing law. Terms differ by market (e.g. UK deals often follow BVCA model
  documents, US deals NVCA ones); describe terms by what they do, not by assuming one market's defaults.
- With TOPY connected, read `cap_table_get` first (fully diluted shares, holders, pool, convertibles). If it
  is empty or out of date, store it with `topy-cap-table` before simulating. Without TOPY, ask for the table.
- Never ask for signed copies of personal documents.

## Workflow
1. **Spot the binding clauses first.** Most of a term sheet is non-binding, but exclusivity/no-shop,
   confidentiality, costs and governing law usually bind on signing. Note the no-shop length (rule of thumb:
   30-60 days is common; longer deserves a question) and who pays legal fees and up to what cap.
2. **Economics: compute the real price.**
   - `price per share = pre-money valuation ÷ pre-money fully diluted shares`.
   - **Option pool shuffle.** If the pool top-up is counted in the pre-money, existing holders pay for it.
     `effective pre-money = headline pre-money − value of new pool shares`.
     Example: pre-money 8.0M, raise 2.0M (post 10.0M), pool must be 10% post → 1.0M of post-money value. If
     the existing pool is worth 0.6M, the top-up is 0.4M of value inside the pre-money → effective pre-money
     7.6M. Ask: size the pool from a hiring plan (`topy-hiring-plan`), not a round number.
   - **Simulate it (connected).** `round_simulate` with the sheet's `pre_money`, `amount`,
     `pool_top_up_pct` (and whether the top-up sits in the pre- or post-money) and the outstanding
     convertibles converting. It returns the post-round table, each holder's dilution and the price per
     share; nothing is saved. Run it once for the offer as written and once per ask (e.g. top-up counted
     post-money, a smaller pool) and show the difference in founder % and effective pre-money.
   - **Liquidation preference.** 1x non-participating: investor takes the greater of its money back or its
     share as if converted. Participating: money back *and* its share of the rest. Multiples above 1x pay
     more before anyone else. Cap: participation stops once the investor reaches a set multiple.
   - **Anti-dilution** (only bites in a down round). Broad-based weighted average:
     `new conversion price = old price × (A + B) ÷ (A + C)`, where A = shares outstanding before the new
     issue (fully diluted), B = shares the new money would buy at the old price, C = shares actually issued.
     Example: old price 1.00; A = 10,000,000; new round 1,000,000 at 0.50 → B = 1,000,000, C = 2,000,000 →
     new price = 1.00 × 11.0M ÷ 12.0M = 0.917. Full ratchet would reset it to 0.50: far harsher.
   - Dividends (cumulative ones accrue and add to the preference), redemption rights, pay-to-play.
3. **Run the exit waterfall** at three to four sale prices, one below the post-money. Example: investor put
   in 2.0M for 20%; founders and others hold 80%.
   | Exit value | 1x non-participating: investor | others | 1x participating: investor | others |
   |---|---|---|---|---|
   | 5M | 2.0M (pref > 20% × 5M = 1.0M) | 3.0M | 2.0M + 20% × 3.0M = 2.6M | 2.4M |
   | 10M | 2.0M (= 20% × 10M) | 8.0M | 2.0M + 1.6M = 3.6M | 6.4M |
   | 30M | 6.0M (converts: 20% × 30M) | 24.0M | 2.0M + 5.6M = 7.6M | 22.4M |
   Read it: participation costs the other holders most at low and mid exits; non-participating converts
   once the as-converted share beats the preference (here above 10M).
4. **Control terms.** For each: what it lets the investor do, and when.
   - Board: seats for founders / investors / independent; who appoints the independent; quorum.
   - Investor consents (protective provisions / reserved matters): a list of actions needing investor
     approval. Normal ones protect the investor's class (new senior shares, changing rights, selling the
     company); watch for operational items (budgets, hiring, every contract above a low threshold).
   - Drag-along: majority can force a sale; check the threshold and minimum price. Tag-along, pre-emption
     (pro-rata), right of first refusal, information rights, founder vesting and leaver terms (good/bad
     leaver definitions and what a "bad leaver" loses), founder warranties and their caps.
5. **Rate every term.** Standard (common at this stage in this market) / Watch (unusual but sometimes fair)
   / Push (materially worse than common practice or than another offer). Rules of thumb for early rounds,
   to be confirmed by the founder's lawyer: 1x non-participating is widely treated as the norm; participation,
   multiples above 1x, full ratchet, cumulative dividends, redemption on demand and operational vetoes are
   usually "Push"; broad-based weighted average anti-dilution is usually "Standard".
6. **Pick the asks.** Choose at most three, ordered by money at stake at the realistic exit range from step
   3, then by control. Trade rather than demand: e.g. accept the pool size if the top-up is counted
   post-money, or accept a board seat if an independent is added. Price is not always the biggest lever.
7. **Compare offers** (if more than one): same waterfall at the same exits, a `round_simulate` run per
   offer on the same stored cap table, effective pre-money, control
   load, speed to close, and what the investor brings that the founder can verify (references from founders
   they backed, including ones that failed).
8. **UK: SEIS/EIS check.** SEIS/EIS shares generally need to be ordinary shares without preferential rights
   to assets on a winding-up and without redemption rights; a liquidation preference or some anti-dilution
   and dividend terms can break relief for those investors. If relief matters, the lawyer must confirm the
   structure and `topy-seis` handles advance assurance; check current HMRC rules.
9. **Write the lawyer brief.** Questions the founder wants answered, the asks, and anything that differs from
   the model documents the lawyer usually uses.

## Output
```
Term sheet review: <company> · <investor> · <instrument> · received <date> · sign by <date>
Binding on signing: no-shop <days> · costs <who, cap> · confidentiality
Headline vs effective: pre-money <x> · pool top-up <y> · effective pre-money <z> · price/share <p>
| Term | What it says | Plain English | Economic / Control | Standard / Watch / Push | Suggested ask |
Waterfall: exit value | investor | founders | others   (3-4 exits, one below post-money)
Top 3 asks: ask | why (money or control at stake) | possible trade
Questions for the lawyer: ...
Not legal advice: <one line>
```

## Quality bar
- Every term in the sheet appears in the table; none is skipped as boilerplate.
- Effective pre-money and the waterfall are computed with the arithmetic shown.
- "Standard" is labelled as a rule of thumb for the stated market and stage, not a fact.
- No more than three asks, each tied to money or control at stake.
- The output says plainly that a lawyer must review before signing.

## Guardrails
- This skill only reads and simulates: `round_simulate` writes nothing. Recording a signed round or new
  holdings is done later through `topy-cap-table` / `topy-fundraising-strategy`, each as a preview, then
  `confirm: true` with the `confirmation` only after the founder agrees. Never confirm for the user.
- Equity and money are simulated only; signing and funds happen with the lawyer, outside the agent.
- Every figure comes from the term sheet, the founder or a TOPY tool result; say which.
- Not legal, tax or investment advice. Say when a lawyer is required: before signing the term sheet (it has
  binding clauses), for all definitive documents, for leaver/vesting terms, warranties and any SEIS/EIS
  structuring. Tax effects for founders (e.g. on vesting or share classes) go to an accountant.
- Never invent market norms, valuation benchmarks or investor reputations; label rules of thumb.
- Never recommend misleading an investor about other offers or their terms.
- Keep term sheets confidential: do not paste them into public tools.

## Related skills
- `topy-cap-table` — ownership before and after, SAFE/ASA conversion and the option pool.
- `topy-fundraising-strategy` — whether the offer meets the raise plan's amount and milestones.
- `topy-data-room` — what due diligence will ask for once the term sheet is signed.
- `topy-seis` — SEIS/EIS advance assurance for UK investors.
