# Database Architecture - AI City Command Center

> **Lead Workstations**: Laptop 2 (Backend) & Laptop 3 (Data & Supporting)  
> **Status**: Phase 0 Conceptual Specification (NO database installed yet)  
> **Planned Database Direction**: PostgreSQL

---

## 1. Overview & Architectural Direction

**PostgreSQL** is the current planned database direction for persistent data storage in the AI City Command Center.

### Phase 0 / Hackathon Guidelines
- **Do NOT install PostgreSQL or configure local database infrastructure yet.**
- For the early stages of the hackathon, backend development can initially operate against structured in-memory repositories seeded with validated JSON data from `data/sample/`.
- All entity models are defined conceptually in [`../docs/07-data-schema.md`](../docs/07-data-schema.md) so they map cleanly to relational tables when database persistence is connected.
- Specific database extensions or geospatial capabilities (such as spatial indexing) can be evaluated later if actually needed during implementation.

---

## 2. Directory Structure

```text
database/
├── schema/      # Future SQL DDL scripts and table migration definitions
└── README.md    # Database documentation and guidelines
```

---

## 3. Conceptual Entity Mapping

When relational persistence is introduced, the conceptual models from [`../docs/07-data-schema.md`](../docs/07-data-schema.md) map as:
- `zones` $\rightarrow$ Geographic zones and priority weights.
- `incidents` $\rightarrow$ Core incident records, coordinates, status, and severity.
- `ai_analysis_results` $\rightarrow$ AI classification and hazard feature records.
- `alerts` $\rightarrow$ Active priority alerts and acknowledgment state.
- `response_logs` $\rightarrow$ Incident dispatch and resolution timeline.

---

## 4. Workstation Guidelines
- Do not run local database daemons or Docker containers during Phase 0.
- All schema modifications must update [`../docs/07-data-schema.md`](../docs/07-data-schema.md) first.
