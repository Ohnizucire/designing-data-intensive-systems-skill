# Full Chapter Section Ledger

Generated from the **main text** of all 14 chapter XHTML files in the user-provided EPUB. Each entry is a substantive section heading; figure captions, notes and bibliography references are excluded. This ledger verifies which sections are represented by the chapter-to-reference coverage map; it does **not** constitute a claim of independently validated implementation behavior.

| Chapter | Sections | Main-text words (approx.) | Module |
|---|---:|---:|---|
| 1 | 20 | 10,708 | `01-workload-and-tradeoffs` |
| 2 | 27 | 9,697 | `01-workload-and-tradeoffs` |
| 3 | 29 | 16,192 | `02-data-modeling` |
| 4 | 32 | 14,308 | `03-storage-and-retrieval` |
| 5 | 30 | 11,749 | `04-evolution-and-communication` |
| 6 | 48 | 18,548 | `05-replication-and-local-first` |
| 7 | 20 | 8,211 | `06-sharding-and-tenancy` |
| 8 | 65 | 23,362 | `07-transactions-and-isolation` |
| 9 | 46 | 19,224 | `08-partial-failure-and-models` |
| 10 | 40 | 17,240 | `09-consistency-and-consensus` |
| 11 | 29 | 12,627 | `10-batch-processing` |
| 12 | 52 | 18,617 | `11-streams-and-cdc` |
| 13 | 52 | 17,549 | `12-end-to-end-correctness` |
| 14 | 13 | 6,319 | `13-ethics-and-data-rights` |

**Count:** 503 indexed headings across 14 chapter bodies.

## Chapter 1: Trade-Offs in Data Systems Architecture

- `Chapter 1. Trade-Offs in Data Systems Architecture` — ~828 words
- `Terminology: Frontends and Backends` — ~208 words
- `Operational Versus Analytical Systems` — ~498 words
-   `Characterizing Transaction Processing and Analytics` — ~686 words
-   `Data Warehousing` — ~745 words
-     `From data warehouse to data lake` — ~519 words
-     `Beyond the data lake` — ~245 words
-   `Systems of Record and Derived Data` — ~532 words
- `Cloud Versus Self-Hosting` — ~321 words
-   `Pros and Cons of Cloud Services` — ~830 words
-   `Cloud Native System Architecture` — ~202 words
-     `Layering of cloud services` — ~402 words
-     `Separation of storage and compute` — ~569 words
-   `Operations in the Cloud Era` — ~660 words
- `Distributed Versus Single-Node Systems` — ~538 words
-   `Problems with Distributed Systems` — ~431 words
-   `Microservices and Serverless` — ~756 words
-   `Cloud Computing Versus Supercomputing` — ~377 words
- `Data Systems, Law, and Society` — ~876 words
- `Summary` — ~359 words

## Chapter 2: Defining Nonfunctional Requirements

- `Chapter 2. Defining Nonfunctional Requirements` — ~332 words
- `Case Study: Social Network Home Timelines` — ~140 words
-   `Representing Users, Posts, and Follows` — ~349 words
-   `Materializing and Updating Timelines` — ~594 words
- `Describing Performance` — ~218 words
- `When an Overloaded System Won’t Recover` — ~332 words
-   `Latency and Response Time` — ~419 words
-   `Average, Median, and Percentiles` — ~457 words
- `The User Impact of Response Times` — ~282 words
-   `Use of Response Time Metrics` — ~231 words
- `Computing Percentiles` — ~176 words
- `Reliability and Fault Tolerance` — ~290 words
-   `Fault Tolerance` — ~401 words
-   `Hardware and Software Faults` — ~415 words
-     `Tolerating hardware faults through redundancy` — ~379 words
-     `Software faults` — ~427 words
-   `Humans and Reliability` — ~490 words
- `How Important Is Reliability?` — ~324 words
- `Scalability` — ~342 words
-   `Understanding Load` — ~435 words
-   `Shared-Memory, Shared-Disk, and Shared-Nothing Architectures` — ~439 words
-   `Principles for Scalability` — ~331 words
- `Maintainability` — ~338 words
-   `Operability: Making Life Easy for Operations` — ~336 words
-   `Simplicity: Managing Complexity` — ~507 words
-   `Evolvability: Making Change Easy` — ~256 words
- `Summary` — ~304 words

## Chapter 3: Data Models and Query Languages

- `Chapter 3. Data Models and Query Languages` — ~414 words
- `Terminology: Declarative Query Languages` — ~213 words
- `Relational Versus Document Models` — ~445 words
-   `The Object-Relational Mismatch` — ~126 words
-     `Object-relational mapping` — ~446 words
-     `The document data model for one-to-many relationships` — ~535 words
-   `Normalization, Denormalization, and Joins` — ~586 words
-     `Trade-offs of normalization` — ~459 words
-     `Denormalization in the social networking case study` — ~490 words
-   `Many-to-One and Many-to-Many Relationships` — ~466 words
-   `Stars and Snowflakes: Schemas for Analytics` — ~812 words
-   `When to Use Which Model` — ~288 words
-     `Schema flexibility in the document model` — ~687 words
-     `Data locality for reads and writes` — ~251 words
-     `Query languages for documents` — ~395 words
-     `Convergence of document and relational databases` — ~204 words
- `Graph-Like Data Models` — ~652 words
-   `Property Graphs` — ~699 words
-   `The Cypher Query Language` — ~690 words
-   `Graph Queries in SQL` — ~841 words
-   `Triple Stores and SPARQL` — ~556 words
- `The Semantic Web` — ~151 words
-     `The RDF data model` — ~284 words
-     `The SPARQL query language` — ~242 words
-   `Datalog: Recursive Relational Queries` — ~1039 words
-   `GraphQL` — ~881 words
- `Event Sourcing and CQRS` — ~1690 words
- `DataFrames, Matrices, and Arrays` — ~801 words
- `Summary` — ~671 words

## Chapter 4: Storage and Retrieval

- `Chapter 4. Storage and Retrieval` — ~363 words
- `Storage and Indexing for OLTP` — ~722 words
-   `Log-Structured Storage` — ~312 words
-     `The SSTable file format` — ~304 words
-     `Constructing and merging SSTables` — ~883 words
-     `Bloom filters` — ~552 words
-     `Compaction strategies` — ~397 words
- `Embedded Storage Engines` — ~195 words
-   `B-Trees` — ~766 words
-     `Making B-trees reliable` — ~317 words
-     `Using B-tree variants` — ~228 words
-   `Comparing B-Trees and LSM-Trees` — ~97 words
-     `Read performance` — ~300 words
-     `Sequential versus random writes` — ~162 words
- `Sequential Versus Random Writes on SSDs` — ~303 words
-     `Write amplification` — ~418 words
-     `Disk space usage` — ~366 words
-   `Multicolumn and Secondary Indexes` — ~249 words
-   `Storing Values Within the Index` — ~412 words
-   `Keeping Everything in Memory` — ~478 words
- `Data Storage for Analytics` — ~173 words
-   `Cloud Data Warehouses` — ~549 words
-   `Column-Oriented Storage` — ~779 words
-     `Column compression` — ~478 words
-     `Sort order in column storage` — ~422 words
-     `Writing to column-oriented storage` — ~244 words
-   `Query Execution: Compilation and Vectorization` — ~630 words
-   `Materialized Views and Data Cubes` — ~541 words
- `Multidimensional and Full-Text Indexes` — ~547 words
-   `Full-Text Search` — ~602 words
-   `Vector Embeddings` — ~855 words
- `Summary` — ~493 words

## Chapter 5: Encoding and Evolution

- `Chapter 5. Encoding and Evolution` — ~706 words
- `Formats for Encoding Data` — ~146 words
- `Terminology clash` — ~133 words
-   `Language-Specific Formats` — ~286 words
-   `JSON, XML, and Binary Variants` — ~515 words
-     `JSON Schema` — ~412 words
-     `Binary encodings` — ~477 words
-   `Protocol Buffers` — ~479 words
-     `Field tags and schema evolution` — ~482 words
-   `Avro` — ~404 words
-     `The writer’s schema and the reader’s schema` — ~262 words
-     `Schema evolution rules` — ~356 words
-     `But what is the writer’s schema?` — ~337 words
-     `Dynamically generated schemas` — ~347 words
-   `The Merits of Schemas` — ~437 words
- `Modes of Dataflow` — ~163 words
-   `Dataflow Through Databases` — ~220 words
-     `Different values written at different times` — ~283 words
-     `Archival storage` — ~133 words
-   `Dataflow Through Services: REST and RPC` — ~457 words
-     `Web services` — ~705 words
-     `The problems with remote procedure calls` — ~673 words
-     `Load balancers, service discovery, and service meshes` — ~677 words
-     `Data encoding and evolution for RPC` — ~303 words
-   `Durable Execution and Workflows` — ~157 words
- `Tasks, activities, and functions` — ~708 words
-   `Event-Driven Architectures` — ~242 words
-     `Message brokers` — ~336 words
-     `Distributed actor frameworks` — ~313 words
- `Summary` — ~430 words

## Chapter 6: Replication

- `Chapter 6. Replication` — ~413 words
- `Backups and Replication` — ~198 words
- `Single-Leader Replication` — ~447 words
-   `Synchronous Versus Asynchronous Replication` — ~625 words
-   `Setting Up New Followers` — ~391 words
- `Databases Backed by Object Storage` — ~482 words
-   `Handling Node Outages` — ~84 words
-     `Follower failure: Catch-up recovery` — ~275 words
-     `Leader failure: Failover` — ~920 words
-   `Implementation of Replication Logs` — ~21 words
-     `Statement-based replication` — ~351 words
-     `Write-ahead log shipping` — ~276 words
-     `Logical (row-based) log replication` — ~337 words
-   `Problems with Replication Lag` — ~470 words
-     `Reading your own writes` — ~729 words
- `Regions and Availability Zones` — ~198 words
-     `Monotonic reads` — ~319 words
-     `Consistent prefix reads` — ~332 words
-   `Solutions for Replication Lag` — ~333 words
- `Multi-Leader Replication` — ~274 words
-   `Geographically Distributed Operation` — ~625 words
-     `Multi-leader replication topologies` — ~278 words
-     `Problems with different topologies` — ~354 words
-   `Sync Engines and Local-First Software` — ~186 words
-     `Real-time collaboration, offline-first, and local-first apps` — ~395 words
-     `Pros and cons of sync engines` — ~539 words
-   `Dealing with Conflicting Writes` — ~219 words
-     `Conflict avoidance` — ~320 words
-     `Last write wins (discarding concurrent writes)` — ~396 words
-     `Manual conflict resolution` — ~502 words
-     `Automatic conflict resolution` — ~439 words
-     `Conflict-free replicated datatypes and operational transformation` — ~450 words
-     `Types of conflict` — ~237 words
- `Leaderless Replication` — ~275 words
-   `Writing to the Database When a Node Is Down` — ~330 words
-     `Catching up on missed writes` — ~234 words
-     `Using quorums for reading and writing` — ~590 words
-     `Understanding the limitations of quorum consistency` — ~724 words
-     `Monitoring staleness` — ~198 words
-   `Single-Leader Versus Leaderless Replication Performance` — ~715 words
-   `Multi-Region Operation` — ~230 words
-   `Detecting Concurrent Writes` — ~307 words
-     `The happens-before relation and concurrency` — ~246 words
- `Concurrency, Time, and Relativity` — ~223 words
-     `Capturing the happens-before relationship` — ~858 words
-     `Version vectors` — ~285 words
- `Version vectors and vector clocks` — ~52 words
- `Summary` — ~588 words

## Chapter 7: Sharding

- `Chapter 7. Sharding` — ~289 words
- `Sharding and Partitioning` — ~301 words
- `Pros and Cons of Sharding` — ~502 words
- `Sharding for Multitenancy` — ~597 words
- `Sharding of Key-Value Data` — ~279 words
-   `Sharding by Key Range` — ~535 words
-     `Rebalancing key-range sharded data` — ~338 words
-   `Sharding by Hash of Key` — ~211 words
-     `Hash modulo number of nodes` — ~237 words
-     `Fixed number of shards` — ~555 words
-     `Sharding by hash range` — ~300 words
- `Partitioning and Range Queries in Data Warehouses` — ~271 words
-     `Consistent hashing` — ~194 words
-   `Skewed Workloads and Relieving Hot Spots` — ~472 words
-   `Operations: Automatic Versus Manual Rebalancing` — ~393 words
- `Request Routing` — ~813 words
- `Sharding and Secondary Indexes` — ~207 words
-   `Local Secondary Indexes` — ~531 words
-   `Global Secondary Indexes` — ~548 words
- `Summary` — ~521 words

## Chapter 8: Transactions

- `Chapter 8. Transactions` — ~578 words
- `What Exactly Is a Transaction?` — ~309 words
-   `The Meaning of ACID` — ~202 words
-     `Atomicity` — ~320 words
-     `Consistency` — ~403 words
-     `Isolation` — ~302 words
-     `Durability` — ~274 words
- `Replication and Durability` — ~482 words
-   `Single-Object and Multi-Object Operations` — ~522 words
-     `Single-object writes` — ~349 words
-     `The need for multi-object transactions` — ~320 words
-     `Handling errors and aborts` — ~437 words
- `Weak Isolation Levels` — ~582 words
-   `Read Committed` — ~59 words
-     `No dirty reads` — ~251 words
-     `No dirty writes` — ~286 words
-     `Implementing read-committed` — ~476 words
-   `Snapshot Isolation and Repeatable Read` — ~715 words
-     `Multiversion concurrency control` — ~522 words
-     `Visibility rules for observing a consistent snapshot` — ~394 words
-     `Indexes and snapshot isolation` — ~327 words
-     `Snapshot isolation, repeatable read, and naming confusion` — ~264 words
-   `Preventing Lost Updates` — ~274 words
-     `Atomic write operations` — ~235 words
-     `Explicit locking` — ~314 words
-     `Automatically detecting lost updates` — ~201 words
-     `Conditional writes (compare-and-set)` — ~299 words
-     `Conflict resolution and replication` — ~267 words
-   `Write Skew and Phantoms` — ~298 words
-     `Characterizing write skew` — ~384 words
-     `More examples of write skew` — ~455 words
-     `Phantoms causing write skew` — ~419 words
-     `Materializing conflicts` — ~257 words
- `Serializability` — ~363 words
-   `Actual Serial Execution` — ~292 words
-     `Encapsulating transactions in stored procedures` — ~416 words
-     `Pros and cons of stored procedures` — ~475 words
-     `Sharding` — ~296 words
-     `Summary of serial execution` — ~109 words
-   `Two-Phase Locking` — ~32 words
- `2PL is not 2PC` — ~296 words
-     `Implementation of 2PL` — ~344 words
-     `Performance of 2PL` — ~333 words
-     `Predicate locks` — ~357 words
-     `Index-range locks` — ~425 words
-   `Serializable Snapshot Isolation` — ~157 words
-     `Pessimistic versus optimistic concurrency control` — ~402 words
-     `Decisions based on an outdated premise` — ~274 words
-     `Detection of stale MVCC reads` — ~297 words
-     `Detection of writes that affect prior reads` — ~297 words
-     `Performance of serializable snapshot isolation` — ~380 words
- `Distributed Transactions` — ~686 words
-   `Two-Phase Commit` — ~356 words
-     `A system of promises` — ~604 words
-     `Coordinator failure` — ~427 words
-     `Three-phase commit` — ~130 words
-   `Distributed Transactions Across Different Systems` — ~326 words
-     `Exactly-once message processing` — ~274 words
-     `XA transactions` — ~387 words
-     `Holding locks while in doubt` — ~238 words
-     `Recovering from coordinator failure` — ~286 words
-     `Problems with XA transactions` — ~314 words
-   `Database-Internal Distributed Transactions` — ~319 words
-   `Exactly-Once Message Processing Revisited` — ~546 words
- `Summary` — ~797 words

## Chapter 9: The Trouble with Distributed Systems

- `Chapter 9. The Trouble with Distributed Systems` — ~326 words
- `Faults and Partial Failures` — ~623 words
- `Unreliable Networks` — ~474 words
-   `The Limitations of TCP` — ~595 words
-   `Network Faults in Practice` — ~399 words
- `Network partitions` — ~198 words
-   `Fault Detection` — ~433 words
-   `Timeouts and Unbounded Delays` — ~448 words
-     `Network congestion and queueing` — ~308 words
- `TCP Versus UDP` — ~154 words
-     `Variability of network delays` — ~256 words
-   `Synchronous Versus Asynchronous Networks` — ~283 words
-     `Can we not simply make network delays predictable?` — ~307 words
- `Latency and Resource Utilization` — ~364 words
-     `Combining circuit switching and packet switching` — ~290 words
- `Unreliable Clocks` — ~312 words
-   `Monotonic Versus Time-of-Day Clocks` — ~32 words
-     `Time-of-day clocks` — ~256 words
-     `Monotonic clocks` — ~356 words
-   `Clock Synchronization and Accuracy` — ~822 words
-   `Relying on Synchronized Clocks` — ~286 words
-     `Timestamps for ordering events` — ~828 words
-     `Clock readings with a confidence interval` — ~419 words
-     `Synchronized clocks for global snapshots` — ~527 words
-   `Process Pauses` — ~1266 words
-     `Provididng response time guarantees` — ~411 words
-     `Limiting the impact of garbage collection` — ~373 words
- `Knowledge, Truth, and Lies` — ~362 words
-   `The Majority Rules` — ~507 words
-   `Distributed Locks and Leases` — ~524 words
-     `Fencing off zombies and delayed requests` — ~622 words
-     `Fencing with multiple replicas` — ~333 words
-   `Byzantine Faults` — ~177 words
- `The Byzantine Generals Problem` — ~225 words
-     `Uses of Byzantine fault tolerance` — ~564 words
-     `Weak forms of lying` — ~287 words
-   `System Model and Reality` — ~653 words
-     `Defining the correctness of an algorithm` — ~246 words
-     `Distinguishing between safety and liveness` — ~379 words
-     `Mapping system models to the real world` — ~340 words
-   `Formal Methods and Randomized Testing` — ~216 words
-     `Model checking and specification languages` — ~325 words
-     `Fault injection` — ~300 words
-     `Deterministic simulation testing` — ~537 words
- `The Power of Determinism` — ~264 words
- `Summary` — ~740 words

## Chapter 10: Consistency and Consensus

- `Chapter 10. Consistency and Consensus` — ~574 words
- `Linearizability` — ~413 words
-   `What Makes a System Linearizable?` — ~1313 words
- `Linearizability Versus Serializability` — ~361 words
-   `Relying on Linearizability` — ~54 words
-     `Locking and leader election` — ~272 words
-     `Constraints and uniqueness guarantees` — ~288 words
-     `Cross-channel timing dependencies` — ~500 words
-   `Implementing Linearizable Systems` — ~850 words
-   `The Cost of Linearizability` — ~317 words
-     `The CAP theorem` — ~534 words
- `The Unhelpful CAP Theorem` — ~263 words
-     `Linearizability and network delays` — ~406 words
- `ID Generators and Logical Clocks` — ~961 words
-   `Logical Clocks` — ~197 words
-     `Lamport timestamps` — ~397 words
-     `Hybrid logical clocks` — ~294 words
-     `Lamport/hybrid logical clocks versus vector clocks` — ~253 words
-   `Linearizable ID Generators` — ~457 words
-     `Implementing a linearizable ID generator` — ~412 words
-     `Enforcing constraints using logical clocks` — ~239 words
- `Consensus` — ~442 words
- `The Impossibility of Consensus` — ~184 words
-   `The Many Faces of Consensus` — ~175 words
-     `Single-value consensus` — ~689 words
-     `Compare-and-set as consensus` — ~263 words
-     `Shared logs as consensus` — ~633 words
-     `Fetch-and-add as consensus` — ~436 words
-     `Atomic commitment as consensus` — ~527 words
-   `Consensus in Practice` — ~111 words
-     `Using shared logs` — ~338 words
-     `From single-leader replication to consensus` — ~579 words
-     `Subtleties of consensus` — ~201 words
- `Consistency Versus Availability in Leader Election` — ~429 words
-     `Pros and cons of consensus` — ~390 words
-   `Coordination Services` — ~446 words
- `Managing Configuration with Coordination Services` — ~121 words
-     `Allocating work to nodes` — ~383 words
-     `Service discovery` — ~335 words
- `Summary` — ~981 words

## Chapter 11: Batch Processing

- `Chapter 11. Batch Processing` — ~1193 words
- `Batch Processing with Unix Tools` — ~243 words
-   `Simple Log Analysis` — ~453 words
-   `Chain of Commands Versus Custom Program` — ~271 words
-   `Sorting Versus In-Memory Aggregation` — ~356 words
- `Batch Processing in Distributed Systems` — ~111 words
-   `Distributed Filesystems` — ~680 words
- `Distributed Filesystems and Network Storage` — ~224 words
-   `Object Stores` — ~684 words
-   `Distributed Job Orchestration` — ~557 words
-     `Resource allocation` — ~421 words
-     `Scheduling workflows` — ~589 words
-     `Handling faults` — ~465 words
- `Batch Processing Models` — ~111 words
-   `MapReduce` — ~557 words
- `MapReduce and Functional Programming` — ~196 words
-   `Dataflow Engines` — ~520 words
-   `Shuffling Data` — ~66 words
- `Shuffle is not random` — ~615 words
-   `Joins and Grouping` — ~560 words
-   `Query Languages` — ~434 words
- `Batch Processing and Cloud Data Warehouses Converge` — ~348 words
-   `DataFrames` — ~277 words
- `Batch Use Cases` — ~171 words
-   `Extract–Transform–Load` — ~447 words
-   `Analytics` — ~298 words
-   `Machine Learning` — ~498 words
-   `Serving Derived Data` — ~717 words
- `Summary` — ~422 words

## Chapter 12: Stream Processing

- `Chapter 12. Stream Processing` — ~493 words
- `Transmitting Event Streams` — ~512 words
-   `Messaging Systems` — ~498 words
-     `Direct messaging from producers to consumers` — ~322 words
-     `Message brokers` — ~223 words
-     `Message brokers compared to databases` — ~356 words
-     `Multiple consumers` — ~225 words
-     `Acknowledgments and redelivery` — ~555 words
-   `Log-Based Message Brokers` — ~309 words
-     `Using logs for message storage` — ~338 words
-     `Logs compared to traditional messaging` — ~427 words
-     `Consumer offsets` — ~256 words
-     `Disk space usage` — ~357 words
-     `When consumers cannot keep up with producers` — ~268 words
-     `Replaying old messages` — ~189 words
- `Databases and Streams` — ~389 words
-   `Keeping Systems in Sync` — ~600 words
-   `Change Data Capture` — ~319 words
-     `Implementing CDC` — ~315 words
-     `Initial snapshot` — ~182 words
-     `Log compaction` — ~391 words
-     `API support for change streams` — ~237 words
-     `CDC versus event sourcing` — ~231 words
- `Change Data Capture and Database Schemas` — ~543 words
-   `State, Streams, and Immutability` — ~451 words
-     `Advantages of immutable events` — ~347 words
-     `Deriving several views from the same event log` — ~394 words
-     `Concurrency control` — ~361 words
-     `Limitations of immutability` — ~476 words
- `Processing Streams` — ~457 words
-   `Uses of Stream Processing` — ~148 words
-     `Complex event processing` — ~252 words
-     `Stream analytics` — ~340 words
-     `Maintaining materialized views` — ~204 words
- `Incremental View Maintenance` — ~371 words
-     `Search on streams` — ~220 words
-     `Event-driven architectures and RPC` — ~228 words
-   `Reasoning About Time` — ~255 words
-     `Event time versus processing time` — ~353 words
-     `Handling straggler events` — ~317 words
-     `Whose clock are you using, anyway?` — ~354 words
-     `Types of windows` — ~467 words
-   `Stream Joins` — ~99 words
-     `Stream–stream join (window join)` — ~385 words
-     `Stream–table join (stream enrichment)` — ~401 words
-     `Time dependence of joins` — ~445 words
-   `Fault Tolerance` — ~220 words
-     `Microbatching and checkpointing` — ~276 words
-     `Atomic commit revisited` — ~220 words
-     `Idempotence` — ~295 words
-     `Rebuilding state after a failure` — ~294 words
- `Summary` — ~756 words

## Chapter 13: A Philosophy of Streaming Systems

- `Chapter 13. A Philosophy of Streaming Systems` — ~188 words
- `Data Integration` — ~297 words
-   `Combining Specialized Tools by Deriving Data` — ~174 words
-     `Reasoning about dataflows` — ~331 words
-     `Derived data versus distributed transactions` — ~293 words
-     `The limits of total ordering` — ~309 words
-     `Ordering events to capture causality` — ~426 words
-   `Batch and Stream Processing` — ~120 words
-     `Maintaining derived state` — ~284 words
-     `Reprocessing data for application evolution` — ~120 words
- `Schema Migrations on Railways` — ~390 words
-     `Unifying batch and stream processing` — ~207 words
- `Unbundling Databases` — ~348 words
-   `Composing Data Storage Technologies` — ~143 words
-     `Creating an index` — ~181 words
-     `The meta-database of everything` — ~442 words
-     `Making unbundling work` — ~391 words
-     `Unbundled versus integrated systems` — ~339 words
-   `Designing Applications Around Dataflow` — ~233 words
-     `Application code as a derivation function` — ~371 words
-     `Separation of application code and state` — ~466 words
-     `Dataflow: Interplay between state changes and application code` — ~305 words
-     `Stream processors and services` — ~526 words
-   `Observing Derived State` — ~302 words
-     `Materialized views and caching` — ~470 words
-     `Stateful, offline-capable clients` — ~286 words
-     `Pushing state changes to clients` — ~365 words
-     `End-to-end event streams` — ~270 words
-     `Reads are events too` — ~478 words
-     `Multishard data processing` — ~258 words
- `Aiming for Correctness` — ~467 words
-   `The End-to-End Argument for Databases` — ~118 words
-     `Exactly-once execution of an operation` — ~239 words
-     `Duplicate suppression` — ~541 words
-     `Uniquely identifying requests` — ~356 words
-     `The end-to-end argument` — ~393 words
-     `Applying end-to-end thinking in data systems` — ~284 words
-   `Enforcing Constraints` — ~178 words
-     `Uniqueness constraints require consensus` — ~253 words
-     `Uniqueness in log-based messaging` — ~328 words
-     `Multishard request processing` — ~825 words
-   `Timeliness and Integrity` — ~533 words
-     `Correctness of dataflow systems` — ~315 words
-     `Loosely interpreted constraints` — ~641 words
-     `Coordination-avoiding data systems` — ~339 words
-   `Trust, but Verify` — ~246 words
-     `Maintaining integrity in the face of software bugs` — ~268 words
-     `Don’t just blindly trust what they promise` — ~354 words
-     `Designing for auditability` — ~259 words
-     `The end-to-end argument again` — ~226 words
-     `Tools for auditable data systems` — ~300 words
- `Summary` — ~458 words

## Chapter 14: Doing the Right Thing

- `Chapter 14. Doing the Right Thing` — ~435 words
- `Predictive Analytics` — ~279 words
-   `Bias and Discrimination` — ~350 words
-   `Responsibility and Accountability` — ~537 words
-   `Feedback Loops` — ~322 words
- `Privacy and Tracking` — ~339 words
-   `Surveillance` — ~530 words
-   `Consent and Freedom of Choice` — ~729 words
-   `Privacy and Use of Data` — ~729 words
-   `Data as Assets and Power` — ~559 words
-   `Remembering the Industrial Revolution` — ~399 words
-   `Legislation and Self-Regulation` — ~517 words
- `Summary` — ~525 words

