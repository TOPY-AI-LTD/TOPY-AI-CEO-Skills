---
name: topy-pitch-deck
description: 'Build the 10-12 slide investor story from the business plan: one claim per slide, the evidence behind it, and numbers that match the plan exactly. Use when the user says things like "turn my business plan into a pitch deck"; "write the slides for our seed round"; "what should go on each slide?"; "review my deck before I send it to investors"; "our deck is 25 slides, help me cut it"; "what''s the story of our pitch?". Uses TOPY when it is connected.'
license: MIT
metadata:
  category: fundraising
  tier: connected
  version: 0.1.0
  docs: https://github.com/TOPY-AI-LTD/TOPY-AI-CEO-Skills/blob/main/plugins/topy-ai-fundraising/skills/topy-pitch-deck/SKILL.md
---
# Pitch deck

Turns a business plan into the short story an investor reads in a few minutes: what is broken, why this
team fixes it, the proof so far, and what the money buys. Each slide makes one claim in its headline and
proves it in the body. Every number is lifted from the plan (or the founder's sourced data) so the deck,
the model and the data room never disagree. The skill writes the content and structure; design is up to
the founder's tool of choice.

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
8. **Run the four tests.**
   - *Skim test*: read only the headlines in order; they must tell the whole story.
   - *Consistency test*: every figure matches `plan_get` output (or the model) exactly; list mismatches.
   - *"So what" test*: each slide answers why an investor should care; cut slides that do not.
   - *Objection test*: list the five questions an investor will ask; each is answered on a slide or in the
     appendix.
9. **Report gaps, do not paper over them.** Missing traction, an unsourced market figure, no competitor
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
- The skill only reads TOPY. Changing a plan figure goes through `topy-plan-revision`: a preview shown to
  the user, then `confirm: true` with the `confirmation` only after they agree. Never confirm for the user.
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
