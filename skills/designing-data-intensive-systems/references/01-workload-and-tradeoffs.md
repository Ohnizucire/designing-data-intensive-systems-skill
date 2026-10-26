# Workload, Nonfunctional Requirements and Trade-offs

**Trigger:** selecting a topology, operational model, latency target or scaling strategy. **Book:** chapters 1–2 (operational versus analytical systems; systems of record; distributed versus single-node; nonfunctional requirements and social timeline fan-out case study).

## Decide

1. Describe real actors, read/write/query shapes, transaction versus analytics mix, live users, burstiness, skew, growth and consequences of failure. Measure end-to-end **response time**, throughput, p50/p95/p99 and queue length; distinguish user experience from server-side processing latency.
2. Translate adjectives into explicit objectives: what percentage of requests complete by what deadline, what data can be lost, what must remain available, and how rapidly recovery must happen? State how results are sampled, and avoid averaging percentiles across heterogeneous windows or hosts.
3. Compare the smallest viable single-process/single-node/one-database path to a targeted optimization and, only when justified, distributed/specialized services. A frontend and backend may already be distributed without requiring a distributed database.
4. Analyze overload as an *unstable feedback problem*: admission, bounded concurrency, queue depth, retries, timeouts, circuit breakers and recovery after a spike. A system may remain overloaded after incoming load drops if accumulated work and retry storms continue.
5. Separate operational from analytical workloads only when their competing access patterns or isolation/security needs justify it; identify canonical records and derived read models. Evaluate cloud versus self-hosting by workload, team, egress, privacy, vendor exit, availability, observability and total cost; neither dominates universally.
6. Include the human costs of complexity: production diagnosis, on-call burden, deployment coordination, maintenance, evolvability and incident learning. Microservices are often justified by independent teams, not purely code aesthetics.

## Evidence and failure probes

- A realistic load distribution, including hot keys and slow dependencies, is exercised; tail latency, queue growth, resource saturation and cost are observable.
- Recovery from a transient overload terminates, rather than retaining a growing retry/backlog loop.
- The promised uptime and data-loss envelope explicitly reflect backup, restore, node and provider failures.
- A simpler candidate is retained unless measurements or indispensable fault boundaries rule it out.

**Stop when:** requirements, workload shape, viable baseline, saturation behavior and objective escalation trigger are all explicit. **Do not infer** product-specific performance from generic architectural labels.
