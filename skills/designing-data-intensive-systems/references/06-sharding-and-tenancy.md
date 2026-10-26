# Sharding, Skew and Tenant Isolation

**Trigger:** distributing keys/records, hot tenants, horizontal partitioning, global indexes, rebalancing or cross-shard queries. **Book:** chapter 7.

## Decide

1. Prove which single-node capacity limit is exceeded. Distinguish read scaling by replicas from shard-driven write capacity or data-size scaling; shard only when a meaningful objective requires it.
2. Choose a partition key by *workload skew and query locality*, not merely key uniqueness. Compare ordered ranges (good ranges, risk hot append), hashing (distributes keys, limits range locality) and mixed strategies. Evenly distributed key counts can conceal hot tenants and hot keys.
3. Record tenant isolation requirements: logical versus physical separation, cost attribution, noisy neighbors, data residency, migrations and tenant-specific retention.
4. Model rebalancing mechanics and routing indirection. Key modulo live-node-count causes disproportionate remapping; fixed shard pools, consistent hashing or adaptable ranges have different operational limits.
5. Decide secondary index scope: shard-local reads may require scatter/gather; global indexes introduce independent sharding, update consistency and cross-shard writes. Trace query fan-out, latency and correctness implications.
6. For transactions spanning shards, route to [transactions](07-transactions-and-isolation.md) and [consensus](09-consistency-and-consensus.md). Don't assume an app-level 'check then write' remains atomic after sharding.

## Tests and proof

- Measure top-key/tenant load, p99 fan-out latency and rebalancing write availability under a realistic skewed distribution.
- Move a shard during concurrent writes and reads; no authoritative gaps, duplicates or stale routing beyond contract.
- Update a record and global secondary index across failure boundaries; document atomic or eventually consistent semantics.

**Stop when:** partition key, data movement, routing, skew mitigation, tenant isolation and cross-shard correctness are all justified and tested or explicitly unverified.
