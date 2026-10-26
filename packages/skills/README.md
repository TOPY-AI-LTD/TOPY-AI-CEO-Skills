# @topy-ai/ceo-skills

The [TOPY.AI](https://topy.ai) AI CEO skills for **Claude Code, Codex, Pi, Cursor, Gemini CLI, OpenCode, GitHub Copilot, Windsurf** and other coding agents: 51 skills for goals and KPIs, business plans, strategy, fundraising, finance, operations and leadership, powered by the TOPY.AI MCP server.

Install them into one project, or for your user so every project gets them.

```sh
npx @topy-ai/ceo-skills install                  # this project, for the agents set up here
npx @topy-ai/ceo-skills install -g               # your user: every project
npx @topy-ai/ceo-skills install -g -a codex,pi   # pick the agents
```

Pi users can also install it as a Pi package: `pi install npm:@topy-ai/ceo-skills`.

## Supported platforms

| Platform | Install | MCP server |
|---|---|---|
| **Claude Code** | `npx @topy-ai/ceo-skills install -a claude`, or the plugin marketplace | `install --mcp` writes `.mcp.json`, or the `topy-ai` plugin |
| **Codex** (CLI, IDE, ChatGPT desktop) | `npx @topy-ai/ceo-skills install -a codex`, or `codex plugin marketplace add TOPY-AI-LTD/TOPY-AI-CEO-Skills` | `codex mcp add topy --url https://topy.ai/mcp`, or the `topy-ai` plugin |
| **Pi** | `pi install npm:@topy-ai/ceo-skills`, or `npx @topy-ai/ceo-skills install -a pi` | `npx -y @topy-ai/ceo-mcp` |
| **Cursor, Gemini CLI, OpenCode, GitHub Copilot, Windsurf, Amp, Cline, Goose, Kiro, Qwen Code, Trae, Roo Code, Kilo Code, Augment, Factory Droid, OpenHands, Antigravity** | `npx @topy-ai/ceo-skills install -a <agent>` (ids in the table below) | Remote URL `https://topy.ai/mcp` |
| **Claude.ai, Claude Desktop** | Upload a skill folder as a zip ([standalone install](#standalone-install)) | Settings → Connectors → `https://topy.ai/mcp` |
| **ChatGPT** | The tools work through the MCP server | Custom MCP server `https://topy.ai/mcp` |
| **Any other agent** | [Standalone install](#standalone-install) into the folder it reads | Remote URL or `npx -y @topy-ai/ceo-mcp` |

Tested end to end on Claude Code, Codex and Pi; the other folders follow each agent's documented skills location.

## Agents and folders

`--agent` (`-a`) takes one or more agent ids, comma-separated. `auto` (the default) installs for the agents already set up in that scope (their folders exist), else for Claude Code; `all` installs for every agent below. Agents that share a folder get one copy.

| `--agent` | Agent | Project scope | User scope (`-g`) |
|---|---|---|---|
| `claude` | Claude Code | `.claude/skills` | `~/.claude/skills` (`CLAUDE_CONFIG_DIR`) |
| `codex` | Codex | `.agents/skills` | `~/.agents/skills` |
| `pi` | Pi | `.agents/skills` | `~/.agents/skills` |
| `cursor` | Cursor | `.agents/skills` | `~/.cursor/skills` |
| `gemini` | Gemini CLI | `.agents/skills` | `~/.gemini/skills` |
| `opencode` | OpenCode | `.agents/skills` | `~/.config/opencode/skills` |
| `copilot` | GitHub Copilot | `.agents/skills` | `~/.copilot/skills` |
| `amp` | Amp | `.agents/skills` | `~/.config/agents/skills` |
| `cline` | Cline | `.agents/skills` | `~/.agents/skills` |
| `windsurf` | Windsurf | `.windsurf/skills` | `~/.codeium/windsurf/skills` |
| `goose` | Goose | `.goose/skills` | `~/.config/goose/skills` |
| `kiro` | Kiro | `.kiro/skills` | `~/.kiro/skills` |
| `qwen` | Qwen Code | `.qwen/skills` | `~/.qwen/skills` |
| `trae` | Trae | `.trae/skills` | `~/.trae/skills` |
| `roo` | Roo Code | `.roo/skills` | `~/.roo/skills` |
| `kilo` | Kilo Code | `.kilocode/skills` | `~/.kilocode/skills` |
| `augment` | Augment | `.augment/skills` | `~/.augment/skills` |
| `droid` | Factory Droid | `.factory/skills` | `~/.factory/skills` |
| `openhands` | OpenHands | `.openhands/skills` | `~/.openhands/skills` |
| `antigravity` | Antigravity | `.agent/skills` | `~/.gemini/antigravity/skills` |

`npx @topy-ai/ceo-skills agents` prints this table and marks the agents found on your machine. The install record lives in `<project>/.topy-ai/skills-install.json`, or `~/.config/topy/skills-install.json` for the user scope (`TOPY_HOME`). Commit the project's skill folders and `.topy-ai/` to share the skills with your team.

## Pick what you need

```sh
npx @topy-ai/ceo-skills list                                   # every skill, by category
npx @topy-ai/ceo-skills install --category strategy,fundraising       # categories (or plugin names like topy-ai-strategy)
npx @topy-ai/ceo-skills install topy-okrs topy-runway     # single skills
```

The 23 core skills (connect, goal tree, operating board, daily brief, weekly review, KPIs and alerts, business plan, plan revision, decision log, risk register…) always come along: the other skills hand off to them. Strategy, fundraising, finance, operations and leadership skills also work without a TOPY account.

## Connect the MCP server

The core skills run on the TOPY.AI MCP server, `https://topy.ai/mcp` (OAuth: sign in to TOPY.AI, no keys to paste; for scheduled agents, an API key as `TOPY_API_KEY`).

```sh
npx @topy-ai/ceo-skills install --mcp      # also adds it to the project's .mcp.json (Claude Code)
npx @topy-ai/ceo-skills mcp -g             # prints the commands for Claude Code, Codex, Gemini CLI, Cursor and Pi
```

## Update and remove

```sh
npx @topy-ai/ceo-skills@latest update                 # this project
npx @topy-ai/ceo-skills@latest update -g              # your user
npx @topy-ai/ceo-skills remove topy-cap-table           # or --all; -a codex removes it for one agent only
npx @topy-ai/ceo-skills doctor                        # check an install
```

`update` brings installed skills to the new version, for the agents you installed them for, and adds new skills in the categories you chose. Files you edited are kept (you'll see `kept …`); pass `--force` to replace them. `remove` also keeps folders you edited unless you pass `--force`. Every command accepts `--dry-run`.

Used `topy skills install` from the old `@topy-ai/ceo` CLI? Its `topy-ai-ceo`, `topy-fundraising` and `topy-ceo-workspace` folders in `~/.claude/skills` and `~/.codex/skills` are replaced by this catalogue (`topy-connect`, `topy-ceo-advisor`, `topy-fundraising-strategy`, the record skills): delete them, then `npx @topy-ai/ceo-skills install -g`.

## Standalone install

Each skill is one self-contained folder with a `SKILL.md` (the open Agent Skills format), so you can also install without this package.

All skills, without Node (macOS, Linux, WSL; change the target to the folder your agent reads):

```sh
git clone --depth 1 https://github.com/TOPY-AI-LTD/TOPY-AI-CEO-Skills.git
mkdir -p ~/.agents/skills
cp -R TOPY-AI-CEO-Skills/plugins/*/skills/* ~/.agents/skills/
```

One skill, no clone:

```sh
mkdir -p ~/.agents/skills
curl -sL https://github.com/TOPY-AI-LTD/TOPY-AI-CEO-Skills/archive/refs/heads/main.tar.gz \
  | tar -xz --strip-components=4 -C ~/.agents/skills TOPY-AI-CEO-Skills-main/plugins/topy-ai-strategy/skills/topy-decision-memo
```

- Windows: download the [ZIP](https://github.com/TOPY-AI-LTD/TOPY-AI-CEO-Skills/archive/refs/heads/main.zip) and copy the folders from `plugins\<plugin>\skills\` to your agent's skills folder, or run `npx @topy-ai/ceo-skills` in PowerShell.
- Claude.ai and Claude Desktop: zip one skill folder (for example `topy-decision-memo/`) and upload it in Settings → Capabilities → Skills.
- Agents without a skills folder: paste a `SKILL.md` into the agent's custom instructions or rules.
- The open `skills` CLI: `npx skills add TOPY-AI-LTD/TOPY-AI-CEO-Skills -a <agent>`.

Copied by hand, skills are updated by copying again; installed with `npx @topy-ai/ceo-skills`, `update` keeps your edits.

## Other ways to install

- Claude Code plugins: `/plugin marketplace add TOPY-AI-LTD/TOPY-AI-CEO-Skills`, then `/plugin install topy-ai-all@topy-ai`.
- Codex plugins: `codex plugin marketplace add TOPY-AI-LTD/TOPY-AI-CEO-Skills`, then `codex plugin add topy-ai@topy-ai` (it brings the MCP server; `codex mcp login topy` signs in).
- Pi packages: `pi install npm:@topy-ai/ceo-skills` or `pi install git:github.com/TOPY-AI-LTD/TOPY-AI-CEO-Skills`.

Source, skills index and changelog: [TOPY-AI-LTD/TOPY-AI-CEO-Skills](https://github.com/TOPY-AI-LTD/TOPY-AI-CEO-Skills).

## License

MIT © TOPY AI LTD.
