# Frontend Service - AI City Command Center

> **Lead Workstation**: Laptop 4 (Frontend & 3D Experience Lead)  
> **Status**: Phase 0 Specification (Implementation NOT started)

---

## 1. Overview & Technology Stack

The frontend client serves as the operational console for city authorities, providing unified situational awareness, geospatial incident display, and one-click response dispatch.

### Planned Architecture & Technologies
- **Core Framework**: React with [Vite](https://vitejs.dev/) for fast local development.
- **Styling & Motion**: Modern styling paired with [Framer Motion](https://www.framer.com/motion/) (`motion`) for layout transitions and alert indicators.
- **3D Command Visualization (P1 Stretch)**:
  - [Three.js](https://threejs.org/)
  - [React Three Fiber](https://docs.pmnd.rs/react-three-fiber/) (`@react-three/fiber`)
  - [Drei](https://github.com/pmndrs/drei) (`@react-three/drei`)
  - Provides a stylized 3D command center perspective with a seamless toggle to the 2D view.
- **Interactive Map Direction**:
  - **MapLibre GL JS** is the current planned map direction; exact implementation details remain subject to POC and integration feasibility.
- **Communication Layer**: REST client fetching from Backend endpoints using client-side polling. Polling interval is configurable in the client environment.

---

## 2. Workstation Mandate & Boundaries

> ### 🛑 PHASE 0 NOTICE
> **Do NOT build the application yet.**  
> **Do NOT install dependencies yet.**  
> Scaffolding and component implementation begin in Phase 1.

### Key Responsibilities for Laptop 4
1. Build the central command dashboard overview (active incidents, status cards, zone overview).
2. Render active incidents on the interactive map (MapLibre GL JS planned direction) with priority markers.
3. Construct the incident detail modal displaying AI analysis, extracted hazards, and suggested response actions.
4. Implement the response dispatch interface with status tracking (`Detected` $\rightarrow$ `Resolved`).
5. Develop the P1 3D animated command environment with seamless toggle to 2D view.
6. Conduct integration testing and lead the approximately 90-second judge demonstration.

---

## 3. Contract Integration

- **API Specification**: See [`../docs/06-api-contract.md`](../docs/06-api-contract.md). Routing prefix will be confirmed during backend setup.
- **Data Models**: See [`../docs/07-data-schema.md`](../docs/07-data-schema.md).
- **Mock Data**: Use sample JSON fixtures in `../data/sample/` for component prototyping before live endpoints are connected.
