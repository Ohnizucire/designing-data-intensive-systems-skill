# Whole-Book Conceptual Traceability

**Source:** Martin Kleppmann and Chris Riccomini, *Designing Data-Intensive Applications*, 2nd edition; uploaded EPUB, O’Reilly Media, 2026; ISBN 9781449373320.

**Reading scope:** This project extracted the full prose of all 14 chapter files (including headings, examples, and section bodies) and used chapter-level and section-level passes to develop the agent guidance; the section coverage index separately enumerates all substantive headings. Bibliographies are excluded from operational synthesis. These notes are an **original interpretation**, not book prose or a claim that the authors endorse a mandatory checklist. The book itself is not redistributed.

| Ch. | Title | Primary branch |
|---|---|---|
| 1 | Trade-Offs in Data Systems Architecture | [`01-workload-and-tradeoffs`](../references/01-workload-and-tradeoffs.md) |
| 2 | Defining Nonfunctional Requirements | [`01-workload-and-tradeoffs`](../references/01-workload-and-tradeoffs.md) |
| 3 | Data Models and Query Languages | [`02-data-modeling`](../references/02-data-modeling.md) |
| 4 | Storage and Retrieval | [`03-storage-and-retrieval`](../references/03-storage-and-retrieval.md) |
| 5 | Encoding and Evolution | [`04-evolution-and-communication`](../references/04-evolution-and-communication.md) |
| 6 | Replication | [`05-replication-and-local-first`](../references/05-replication-and-local-first.md) |
| 7 | Sharding | [`06-sharding-and-tenancy`](../references/06-sharding-and-tenancy.md) |
| 8 | Transactions | [`07-transactions-and-isolation`](../references/07-transactions-and-isolation.md) |
| 9 | The Trouble with Distributed Systems | [`08-partial-failure-and-models`](../references/08-partial-failure-and-models.md) |
| 10 | Consistency and Consensus | [`09-consistency-and-consensus`](../references/09-consistency-and-consensus.md) |
| 11 | Batch Processing | [`10-batch-processing`](../references/10-batch-processing.md) |
| 12 | Stream Processing | [`11-streams-and-cdc`](../references/11-streams-and-cdc.md) |
| 13 | A Philosophy of Streaming Systems | [`12-end-to-end-correctness`](../references/12-end-to-end-correctness.md) |
| 14 | Doing the Right Thing | [`13-ethics-and-data-rights`](../references/13-ethics-and-data-rights.md) |

## Chapter-by-chapter arguments and implications

### Chapter 1 — Trade-Offs in Data Systems Architecture

**Central argument:** Business and user requirements shape infrastructure boundaries; operational and analytical systems optimize for different access patterns; a source of truth is a *role* in a dataflow, not a product. Cloud-native disaggregation, service separation and global distribution offer benefits only at specific costs.

**Implication for an engineering agent:** The trade-off chapter constrains the entire design: verify which replicated/derived state must be recoverable, which deployment responsibilities are outsourced, and which human/social consequences arise.

### Chapter 2 — Defining Nonfunctional Requirements

**Central argument:** The timeline fan-out example illustrates that changing query patterns changes architecture. Tail latency, queuing feedback, overload recovery, fault tolerance, scalability and maintainability are separate properties; improvements in one may harm another.

**Implication for an engineering agent:** Measure distribution, not averages alone; test the overloaded system after the spike and assess operability/evolvability alongside throughput.

### Chapter 3 — Data Models and Query Languages

**Central argument:** Relations, documents and graphs serve different relationship structures and query patterns. Normalization reduces inconsistency; denormalization changes the write obligation. Graph languages and event sourcing answer different representation problems; DataFrames/analytics represent different computations.

**Implication for an engineering agent:** A model choice must explain query semantics, update anomaly exposure and where each duplicated fact is corrected.

### Chapter 4 — Storage and Retrieval

**Central argument:** LSM and B-tree trade-offs extend beyond raw point throughput to write amplification, compaction, disk use, read predictability and workload shape. Column storage, vectorized execution and materialized views serve analytical reads; inverted and vector indexes address different retrieval semantics.

**Implication for an engineering agent:** An index is a derived structure and therefore participates in updates, rebuild, migration, deletion and correctness checks, not only query optimization.

### Chapter 5 — Encoding and Evolution

**Central argument:** Schema evolution is a producer/consumer contract across time. Different copies of data may have been written by many old versions, and stale clients can overwrite unknown new fields. REST/RPC, asynchronous events and durable workflows differ in latency, coupling and failure behavior.

**Implication for an engineering agent:** Treat the database as messaging across deployments; compatibility tests must include stored historical bytes and old offline clients.

### Chapter 6 — Replication

**Central argument:** Replication makes state available or closer but changes write acknowledgment, stale reads, leader failover and concurrent-update semantics. Local-first sync and leaderless replication require explicit merge/causality; a physical last-write timestamp may silently lose intent.

**Implication for an engineering agent:** Replica consistency is not ACID consistency. Lost acknowledgments, old-leader writes and session reads connect replication to transactions and system models.

### Chapter 7 — Sharding

**Central argument:** Sharding solves particular capacity problems while introducing routing, rebalancing, hotspots, tenant isolation and cross-shard index/transaction coordination. Key uniformity does not imply load uniformity; automatic rebalancing itself has operational costs.

**Implication for an engineering agent:** A global secondary index behaves like another distribution problem and may require extra atomicity or explicit eventual semantics.

### Chapter 8 — Transactions

**Central argument:** ACID properties do not remove the need to specify invariants. Read committed and snapshot isolation have well-known anomalies; serializable isolation, predicate/index-range locking, SSI and atomic constraints enforce different scopes. 2PC introduces uncertain coordination states.

**Implication for an engineering agent:** Focus on write skew/phantoms and duplicate side effects; end-to-end exactly-once effects are an application property, not a broker marketing setting.

### Chapter 9 — The Trouble with Distributed Systems

**Central argument:** Distributed nodes can fail independently, network delay is unbounded in common models, timeouts leave outcomes unknown, and physical clocks are not universal orderings. Paused workers and stale leases require fencing. Safety/liveness and model checking/simulation make claims testable.

**Implication for an engineering agent:** Design must account for the gap between abstract system models and the real software/hardware configuration. Fault injection should be repeatable.

### Chapter 10 — Consistency and Consensus

**Central argument:** Linearizability of operations differs from serializability of transactions. Logical clocks order events without necessarily guaranteeing real-time order. Distributed uniqueness, shared logs, leader election and atomic decisions often demand coordination/consensus, which affects availability during partitions.

**Implication for an engineering agent:** Avoid reducing CAP to an unconditional pick-two slogan; state exactly which user operations block or remain safe.

### Chapter 11 — Batch Processing

**Central argument:** Batch processors exploit bounded inputs and replayable jobs. Sorting, grouping, distributed shuffle, fault handling and job scheduling shape scalability. DataFrame/SQL engines and distributed workers are implementation options whose fit follows workload and reprocessing needs.

**Implication for an engineering agent:** Every published batch result is derived state with an input version, partial-failure policy and eventual service cutover contract.

### Chapter 12 — Stream Processing

**Central argument:** Log-based brokers, queues, CDC, event sourcing and streams are related but distinct. Exactly-once delivery claims are narrower than business effects. Snapshot plus live log catch-up, message order, event versus processing time, late data, joins and checkpoints require explicit decisions.

**Implication for an engineering agent:** Streams are the update mechanism connecting authoritative data to derived views; their evolution and replay must preserve domain semantics.

### Chapter 13 — A Philosophy of Streaming Systems

**Central argument:** Derived data integration provides composability but shifts verification onto the end-to-end dataflow. Timeliness differs from integrity; request IDs, idempotency, uniquely enforced constraints, reconciliation, provenance and audit help detect errors even when components claim reliability.

**Implication for an engineering agent:** A correct component chain can still produce incorrect business outcomes. Check invariants at the application boundary and compare recomputed projections.

### Chapter 14 — Doing the Right Thing

**Central argument:** Optimization targets and data models can harm people, particularly in predictive scoring, tracking and profiling. Consent requires meaningful choice; proxy features can encode discrimination, and feedback loops can amplify harm. Privacy is about individual agency, not simple secrecy.

**Implication for an engineering agent:** Rights to correct/export/delete interact with retained logs, model features, backups and every derived copy. Ethical evaluation is iterative and participatory, not only a checkbox.

## Cross-chapter interactions

No chapter stands on its own in a real system: data models constrain indexes; indexes are derived state; derivation creates compatibility and lag; replication creates concurrency; sharding widens coordination scope; partial failures force retries; retries interact with business invariants; observability/audit must verify integrity; privacy propagates across every retained and derived copy.

Use [cross-chapter dependencies](../references/cross-chapter-dependencies.md) as the practical routing map.

For the complete source section inventory (not just conclusions or a table of contents), see [the full section ledger](section-ledger.md).

## Limits

Product implementations, library/library-version guarantees, laws and performance numbers need current independent validation. This pack provides reasoning procedures and tests, not production certifications. Structural validations do not constitute baseline-vs-skill agent behavior tests.
