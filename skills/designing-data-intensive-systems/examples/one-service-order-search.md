# Example — A Modest Order Application With Search

**Goal:** Build orders, payments and search without unnecessary distributed infrastructure.

**Assumptions (not benchmarks):** one team, manageable data on one primary SQL node, noncritical product-search freshness, no global write-region requirement. If assumptions change, reconsider.

- **Authority:** relational database for orders, inventory reservations and payment-attempt IDs. Domain invariants: no oversell, one charge intent per logical checkout, stable order states.
- **Transactions:** atomic decrement/conditional inventory update and order state in one database transaction; unique `checkout_request_id` to suppress duplicate effects. An external payment service requires idempotency key and reconciliation, not a claim of global atomicity.
- **Read model:** initially SQL indexes/full-text if adequate. Only if observed search needs outgrow it: create derived external search index with outbox/CDC, replay and rebuild; tolerate explicitly stated search lag.
- **Reliability:** bounded webhook retries, crash-between-commit-and-event test, backup restore drill, p99 under burst and a slow payment provider.
- **Evolution:** support old/new mobile clients and event schema during rolling deployment.
- **Data rights:** propagate correction and deletion to index/history where relevant; payment retention and regulatory duties reviewed separately.

**Escalate when:** measured index latency, data volume, write contention, fault isolation or product requirements exceed the single-node baseline. Not because microservices/streaming are fashionable.

**End-to-end probes:** two simultaneous checkouts for final item; payment succeeds then response lost; webhook delivered repeatedly; rebuild search index after removal; old client updates new order; restore primary after crash. All probes must preserve user-visible invariants.
