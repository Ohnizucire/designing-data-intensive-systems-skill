# Batch Data Pipelines and Derived Datasets

**Trigger:** ETL/ELT, bulk backfill, analytical query, offline reports, model preparation or periodic data transformation. **Book:** chapter 11.

## Decide

1. Define immutable or versioned input snapshot, schema, output contracts, file/object paths, provenance, success markers and rerun rules. Batch means processing a bounded dataset, not necessarily a heavyweight cluster.
2. Start with the smallest reproducible tool: streaming Unix pipeline, local script/SQL or embedded analytical engine. Use distributed execution only where input size, compute demand, parallelism or scheduling genuinely require it.
3. Understand working-set behavior: streaming/sorting versus in-memory hash aggregation; distributed shuffle, joins and grouping move large amounts of data and can dominate costs.
4. If using object storage or a distributed filesystem, reason about object semantics, failure domains, task retries, reprocessing, checkpoint placement, partition sizing, skew and worker scheduling. Treat partial output as uncommitted until publication/cutover is safe.
5. Use columnar data and execution where analytical read patterns benefit. Maintain separation from latency-sensitive operational workloads if necessary.
6. Serving a batch-created search index, report or ML feature set requires a projection owner, freshness target, version/cutover, rebuild and rollback path. Ensure training/serving feature definitions are compatible.

## Tests and proof

- Rerun same versioned input and compare output equivalence/identity (or bounded nondeterminism clearly defined).
- Crash workers after partial writes; retry produces no duplicate published artifacts or missing partitions.
- Exercise skewed join/group keys and failure near job completion; observe memory, spill and cost.
- Backfill a historical dataset while normal writes continue; verify snapshot boundary and catch-up policy.

**Stop when:** input provenance, output publication, restartability, resource plan and validation checks are evidenced.
