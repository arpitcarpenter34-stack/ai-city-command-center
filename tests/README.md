# Testing Strategy - AI City Command Center

> **Lead Workstation**: Laptop 3 (Testing & Supporting Lead)  
> **Status**: Phase 0 Specification (Test Harnesses Defined)

---

## 1. Overview & Quality Mandate

In a rapid 36-hour hackathon, testing protects the **P0 demo flow** from regression. Each workstation maintains tests within their dedicated test directory.

```text
tests/
├── frontend/    # Component render checks, user flow tests, mock contract validations
├── backend/     # Endpoint tests, schema validation, severity calculation tests
├── ai/          # Inference pipeline benchmarks, schema conformity, fallback validation
└── README.md    # Testing philosophy and execution protocols
```

---

## 2. Directory Test Scopes

### 2.1 `tests/frontend/` (Laptop 4 & Laptop 3)
- Validates that UI components render correctly without uncaught runtime errors.
- Verifies that mock API responses from `data/sample/` render active incident pins and alert modals.
- Ensures the 2D map view functions properly if 3D rendering is toggled off.

### 2.2 `tests/backend/` (Laptop 2 & Laptop 3)
- Validates backend routes using automated test harnesses.
- Tests the deterministic fallback logic when the AI module is simulated as unavailable or timing out.
- Verifies hybrid severity scoring calculations against boundary condition test vectors.

### 2.3 `tests/ai/` (Laptop 1 & Laptop 3)
- Evaluates candidate models on classification consistency and responsiveness.
- Tests that model outputs strictly match the output schema in `docs/04-ai-strategy.md`.
- Verifies that the simplified rule-based fallback workflow reliably returns valid categories and hazard features.

---

## 3. Pull Request Testing Rule

As defined in [`../docs/10-development-rules.md`](../docs/10-development-rules.md):
- Before merging any branch into `main`, relevant module tests must pass locally.
- Unverified code that breaks the approximately 90-second demo path will be reverted immediately.
