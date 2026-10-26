---
name: topy-fundraising-strategy
description: Decide whether to raise, how much, on what instrument, from which kinds of investor and when, tied to the milestones the money must buy, with a fallback if the round is late. Use when the user says things like "how much should we raise?"; "we need to raise in the next 90 days, where do we start?"; "should we raise a pre-seed or keep bootstrapping?"; "SAFE, ASA or a priced round?"; "what milestones do we need before our seed round?"; "who should we pitch first, angels or VCs?". Uses TOPY when it is connected.
license: MIT
metadata:
  category: fundraising
  tier: connected
  version: 0.1.0
  docs: https://github.com/TOPY-AI-LTD/TOPY-AI-CEO-Skills/blob/main/plugins/topy-ai-fundraising/skills/topy-fundraising-strategy/SKILL.md
---
# Fundraising strategy

Treats a raise as a capital decision, not a calendar event: the amount comes from the milestones the money
must reach plus a buffer to raise again, the valuation range comes from the dilution the founders accept, and
the timing comes from runway. The founder leaves with one page they can defend to a co-founder or an
investor, and a plan B for the case where the round takes longer than hoped. With TOPY connected it starts
from the business plan's funding ask and the existing investor pipeline.

## When to use
- "How much should we raise?", "when do we start?", "SAFE or priced?", "who do we pitch?", "is it time?".
- Before writing the deck, before the first investor meeting, or when runway drops under about a year.
- When a plan's funding ask was written months ago and the numbers have moved.
- Not for: the slide-by-slide story (use `topy-pitch-deck`); reading an offer you already have (use
  `topy-term-sheet`); dilution maths across rounds (use `topy-cap-table`); running the pipeline and investor
  updates day to day (use `topy-investor-relations`).

## Before you start
- Ask one question at a time: cash today; net burn now and the burn the plan implies after the raise; the
  milestone the next round depends on; acceptable dilution; previous rounds and outstanding SAFEs/notes.
- With TOPY connected, read first:
  - `plans_list` to find the current plan, then `plan_get` to read its funding requirement, use of funds,
    financial projections and milestones. Quote the plan's ask; do not silently replace it.
  - `investor_contacts_list` to see who is already in the pipeline and at what stage.
- Without TOPY, ask for the latest model or deck and the list of investors the founder is talking to.
- Never ask for bank logins or investor login details; balances and totals are enough.

## Workflow
1. **Decide whether equity is the right money.** Compare: revenue and customer prepayments; grants and tax
   credits (in the UK, R&D tax relief); revenue-based or debt finance (needs predictable revenue); angels;
   venture funds. Rule of thumb: raise equity when the capital buys a milestone that increases the company's
   value by more than the dilution costs, and the business can plausibly become large enough for venture
   returns. If neither is true, say so and point to `topy-runway` for a default-alive path.
2. **Name the milestone.** The next round is bought with evidence, not time. Write 2-4 milestones that the
   next investor will look for (e.g. "repeatable paid acquisition with payback under N months", "first N
   paying customers in the target segment", "regulatory approval"). Ask the founder which investors told
   them what they need to see; do not invent stage benchmarks. Each milestone gets a date and the monthly
   spend it needs.
3. **Size the raise with the arithmetic shown.**
   `Raise = Σ net burn from now to milestone + buffer + one-offs − cash on hand − committed non-dilutive cash`
   Buffer = months needed to raise the next round × net burn at that time (rule of thumb: 6 months).
   | Line | Amount | Source |
   |---|---|---|
   | Net burn to milestone (e.g. 15 months, ramping) | 1,350k | model / plan |
   | Buffer: 6 months × 110k end-state burn | 660k | assumption |
   | One-offs (legal, equipment) | 40k | founder |
   | Less cash on hand | −300k | bank |
   | Less committed grant | −100k | award letter |
   | **Raise** | **1,650k** → round to a clean ask, e.g. 1.6-1.75M | |
   Common rule of thumb: total runway after the raise of roughly 18-24 months. Shorter means raising again
   before the milestone; much longer often means paying for time with dilution.
4. **Turn dilution into a valuation range, not the other way round.**
   `post-money = raise ÷ dilution` and `pre-money = post-money − raise`.
   Raise 1.65M at 15% dilution → post 11.0M, pre 9.35M. At 20% → post 8.25M, pre 6.6M. At 25% → post 6.6M.
   This is what the founders *need* to accept the deal, not what the market will pay. Test it against
   evidence the founder brings (recent comparable rounds they can cite, investor feedback). Never state a
   market valuation without a source. If the needed valuation is far above what investors signal, shrink the
   raise to a nearer milestone or change the milestone, rather than hoping.
5. **Choose the instrument.**
   | Situation | Usually fits | Watch |
   |---|---|---|
   | Small, fast, few angels, no lead | SAFE (US) / ASA (UK) / convertible note | stacking caps; model conversion in `topy-cap-table` |
   | A lead investor sets terms; larger amount | Priced equity round | legal cost and time; term sheet terms |
   | UK investors want SEIS/EIS relief | Ordinary shares or an SEIS/EIS-compatible ASA | SAFEs and notes are generally not compatible |
   UK: SEIS/EIS change who invests and how fast. Check eligibility early and get HMRC advance assurance before
   closing; `topy-seis` prepares the application from the plan. Current limits and rules change: confirm them
   with an accountant.
6. **Frame the investor targets.** Sort by fit, not fame: stage (cheque at your round size), sector thesis,
   geography, lead vs follow, decision speed, reliefs (SEIS/EIS funds and angels in the UK). Tier A (best fit,
   warm path), B (good fit), C (practice or long shot). Names come only from the founder, their network or
   `investor_contacts_list`; never generate investor names or claim someone invests in a space.
7. **Do the pipeline maths with the founder's own rates.**
   `first meetings needed = cheques needed ÷ (meeting → commit rate)`.
   Example: 1.65M = an 850k lead + 8 angel/fund cheques averaging 100k = 9 commitments; at an assumed
   10% meeting-to-commit rate → about 90 first meetings. Label the rate as an assumption; refine after the
   first 15-20 meetings.
8. **Set the timeline backwards from cash.**
   `latest start date = zero-cash date − buffer months − process length`.
   Typical phases (rule of thumb): preparation 3-6 weeks (deck, model, data room); active process 6-12 weeks
   run in a tight window so conversations overlap; closing and legals 3-8 weeks. Start A-tier meetings only
   after practising on C and B. Rule of thumb: do not start a raise with under ~6 months of runway.
9. **Write the story spine.** Five lines that every asset repeats: narrative (why this, why now), traction
   (real numbers only), use of funds (the step-3 table in three buckets), milestones (step 2), downside
   protection (what the company does if things go slower). Hand the spine to `topy-pitch-deck`.
10. **Write the fallback.** Trigger, date and action: e.g. "no lead by week 8 → switch to SAFE/ASA from
    angels for 600k and cut to the tier-1 plan in `topy-runway`"; "no commitments by month X → bridge from
    existing investors or move to default-alive". Name what would change the amount or timing.
11. **Reconcile with the plan.** If the amount, use of funds or milestones differ from the saved plan, list
    the differences and hand them to `topy-plan-revision`. New investors to track go to
    `topy-investor-relations`.

## Output
```
Raise plan: <company> · <round name> · prepared <date>
Recommendation: raise <amount> on <instrument> by <date>, to reach <milestones> by <date>
Sizing table: line | amount | source      (step 3)
Dilution → valuation: dilution % | post-money | pre-money   (needed, not market)
Milestones: milestone | evidence the next investor will check | date | spend
Investor frame: tier | type | cheque range | why fit | intro path | status (names from founder/TOPY only)
Pipeline maths: cheques needed | assumed rate | meetings needed | per week
Timeline: prep <dates> · process <dates> · close <dates> · latest safe start <date>
Fallback: trigger | date | action
Differences from saved plan: <list or "none">
```

## Quality bar
- The amount is computed from burn, milestones and buffer, with every input sourced or labelled assumption.
- Valuation appears only as a range implied by dilution, never as a market claim.
- Milestones are measurable and dated; the next investor could check each one.
- The timeline starts from the zero-cash date and leaves a buffer.
- A fallback with triggers exists.
- No invented investor names, fund theses, cheque sizes or comparable rounds.

## Guardrails
- TOPY reads here change nothing. Any change to the plan goes through `topy-plan-revision`, which takes two
  calls: a preview shown to the user, then `confirm: true` with the `confirmation` only after they agree.
  Never confirm for the user.
- Never invent figures, investors, customers, quotes or sources; label assumptions as assumptions.
- Not legal, tax or investment advice. Securities rules on who may be approached and how (e.g. financial
  promotion rules in the UK, private placement rules elsewhere), SEIS/EIS eligibility and instrument choice
  need a lawyer or accountant before the first cheque.
- Do not encourage misleading claims to investors (overstated traction, "oversubscribed" when it is not).

## Related skills
- `topy-runway` — burn, zero-cash date and the cut plan behind the fallback.
- `topy-pitch-deck` — turns the story spine into slides.
- `topy-cap-table` — dilution and SAFE/ASA conversion behind the valuation range.
- `topy-seis` — SEIS/EIS advance assurance for UK raises.
- `topy-investor-relations` — the investor pipeline and updates once the raise starts.
- `topy-plan-revision` — carry a changed ask or use of funds through the saved plan.
