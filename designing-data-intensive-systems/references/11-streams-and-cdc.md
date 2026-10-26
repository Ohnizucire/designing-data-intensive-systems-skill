# Streams, Messaging, Change Data Capture and Event Time

**Trigger:** events, queues, broker offsets, CDC, stream joins/windows, replay, realtime projections and change propagation. **Book:** chapter 12.

## Decide

1. Separate **work queues** (dispatch + acknowledgment) from **partitioned append-only logs** (durable ordered history + replay), synchronous RPC, and raw event feeds. Specify delivery as at-most-once, at-least-once or a constrained exactly-once mechanism with its actual side-effect boundary.
2. Identify event producer, immutable identity, key/partition, ordering domain, retention, schema/version, consumer group and permitted lag. Order within a shard is not global total order.
3. For database-originated changes choose transactional outbox/CDC when transaction-to-publication gap matters. Distinguish CDC physical row changes from business-level domain events/event sourcing; document the coupling impact of exposing internal schemas.
4. To bootstrap a derived index, snapshot source state and establish a continuous log position/boundary; merge snapshot and streaming updates without missing/duplicating facts. Plan log compaction, delete tombstones, retention and resnapshot.
5. Treat consumers as crashable. Acknowledge after durable effects, store dedup identity transactionally where needed, make external effects idempotent/reconcilable; bound retries, poison-message behavior, backlog and backpressure.
6. For time-sensitive computations specify **event time** versus processing time, window choice, watermark/late-event tolerance, correction/retractions and clock quality. For stream–table joins state whether 'as of event time' or 'latest' table version applies.
7. Assess checkpoint/replay and application upgrade compatibility: state serialization, offset commits, resharding and what reconstructing old output means after code/schema changes.

## Tests and proof

- Kill consumer after effect but before acknowledgment; redelivery does not duplicate business action.
- Restore initial snapshot then replay overlapping changes, including deletes, schema evolution and out-of-order events.
- Inject late events across a window boundary, and stream–table changes between event and processing time.
- Hold consumer offline until backlog reaches configured limits; measure recovery and data loss/rejection semantics.

**Stop when:** producer contract, delivery/order scope, snapshot/replay boundary, lag and correction policy, and crash probe are explicit.
