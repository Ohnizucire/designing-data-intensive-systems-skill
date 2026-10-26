# Partial Failures, Clocks, Leases and System Models

**Trigger:** networked services, timeouts, failover, distributed locks, heartbeat, reliability modeling or concurrency fault testing. **Book:** chapter 9.

## Decide

1. Enumerate failures: delayed/dropped/duplicated messages, asymmetric partition, crash/restart, paused process, overloaded network, storage faults and clock error. A timeout creates an **unknown outcome**, not proof that a command did not execute.
2. Bound remote calls: deadlines, retry budget, exponential backoff/jitter, admission and circuit breaking. Put idempotency or reconciliation before automatic retries of mutating operations.
3. Use **monotonic** clocks to measure durations/deadlines; wall clocks to express calendar time, acknowledging jumps, drift and synchronization uncertainty. Order distributed events with causal metadata or consensus rather than naive timestamp comparisons.
4. Specify *safety* and *liveness* separately under each fault assumption. Define whether the model is crash-stop/crash-recovery, partially synchronous, asynchronous or Byzantine; guard against malformed data without adopting heavyweight Byzantine consensus by default.
5. Treat a distributed lease/lock holder as potentially stale after a pause. Use monotonically increasing **fencing tokens checked at the protected resource**, or a strong conditional update at the authority. Lease expiry alone cannot revoke a delayed operation.
6. Validate exceptional interleavings by property-based concurrency tests, fault injection, deterministic simulation or model checking (TLA+/related) proportional to risk. Deterministic tests make rare schedules reproducible but do not themselves prove an unmodeled implementation correct.

## Tests and proof

- Remote operation commits, then response disappears; client sees unknown status and reconciles without duplication.
- Old leader resumes after lease expiry and attempts a delayed write; authority rejects stale fencing token.
- Partition the network asymmetrically, suspend worker, skew clocks and test bounded queue/retry behavior.
- State which failure classes cannot be tested and what assumptions the design relies upon.

**Stop when:** every relevant partial-failure state has defined client behavior, safety condition, recovery path and a test or named evidence gap.
