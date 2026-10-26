# Source and Writing-Standard Audit — 2026-10-26

## Book source

- User-uploaded complete EPUB: *Designing Data-Intensive Applications*, 2nd ed., Martin Kleppmann and Chris Riccomini, O'Reilly Media, ISBN 9781449373320. Metadata date: 2026-02-18.
- EPUB SHA-256 (local source identifier): `9e1159d2c06a39a5168d0fa0ec9c9bdb1dc3f478cf23061396cdfc41892bb385`.
- All 14 main chapter XHTML files extracted; approximately 204,351 words of **main text**, excluding chapter bibliographies, indexed for section-level review. Original bibliography and footnotes remain in the source EPUB.
- `503` substantive chapter sections indexed in `provenance/section-ledger.md`; all 14 chapters have a main decision module and a conceptual argument in `provenance/whole-book-map.md`. Cross-chapter obligations in `references/cross-chapter-dependencies.md` connect the concepts.
- **Reading qualification:** Complete chapter bodies were processed to create the section ledger and conceptual synthesis, and technical passages were examined. This is a systematic full-book structural/content analysis, but it is not a claim that a separate human-style line-by-line commentary exists for every sentence or cited reference. Source bibliography and third-party empirical claims have not been independently verified.

## Original operational interpretation vs source

The book's conceptual claims and trade-offs are the source. The routing mechanism, 13 references, checklists, completion gates, decision record, test requirements and agent evaluation rubric are newly designed operationalizations. They are not quotations nor statements of author endorsement. No source text is included in this bundle.

## Writing-for-agents sources

- Matt Pocock [`SKILL.md`](https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-for-agents/SKILL.md) — source blob `a37608daf6e835e767deecfb498facecaaba82ba`.
- Matt Pocock [`SKILL-MECHANICS.md`](https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-for-agents/SKILL-MECHANICS.md) — source blob `9cdbdb22aadc438755392216e75ad9a14cc9832e`.
- Superpowers `using-superpowers`, `brainstorming`, `writing-skills`, `test-driven-development`, and `verification-before-completion` skill documentation read in this session/conversation.

| Requirement | Concrete choice | Status |
|---|---|---|
| English-only authored files | `SKILL.md`, references, example, README, tests, audit | structurally inspected; full natural-language proof not possible via static regex |
| Front-loaded context pointer | condition-rich frontmatter `description` | present |
| Model-invoked vs user-invoked | only one model-invoked skill; topical refs are plain files | present |
| Progressive disclosure | module router in entrypoint; only triggered references loaded | present |
| Clear steps + stopping rules | seven steps each with `Done` criterion | present |
| Co-location / single owner | each reference specializes by topic; cross-chapter file maps dependency rather than duplicating procedures | inspected |
| Avoid no-op/negative prompts | decisive positive actions and observable artifacts | inspected |
| Source traceability | whole-book chapter map + all indexed headings | present |
| Behavior test discipline | baseline/skill scenarios and pressure cases with rubric | supplied; **not run** |
| Verified completion claims | `validate_pack.py` static gate; agent behavior and production explicitly unverified | present |

## Required next validation

1. Run static validator on expanded directory and ZIP; inspect results and fix any failures.
2. Run behavior baseline and skill-enabled agent scenarios in fresh contexts with several repetitions and intended models; capture actual output and failure rationalizations.
3. Perform real application's integration, load, fault-injection and restore tests. Claims should identify exactly which were executed.

This report intentionally distinguishes *full-source processing* from *independent agent behavior verification* and *production certification*.


## Cross-agent distribution — 2026-10-26

- Moved the canonical skill to `skills/designing-data-intensive-systems/` for the Skills CLI and the default Hermes GitHub tap format; kept all original cross-chapter content and relative reference paths.
- Documented Claude Code, Codex and Hermes Agent discovery, native Hermes GitHub installation, and NPX/NPM commands in `COMPATIBILITY.md`.
- Added offline directory-copy tests and an npm-dependent GitHub Actions installation smoke test. Neither qualifies as a live model-behavior evaluation.
