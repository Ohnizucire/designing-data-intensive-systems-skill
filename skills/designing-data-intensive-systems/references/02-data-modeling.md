# Data Models and Query Semantics

**Trigger:** modeling entities and relationships, choosing relational/document/graph, denormalizing, event sourcing or analytical data models. **Book:** chapter 3.

## Decide

1. Write the questions the application must answer and the updates it must safely perform before choosing schema syntax. Distinguish identity, one-to-many, many-to-many, ownership, cardinality and access locality.
2. Prefer relations/normalization where changing facts and references must remain consistent; document models for naturally self-contained aggregates with locality and flexible shape; graph traversals for densely connected or variable-length relationships. Don't select models on marketing categories alone: products overlap in capabilities.
3. Assess *joins versus denormalization*: embedding may speed a read but duplicates facts and adds update obligations. For every denormalized field, specify source, transformation, update ordering and rebuild.
4. Distinguish schema-on-write, flexible schemas and schema evolution. A document store's lack of enforced schema does not remove downstream contracts, migrations or data quality duties.
5. Distinguish domain event sourcing (business facts as primary history) from ordinary mutable state and from database-level change data capture. Use event sourcing only if domain audit/history/recomputation warrants the new invariants and event evolution burden.
6. For analytics, prefer models appropriate for aggregation (fact/dimension, star schema where useful), not blindly the operational schema. For matrix/DataFrame work, record the mapping back to authoritative entities and versions.
7. Evaluate query expressiveness (SQL recursive queries, Cypher/SPARQL/Datalog/GraphQL where relevant) separately from storage engine and consistency guarantees.

## Tests and proof

- Sample multi-entity writes preserve references, uniqueness and the declared aggregate boundary.
- Update a shared fact and confirm every derived/embed path converges or has a stated staleness policy.
- Query scenarios exercise joins, graph traversals and history evolution, including deleted and changed entities.
- Explain the query plan on representative data; model and index decisions must agree.

**Stop when:** every entity/relationship and dominant query has a justified representation, update owner and evolution/rebuild policy.
