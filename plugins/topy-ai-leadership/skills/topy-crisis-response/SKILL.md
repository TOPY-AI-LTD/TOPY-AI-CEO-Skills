---
name: topy-crisis-response
description: 'Lead a company through a live crisis: classify severity, contain in the first hours, sequence who hears what and when, recover, and run a blameless review, kept as an incident record in TOPY with its alert, risk and decisions. Use when the user says things like "we have a crisis, what do I do in the next two hours?"; "our production data may have leaked"; "our biggest customer just threatened to leave"; "my co-founder / CTO is quitting"; "a post about us is going viral and it''s bad"; "we can''t make payroll next month". Uses TOPY when it is connected.'
license: MIT
metadata:
  category: leadership
  tier: connected
  version: 0.2.0
  docs: https://github.com/TOPY-AI-LTD/TOPY-AI-CEO-Skills/blob/main/plugins/topy-ai-leadership/skills/topy-crisis-response/SKILL.md
---
# Crisis response

For the moment something has gone badly wrong. The skill gets the founder from shock to a plan: how serious
it is, what to stop or protect in the next two hours, who must hear it from the company first and in what
words, how to recover over the following days, and how to learn from it without blame. Containment always
comes before root cause and before polishing the message.

## When to use
- Security or data incidents, outages, a key person leaving, a major customer loss, a public backlash, a
  cash shortfall, a legal threat, a serious workplace complaint.
- Writing the review after the dust settles.
- Not for: slow-burn risks that are not yet incidents (use `topy-risk-register`); a planned, non-urgent
  change people may resist (use `topy-stakeholder-alignment`); runway planning without an emergency (use `topy-runway`).

## Before you start
- Ask only what is needed to act, one question at a time: what happened and when; known vs suspected; who is
  affected; what is exposed (data, money, contracts, safety); who can act now.
- If people's safety is at risk, the first step is emergency services, not this skill.
- With TOPY connected, read first: `incidents_list` (status open) so the same incident is not opened twice;
  `alerts_list` for the alert that fired (a KPI crossing a threshold is often the first signal) and its time;
  `risks_list` to see whether this risk was already on the register and what mitigation was planned.
- Without TOPY, ask whether anyone had flagged this risk before and what was agreed then.

## Workflow
1. **Call the severity** (decide in minutes; it can be raised or lowered later):
   | Level | Meaning | Response |
   |---|---|---|
   | 1 | Contained annoyance | One owner, monitor, no wide escalation |
   | 2 | Operational disruption | Stabilise, tell affected teams, set a deadline |
   | 3 | Material impact on customers, revenue or reputation | Founder leads, containment plan, external message reviewed |
   | 4 | Existential, legal or safety exposure | Immediate founder response with lawyer, HR and comms as needed |
2. **First 2 hours: contain.**
   - Name an incident lead (one person) and a scribe who keeps a timestamped log of facts and decisions.
   - Stop the bleeding: revoke access, pause the feature or campaign, freeze payments, secure evidence.
   - Separate facts from suspicion in the log; do not speculate in writing about causes or blame.
   - Decide who must be told now (step 4) and draft a holding statement.
   - With TOPY connected, open the record: preview `incident_create` with `incident_type` (`security`,
     `outage`, `customer`, `people`, `financial`, `legal`, `reputation`), `severity` (the level above),
     `summary` (facts only), `impact` (what and who is affected, as ranges), `mitigation` (containment so far),
     `status: "open"`, `owner_user_id` (the incident lead, if they have a TOPY account). Put the alert id and
     the related risk id in its details. Confirm on a yes; containment never waits for the record.
   - Level 3-4: call the company's lawyer. Some obligations have short clocks: for example, under UK and
     EU GDPR a reportable personal-data breach must generally be notified to the regulator within 72 hours
     of becoming aware of it. Insurance policies and contracts may also require prompt notice. The lawyer
     confirms what applies.
3. **First 24 hours: stabilise.** Set a check-in rhythm (e.g. every 2-4 hours at level 3-4); update the
   facts log (and the incident with `incident_update` at each check-in: read with `incident_get`, merge, then
   preview); confirm the blast radius is not growing; brief each audience in sequence; make the decisions
   that cannot wait (refunds, credits, temporary coverage of a departed person's work).
4. **Sequence the communication.** Narrow and private first, then wider:
   1) the people needed to contain it; 2) the strongest ally and the most powerful approver (often the lead
   investor or chair); 3) directly affected customers or staff; 4) the rest of the team; 5) partners;
   6) the public, if needed. Nobody important should learn it from the press or a group chat.
   Message by audience:
   | Audience | Lead with | Avoid |
   |---|---|---|
   | Board / investors | What happened, impact range, control, what you need | Minimising, surprises later |
   | Team | What happened, what it means for them, what to do and not say | Speculating on blame |
   | Affected customers | What happened to them, what we did, what they should do, when we update | Legal jargon, vague timing |
   | Partners | Continuity, specific next steps | Over-sharing unconfirmed facts |
   | Public | Acknowledge, act, update time | Arguing, deleting criticism |
5. **Draft the holding statement:** what we know, what we are doing, what affected people should do, when
   the next update comes. No guesses, no blame, no promises you cannot keep. Lawyer reviews it at level 3-4.
6. **First 2 weeks: recover.** Close the containment actions; restore service or cover; agree decisions on
   compensation, personnel and process; brief stakeholders on resolution; watch for second-order effects
   (churn, morale, recruiting).
7. **Run a blameless review** within two weeks (rule of thumb): timeline, what went well, contributing
   causes (the system, not the person), what was lucky, actions with owners and dates.
8. **Record it.** With TOPY connected, each write previewed and confirmed on a yes:
   - close the incident with `incident_update`: `root_cause` (system causes), `mitigation` (what fixed it and
     what prevents a repeat), `status: "closed"` (`mitigated` while the fix is temporary); the alert is resolved through `topy-alerts`;
   - update the matching risk with `risk_update` (status `occurred`, new scores, mitigation) or, if there was
     none, add it with `risk_create` so the exposure stays tracked;
   - save the key calls (e.g. "notify all customers", "pause launch") with `decision_create`.
   `incident_delete` only for a duplicate or a mistake: permanent (W4). A false alarm is resolved with that as
   the root cause, not deleted.

## Output
```
Crisis plan: <short name> · level <1-4> · lead <name> · opened <time> · incident <id, if saved>
Facts (confirmed) · Unknowns · Exposure (data/money/contracts/safety)
Next 2 hours | action | owner | done by
Next 24 hours | action | owner | done by
Next 2 weeks | action | owner | done by
Communication sequence | # | audience | messenger | channel | when | key message
Holding statement: <4-6 sentences>
Check-ins: every <n> hours until <condition>
```
Post-incident review:
```
Timeline · Impact · What worked · Contributing causes · What was luck · Actions (owner, date) · Follow-up date
```

## Quality bar
- One named lead; a facts log separate from speculation.
- Containment actions come first and have owners and times.
- Every audience has a messenger, a time and a tailored message; affected people hear before the public.
- The holding statement contains no guesses, blame or unkeepable promises.
- Legal, regulatory, insurance and employment points are flagged for professionals with the urgency they need.
- The review names system causes, not scapegoats.

## Guardrails
- Changes in TOPY take two calls: a preview first, shown to the user, then `confirm: true` with the
  `confirmation` only after they agree. Never confirm for the user.
- The agent never speaks for the company: every external statement, customer notice or regulator contact is
  drafted here and sent only by the founder (or with their explicit approval of that exact text, one at a time).
- Personal-data breach: state the statutory clock (e.g. 72 hours under UK/EU GDPR from awareness) at the start,
  and recommend a lawyer immediately.
- Never invent facts, impact figures, customer counts or quotes; label estimates as ranges.
- Not legal advice: breach notification, regulator contact, litigation threats, dismissals, suspensions,
  workplace investigations and public statements about individuals go to a lawyer or HR adviser.
- Never suggest destroying records, misleading regulators, customers or investors, or retaliating.

## Related skills
- `topy-alerts` — the alert that fired, and resolving it when the incident closes.
- `topy-stakeholder-alignment` — deeper stakeholder mapping when recovery needs buy-in.
- `topy-risk-register` — keep the risk and its mitigation tracked after the incident.
- `topy-decision-log` — the decisions made under pressure, reviewed later.
- `topy-runway` — when the crisis is cash.
- `topy-ceo-advisor` — the strategic call that follows stabilisation.
