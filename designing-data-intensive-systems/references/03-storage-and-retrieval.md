# Storage Engines, Retrieval and Search

**Trigger:** tuning reads/writes or choosing an index, storage engine, analytics layout or retrieval technology. **Book:** chapter 4.

## Decide

1. Trace the actual query shape (point, range, sort, join, aggregation, full-text, nearest-neighbor), predicates, cardinalities and data distribution. Start with query plans and instrumentation before adding a database.
2. Compare B-tree and log-structured/LSM designs on measured read/write mix, range scans, write amplification, compaction cost, temporary space, SSD behavior and p99 latency. Storage-engine trade-offs depend on implementation and workload; benchmark using representative data and bursts.
3. Derive secondary indexes from WHERE/JOIN/ORDER BY access patterns. For composite indexes consider leading-column order and selectivity; for covering/clustered indexes assess read locality, write amplification and storage budget. Explain how index changes will be deployed and backfilled.
4. For high-volume analytics, consider column layout, compression, vectorized operators and preaggregations/materialized views when scanning few columns from many rows. Materialized results are derived state with freshness and rebuild obligations.
5. For keyword search, model tokenization, analyzers, language, ranking and an inverted index. For semantic retrieval, model embedding quality, approximate-nearest-neighbor recall, embedding version and hybrid lexical/vector needs. Index recall is not answer correctness; evaluate on labeled domain queries.
6. Storage locality is a deployment concern too: cloud compute/storage disaggregation changes network transfer costs and failure paths. Embedded/single-node engines may be preferable at modest scale.

## Tests and proof

- Record explain plans, cardinality estimates, p95/p99 latency, write amplification when measurable and index storage cost before and after changes.
- Exercise compaction/background maintenance and queries concurrently, rather than benchmarking warm reads alone.
- Verify index backfill, incremental updates, delete propagation and complete reindexing after loss.
- For search, use relevant/irrelevant test sets and report recall/precision or ranking metrics appropriate to the application.

**Stop when:** each index/layout decision responds to an observed access path, has a cost and passes representative query and recovery probes.
