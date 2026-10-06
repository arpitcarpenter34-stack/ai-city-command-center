# AI & Machine Learning Subsystem - AI City Command Center

> **Lead Workstation**: Laptop 1 (AI/ML Lead)  
> **Status**: Phase 0 Specification (Model Evaluation Pending)  
> **Model Status**: **DECISION PENDING / NOT YET LOCKED**

---

## 1. Overview & Objectives

The AI subsystem delivers automated urban incident intelligence for the command center. It evaluates incoming unstructured reports and telemetry signals to detect anomalies, classify incident types, extract hazard indicators, and inform the hybrid severity engine.

### Operational Principles
- **Core Intelligence**: AI provides genuine urban incident intelligence—not cosmetic decoration.
- **Support Authority Decision-Making**: AI provides decision support while city authorities maintain ultimate operational oversight.
- **Pretrained & Local Inference Preferred**: Training deep learning models from scratch is excluded. The strategy prioritizes pretrained models and local inference where feasible.
- **LLM Positioning**: A Large Language Model (LLM) is **optional and is NOT required for P0**.
- **Resilient Fallback**: A simplified, deterministic rule-based workflow using controlled local validated data must always be ready to operate if the AI pipeline is unavailable.

---

## 2. Model Selection Guidelines

> ### ⚠️ ARCHITECTURAL DIRECTIVE: MODEL CHOICE IS NOT LOCKED
> **Exact AI model will be selected after a local proof-of-concept.**  
> Do NOT invent or hard-code a specific model choice at this stage.

### Evaluated Model Categories (Local POC Phase)
- **Lightweight Pretrained Classifier**: Fast local models for text classification and incident categorization.
- **Embedding-Based Classifier**: Vector embedding matching for mapping incident descriptions to municipal taxonomy.
- **Lightweight Pretrained Computer Vision Model**: Evaluated for P1 image/crowd feed analysis if visual telemetry is activated.
- **Rule-Assisted Intelligence**: Keyword and heuristic logic providing deterministic feature extraction and fallback.
- **Optional Language Model**: Evaluated as an optional enhancement; explicitly not required for P0.

---

## 3. Workstation Mandate & Boundaries

> ### 🛑 PHASE 0 NOTICE
> **Do NOT build application or model code yet.**  
> **Do NOT install random dependencies yet.**  
> Implementation begins during Phase 1 following verified project initialization.

### Key Responsibilities for Laptop 1
1. Evaluate candidate models based on qualitative operational criteria (classification quality, consistency, responsiveness, local feasibility, stability).
2. Author the deterministic fallback workflow utilizing controlled local validated data.
3. Expose a clean, standardized Python interface for the backend service:
   ```python
   def analyze_incident(payload: dict) -> dict:
       ...
   ```
4. Support the hybrid severity calculation by providing detected features and confidence ratings.
5. Author automated tests in `tests/ai/` validating input/output schemas and fallback reliability.

---

## 4. Failure Handling & Fallback Workflow

If the AI module encounters an error or exceeds the configured timeout threshold:
- The system automatically transitions to the simplified rule-based workflow.
- Pre-validated local fixtures in `data/sample/` supply consistent fallback intelligence.
- The command center experiences zero downtime or unhandled exceptions.
