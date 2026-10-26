# Consistency Models, Logical Ordering and Consensus

**Trigger:** global uniqueness, linearizable read/write, leader election, shared logs, distributed coordination or real-time ordering. **Book:** chapter 10.

## Decide

1. State the required consistency precisely. **Serializability** says transactions behave like some serial order; **linearizability** says operations appear atomic and respect real-time order. They solve different questions; **strict serializability** combines both.
2. Identify dependencies from another channel (e.g., users see a write confirmation via message and then immediately query elsewhere); this may require stronger read semantics than a system's ordinary eventual convergence.
3. Determine which operations truly require coordination: unique assignment across competing nodes, single active leader, linearizable compare-and-set, or atomic commitment. Prefer per-key/per-shard coordination to a global serialized bottleneck when domain permits.
4. Choose logical clock primitives deliberately: Lamport timestamps capture ordering consistent with causality but cannot determine concurrency; hybrid logical clocks blend physical time with logical ordering; version vectors express causal/concurrent relations at higher metadata cost. None automatically makes a distributed ID generator linearizable.
5. For consensus-ordered logs, reason about majorities, leader election, confirmed entry preservation, quorum intersection, reconfiguration and the availability impact of a partition. Reuse vetted databases or coordination services rather than writing consensus from scratch.
6. Resist 'CAP pick two' shorthand: partitions can happen; choose precisely what operations must remain safe or available under them. Address network-delay costs even without an explicit partition.

## Tests and proof

- Race two requests for one username/resource and show at most one successful reservation at the defined authority.
- Force a leader change after an acknowledged log entry and verify no elected leader forgets it.
- Partition replicas and demonstrate explicitly which reads/writes fail, block, proceed or may be stale.
- Verify causality-sensitive requests across alternate channels and clients.

**Stop when:** the required consistency property and coordination scope are named; failure-time safety/liveness and latency trade-offs have concrete tests.
