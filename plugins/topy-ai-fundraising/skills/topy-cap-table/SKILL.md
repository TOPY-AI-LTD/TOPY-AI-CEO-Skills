---
name: topy-cap-table
description: 'Build a fully diluted cap table and model dilution across rounds: SAFE/ASA and convertible conversion, option pool top-ups and the founders'' ownership after each step. Not legal or tax advice. Use when the user says things like "how much will I own after the seed round?"; "build our cap table"; "how do our SAFEs convert?"; "how big should the option pool be?"; "model dilution across the next two rounds"; "what does a 5 million post-money cap mean for us?".'
license: MIT
metadata:
  category: fundraising
  tier: standalone
  version: 0.1.0
  docs: https://github.com/TOPY-AI-LTD/TOPY-AI-CEO-Skills/blob/main/plugins/topy-ai-fundraising/skills/topy-cap-table/SKILL.md
---
# Cap table and dilution

Shows the founder, step by step, who owns what today and after each financing: convertibles turning into
shares, the option pool being topped up, new money coming in. The arithmetic is visible so the founder can
check it and explain it to a co-founder or investor. **This is a model for decisions, not legal or tax
advice: the company's legal records (share register, signed instruments) are the source of truth, and a
lawyer must confirm conversions and an accountant the tax treatment before anything is issued.**

## When to use
- "Cap table", "dilution", "how do SAFEs convert", "option pool size", "what will I own".
- Before agreeing a SAFE/ASA cap, before signing a term sheet, and when planning the next two rounds.
- Not for: reading the other terms of a term sheet (use `topy-term-sheet`); deciding how much to raise
  (use `topy-fundraising-strategy`).

## Before you start
- Ask one question at a time: current holders and share counts; options granted and the unallocated pool;
  each convertible's amount, cap type, discount, interest and date; the round being modelled.
- Ask for the exact wording of each convertible's conversion clause when it matters: "post-money" and
  "pre-money" caps convert differently, and definitions of capitalisation vary between documents.
- No TOPY tools are needed. Never ask for personal identity details of shareholders; names or labels suffice.

## Workflow
1. **Build today's fully diluted table.** Fully diluted = issued shares + granted options (vested or not)
   + unallocated pool + shares promised in writing. Convertibles are shown separately until a priced round.
   | Holder | Class | Shares | % fully diluted |
   |---|---|---|---|
   | Founder A | Ordinary | 4,500,000 | 45.0% |
   | Founder B | Ordinary | 4,500,000 | 45.0% |
   | Option pool (granted + unallocated) | Options | 1,000,000 | 10.0% |
   | **Total** | | **10,000,000** | **100%** |
2. **Convert a post-money SAFE/ASA.** Ownership = investment ÷ post-money cap, measured on the
   capitalisation just before the new money. Example: 500k at a 5.0M post-money cap → 10%.
   Solve for SAFE shares S: `S ÷ (10,000,000 + S) = 0.10` → `S = 1,111,111`. Conversion price =
   5,000,000 ÷ 11,111,111 = 0.45 per share. Several post-money SAFEs each take their percentage, so they
   dilute the founders (not each other): two 10% SAFEs cost the founders 20 points before the round starts.
   Under the widely used post-money SAFE form, a pool increase made in the priced round generally falls on
   existing holders rather than the SAFE; check the "capitalisation" definition in the actual document.
3. **Convert a pre-money cap or convertible note.** Conversion price = the lower of
   `cap price = pre-money cap ÷ pre-money fully diluted shares` and `round price × (1 − discount)`.
   Notes add accrued interest: `amount converting = principal × (1 + rate × years)` (simple interest; check
   the note). Illustrative: 250k at 8% for 1 year = 270k; cap 4.0M on 10,000,000 shares → 0.40; round
   price 0.69 with 20% discount → 0.552; converts at 0.40 → 675,000 shares.
4. **Model the priced round with the pool top-up ("pool shuffle").** Example: raise 2.0M at 8.0M pre-money
   (post 10.0M → new investor 20%), pool to be 10% of post-money, pool top-up counted in the pre-money.
   Let N = post-money fully diluted shares. Pre-round shares after SAFE conversion = 11,111,111;
   existing pool 1,000,000.
   - Investor shares = 0.20 N; total pool = 0.10 N; top-up P = 0.10 N − 1,000,000.
   - Pre-money shares = 0.80 N = 11,111,111 + P = 10,111,111 + 0.10 N → 0.70 N = 10,111,111.
   - N = 14,444,444; P = 444,444; investor = 2,888,889; price = 2,000,000 ÷ 2,888,889 = 0.692.
   | Holder | Shares | Before round | After round |
   |---|---|---|---|
   | Founders A + B | 9,000,000 | 81.0% | 62.3% |
   | SAFE holder | 1,111,111 | 10.0% | 7.7% |
   | Option pool | 1,000,000 → 1,444,444 | 9.0% | 10.0% |
   | Seed investor | 2,888,889 | — | 20.0% |
   | **Total** | **14,444,444** | | **100%** |
   Check: pre-money shares (11,555,556) × 0.692 ≈ 8.0M. The top-up (444,444 × 0.692 ≈ 0.31M) sits inside the
   pre-money, so the founders' effective pre-money is about 7.7M, not 8.0M.
5. **Chain rounds.** Each round: `ownership after = ownership before × (1 − new round % − pool top-up %)`
   (when the top-up is a share of post-money). Founders at 62.3% after seed; a Series A selling 20% with a
   further 5-point pool top-up → 62.3% × 0.75 = 46.7%. Show a path table: round | raise | pre | post | new
   investor % | pool % | founders %.
6. **Size the pool from hires, not habit.** Pool = Σ expected grants for hires in the next 12-24 months
   (from `topy-hiring-plan`), plus a small reserve. A pool sized "because 10-15% is common" (rule of thumb)
   often over-dilutes founders when the top-up sits in the pre-money. Negotiate with the hiring plan in hand.
7. **Run the sensitivities.** Founders' ownership after the round at ±20% on pre-money, ±5 points on pool
   size, and with/without each SAFE. Show which lever moves founder ownership most.
8. **Country notes.** UK: tax-advantaged options usually mean EMI (with an HMRC-agreed valuation and timely
   notification); SEIS/EIS investors must meet conditions (e.g. not being "connected" with the company,
   which includes holding more than 30%), and ordinary shares without preferences are generally required.
   `topy-seis` covers advance assurance. US and elsewhere: option pricing and securities filings have their
   own rules. In every country, the lawyer and accountant confirm before issuing.
9. **Reconcile with the legal record.** The model must tie to the share register / stock ledger and registry
   filings. Any difference (an undocumented promise, an unrecorded transfer) is listed for the lawyer.

## Output
```
Cap table model: <company> · as of <date> · prepared <date>
Today (fully diluted): holder | class | shares | %
Convertibles: instrument | amount | cap (pre/post) | discount | interest | conversion price | shares
After each event: holder | shares | % before | % after   (with the equations shown)
Ownership path: round | raise | pre | post | investor % | pool % | founders %
Effective pre-money after pool top-up: <value>
Sensitivity: lever | change | founders % after
For the lawyer/accountant: <list>
Not legal or tax advice: <one line>
```

## Quality bar
- Every table totals 100% and every share count reconciles to the step before.
- Each conversion shows its formula and which cap type (pre or post) was used.
- The pool top-up's effect on effective pre-money is shown.
- Assumptions (future valuations, round sizes) are labelled as assumptions, not forecasts.
- Differences from the legal record are listed, not smoothed over.

## Guardrails
- Not legal or tax advice. A lawyer must confirm conversion mechanics against the signed instruments, and
  draft any issue, transfer or option grant; an accountant must confirm tax (option schemes, SEIS/EIS,
  founder share valuations). Say so in the output.
- Never invent valuations, round sizes or investor terms; future rounds are scenarios the founder chose.
- Never alter or "clean up" historical records in the model to look tidier; flag them instead.
- Share and holder data is confidential; minimise personal details.

## Related skills
- `topy-term-sheet` — the pool, preference and anti-dilution terms that drive these numbers.
- `topy-fundraising-strategy` — the dilution budget that sets the raise and valuation range.
- `topy-hiring-plan` — the hires that size the option pool.
- `topy-seis` — SEIS/EIS advance assurance for UK investors.
- `topy-data-room` — where the cap table goes for due diligence.
