---
name: designing-data-intensive-systems
description: Use when designing, building, debugging or reviewing persistent data flows, database queries and indexes, schema changes, concurrent state changes, remote or offline sync, distribution, data pipelines, or recovery and reliability requirements in any application.
---

# Designing Data-Intensive Systems

**Core idea:** Design around observable requirements, authoritative state and end-to-end invariants. Every extra component introduces a new failure and evolution boundary. Use only the branches a change actually reaches.

This is an original agent decision guide grounded in *Designing Data-Intensive Applications*, second edition, by Martin Kleppmann and Chris Riccomini. It translates the **interacting arguments across all 14 chapters** into procedures, not cookbook technology mandates. The source [chapter map](provenance/whole-book-map.md) and [cross-chapter dependencies](references/cross-chapter-dependencies.md) clarify the underlying reasoning. No book text is bundled.

## Procedure

1. **Trace the change.** Inspect existing code, queries, schemas, clients, jobs, integrations, runtime constraints and tests; for greenfield work, inspect the specification. Draw the affected read/write/derive paths. **Done:** each affected path has a producer, consumer and an identified source of truth or documented uncertainty.
2. **Define correctness.** Write user-visible invariants, concurrency assumptions, the cost of stale or missing data, and the acceptable failure response. Distinguish safety (bad things never happen) from liveness (good things eventually happen). **Done:** every critical write has an enforcing boundary and an executable or planned failure probe.
3. **Quantify the workload.** Record access patterns, realistic data distribution, p95/p99 response targets when appropriate, resource and money budgets, RPO/RTO, data lifecycle, and coexistence of old/new clients. Mark unavailable numbers `unknown / measure`; don't invent benchmarks. **Done:** all architecture-changing constraints are evidenced, assumed, or assigned a measurement.
4. **Load triggered references.** Match every relevant branch below, including implications across branches. Read [cross-chapter dependencies](references/cross-chapter-dependencies.md) when any change spans two data systems or more than one branch. **Done:** every affected boundary has a decision, or a concrete remaining question.
5. **Choose proportionately.** Compare the smallest sufficient candidate against additional complexity with its latency, operability, consistency, cost, recovery and migration consequences. For substantive decisions, fill [decision record](references/decision-record.md). **Done:** a choice is justified, rejected options have reasons, and redesign triggers are measurable.
6. **Verify actual behavior.** Follow the repository's development/testing conventions. Test the invariant at its owner, then its end-to-end behavior across retries, concurrency, version mixtures, partial failure and recovery, as applicable. **Done:** executed commands/results are separated from planned or provider-claimed guarantees.
7. **Report.** State decision, invariant, observed evidence, untested failure cases, recovery/rollback and revisit conditions. **Done:** a maintainer can tell `verified`, `documented`, `proposed` and `unknown` conclusions apart.

## Branch pointers — load on demand

| Observable change / concern | Required reference | Book chapters |
|---|---|---|
| SLO, overload, cost, deployment topology, complexity | [Workload and trade-offs](references/01-workload-and-tradeoffs.md) | 1–2 |
| Entity relations, denormalization, graph, event model, analytics schema | [Data modeling](references/02-data-modeling.md) | 3 |
| Index selection, query plan, storage, text/vector search, OLAP | [Storage and retrieval](references/03-storage-and-retrieval.md) | 4 |
| Data encoding, old clients, migration, APIs, RPC, workflows | [Evolution and communication](references/04-evolution-and-communication.md) | 5 |
| Replication lag, leader failover, offline sync, concurrent replicas | [Replication and local-first](references/05-replication-and-local-first.md) | 6 |
| Shards, tenants, skew, hot keys, routing, global indexes | [Sharding and tenancy](references/06-sharding-and-tenancy.md) | 7 |
| Race, transaction, isolation, write skew, distributed commit | [Transactions and isolation](references/07-transactions-and-isolation.md) | 8 |
| Network timeout, uncertain result, clock, lock lease, crash, testing failures | [Partial failure and system models](references/08-partial-failure-and-models.md) | 9 |
| Linearizable reads, uniqueness, order, leader election, consensus | [Consistency and consensus](references/09-consistency-and-consensus.md) | 10 |
| File pipeline, ETL, backfill, SQL analytics, batch, large data | [Batch processing](references/10-batch-processing.md) | 11 |
| Queue, CDC, replay, event time, lag, stream join, projection | [Streams and CDC](references/11-streams-and-cdc.md) | 12 |
| Multiple stores, derived state, deduplication, integrity, audit | [End-to-end dataflow correctness](references/12-end-to-end-correctness.md) | 13 |
| Personal data, tracking, predictions, fairness, deletion, governance | [Ethics and data rights](references/13-ethics-and-data-rights.md) | 14 |

**Output size:** A local CRUD change may need only decision / invariant / evidence / risk. A multi-boundary change requires a complete decision record. The references contain the checks; repeat only relevant results. **Implementation skill precedence:** use applicable test-driven development, debugging and code-review workflows already available to the agent; this skill defines the *data correctness decision*, not a second coding workflow.
