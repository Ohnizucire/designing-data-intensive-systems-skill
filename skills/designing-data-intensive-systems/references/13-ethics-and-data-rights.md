# Ethical Consequences, Privacy and Data Rights

**Trigger:** processing data about people, tracking, analytics/profiling, automated decisions, third-party disclosures or deletion/retention. **Book:** chapters 1 and 14, with propagation from chapters 11–13.

## Decide

1. Inventory collected data and derived/inferred data; associate purpose, access, retention, storage region, processor/vendor, human consequences and affected people (including nonusers).
2. Data minimization is an architectural choice: collect only what is necessary, limit lifetime/replication, and map deletion/export/correction through backups, CDC streams, caches, indexes, models and external processors. 'Delete row in primary database' is not an end-to-end deletion design.
3. Distinguish legal basis/consent from ethical adequacy. Consent is meaningful only when choice, comprehensibility and withdrawal are real; legal rules depend on jurisdiction and current regulations, so verify externally rather than treating book examples as current legal advice.
4. For predictive decisions, identify biased historical data, proxy variables, false positives, group disparities, feedback loops, appeal/correction and accountable human review. Model statistical uncertainty rather than expressing predictions as indisputable individual facts.
5. Map how targeting/surveillance, cross-dataset joining, retention and information asymmetry could harm people even if the software performs exactly as specified. Seek input from affected stakeholders when stakes justify it.
6. Balance auditability/immutable histories with privacy and erasure: scope event payloads, encryption/key lifecycle, redaction/compaction and derivation rebuild; record any unresolved legal/security conflict for appropriate review.

## Tests and proof

- A subject request to delete or correct data is followed across authoritative and derived systems, with documented limits for immutable records, backups and externally shared data.
- Automated decisions can be explained, challenged and corrected, with monitored failure modes and disproportionate impact assessments where appropriate.
- A breach/threat model includes collection minimization, access restrictions, retention and vendors.

**Stop when:** data purposes and consequences are documented, affected rights have an end-to-end mechanism, and high-impact trade-offs have accountable review.
