---
name: topy-projects
description: Projects and ideas in TOPY.AI — create a project from an idea or an existing website, update its details, archive it, and generate or brainstorm startup ideas. Use when the user wants to start working on a new company or idea in TOPY, change what a project says about the business, or explore ideas.
---

# Projects and ideas

Follow the shared rules in `topy-ai-ceo`. A project is the company or idea TOPY works on; plans and
records belong to a project.

- **See them.** `projects_list`; details with `project_get`.
- **From an idea.** `project_create_from_idea` with a clear `title` and a `description` (what it does,
  for whom, how it makes money; add `keywords`, `industries`, `unique_selling_points` when known).
- **From a website.** `project_create_from_website` with the `url`; it reads the site as a job — follow
  it with `project_job_get` until it finishes, then `project_get`.
- **Change details.** `project_update` (name, one-liner, description, industry, target market,
  geography, website, keywords). Keep the user's wording.
- **Archive / restore.** `project_delete` / `project_restore` (archiving is reversible).
- **Ideas.** `ideas_generate` around a topic or market; `idea_get`; `idea_brainstorm` (by `idea_id`, or a
  free-text `term`) for market, competitors and angles; `idea_to_project` turns a saved idea into a project.

Then continue with `topy-business-plan` when the user wants a plan for it.
