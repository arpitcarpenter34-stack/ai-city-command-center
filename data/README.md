# Data Management - AI City Command Center

> **Lead Workstation**: Laptop 3 (Data, Supporting & Integration Lead)  
> **Status**: Phase 0 Specification

---

## 1. Directory Structure & Organization

This directory manages all data artifacts utilized by the AI City Command Center across development, testing, and runtime:

```text
data/
├── raw/         # Unmodified synthetic input logs, raw sensor streams, raw incident text
├── processed/   # Cleaned, tokenized, or normalized data artifacts ready for inference
├── sample/      # Seed JSON fixtures used for local MVP baseline, testing, and UI mocks
└── README.md    # Data documentation and schema governance
```

---

## 2. Directory Policies & Boundaries

### 2.1 `data/raw/`
- Contains synthetic raw urban signals, multi-source telemetry logs, and test feeds.
- **Git Policy**: Large files or generated batches are ignored by `.gitignore`. Only `.gitkeep` and essential synthetic samples are committed.

### 2.2 `data/processed/`
- Stores cleaned and normalized data artifacts transformed by helper scripts in `scripts/`.
- Preserves pre-computed geographic bounding boxes, token dictionaries, or normalized municipal category mappings.

### 2.3 `data/sample/`
- **Critical Hackathon Asset**: Maintained directly by Laptop 3 to unblock Laptop 4 (Frontend) and Laptop 2 (Backend).
- Houses standard JSON fixtures representing valid incidents, zones, alerts, and response states conforming exactly to [`../docs/07-data-schema.md`](../docs/07-data-schema.md).
- Acts as the reliable fallback data source for local development and offline judge presentations.

---

## 3. Data Governance & Hackathon Rules
- **No Real PII or Confidential Data**: Use only synthetic or public municipal data.
- **Strict Schema Adherence**: Sample fixtures must strictly mirror the contracts defined in [`../docs/06-api-contract.md`](../docs/06-api-contract.md) and [`../docs/07-data-schema.md`](../docs/07-data-schema.md).
- **Zero Invented PS Requirements**: Data fields must remain confined to validated problem statement requirements.
