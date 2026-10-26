---
name: topy-fundraising
description: Fundraising with TOPY.AI — check a business plan the way an investor would, draft a UK SEIS Advance Assurance application, keep the investor pipeline, and write investor updates. Use when the user is preparing to raise, mentions SEIS/EIS, investors, a pitch, or an investor update.
---

# Fundraising

Follow the shared rules in `topy-ai-ceo`.

## Is the plan investor-ready?

1. `plans_list` → the newest finished plan (or the one the user names); read it with `plan_get` `full: true`.
2. Check like a seed investor: specific problem and customer; market sized with sources; financial
   assumptions stated and the same in every section; use of funds tied to milestones; honest risks.
3. Give the five fixes that matter most, most important first, each with its section. Offer
   `plan_section_suggest` for a fix the user picks, or `topy-plan-revision` when a figure has to change
   everywhere. Don't change anything unasked.

## SEIS Advance Assurance (UK)

`plan_seis_assurance` with the plan and the route (`activity_type`: `qualifying_trade`,
`rd_intended_to_lead_to_qualifying_trade` or `rd_existing_qualifying_trade`; ask if unsure). It drafts
the answers from the plan; show them and remind the user HMRC needs the supporting documents listed.

## Investor pipeline and updates

- Contacts: `investor_contacts_list`, `investor_contact_create` / `_update` / `_delete` (deletes are
  permanent — the preview says so).
- Updates: read `decisions_list`, `growth_experiments_list`, `journal_entries_list`, `risks_list` and
  the last `investor_updates_list` entry; draft highlights, metrics (only figures you found — mark
  gaps), lowlights, decisions and asks in under 400 words; after the user approves, save it with
  `investor_update_create`.
