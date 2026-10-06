# Automation & Utility Scripts - AI City Command Center

> **Lead Workstation**: Laptop 3 (Supporting & Quality Lead)  
> **Status**: Phase 0 Specification

---

## 1. Overview & Purpose

The `scripts/` directory hosts lightweight developer utilities and automation scripts designed to accelerate testing, data seeding, and environment verification during the 36-hour hackathon.

---

## 2. Planned Utility Scripts

During Phase 1 and Phase 2, the following standalone scripts may be introduced:

1. **`generate_sample_data.py`**:
   - Generates and refreshes realistic synthetic incident fixtures in `data/sample/`.
   - Ensures mock datasets strictly follow the schemas in `docs/07-data-schema.md`.

2. **`verify_environment.py` / `verify_environment.sh`**:
   - Performs pre-flight verification on developer workstations (Python version, Node version, environment variables present in `.env`).

3. **`run_mock_server.py`**:
   - Starts a lightweight static HTTP mock server serving endpoints from `data/sample/` to unblock Laptop 4 if backend integration is delayed.

---

## 3. Engineering Guidelines
- **Zero Bloat**: Scripts should rely only on standard Python / Node library tools where possible.
- **Non-Destructive**: Never author scripts that purge uncommitted local files or mutate production resources.
- **Documented Execution**: Every script added must include header comments detailing usage and expected arguments.
