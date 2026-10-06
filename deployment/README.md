# Deployment & Execution Strategy - AI City Command Center

> **Status**: Phase 0 Specification (NO infrastructure provisioned yet)  
> **Hackathon Priority**: Local Host Resilience First

---

## 1. Hackathon Execution Policy

> ### 🛑 PHASE 0 NOTICE
> **Do NOT create Docker files or container orchestrations yet.**  
> **Do NOT create cloud deployment infrastructure yet.**  
> For the 36-hour hackathon, stability and local zero-latency demonstration are paramount.

---

## 2. Hackathon Target Environment (Local Native)

To ensure zero risk from venue Wi-Fi congestion, cloud rate limits, or build delays, the presentation environment runs locally across workstations:

| Component | Target Host / Port | Execution Command (Phase 1) |
| :--- | :--- | :--- |
| **Frontend UI** | `http://localhost:5173` | `npm run dev` (Vite) |
| **Backend API** | `http://localhost:8000` | `uvicorn main:app --reload` (FastAPI) |
| **AI Inference** | Local Python Module | Integrated within Python backend service |
| **Data Layer** | Local Validated Seed Data | Loaded from `data/sample/` |

---

## 3. Future Deployment Vision (P3 Roadmap)

As part of the long-term P3 enterprise roadmap (out of scope for the hackathon MVP):
- Containerization for standardized municipal deployment.
- Multi-city enterprise hosting and scalability.
- Edge deployment for localized hardware and camera sensor nodes.

Detailed production architecture decisions will be evaluated post-hackathon based on actual municipal infrastructure requirements.
