---
name: topy-hiring-plan
description: Decide which roles to hire, in what order and when, what they cost against runway, and what each hire must achieve, with a scorecard per role; with TOPY each hire is saved as a hire milestone. Use when the user says things like "who should we hire first?"; "build me a hiring plan for the next 12 months"; "can we afford two engineers and a salesperson?"; "should this be a full-time hire or a contractor?"; "write a scorecard for our first sales hire"; "our plan says we hire 6 people, is that realistic?". Uses TOPY when it is connected.
license: MIT
metadata:
  category: operations
  tier: connected
  version: 0.2.0
  docs: https://github.com/TOPY-AI-LTD/TOPY-AI-CEO-Skills/blob/main/plugins/topy-ai-operations/skills/topy-hiring-plan/SKILL.md
---
# Hiring plan

Turns the company's next milestones into a short, ordered list of hires. Each role is justified by the
work it unblocks, timed by a trigger rather than a calendar wish, costed against runway, and defined by a
scorecard of outcomes so the founder knows what "a good hire" means before the first interview. With TOPY
connected it starts from the team and milestone sections of the business plan and the hire milestones already
in TOPY, and saves each agreed hire as a milestone so the operating board tracks it.

## When to use
- "Who do we hire first?", "hiring plan", "can we afford X?", "contractor or employee?", "scorecard for...".
- Before a raise (use of funds), after a raise (deploying it), or when the founder is the bottleneck on
  more than one function.
- Not for: drawing the org chart and ownership lines (use `topy-org-design`); cutting burn when cash is short
  (use `topy-runway`); changing the headcount figures inside a saved plan (use `topy-plan-revision`).

## Before you start
- Ask one question at a time: the milestones that matter most; who is on the team today and where their
  hours go; cash and burn (or a hiring budget); hiring locations.
- With TOPY connected, read first:
  - `plans_list` to find the current plan for the project, then `plan_get` to read its team, milestones,
    operations and financial sections. Note the headcount and salary assumptions the plan already makes;
    the hiring plan must either match them or say plainly where it differs.
  - `milestones_list` and keep those with `milestone_type: hire`: hires already planned (often extracted from
    the plan, with `details.origin`), their `status`, `due_date` and costs. Build on them, don't duplicate.
- Without TOPY, ask for the milestones and the planned headcount line from whatever model or deck exists.
- Never ask for employees' personal data. Roles and costs are enough.

## Workflow
1. **Start from milestones, not roles.** List the 3-5 outcomes for the next 12-18 months (e.g. "first 20
   paying customers", "SOC 2 ready", "self-serve onboarding live"). For each, write the work it needs and
   who does that work today.
2. **Find the bottlenecks.** For each workstream mark: owner today, hours per week it really needs, hours it
   gets, and the cost of it slipping a quarter. A workstream that is under-staffed *and* on the critical
   path to a milestone is a hiring candidate; one that is merely busy is not.
3. **Choose the form of help** with this decision rule:
   | The work is... | Prefer |
   |---|---|
   | Recurring, core to the product or customer, needs context that compounds | Employee |
   | Specialised, bounded, or needed for under ~6 months | Contractor / agency / fractional |
   | Repetitive and well specified | Automation or tooling first, then a hire |
   | Unclear even to the founder | Founder does it first until it can be written down |
   Rule of thumb, not law: whether someone is legally an employee or a contractor depends on how the work
   is actually done, not the contract label. Flag this for a lawyer or HR adviser in the hiring country.
4. **Set a trigger for each hire.** A trigger is an observable condition: "when inbound demos exceed what the
   founder can run in 10 hours a week", "when the seed round closes", "when MRR passes the level that covers
   the role". Calendar dates are only the estimate of when the trigger fires.
5. **Sequence.** Order by: critical path first; roles that make later hires easier (a first engineer before a
   second, a sales lead before SDRs) before roles that depend on them; no manager hired before there is a
   team or a plan for one within two quarters (rule of thumb).
6. **Cost each role fully.** Monthly cost = base salary ÷ 12 + employer taxes and benefits + equipment and
   software + recruiting cost (spread or one-off). Employer on-costs vary by country: ask the founder or
   their accountant for the local figure and label any placeholder as an assumption. Add a ramp: a new hire
   is rarely at full output in month one; state the ramp you assume.
7. **Check against runway.** Build the table month by month: existing burn + each hire from start month.
   Show runway with and without the plan. If runway drops below the founder's floor (ask it; many founders
   use a fundraising-buffer floor), mark the **cut line**: the hires that wait if the raise slips.
8. **Write a scorecard per first hire** (see Output). Outcomes must be measurable and dated; competencies are
   few and tied to those outcomes; deal-breakers are explicit.
9. **Plan the loop for each role.** Stages, owner, and what each stage tests, mapped to the scorecard:
   screen (motivation, must-haves), work sample or case (the top outcome), deep-dive on past work
   (competencies), references (patterns, not praise), founder close. Every stage tests something no other
   stage does.
10. **Reconcile with the plan.** If the hiring plan changes headcount, start months or salary lines from the
    saved business plan, list the differences and hand them to `topy-plan-revision`; do not edit the plan here.
11. **Save each hire as a milestone (TOPY, with a yes).** Adding a hire is a D2 decision: show the full
    list first. For each new role, preview `milestone_create` with `name` ("Hire: first AE"),
    `milestone_type: "hire"`, `status: "planned"`, `due_date` (the target start), and `details`
    {`objective_id` (the goal it serves), `owner_role` (who runs the hiring), `salary_gbp` (annual base),
    `cost_gbp` (fully loaded monthly cost), `start_month` (e.g. "2027-04"), `origin: {"type": "founder"}`}.
    Confirm each only after the founder agrees. Existing hire milestones that change (date, cost, cancelled)
    are updated through `topy-milestones`; one marked `edited` or extracted from the plan is named before it
    is touched. A cancelled hire is `superseded`, not deleted.
12. **Offer to record the decision.** Offer to save "Hiring plan for <period>" with `decision_create`: the
    options considered (e.g. hire now, contractor, wait), the chosen sequence, the cut line and the review date.

## Output
```
Hiring plan: <company> · <period> · prepared <date>
Milestones: 1) ... 2) ... 3) ...
| # | Role | Form (employee/contractor/fractional) | Unblocks milestone | Trigger | Est. start | Monthly cost | Hiring owner |
Budget: burn today <x>/mo · with plan <y>/mo by <month> · runway <a> → <b> months
Cut line if the raise slips: roles below #<n> wait; runway then <c> months
Assumptions: on-costs <%, source>, ramp <months>, salaries <source>
Differences from the saved plan: <list or "none">
```
Scorecard (one per first hire):
```
Role: <title> · reports to <role> · start <month>
Mission: one sentence on why the role exists
Outcomes (12 months): 3-5, each measurable and dated
Competencies: 4-6, each tied to an outcome
Must-haves / deal-breakers: ...
Interview loop: stage | interviewer | what it tests | scorecard item
```

## Quality bar
- Every role traces to a milestone and has an observable trigger.
- The budget table runs month by month and shows runway before and after.
- A cut line exists and says what happens if fundraising is late.
- Every scorecard outcome could be checked by someone else in a year.
- Salary and on-cost figures come from the founder, their accountant or a source they name; otherwise they
  are marked assumptions.
- Differences from the saved business plan are listed, not silently overwritten.
- Every agreed hire exists once as a `hire` milestone with cost, salary and start month.

## Guardrails
- Changes in TOPY take two calls: a preview first, shown to the user, then `confirm: true` with the
  `confirmation` only after they agree. Never confirm for the user.
- Adding headcount is D2: always the founder's yes, never under a standing permission. Changes to the plan's
  headcount or salary figures go through `topy-plan-revision`, never edited here.
- Never invent salary benchmarks, candidate names or market data; label assumptions as assumptions.
- Employment status, contracts, visas, equity grants, notice periods and anti-discrimination rules are
  legal questions: flag them for a lawyer or HR adviser in the relevant country.
- Scorecards describe the work, never protected characteristics (age, gender, nationality, family status
  and the like). Rewrite any "culture fit" item into an observable behaviour.
- Not investment or tax advice: equity and payroll tax treatment goes to an accountant.

## Related skills
- `topy-org-design` — where the new roles sit, who owns what, and spans of control.
- `topy-runway` — burn, runway and the cut plan the cut line feeds.
- `topy-financial-model` — the headcount driver in the model.
- `topy-plan-revision` — carry changed headcount or salaries through the saved plan.
- `topy-milestones` — track hire milestones to done, missed or superseded.
- `topy-decision-log` — keep the hiring decision and review it later.
