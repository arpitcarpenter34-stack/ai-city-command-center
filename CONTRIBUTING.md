# Contributing Guidelines - AI City Command Center

Welcome to the **AI City Command Center** 36-hour hackathon project. Because we operate in an intensive, multi-developer environment across four workstations, strict adherence to these collaboration standards ensures stable integration and protects our P0 demo.

---

## 1. Golden Rules of the 36-Hour Hackathon

1. **P0 Before P1**: Never work on P1 (Traffic/Crowd intelligence, 3D animations) if P0 (Core Command Overview, Detection, Analysis, Severity, Map, Alerts, Tracking) is broken or incomplete.
2. **Never Break the P0 Demo Flow**: If an experimental feature threatens the stability of the core judge presentation flow, disable it immediately and fall back to the validated baseline.
3. **No Unilateral Contract Changes**: The REST API contract ([`docs/06-api-contract.md`](./docs/06-api-contract.md)) and Data Schema ([`docs/07-data-schema.md`](./docs/07-data-schema.md)) are shared boundaries. Any change requires agreement between Laptop 2 (Backend), Laptop 4 (Frontend), Laptop 1 (AI), and Laptop 3 (Supporting).
4. **No Random Dependencies**: Do not run arbitrary package install commands without clearing with the team. Minimize bloat.
5. **No Hardcoded Secrets**: Never commit `.env` or API credentials. Use [`.env.example`](./.env.example).
6. **Keep Fallbacks Working**: AI and external calls must always have a graceful deterministic fallback path.

---

## 2. Git & Branching Strategy

GitHub is our **single source of truth**. 

```text
main (Protected, always deployable, demo-ready)
  └── feature/laptop-X-<feature-name>
        └── Pull Request
              └── Review & Verification
                    └── Merge to main
```

### Branch Naming Convention
Branches must reflect the workstation and task:
- `feat/laptop1-ai-incident-classifier`
- `feat/laptop2-api-incidents-endpoint`
- `feat/laptop3-sample-data-pipeline`
- `feat/laptop4-interactive-map-view`
- `fix/laptop2-cors-headers`
- `docs/laptop3-api-contract-update`

### Direct Push Policy
- **Direct pushes to `main` are strictly forbidden.**
- All changes must pass through a Pull Request (PR) or fast peer-review by at least one other workstation lead.

---

## 3. Commit Guidelines

- **Keep Commits Small & Meaningful**: Avoid massive end-of-day commits. Commit each completed step (e.g., "Add incident schema validation", "Wire mock alert trigger").
- **Commit Message Format**:
  - `feat(<module>): brief description of new feature`
  - `fix(<module>): describe bug resolved`
  - `docs(<module>): describe documentation added or updated`
  - `refactor(<module>): describe code cleanup without behavior change`
  - `test(<module>): add or update automated/manual test suite`

---

## 4. Workstation Handoff Protocol

Each workstation owns a defined operational scope:
- **Laptop 1 (AI/ML)**: Works exclusively in `ai/` and interfaces with backend schemas.
- **Laptop 2 (Backend)**: Works in `backend/` and `database/`.
- **Laptop 3 (Supporting & Integration)**: Works in `data/`, `tests/`, `scripts/`, and project documentation.
- **Laptop 4 (Frontend & 3D)**: Works in `frontend/` and coordinates end-to-end user experience.

> **Caution**: Do not edit another workstation's primary folder without active verbal/written communication and approval.

---

## 5. Daily Sync & Check-In Milestones (36-Hour Timeline)

- **Hour 00 - 04**: Environment setup, contract alignment, mock data readiness.
- **Hour 04 - 12**: P0 backend endpoints up, basic React shell running, AI classification baseline running.
- **Hour 12 - 20**: P0 integration: Frontend talking to Backend, Backend querying AI/fallback, Map displaying incidents.
- **Hour 20 - 26**: First end-to-end dry run of the 90-second demo script.
- **Hour 26 - 32**: P1 feature integration (3D command view, crowd/traffic layers) ONLY IF P0 is 100% stable.
- **Hour 32 - 36**: Complete code freeze. Rehearsal of the demo presentation.
