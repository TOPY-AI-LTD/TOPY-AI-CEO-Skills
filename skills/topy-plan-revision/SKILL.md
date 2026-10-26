---
name: topy-plan-revision
description: Revise a TOPY.AI business plan for a change that runs through it — a funding amount, price, milestone, KPI, hire or team change — updating every affected section (GTM, financials, use of funds...) consistently as a new version. Use when the user says something like "we're raising £250k now", "push launch to Q3", "add a CTO", "change the target to 300 customers" for an existing plan.
---

# Revise a plan for a change

Follow the shared rules in `topy-ai-ceo`. Never edit sections one by one for this: the revision keeps
every figure consistent and keeps the original plan.

1. **Which plan.** `plans_list` for the project; take the plan the user means (ask if unclear).
2. **Analyse.** `plan_revise_analyze` with `plan_id` and the change in the user's words
   (`change_request`). It changes nothing and costs no credits. Follow the returned job with
   `plan_status` (`job_id`) until `success` (usually under a minute).
3. **Show the analysis** from the job's `result_json.analysis`:
   - `change_summary`;
   - every `fact_changes` item: old → new;
   - every `derived_figures` item with its `basis` — point out the ones marked as assumptions;
   - the sections it will update (`impact` minor / major, and what changes); sections marked `none` are
     left as they are.
   Ask the user to confirm or correct the figures, and whether to leave any section out.
4. **Apply.** `plan_revise_apply` with `plan_id`, `analysis_job_id`, the user's `corrections` (their
   words; they override the analysis) and `selected` only if they left sections out. Preview, then
   confirm after the user agrees. It writes a **new version** ("… (revised <date>)"); the original stays.
5. **Follow** with `plan_status` (`job_id`) — about 4 minutes. Report the revised sections, any
   consistency fixes, and any `remaining_issues` it lists as worth a look. Give the new plan's id.

If the analysis looks wrong (a figure misread, a section missed), correct it in step 4 rather than
starting over; run a new analysis only if the change itself was misunderstood.
