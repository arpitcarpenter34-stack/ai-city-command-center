# Document 06: Conceptual API Contract Specification

> **Project**: AI City Command Center  
> **Status**: Specification Only (Do NOT implement yet)  
> **Lead Owners**: Laptop 2 (Backend) & Laptop 4 (Frontend)

---

## 1. Overview & General Standards

This document establishes the conceptual REST API contract connecting the Frontend (`frontend/`), Backend (`backend/`), and AI subsystem (`ai/`). All implementations should follow these conceptual models to enable independent parallel development across workstations.

### General Conventions
- All response bodies use standardized `application/json`.
- All timestamps follow ISO-8601 UTC format (`YYYY-MM-DDTHH:MM:SSZ`).
- **Base Routing Prefix**: The final URL prefix (such as `/api` or `/api/v1`) is an **implementation detail to be decided during backend setup**. Endpoints below are documented conceptually from root.
- Error responses follow a uniform structure:
  ```json
  {
    "status": "error",
    "error_code": "RESOURCE_NOT_FOUND",
    "message": "Detailed description of error condition"
  }
  ```

---

## 2. Conceptual Endpoints

---

### Endpoint 1: Health & System Status
- **Path**: `/health`
- **Method**: `GET`
- **Owner**: Laptop 2 (Backend)
- **Purpose**: Verifies backend availability, AI engine status, and data storage accessibility.
- **Request Parameters / Body**: None.
- **Expected Response (`200 OK`)**:
  ```json
  {
    "status": "healthy",
    "timestamp": "2026-10-06T07:18:00Z",
    "subsystems": {
      "backend": "online",
      "ai_engine": "available",
      "data_layer": "ready"
    }
  }
  ```

---

### Endpoint 2: List Incidents
- **Path**: `/incidents`
- **Method**: `GET`
- **Owner**: Laptop 2 (Backend)
- **Purpose**: Retrieves a collection of active and recent urban incidents for display on the command overview and interactive map.
- **Request Parameters (Optional Query Filters)**:
  - `status` *(e.g., `detected`, `investigating`, `dispatched`, `in_progress`, `resolved`)*
  - `zone_id` *(e.g., `ZONE-01`)*
  - `severity` *(e.g., `critical`, `high`, `medium`, `low`)*
- **Expected Response (`200 OK`)**:
  ```json
  {
    "total_count": 2,
    "incidents": [
      {
        "id": "INC-001",
        "title": "Road Blockage and Collision",
        "category": "traffic_collision",
        "severity": "critical",
        "status": "investigating",
        "zone_id": "ZONE-03",
        "location": {
          "latitude": 28.6139,
          "longitude": 77.2090,
          "address": "Expressway Corridor"
        },
        "created_at": "2026-10-06T07:10:00Z",
        "updated_at": "2026-10-06T07:15:00Z"
      },
      {
        "id": "INC-002",
        "title": "Water Main Rupture",
        "category": "utility_failure",
        "severity": "medium",
        "status": "detected",
        "zone_id": "ZONE-01",
        "location": {
          "latitude": 28.6250,
          "longitude": 77.2150,
          "address": "Commercial District North"
        },
        "created_at": "2026-10-06T07:05:00Z",
        "updated_at": "2026-10-06T07:05:00Z"
      }
    ]
  }
  ```

---

### Endpoint 3: Incident Details
- **Path**: `/incidents/{id}`
- **Method**: `GET`
- **Owner**: Laptop 2 (Backend)
- **Purpose**: Fetches complete contextual details, associated AI analysis metrics, and dispatch timeline for an individual incident.
- **Request Parameters**:
  - `id` *(path parameter)*
- **Expected Response (`200 OK`)**:
  ```json
  {
    "id": "INC-001",
    "title": "Road Blockage and Collision",
    "description": "Multi-vehicle incident blocking lanes in a high-priority corridor.",
    "category": "traffic_collision",
    "severity": "critical",
    "status": "investigating",
    "zone_id": "ZONE-03",
    "location": {
      "latitude": 28.6139,
      "longitude": 77.2090,
      "address": "Expressway Corridor"
    },
    "ai_analysis": {
      "confidence": 0.88,
      "extracted_hazards": ["lane_blocked", "sensitive_corridor"],
      "recommended_action": "dispatch_traffic_control",
      "inference_mode": "ai_inference"
    },
    "response_plan": {
      "assigned_agency": "Traffic Management Division",
      "current_stage": "investigating"
    },
    "created_at": "2026-10-06T07:10:00Z",
    "updated_at": "2026-10-06T07:15:00Z"
  }
  ```

---

### Endpoint 4: Run AI Incident Analysis
- **Path**: `/analysis`
- **Method**: `POST`
- **Owner**: Laptop 1 (AI) & Laptop 2 (Backend)
- **Purpose**: Evaluates unclassified urban telemetry or incident descriptions, invoking the AI intelligence pipeline (or rule-based fallback) to classify the incident and suggest response priorities.
- **Expected Request Body**:
  ```json
  {
    "raw_text": "Pedestrian congestion surge reported near Stadium Plaza",
    "source_type": "sensor_feed",
    "zone_id": "ZONE-05",
    "metrics": {
      "density_indicator": "high"
    }
  }
  ```
- **Expected Response (`200 OK`)**:
  ```json
  {
    "detected": true,
    "suggested_category": "crowd_surge",
    "confidence_score": 0.87,
    "hazard_flags": ["high_density_zone"],
    "computed_severity": "critical",
    "recommended_action": "deploy_crowd_management",
    "inference_mode": "ai_inference"
  }
  ```

---

### Endpoint 5: Active Alerts
- **Path**: `/alerts`
- **Method**: `GET`
- **Owner**: Laptop 2 (Backend)
- **Purpose**: Provides a prioritized list of high-urgency notifications requiring operator intervention.
- **Request Parameters**:
  - `acknowledged` *(optional boolean query filter)*
- **Expected Response (`200 OK`)**:
  ```json
  {
    "active_alerts_count": 1,
    "alerts": [
      {
        "alert_id": "ALT-001",
        "incident_id": "INC-001",
        "severity": "critical",
        "headline": "CRITICAL HAZARD: Lane Blocked on Central Expressway",
        "message": "Immediate traffic coordination required.",
        "acknowledged": false,
        "created_at": "2026-10-06T07:10:05Z"
      }
    ]
  }
  ```

---

### Endpoint 6: City Operational Zones
- **Path**: `/zones`
- **Method**: `GET`
- **Owner**: Laptop 2 (Backend)
- **Purpose**: Delivers geographic zone metadata, coordinates, and current operational zone status for map visualization.
- **Request Parameters / Body**: None.
- **Expected Response (`200 OK`)**:
  ```json
  {
    "zones": [
      {
        "zone_id": "ZONE-01",
        "name": "Commercial District",
        "criticality_weight": 0.6,
        "status": "normal",
        "active_incidents": 1,
        "center_coordinates": {
          "latitude": 28.6250,
          "longitude": 77.2150
        }
      },
      {
        "zone_id": "ZONE-03",
        "name": "Central Transit Corridor",
        "criticality_weight": 0.9,
        "status": "elevated_alert",
        "active_incidents": 1,
        "center_coordinates": {
          "latitude": 28.6139,
          "longitude": 77.2090
        }
      }
    ]
  }
  ```

---

### Endpoint 7: Update Incident Response Status
- **Path**: `/incidents/{id}/response`
- **Method**: `PATCH`
- **Owner**: Laptop 2 (Backend)
- **Purpose**: Updates the operational dispatch stage of an incident as emergency teams respond and resolve the situation.
- **Request Parameters**:
  - `id` *(path parameter)*
- **Expected Request Body**:
  ```json
  {
    "status": "dispatched",
    "action_note": "Response team dispatched to secure intersection",
    "assigned_unit": "Unit-04"
  }
  ```
- **Expected Response (`200 OK`)**:
  ```json
  {
    "incident_id": "INC-001",
    "previous_status": "investigating",
    "current_status": "dispatched",
    "assigned_unit": "Unit-04",
    "updated_at": "2026-10-06T07:16:30Z"
  }
  ```
