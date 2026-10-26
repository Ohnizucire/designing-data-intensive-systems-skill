# Cross-Chapter Dependencies — Think About the Whole System

Read when a design spans two stores, two consistency domains, or two topics in the router. **Use this table to load the corresponding reference files**; it is a dependency map, not a replacement for their procedures.

| Architectural decision | Coupled obligations | Source reasoning |
|---|---|---|
| Cache, index, search or ML feature set | Name authoritative source; update or CDC path; projection lag; rebuild; deletion propagation | ch1 systems of record → ch4 indexes → ch12 CDC → ch13 derivation → ch14 data rights |
| Normalize versus duplicate facts | Model update anomalies; optimize read paths; track freshness/drift; confirm source | ch3 normalization → ch4 index/view → ch8 transactions → ch13 correctness |
| Replicated read after a write | Specify read-your-writes and monotonic reads; never check critical global constraints via stale copies | ch6 lag → ch8 invariants → ch10 linearizability → ch13 user-visible correctness |
| Offline or multi-leader editing | Domain conflict semantics, causal metadata, durable sync, schema upgrades, per-user deletion | ch5 evolution → ch6 CRDT/sync → ch9 clocks → ch14 privacy |
| Adding shard or global secondary index | Index routing, skew, consistency, cross-shard transaction/coordination and migration | ch4 index → ch7 sharding → ch8 atomicity → ch10 consensus |
| Exactly-once business effect | Stable logical request IDs, database-owned idempotency, retry ambiguity, broker acknowledgment | ch5 RPC → ch8 transaction → ch9 unknown outcome → ch12 brokers → ch13 end-to-end |
| Multi-step workflow across services | Separate local atomic transactions from eventual compensations; durable task state; external effects | ch5 durable workflows → ch8 2PC → ch9 failure → ch13 integrity |
| Rebalancing or leader election | Preserved commit acknowledgement, stale worker fencing, quorum constraints and outage policy | ch6 failover → ch7 routing → ch9 leases → ch10 consensus |
| Batch backfill into a live projection | Snapshot boundary, stream catch-up, versioned transformation, atomic publication | ch11 batch → ch12 CDC → ch13 derived view |
| Stream event-time analytics | Event time and watermark policy, unreliable clocks, corrections, replay semantics | ch9 clocks → ch12 windows/joins → ch13 corrections |
| Cloud native disaggregated data | Remote I/O latency/cost, partial failure, durability promises, recovery and provider lock-in | ch1 cloud architecture → ch2 SLO → ch8 durability → ch9 network |
| Global search + personalization | Index/embedding versions, ranking quality, click-feedback and consent, ability to revoke derived personal data | ch4 retrieval → ch12 projections → ch14 feedback and rights |
| Privacy request and immutable event history | Historical event retention, model/index replicas, key destruction vs audit requirements, rebuilt derived state | ch12 event log → ch13 provenance → ch14 rights |
| Reliability claim from a system component | End-to-end observability, recovery tests, invariant audits, not merely provider uptime | ch2 reliability → ch9 fault model → ch13 trust-but-verify |
| Capacity growth and technology selection | Workload percentiles/overload and cost first; single-node baseline; specialized services only with evidence | ch1 trade-offs → ch2 requirements → ch4 storage → ch7 sharding |

**Completion:** every applicable dependency was considered and its invariant or limitation appears in the decision, not only as an architectural diagram label.
