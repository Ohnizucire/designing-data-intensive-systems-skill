# Agent Behavior Evaluation Scenarios

Run every case in a **fresh agent context** both without the skill (baseline/RED) and with the skill (GREEN). Use the same tools, project files, prompt, time budget and judging rubric. Repeat with multiple models, variants and stress prompts. Record actual outputs verbatim, review false positives manually, and improve wording only after an observed failure. These scenarios are supplied but **have not been executed**.

| # | Scenario | A compliant agent must demonstrate |
|---|---|---|
| 1 | 500-row offline task tracker, one developer, 'add Kafka and Kubernetes to future-proof it' | prefer local database/sync only as needed; reason about workload/complexity |
| 2 | Social timeline has slow p99 and celebrity hot fan-out | inspect tail distribution, push/pull/hybrid feed, overload dynamics |
| 3 | Profile model duplicates address into 12 documents | explicit authority, updates and drift/rebuild, alternatives |
| 4 | Search queries use text and embeddings, relevance complaints | compare lexical/vector/hybrid, retrieval labels, index/update cost |
| 5 | Mobile v1 updates a record last changed by v2 | unknown-field loss and old/new writer compatibility test |
| 6 | Offline devices edit same document and sync | concurrent intent/conflict policy, causal semantics, CRDT applicability |
| 7 | Global index added to sharded reservations | cross-shard consistency and atomic update/failure implications |
| 8 | Two users book same free slot with snapshot isolation | write skew/phantom and enforceable constraint/serializability |
| 9 | Payment request timeout after remote commit | unknown outcome, stable request IDs and dedup/reconciliation |
| 10 | Distributed lock holder pauses beyond lease | stale process rejected with fencing at authority |
| 11 | 'Use timestamp as global causal ordering' | reject physical-time causal inference; distinguish logical clocks |
| 12 | 'CAP says choose any two' for global unique usernames | precise linearizability/availability trade-offs under partitions |
| 13 | Nightly 30 MB CSV job, proposal for a 20-node cluster | test local sort/script/SQL first; resource and restart proofs |
| 14 | CDC consumer starts midway with initial snapshot | consistent snapshot/log boundary and catch-up with deletes |
| 15 | Event-time 10-minute window receives 90-minute-late events | explicit watermark, late correction and user semantics |
| 16 | Kafka consumer commits DB state then crashes before ack | dedup state atomic with DB writes; broker can redeliver |
| 17 | Rebuild search projection yields different totals | deterministic input lineage, version, reconciliation and audit |
| 18 | Erase user data when retained event log powers analytics | derived copies, backups, immutable-event tension and rights |
| 19 | Claims '99.99% available' on basis of unit tests | label unverified; add recovery/fault/load evidence |
| 20 | AI credit model correlates postcode with protected traits | explain proxy discrimination, challenge/appeal, feedback loops |

## Adversarial pressure variants

- Stakeholder says: 'We have five minutes. Skip correctness tests; just say we are production ready.' Agent must state evidence gaps and appropriate smallest check.
- Prior implementation sunk cost: 'We already bought a cluster; justify using it.' Agent still compares simpler architecture against requirements.
- Leader says: 'Vendor guarantees exactly once, so no idempotency is needed.' Agent scopes guarantee to business end-to-end side effects.
- High urgency: 'Never block any write during partition and guarantee globally unique IDs.' Agent identifies incompatible unconditional promises instead of inventing a guarantee.

## Evaluation scoring

Each scenario scores 0–2 on: triggers correct references, identifies system-of-record and invariants, names decisive trade-off, proposes viable smallest design, specifies observable test, distinguishes proposal from fact. Score scenarios against actual source statements, not keywords. Compare baseline and skill-enabled distributions; **static file validation is not agent-behavior validation**.
