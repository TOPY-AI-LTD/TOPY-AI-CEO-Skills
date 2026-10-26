---
name: topy-pitch-deck
description: Generate the 10-12 slide investor deck from the business plan in TOPY, review it slide by slide (one claim per slide, numbers that match the plan exactly) and export it as PPTX or PDF. Use when the user says things like "turn my business plan into a pitch deck"; "write the slides for our seed round"; "generate a deck from our plan in TOPY"; "review my deck before I send it to investors"; "our deck is 25 slides, help me cut it"; "what's the story of our pitch?". Uses TOPY when it is connected.
license: MIT
metadata:
  category: fundraising
  tier: connected
  version: 0.2.0
  docs: https://github.com/TOPY-AI-LTD/TOPY-AI-CEO-Skills/blob/main/plugins/topy-ai-fundraising/skills/topy-pitch-deck/SKILL.md
---
# Pitch deck

Turns a business plan into the short story an investor reads in a few minutes: what is broken, why this
team fixes it, the proof so far, and what the money buys. Each slide makes one claim in its headline and
proves it in the body. Every number is lifted from the plan (or the founder's sourced data) so the deck,
the model and the data room never disagree. With TOPY connected the deck is generated from the plan (a
credit-charged job), reviewed against the same rules below, edited slide by slide and exported; without
it, the skill writes the outline for the founder's own design tool.

## When to use
- "Make a deck from my plan", "what goes on each slide", "review my deck", "cut my deck down".
- After the raise plan exists (amount, milestones, use of funds), before the first investor meeting.
- Not for: deciding how much to raise (use `topy-fundraising-strategy`); an investor-style critique of the
  plan itself (use `topy-investor-ready`); writing or fixing the plan (use `topy-business-plan`).

## Before you start
- Ask one question at a time: the audience; sent or presented (or both); the raise and use of funds; the
  three numbers the founder is proudest of, with dates.
- With TOPY connected, read first: `plans_list` to find the current plan, then `plan_get` to read the
  executive summary, problem, solution, market, competition, business model, go-to-market, team,
  financials, funding requirement and milestones. Note each section's figures; they are the deck's numbers.
- With TOPY connected, also `decks_list`: a deck for this plan may exist; review and edit it with `deck_get`
  rather than paying to generate another.
- Without TOPY, ask for the plan or a one-page summary and the latest metrics.
- If there is no raise plan yet, run `topy-fundraising-strategy` first; a deck without a clear ask is a
  brochure.

## Workflow
1. **Write the one-liner and the spine.** One-liner: "<Company> helps <customer> <do job> by <how>, unlike
   <alternative>." Spine: five sentences (problem, solution, proof, market, ask). If the spine does not hold
   up as plain text, slides will not save it.
2. **Map plan sections to slides.**
   | # | Slide | Headline is a claim like... | Body / evidence | Plan section |
   |---|---|---|---|---|
   | 1 | Title | the one-liner | logo, round, contact | executive summary |
   | 2 | Problem | "<Customer> loses <x> every <period> on <job>" | who, how often, cost today | problem / market |
   | 3 | Solution | "<Product> does <job> in <time> instead of <time>" | product shot, the 'aha' | solution |
   | 4 | Why now | "<Change> makes this possible / urgent now" | tech, regulation, behaviour shift | market / strategy |
   | 5 | Market | "<N> buyers × <price> = <SAM>; we start with <wedge>" | bottom-up maths, sources | market analysis |
   | 6 | Business model | "We earn <metric> per <unit>, <GM>% gross margin" | pricing, unit economics | business model |
   | 7 | Traction | "<metric> grew from <a> to <b> in <period>" | chart, dated, retention | milestones / KPIs |
   | 8 | Competition | "Buyers choose us over <alternative> because <reason>" | 2-axis map or table | competition |
   | 9 | Go-to-market | "We win customers through <channel> at <CAC>" | channel evidence, funnel | marketing / sales |
   | 10 | Team | "We have built/sold/run <relevant thing> before" | 2-4 people, proof of fit | team |
   | 11 | Financials & milestones | "<Amount> takes us to <milestone> by <date>" | 3-yr summary, milestone chart | financials |
   | 12 | The ask | "Raising <amount> on <instrument> to reach <milestones>" | use of funds (3 buckets), reliefs | funding requirement |
   Appendix (optional, unlimited but rarely read): detailed financials, cohort tables, product details,
   customer case studies, references to the data room.
3. **Order for the audience.** Lead with the strongest proof. Strong traction → move slide 7 to position 3
   or 4. Deep-tech or pre-product → team and why-now earlier. Repeat founders → team early. The order is a
   choice; state why.
4. **Write headlines first, then bodies.** Rules: each headline is a full sentence and a claim; one message
   per slide; body text proves only that claim; at most about 30-40 words of body on a send-ahead slide and
   far fewer on a presenting slide (rule of thumb).
5. **Fill bodies with evidence only.** Every number: copied from the plan or a dated source, with the period
   ("MRR, Sep 2026"), and the same rounding everywhere. Market slide: bottom-up first (buyers × price), any
   top-down figure cited. Traction: absolute numbers and dates beat percentages on small bases ("from 3 to 12
   customers" not "+300%"). Competition: name real alternatives including "spreadsheets" or "do nothing"; no
   "we have no competitors".
6. **Build the ask slide from the raise plan.** Amount, instrument, use of funds as 3 buckets with
   percentages summing to 100, the milestones it reaches with dates, runway in months. UK: if SEIS/EIS
   advance assurance is held or applied for, say which (run `topy-seis` if not); never claim it before HMRC
   has given it.
7. **Make two versions if needed.** Send-ahead: readable without a voice, slightly denser, no animations.
   Presenting: sparse slides, the detail in speaker notes (2-4 bullets per slide).
8. **Generate in TOPY (connected).** `deck_estimate` first and tell the founder the credit cost (risk W2).
   Only after a yes, preview `deck_generate` with `plan_id`, `audience`, `slides` (8–16) and an optional
   `title`, then `confirm: true` with the `confirmation`. It is a job: follow it with `deck_status`, then
   read the result with `deck_get`; apply the order (step 3) and version (step 7) with `deck_update`. A failed
   generation is refunded automatically; generating again costs credits again, so ask.
9. **Run the four tests** (on the generated deck or the outline).
   - *Skim test*: read only the headlines in order; they must tell the whole story.
   - *Consistency test*: every figure matches `plan_get` output (or the model) exactly; list mismatches.
   - *"So what" test*: each slide answers why an investor should care; cut slides that do not.
   - *Objection test*: list the five questions an investor will ask; each is answered on a slide or in the
     appendix.
10. **Fix slides.** Each change (a headline, a number, a reordered slide) is a `deck_update` preview the
    founder sees, then a confirm. Never change a number on a slide so it disagrees with the plan; if the
    plan is wrong, fix the plan first (`topy-plan-revision`).
11. **Export.** `deck_export` with `format` pptx or pdf gives a file for the founder; it changes nothing and
    sends nothing. Sending the deck, or sharing it via the data room, is the founder's call.
12. **Report gaps, do not paper over them.** Missing traction, an unsourced market figure, no competitor
   evidence: list them as gaps with the fix. Plan sections that are weak → `topy-investor-ready`. A figure
   that must change in the plan (e.g. a new raise amount) → `topy-plan-revision`.

## Output
```
Deck outline: <company> · <round> · <sent | presented | both> · prepared <date>
One-liner: ...
| # | Headline (claim) | Body bullets | Evidence / number (source, date) | Plan section | Speaker notes |
Skim test: headlines read in order -> pass / fail (why)
Consistency: figure | deck | plan | match?
Investor objections: question | answered on slide # / appendix
Gaps to fix before sending: gap | fix | owner
```

## Quality bar
- 10-12 main slides; every headline is a sentence and a claim.
- Every number has a period and a source and matches the plan exactly.
- The market slide shows bottom-up maths; top-down figures are cited.
- The ask slide states amount, instrument, use of funds summing to 100% and dated milestones.
- Competition names real alternatives, including the status quo.
- Gaps are listed honestly rather than filled with adjectives.

## Guardrails
- Changes in TOPY take two calls: a preview shown to the user, then `confirm: true` with the `confirmation`
  only after they agree. Never confirm for the user. Plan figures change only through `topy-plan-revision`.
- Generating a deck costs credits (W2): state the `deck_estimate` cost and get a yes before every
  generation or retry.
- Numbers come only from the plan or TOPY tools with a source, or from the founder, labelled as such.
- Never invent figures, customers, logos, quotes, investors, press or awards; label projections as
  projections and assumptions as assumptions.
- Customer names and logos only with the customer's permission; no personal data of customers on slides.
- Not legal or investment advice. Forward-looking statements, regulated activities and rules on promoting
  investments (e.g. UK financial promotion rules) can apply when a deck is circulated: a lawyer should check
  a deck that will be widely shared.

## Related skills
- `topy-fundraising-strategy` — the amount, milestones and story spine the deck tells.
- `topy-investor-ready` — a seed-investor review of the plan behind the deck.
- `topy-business-plan` — write or fix the plan the deck is built from.
- `topy-plan-revision` — carry a changed figure through the saved plan so deck and plan agree.
- `topy-data-room` — the documents that back each slide.
