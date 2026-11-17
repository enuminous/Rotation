# Registry schema and semantics

`data/evidence.json` records one **claim** per ID and a list of source IDs into `data/sources.json`.

**Statuses:** `ESTABLISHED_MATH` is a conventional mathematical identity under explicit assumptions; `FORMALIZED_CONDITIONAL` is source-formalized conditional mathematics (not independently recompiled in this atlas); `OBSERVED_LOCAL` is direct observation of bounded systems; `MODEL_CONSTRAINT` is a constrained inference in a specified data/model fit; `REPORTED_CONTESTED` is a published interpretation requiring independent adjudication; `PROPOSED_MODEL` is not empirically validated; `OPEN` is a missing link or test; `CONTROL_NULL` is a concrete mathematical null/control.

**Relevance:** `local_only` never automatically supports global rotation; `neutral` is mathematical or observational background; `candidate_global` motivates testing but is not detection; `against_specific_global_model` challenges one precisely defined model only; `against_unique_detection` points to identifiability; `counterexample` and `against_universal_literality` refute particular overbroad verbal statements; `unresolved_bridge` identifies required mathematics.

Entries have independent source provenance. **A link and a SHA-256 are not external replication, proof, or source approval.** Numerical claims in summaries must stay scoped to source analysis and confidence conditions.

Adding a new claim: provide an ID, field domain, literal claim, supported status, explicit sources, limitation, and relationship to universal cosmic rotation. For a proposed discovery, also add an independent comparator, preregistered metric, falsifier, and source of data custody under `docs/EXPERIMENTS.md`.

Validation: `python scripts/validate_evidence.py`.
