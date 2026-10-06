# Backend Service - AI City Command Center

> **Lead Workstation**: Laptop 2 (Backend Architecture Lead)  
> **Status**: Phase 0 Specification (Implementation NOT started)

---

## 1. Overview & Technology Stack

The backend serves as the core orchestration service, exposing validated REST endpoints, handling business logic, coordinating AI evaluation, and managing data persistence.

### Planned Architecture & Technologies
- **Language & Runtime**: Python
- **API Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Data Persistence**:
  - *Initial Development Baseline*: Structured in-memory repositories seeded with validated JSON fixtures from `data/sample/`.
  - *Planned Direction*: PostgreSQL (see [`../database/README.md`](../database/README.md)).
- **AI Integration**: Modular Python invocation of Laptop 1's AI service with a configurable timeout guard triggering the deterministic fallback workflow.

---

## 2. Workstation Mandate & Boundaries

> ### 🛑 PHASE 0 NOTICE
> **Do NOT build the application yet.**  
> **Do NOT install dependencies yet.**  
> Implementation begins during Phase 1 following verified project initialization.

### Conceptual Responsibilities for Laptop 2
1. **API Layer**: Expose conceptual REST endpoints defined in [`../docs/06-api-contract.md`](../docs/06-api-contract.md):
   - `/health`
   - `/incidents`
   - `/incidents/{id}`
   - `/analysis`
   - `/alerts`
   - `/zones`
   - `/incidents/{id}/response`
   *(Final routing prefix such as `/api` or `/api/v1` is an implementation detail to be finalized during backend setup).*
2. **Request Validation**: Enforce schema validation on all incoming payloads.
3. **Incident Management**: Coordinate incident creation, zone assignment, and lifecycle state transitions.
4. **AI Integration**: Mediate calls to the AI subsystem with timeout handling triggering the rule-based fallback.
5. **Severity Calculation**: Execute the hybrid severity scoring engine combining AI analysis with deterministic municipal rules.
6. **Alert & Response Coordination**: Manage alert triggers and response tracking updates.

---

## 3. Contract Integration & Handoffs

- **API Specifications**: Strictly follow [`../docs/06-api-contract.md`](../docs/06-api-contract.md). Any endpoint changes require mutual coordination with Laptop 4.
- **AI Interface**: Coordinates with Laptop 1 on the standardized analysis input/output signatures.
- **Data Schemas**: Derive models directly from [`../docs/07-data-schema.md`](../docs/07-data-schema.md).
