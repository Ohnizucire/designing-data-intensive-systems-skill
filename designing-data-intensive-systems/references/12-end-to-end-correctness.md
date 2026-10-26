# End-to-End Integrity of Multi-System Dataflows

**Trigger:** combining multiple stores, projections, event-based applications, rebuilding data, deduplication, constraints, audit or data reconciliation. **Book:** chapter 13, integrated with chapters 1, 8, 10 and 12.

## Decide

1. Build a dependency graph: **authoritative facts → deterministic transformations → derived state → clients**. For every arrow record an event identity/version, replay order domain, ownership, freshness, rebuild and drift-detection path.
2. Separate integrity from timeliness. A search index can be a correct but delayed projection; money transfers and competing uniqueness decisions may require immediate coordinated enforcement. Expose pending/confirmed states wherever the application permits eventual decisions.
3. Make *logical operations* uniquely identifiable end to end. A message broker's offset, transaction guarantee or dedup window does not guarantee a payment, email, upload or remote API call happened once across all services.
4. Co-locate critical constraints or use an appropriate consensus/transaction boundary. For coordination-avoiding designs, show mathematically/domain-wise why concurrent independent updates cannot violate the invariant; do not assume eventual consistency makes a broken invariant repairable.
5. Maintain projections as reproducible derivations. Define how to reconstruct after corruption, migration, new feature deployment or lost derived state. Replaying with changed transformation code may intentionally yield different outputs; version transformation and compare results.
6. Verify integrity beyond component-level success: checksums for transport/storage, counts/reconciliation totals for domain state, invariant scans, audit provenance and independent periodic recomputation. An audit log is useful only if its trust and tampering assumptions are explicit.
7. Include read-side and clients in the chain: stale or out-of-order user-visible state, offline updates and cross-channel dependencies can invalidate the *user-visible* promise even when the database is healthy.

## Tests and proof

- Rebuild projection from canonical data, compare with live result and identify any unexplained drift.
- Duplicate a request across client, service, broker and consumer; one logical authoritative effect survives.
- Simulate storage/software corruption that lower-level checks miss; reconciliation detects it.
- Verify business invariant under asynchronous/reordered propagation; if validation is delayed, the UI declares it provisional.

**Stop when:** every derived view can be justified from authoritative inputs, end-to-end dedup/integrity is checked, and recovery/correction is reproducible.
