# Designing Data-Intensive Systems — Agent Skill

A reusable, technology-agnostic **Agent Skill** for designing, implementing, debugging, and reviewing applications that persist, exchange, or derive data.

Inspired by the **complete second edition** of *Designing Data-Intensive Applications* (Martin Kleppmann and Chris Riccomini, 2026), this project turns interconnected systems-design principles into actionable decisions and verification criteria. It applies to everyday CRUD services as well as distributed systems: **start with the simplest architecture that meets the requirements**.

> **Scope and status:** This is an independent, original operational interpretation of the book, not an official companion or a reproduction of its text. Static package checks pass; behavioral tests with independent agents and production-system tests have **not** been run.

## What the agent does

1. Trace affected reads, writes, materialized views, clients, and sources of truth.
2. State end-to-end invariants, safety/liveness expectations, and failure behavior.
3. Establish workload, operational constraints, latency budgets, and recovery targets using measured values or explicit unknowns.
4. Load only the relevant topic references and their cross-chapter implications.
5. Compare the smallest sufficient architecture against more complex alternatives.
6. Verify invariants through tests, concurrency/fault scenarios, migrations, and recovery checks as applicable.
7. Report decisions, evidence, unknowns, rollback plans, and measurable redesign triggers.

Each step has an observable **Done** criterion in [`SKILL.md`](designing-data-intensive-systems/SKILL.md). The skill adds data-engineering judgment; it does not replace your agent's coding, TDD, review, or debugging workflows.

## Install

Copy the skill folder into your agent's discoverable skills directory. For agents supporting the common `~/.agents/skills/` location:

```bash
git clone https://github.com/Ohnizucire/designing-data-intensive-systems-skill.git
mkdir -p ~/.agents/skills
cp -r designing-data-intensive-systems-skill/designing-data-intensive-systems ~/.agents/skills/
```

Other agents may use different skill directories. For **Hermes Agent**, enable its skills toolset, configure the skill location according to your Hermes installation, and optionally invoke `skill_view("designing-data-intensive-systems")`.

### Example prompt

```text
Review this application using designing-data-intensive-systems.
Trace the complete data lifecycle, identify authoritative state and
failure boundaries, justify the least-complex design that meets the
requirements, and show which invariants are verified versus untested.
```

## What's included

| Path | Purpose |
| --- | --- |
| [`designing-data-intensive-systems/SKILL.md`](designing-data-intensive-systems/SKILL.md) | Model-invoked entrypoint, procedure, and conditional routing |
| [`references/`](designing-data-intensive-systems/references/) | 13 topic modules, cross-chapter dependencies, and a decision record |
| [`provenance/whole-book-map.md`](designing-data-intensive-systems/provenance/whole-book-map.md) | Conceptual connections across the 14 chapters |
| [`provenance/section-ledger.md`](designing-data-intensive-systems/provenance/section-ledger.md) | Section-level source coverage index |
| [`examples/`](designing-data-intensive-systems/examples/) | Applied architecture example |
| [`tests/agent-scenarios.md`](designing-data-intensive-systems/tests/agent-scenarios.md) | 20 proposed agent behavior evaluation scenarios |
| [`scripts/validate_pack.py`](designing-data-intensive-systems/scripts/validate_pack.py) | Static structural validation |
| [`AUDIT.md`](AUDIT.md) | Source, writing-standard, and verification limitations |

The 13 modules cover workload trade-offs; modeling; storage and retrieval; schema evolution; replication and local-first design; sharding; transactions; partial failures; consistency and consensus; batch processing; streams and CDC; end-to-end data correctness; and ethics and data rights.

## Verify the package

```bash
python3 designing-data-intensive-systems/scripts/validate_pack.py
```

The static validator checks routing, coverage, references, and declared test scenarios. **Passing it does not demonstrate that an agent follows the instructions correctly.** Run the scenarios in [`tests/agent-scenarios.md`](designing-data-intensive-systems/tests/agent-scenarios.md) in fresh agent contexts, with and without the skill, before making behavioral quality claims. Validate each real system independently.

## Design standards and attribution

- Source concepts: *Designing Data-Intensive Applications*, 2nd ed., Martin Kleppmann and Chris Riccomini. The copyrighted EPUB is **not included**.
- Agent documentation principles: [Matt Pocock's Writing for Agents](https://github.com/mattpocock/skills/tree/main/skills/productivity/writing-for-agents) and [Superpowers](https://github.com/obra/superpowers) guidance on writing/verifying skills.
- These inspirations do not imply endorsement or certification by the book authors or the referenced skill projects.

All repository documentation and skill instructions are in English. No license is asserted for this repository; consult the repository owner about reuse beyond rights provided by applicable law.
