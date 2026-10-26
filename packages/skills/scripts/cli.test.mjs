// node --test: runs the CLI against temporary projects and a temporary HOME.
import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import { appendFileSync, cpSync, existsSync, mkdirSync, mkdtempSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { dirname, join } from "node:path";
import { test } from "node:test";
import { createHash } from "node:crypto";
import { fileURLToPath } from "node:url";

const BIN = join(dirname(fileURLToPath(import.meta.url)), "..", "bin", "topy-skills.mjs");
const catalog = JSON.parse(readFileSync(join(dirname(BIN), "..", "catalog.json"), "utf8"));
const core = catalog.skills.filter((s) => s.category === "core").map((s) => s.id);

function sandbox() {
	const dir = mkdtempSync(join(tmpdir(), "topy-skills-test-"));
	const home = join(dir, "home");
	const project = join(dir, "project");
	mkdirSync(home, { recursive: true });
	mkdirSync(project, { recursive: true });
	const env = { ...process.env, HOME: home, CLAUDE_CONFIG_DIR: "", CODEX_HOME: "", TOPY_HOME: "" };
	for (const k of ["CLAUDE_CONFIG_DIR", "CODEX_HOME", "TOPY_HOME"]) delete env[k];
	const run = (...args) => {
		const r = spawnSync(process.execPath, [BIN, ...args], { cwd: project, env, encoding: "utf8" });
		return { code: r.status, out: r.stdout + r.stderr };
	};
	return { dir, home, project, run, done: () => rmSync(dir, { recursive: true, force: true }) };
}

test("project scope installs every skill for Claude Code by default", () => {
	const t = sandbox();
	try {
		const r = t.run("install");
		assert.equal(r.code, 0, r.out);
		for (const s of catalog.skills) assert.ok(existsSync(join(t.project, ".claude", "skills", s.id, "SKILL.md")), s.id);
		assert.ok(!existsSync(join(t.project, ".agents")));
		const state = JSON.parse(readFileSync(join(t.project, ".topy-ai", "skills-install.json"), "utf8"));
		assert.equal(state.scope, "project");
		assert.equal(state.skills.length, catalog.skills.length);
		assert.equal(t.run("doctor").code, 0);
	} finally {
		t.done();
	}
});

test("user scope installs into ~/.claude and ~/.agents (Codex, Pi) and leaves the project alone", () => {
	const t = sandbox();
	try {
		const r = t.run("install", "-g", "-a", "claude,codex,pi", "--category", "strategy");
		assert.equal(r.code, 0, r.out);
		for (const root of [join(t.home, ".claude", "skills"), join(t.home, ".agents", "skills")]) {
			assert.ok(existsSync(join(root, "topy-decision-memo", "SKILL.md")));
			for (const id of core) assert.ok(existsSync(join(root, id, "SKILL.md")), `core ${id}`);
			assert.ok(!existsSync(join(root, "topy-cap-table")));
		}
		const state = JSON.parse(readFileSync(join(t.home, ".config", "topy", "skills-install.json"), "utf8"));
		assert.equal(state.targets.length, 2);
		assert.deepEqual(state.targets.find((x) => x.dir.endsWith(".agents/skills")).agents, ["codex", "pi"]);
		assert.ok(!existsSync(join(t.project, ".claude")));
		assert.equal(t.run("doctor", "--global").code, 0);
	} finally {
		t.done();
	}
});

test("agents that share .agents/skills get one copy; auto picks up agent folders", () => {
	const t = sandbox();
	try {
		let r = t.run("install", "topy-runway", "--agent", "codex,pi,cursor,gemini");
		assert.equal(r.code, 0, r.out);
		assert.ok(existsSync(join(t.project, ".agents", "skills", "topy-runway", "SKILL.md")));
		assert.equal((r.out.match(/installed .*topy-runway/g) || []).length, 1);
		mkdirSync(join(t.project, ".windsurf"));
		r = t.run("install", "topy-okrs", "--agent", "auto");
		// auto reuses the recorded targets, not newly appearing folders
		assert.ok(!existsSync(join(t.project, ".windsurf", "skills")));
		r = t.run("install", "topy-okrs", "-a", "windsurf");
		assert.ok(existsSync(join(t.project, ".windsurf", "skills", "topy-okrs", "SKILL.md")));
		assert.match(t.run("agents").out, /pi +Pi +\.agents\/skills/);
		assert.equal(t.run("install", "-a", "nope").code, 2);
	} finally {
		t.done();
	}
});

test("a 0.3.0 user record (Codex in ~/.codex/skills) keeps updating there", () => {
	const t = sandbox();
	try {
		const dir = join(t.home, ".codex", "skills", "topy-connect");
		mkdirSync(dirname(dir), { recursive: true });
		cpSync(join(dirname(BIN), "..", "skills", "topy-connect"), dir, { recursive: true });
		const file = join(dir, "SKILL.md");
		writeFileSync(file, "old");
		const stateDir = join(t.home, ".config", "topy");
		mkdirSync(stateDir, { recursive: true });
		const sha = (s) => createHash("sha256").update(s).digest("hex");
		writeFileSync(join(stateDir, "skills-install.json"), JSON.stringify({ version: "0.3.0", scope: "user", agents: ["codex"], selection: { categories: [], skills: ["topy-connect"] }, skills: ["topy-connect"], files: { [file]: sha("old") } }));
		const r = t.run("update", "-g");
		assert.equal(r.code, 0, r.out);
		assert.notEqual(readFileSync(file, "utf8"), "old");
		assert.match(r.out, /Codex now reads ~\/\.agents\/skills/);
		assert.ok(!existsSync(join(t.home, ".agents")));
	} finally {
		t.done();
	}
});

test("package.json declares the skills for Pi", () => {
	const pkg = JSON.parse(readFileSync(join(dirname(BIN), "..", "package.json"), "utf8"));
	assert.deepEqual(pkg.pi.skills, ["./skills"]);
	assert.ok(pkg.keywords.includes("pi-package"));
});

test("update keeps edited files unless --force", () => {
	const t = sandbox();
	try {
		t.run("install", "topy-decision-memo");
		const file = join(t.project, ".claude", "skills", "topy-decision-memo", "SKILL.md");
		appendFileSync(file, "\nmy note\n");
		let r = t.run("update");
		assert.match(r.out, /kept .*topy-decision-memo/);
		assert.match(readFileSync(file, "utf8"), /my note/);
		r = t.run("update", "--force");
		assert.doesNotMatch(readFileSync(file, "utf8"), /my note/);
	} finally {
		t.done();
	}
});

test("remove keeps edited folders, --force removes them; --mcp writes .mcp.json once", () => {
	const t = sandbox();
	try {
		t.run("install", "--category", "fundraising", "--mcp");
		const mcp = JSON.parse(readFileSync(join(t.project, ".mcp.json"), "utf8"));
		assert.equal(mcp.mcpServers["topy"].url, "https://topy.ai/mcp");
		const dir = join(t.project, ".claude", "skills", "topy-term-sheet");
		appendFileSync(join(dir, "SKILL.md"), "x");
		t.run("remove", "topy-term-sheet", "topy-pitch-deck");
		assert.ok(existsSync(dir));
		assert.ok(!existsSync(join(t.project, ".claude", "skills", "topy-pitch-deck")));
		t.run("remove", "--all", "--force");
		assert.ok(!existsSync(dir));
		assert.ok(!existsSync(join(t.project, ".topy-ai", "skills-install.json")));
	} finally {
		t.done();
	}
});

test("bad input exits 2", () => {
	const t = sandbox();
	try {
		assert.equal(t.run("install", "--category", "nope").code, 2);
		assert.equal(t.run("install", "--scope", "team").code, 2);
		assert.equal(t.run("update").code, 2);
	} finally {
		t.done();
	}
});
