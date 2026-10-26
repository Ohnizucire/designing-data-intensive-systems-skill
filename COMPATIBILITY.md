# Claude Code, Codex and Hermes Agent — Compatibility

## Shared standard

This repository follows the [Agent Skills specification](https://agentskills.io/specification): one skill directory containing a `SKILL.md` with YAML frontmatter fields `name` and `description`, and supporting files referenced relative to that directory. **The canonical source is `skills/designing-data-intensive-systems/`.** The installer creates agent-specific copies or symlinks; maintaining duplicate skill directories in Git would introduce drift.

## Installation locations

| Agent | Project-local directory | Global/user directory |
| --- | --- | --- |
| Claude Code | `.claude/skills/designing-data-intensive-systems/` | `~/.claude/skills/designing-data-intensive-systems/` |
| OpenAI Codex | `.agents/skills/designing-data-intensive-systems/` | `~/.agents/skills/designing-data-intensive-systems/` |
| Hermes Agent | `.hermes/skills/designing-data-intensive-systems/` | `~/.hermes/skills/designing-data-intensive-systems/` |

The instructions are agent-neutral. The entrypoint is a **model-invoked** skill, with 13 references loaded only when their topic is relevant. The skill doesn't depend on Claude-only hooks, runtime tools or vendor-specific frontmatter.

## Universal NPX / NPM installation

~~~bash
# Global (available across projects)
npx skills add Ohnizucire/designing-data-intensive-systems-skill -g -a claude-code -a codex -a hermes-agent -y

# Project-local (run inside the target project)
npx skills add Ohnizucire/designing-data-intensive-systems-skill -a claude-code -a codex -a hermes-agent -y

# Discover without installing
npx skills add Ohnizucire/designing-data-intensive-systems-skill --list
~~~

`npm exec --yes -- skills add ...` is an equivalent npm invocation. The [Vercel Labs Skills CLI](https://github.com/vercel-labs/skills) supports all three agent IDs, the GitHub `owner/repo` source format and the `--copy` option. No custom `package.json` is necessary for a skills-only repository.

Verify global installation:

~~~bash
test -f ~/.claude/skills/designing-data-intensive-systems/SKILL.md
test -f ~/.agents/skills/designing-data-intensive-systems/SKILL.md
test -f ~/.hermes/skills/designing-data-intensive-systems/SKILL.md
~~~

For project-local installation, verify the corresponding paths relative to the project root.

## Hermes native installation and repository trust

~~~bash
hermes skills install Ohnizucire/designing-data-intensive-systems-skill/skills/designing-data-intensive-systems
hermes skills list

# Optional GitHub tap:
hermes skills tap add Ohnizucire/designing-data-intensive-systems-skill
hermes skills search designing-data-intensive-systems
~~~

Hermes scans project skills in `.hermes/skills/` and `.agents/skills/`, but new project-local skill roots must be trusted with `hermes skills trust`. A global `~/.hermes/skills/` install does not require project trust. Skill availability in an existing session may require refresh or a new session.

## Verification limits

The repository's offline Python test simulates copying the skill to all three documented directories and checks relative references. GitHub Actions additionally runs a real `npx skills add` smoke test using the repository as a local source; this job needs network access to the NPM registry. Both are installation/package checks, **not** proof that independent models invoke the skill appropriately. Behavioral evaluation scenarios remain unexecuted.

## Upstream documentation (checked 2026-10-26)

- [Claude Code skill guide](https://code.claude.com/docs/en/skills)
- [Anthropic Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [Codex — Build Skills](https://learn.chatgpt.com/docs/build-skills)
- [Hermes — Skills System](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/)
- [Vercel Labs Skills CLI](https://github.com/vercel-labs/skills)
- [Agent Skills specification](https://agentskills.io/specification)
