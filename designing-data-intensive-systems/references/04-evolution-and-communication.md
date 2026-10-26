# Encoding, Compatibility and Service Communication

**Trigger:** evolving persisted data, wire formats, APIs, messages, workflow states, or concurrent client/server versions. **Book:** chapter 5.

## Decide

1. Enumerate all writers and readers: deployed servers, mobile/offline clients, persisted historical values, RPC peers, event consumers, backups, workflow workers. A database is a message to a *future version of the application*.
2. State backward versus forward compatibility from writer and reader viewpoints; test a matrix of old/new readers and writers. Identify field defaulting, removal, type change, unknown-field preservation and data loss from read-modify-write by outdated clients.
3. Pick encodings for the contract: JSON/XML textual interoperability; schema-defined Protobuf/Avro when size, throughput, discipline or compatibility justify them. Account for numeric precision, binary payloads, schema identity, field IDs and reserved fields. Verify actual format rules rather than assuming any format guarantees evolvability.
4. For rollout use additive/expand → compatible readers/writers → backfill → switch read/write path → contract, with rollback and mixed-version checks at each step. This is an engineering adaptation, not a book-prescribed deployment recipe.
5. Distinguish local procedure calls from network RPC: remote calls are slow, can timeout after success and can return errors, or duplicate work on retry. Design protocol semantics rather than treating an RPC call as a local function invocation.
6. Decide whether synchronous RPC, asynchronous messaging or durable workflows match each task's latency, coupling, retry and state requirements. For workflows, record task identity, durable execution state, idempotent activities, cancellation and compensation; workflows alone do not make arbitrary side effects atomic.

## Tests and proof

- Decode old persisted records with new code and new records with supported old code; round-trip unknown fields if the system promises preservation.
- Old client updates new-format records without destroying fields it does not know.
- Simulate client/server deploy skew, queued older events, duplicate RPCs and abandoned/resumed workflow tasks.

**Stop when:** every live and retained dataflow has a compatibility matrix, explicit failure/retry semantics and a reversible migration plan or justified irreversible boundary.
