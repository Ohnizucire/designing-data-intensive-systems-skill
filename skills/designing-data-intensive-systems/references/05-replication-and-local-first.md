# Replication, Freshness, Offline Sync and Conflict Resolution

**Trigger:** replicated databases, follower reads, high availability, multi-region, leaderless writes or locally editable offline data. **Book:** chapter 6.

## Decide

1. Separate **backup** (historical recovery) from **replication** (copies for availability/load). Select synchronous/asynchronous leader-based, multi-leader or leaderless behavior by durability, write availability, latency and conflict costs.
2. For asynchronous replicas specify read-your-writes, monotonic reads and consistent-prefix expectations; define routing/session stickiness/version tokens if freshness matters. A replicated copy can be healthy but stale.
3. Plan follower creation (snapshot plus log catch-up), bounded lag, leader failure/failover, old-leader fencing and split-brain prevention; test the interval in which acknowledgments and durable replication disagree.
4. For multi-writer/offline-first clients define conflict classes per field/entity, not one global 'merge'. Consider domain operations, conflict avoidance, user intervention, CRDTs or operational transformation only where their mathematical assumptions match required semantics. Last-write-wins can silently discard valid concurrent changes.
5. Determine whether two writes are ordered by *happens-before* or concurrent; physical timestamps cannot establish causality reliably. Version vectors express partial order but carry metadata and merging costs.
6. For leaderless quorum designs, model read/write quorums, replication lag, read repair/anti-entropy and concurrent siblings. A quorum calculation alone is not a universal guarantee of linearizability.

## Tests and proof

- Write and immediately read from different replicas/sessions; match promised staleness contract.
- Kill leader while a write is in-flight; show which acknowledged writes survive, how clients retry and how a stale old leader is rejected.
- Make simultaneous offline edits and reconnect in differing orders; preserve domain invariants, visible intent and deterministic conflict policy.
- Restore from a backup that predates replication and verify derived/index rebuilding.

**Stop when:** every replica mode names its user-visible guarantee, conflict policy, durability/failover behavior and reconciliation evidence.
