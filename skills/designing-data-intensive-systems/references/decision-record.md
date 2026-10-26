# Data-System Decision Record (Agent Output Contract)

This **operational template is authored for agents**, not a quoted standard from DDIA. Compress fields for trivial work; fill explicitly for consequential changes.

1. **Problem and evidence:** actor/user goal; changed paths; existing environment; observed facts vs assumptions; real workload, data shape and failure history.
2. **Authoritative data graph:** systems of record, derived copies, lifecycle, dataflow, version boundaries, ownership and model/query requirements.
3. **Invariants and contracts:** atomic owner, expected consistency/freshness, ordering scope, idempotent logical operation IDs, old/new compatibility, user-facing effects.
4. **Nonfunctional limits:** end-to-end p95/p99, throughput, skew, load shape, budgets, RTO/RPO, privacy rights; unknown metrics marked with a measurement method.
5. **Options:** smallest viable architecture; targeted optimization; more distributed/complex option only if justified. Compare correctness, failure behavior, operational maintenance, cost, migration and reversibility.
6. **Decision:** selected candidate, rejected alternatives with reasons, trade-offs accepted, escalation conditions that can be measured.
7. **Failure model:** timeout-after-commit, crash/restart, duplicate/reorder, stale replicas, hot shards, schema skew, data corruption, regional loss where relevant.
8. **Verification matrix:** test case, precondition, expected invariant, command/tool and *observed* result (or `not run`). Require production-like data for load claims.
9. **Release and ownership:** rollout/backfill/cutover/rollback/recovery, monitoring, reconciliations, human decision ownership, open risks.

**Evidence labels:** `verified` (recent execution and output), `documented` (specific engine/version guarantee with citation), `proposed` (unimplemented or untested), `unknown` (needs proof). A successful unit test does not imply production reliability.
