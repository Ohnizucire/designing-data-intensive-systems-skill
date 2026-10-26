# Transactions, Isolation and Atomic Commitment

**Trigger:** race conditions, multi-record invariants, uniqueness, balance, reservation or transactions spanning services/shards. **Book:** chapter 8, with end-to-end effects from chapter 13.

## Decide

1. Specify invariants as assertions over state and possible concurrent transitions. Separate ACID **consistency** (application invariants) from replica freshness; durability is a claim with concrete storage/failure scope, not a synonym for 'uses SQL'.
2. Recognize anomalies: dirty read/write, nonrepeatable read, lost update, read skew, write skew and phantom. Read committed prevents some but not all anomalies; snapshot isolation often prevents read skew yet permits write skew. Database-specific isolation names are unreliable shortcuts.
3. Prefer the least complex sufficient enforcement **at the authority**: unique/check constraint; atomic UPDATE/CAS; row/range lock; serializable transaction/SSI; explicit materialized conflicts if necessary. Test absence-of-row predicates: `SELECT FOR UPDATE` cannot lock a row that does not exist.
4. Keep strongly coupled invariants in one transactional owner when practical. Retry a **whole aborted transaction**, not blindly a half-committed sequence. Pair external actions with stable logical request IDs and documented idempotent outcomes.
5. If atomic commit spans shards/systems, assess 2PC coordinator/prepare log, locks held during uncertainty, failure recovery and operational cost. **Two-phase locking (2PL)** controls concurrency; **two-phase commit (2PC)** controls atomic distributed decisions—they are different.
6. Prefer local atomic commit plus durable outbox/CDC/idempotent consumer where it meets the requirement. Workflow compensation is a different business guarantee from atomic rollback; explain the visible intermediate states.
7. For broker + database consumption, atomically record processed message identity with the resulting authoritative writes; acknowledge after commit. Scope dedup retention to redelivery horizon and external effects; 'exactly once' needs an end-to-end definition.

## Tests and proof

- Simulate two independent writers observing a shared precondition (booking, last doctor on call, balance): invariant must survive all interleavings.
- Lose commit acknowledgment; retry using same operation ID returns one logical effect.
- Crash between prepare/commit, database write/message publish and broker acknowledgment; test recovery or explicit compensation.
- Verify actual isolation and constraint guarantees against the selected engine/version, not a generic ACID label.

**Stop when:** every invariant has an enforcement boundary and a red/green concurrency or crash probe; distributed uncertainty and recovery states are documented.
