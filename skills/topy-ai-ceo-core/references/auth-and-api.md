# Connecting to TOPY

`topy-ai-ceo-core` itself never calls TOPY. When the user wants something done in their TOPY account
(plans, revisions, projects, records), hand over to the product skills, starting with `topy-ai-ceo`.

They reach TOPY in one of these ways — never by asking the user for a key in the chat:

1. **MCP tools** from the TOPY connector, `https://topy.ai/mcp` (Claude, ChatGPT, Claude Code, Cursor),
   signed in with the user's TOPY account.
2. **The `topy` CLI** (`npm i -g @topy-ai/ceo`, `topy login`), or `TOPY_API_KEY` from Dashboard → API keys.

Every change is previewed first and runs only after the user confirms it. The REST API underneath is
`https://topy.ai/api/v1`; the tool catalogue is at `https://topy.ai/api/v1/agent/tools`.
