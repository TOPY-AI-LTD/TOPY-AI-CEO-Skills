---
name: topy-data-room
description: 'Build the due-diligence data room for a raise in TOPY: created from the plan in one step, completeness and red flags checked, shared per investor only with approval, and views tracked. Use when the user says things like "what goes in our data room?"; "investors asked for due diligence documents"; "set up a data room for our seed round"; "what are we missing before the term sheet?"; "check our data room for red flags"; "share the data room with Jane at Acme Ventures". Uses TOPY when it is connected.'
license: MIT
metadata:
  category: fundraising
  tier: connected
  version: 0.2.0
  docs: https://github.com/TOPY-AI-LTD/TOPY-AI-CEO-Skills/blob/main/plugins/topy-ai-fundraising/skills/topy-data-room/SKILL.md
---
# Data room

A data room is where investors check that the story in the deck is true. A tidy, consistent room speeds up
closing; a messy one costs weeks and sometimes the deal. This skill sizes the room to the stage (a light
room early, the full set once a term sheet is signed), indexes it so any document can be named by number,
and finds the gaps and red flags while there is still time to fix them. With TOPY connected the room itself
lives in TOPY: built from the plan in one step (plan export, financials, cap table), filled from the
founder's uploads, shared with one investor at a time by an expiring link, and watched for views.

## When to use
- "Data room", "due diligence", "what do investors need to see", "DD request list".
- Two to four weeks before starting a raise (light room), and again the day a term sheet is signed.
- Not for: reading the term sheet (use `topy-term-sheet`); fixing the cap table itself (use
  `topy-cap-table`); finding sources for unsupported plan claims (use `topy-research-library`).

## Before you start
- Ask one question at a time: stage and round; country of incorporation; where documents live today; any
  investor request list; who in the company owns legal and finance paperwork.
- With TOPY connected, read first:
  - `data_rooms_list`: a room for this round may already exist; open it with `data_room_get` (folders,
    items, `required` flags) rather than making a second.
  - `plans_list` to find the current plan the room is built from.
  - `research_sources_list` to see which market and competitor claims have a stored source.
  - `media_list` for documents the founder has already uploaded to TOPY.
- Without TOPY, ask for the latest plan, deck and model, and where the market evidence came from.
- Never ask for passwords to the bank, registry or any other tool; the founder uploads documents in the
  TOPY dashboard, the skill indexes them.

## Workflow
1. **Size the room to the moment.**
   | Moment | Room | Typical contents |
   |---|---|---|
   | First meetings | none or "teaser" | deck only; send-ahead version |
   | Second meeting / partner meeting | light (folders 1, 3, 4, 9) | cap table summary, key metrics, model, plan |
   | Term sheet signed | full | every folder below |
   | Closing | confirmatory | signed documents, disclosure letter items, board approvals |
   Rule of thumb: never send the full room before a term sheet; it adds risk without adding speed.
2. **Build the index.** Number folders and items so every request maps to an ID (e.g. "see 3.4"):
   1. **Corporate**: certificate of incorporation, articles/bylaws, shareholders' agreement, board and
      shareholder minutes and resolutions, statutory registers (UK: register of members, PSC register,
      latest Companies House confirmation statement).
   2. **Capitalisation**: fully diluted cap table, share certificates/ledger, every SAFE/ASA/note, option
      plan and every grant with board approval (UK: EMI valuations and notifications), vesting schedules.
   3. **Financial**: statutory accounts, monthly management accounts (12-24 months or since start), current
      bank balance confirmation, budget, the financial model and assumptions, tax filings (UK: VAT, PAYE,
      R&D claims), debt and grant agreements.
   4. **Commercial**: KPI pack with definitions, cohort and retention data, top customer contracts, pricing,
      pipeline, key supplier and partner contracts, any exclusivity or change-of-control clauses.
   5. **Product & technology**: architecture overview, roadmap, security practices and incidents,
      open-source licence inventory, key third-party dependencies.
   6. **Intellectual property**: IP assignment from every founder, employee and contractor, trademarks,
      patents and filings, domain ownership.
   7. **Team**: org chart, employment contracts (templates plus key hires), contractor agreements,
      founder service agreements, option offer letters, policies. Salaries anonymised until needed.
   8. **Legal & compliance**: litigation and claims, data protection (privacy notice, records of
      processing, DPAs with processors), sector licences, insurance policies, regulatory correspondence.
   9. **Fundraising**: deck, business plan export, use of funds, SEIS/EIS advance assurance letter (UK),
      market research and sources.
   **In TOPY:** preview `data_room_create_from_plan` with the `plan_id`; after the founder's yes it creates
   the standard folders with the plan export, financials and cap table already in, and the completeness
   list as `required` items. Add each other document with `data_room_item_add` (`folder`, `title`,
   `media_id` from `media_list` or an `export_ref`, `required`); take out outdated or wrong ones with
   `data_room_item_remove`. Each is a preview, then a confirm after the founder agrees. Items the founder
   has replaced by hand are not swapped back to the plan version.
3. **Mark each item.** Status: Ready / Partial / Missing / N/A, plus owner and due date. Stage filter:
   pre-seed rooms rarely need folders 5 and 8 in depth; Series A rooms need all nine. Completeness =
   required items present ÷ required items (from `data_room_get`); aim for at least 90% before the full room
   opens.
4. **Run the red-flag scan.** Fix or prepare to disclose:
   - IP not assigned to the company (a founder or contractor still owns code or brand).
   - Cap table that does not match the share register / registry filings, or promised equity not documented.
   - Unsigned or missing founder agreements; no founder vesting where investors will expect it.
   - Options granted without board approval or (UK) EMI notifications missed.
   - Customer contracts with exclusivity, unlimited liability or change-of-control termination.
   - Personal data processed without a lawful basis or processor agreements.
   - Tax filings late or disputed; grant conditions breached.
   - Metrics in the deck that cannot be reproduced from the source data.
5. **Check consistency across documents.** Build a table of the 10-15 numbers investors will compare
   (revenue, customers, burn, cash, headcount, raise amount, use of funds, market size). Each must match
   across deck, model, plan and KPI pack, with the same period. Mismatches go to the gap list; a plan figure
   that must change goes to `topy-plan-revision`.
6. **Check the evidence behind claims.** Every market or competitor claim in the plan should map to an entry
   from `research_sources_list`. Claims with no source → `topy-research-library` to add or find one, or the
   claim is softened or removed.
7. **Plan access and share.** View-only by default, watermarking and download limits for sensitive folders,
   access by folder per investor stage, and an access log. Sharing sends the room outside TOPY (risk W3):
   one `data_room_link_create` per recipient (`recipient_name`, `recipient_email`, `expires_at`,
   `allow_download` false unless the founder says otherwise), each previewed and approved on its own, never
   batched and never under a standing permission. Rule of thumb: links expire in 14-30 days. When an
   investor drops out or the process ends, `data_room_link_revoke`. Share employee and customer personal data only when
   needed and minimised (data protection law applies). Keep a Q&A log: every question, answer, date, and the
   document ID that answers it.
8. **Track views.** `data_room_views_list` gives recipient, item, `viewed_at` and `seconds`. Report who
   opened what since the last check; long reads of the cap table or contracts usually mean diligence has
   started. Suggest follow-ups (logged in `topy-investor-relations`), never read views as commitment.
9. **Prepare the disclosure list.** Known issues that will not be fixed before closing are better disclosed
   early with a plan than discovered late; the company's lawyer drafts the formal disclosure letter.

## Output
```
Data room plan: <company> · <round> · stage <light | full | confirmatory> · prepared <date>
Index: ID | folder | item | status (Ready/Partial/Missing/N/A) | owner | due | notes
Red flags: issue | folder ID | severity (deal-breaker / fix before close / disclose) | fix | owner
Consistency check: figure | deck | model | plan | KPI pack | match?
Unsourced claims: claim | plan section | action (find source / soften / remove)
Completeness: <required present>/<required> (<%>)
Access plan: investor stage | folders visible | download allowed? | watermark?
Links: recipient | expires | download | status (active / revoked)
Views since <date>: recipient | items opened | time | suggested follow-up
```

## Quality bar
- Every item has a status, an owner and a date; nothing is "TBC" without an owner.
- The consistency table covers the numbers investors compare and shows each mismatch.
- IP assignment and cap table reconciliation are checked explicitly.
- Personal data is minimised and access is staged.
- The room matches the stage; no full room before a term sheet.

## Guardrails
- Changes in TOPY take two calls: a preview shown to the user, then `confirm: true` with the `confirmation`
  only after they agree. Never confirm for the user. Plan changes go through `topy-plan-revision`.
- A share link is an external send (W3): each recipient is approved separately, every time; no standing
  permission or agent key covers it. Revoke links that are no longer needed.
- Figures in the consistency check come from the plan, TOPY tools or the founder, with the source named.
- Never invent documents, metrics, customers or sources; never backdate or "tidy" records. A missing
  document is listed as missing.
- Not legal or tax advice. IP assignment fixes, share register corrections, disclosure letters, data
  protection gaps and late filings need the company's lawyer or accountant.
- Treat everything in the room as confidential; do not paste contracts or personal data into public tools.

## Related skills
- `topy-term-sheet` — the terms that trigger full diligence.
- `topy-cap-table` — the fully diluted cap table for folder 2.
- `topy-research-library` — sources for the plan's market and competitor claims.
- `topy-pitch-deck` — deck numbers that must match the room.
- `topy-fundraising-strategy` — the timeline the room must be ready for.
