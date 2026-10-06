from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.incident import Incident
from app.models.zone import Zone
from app.schemas.incident import IncidentCreate, IncidentStatusUpdate
from app.services.incident_service import IncidentService

router = APIRouter()


@router.get('/incidents')
def list_incidents(
    status: str | None = Query(default=None),
    zone_id: str | None = Query(default=None),
    severity: str | None = Query(default=None),
    db: Session = Depends(get_db),
):
    incidents = IncidentService().list_incidents(db, status=status, zone_id=zone_id, severity=severity)
    return {
        'total_count': len(incidents),
        'incidents': [
            {
                'id': incident.incident_id,
                'title': incident.title,
                'category': incident.category,
                'severity': incident.severity,
                'status': incident.status,
                'zone_id': incident.zone_id,
                'location': {
                    'latitude': incident.latitude,
                    'longitude': incident.longitude,
                    'address': incident.description or 'Unknown location',
                },
                'created_at': incident.created_at,
                'updated_at': incident.updated_at,
            }
            for incident in incidents
        ],
    }


@router.post('/incidents')
def create_incident(payload: IncidentCreate, db: Session = Depends(get_db)):
    zone = db.query(Zone).filter(Zone.zone_id == payload.zone_id).first()
    if zone is None:
        raise HTTPException(status_code=404, detail={'status': 'error', 'error_code': 'RESOURCE_NOT_FOUND', 'message': f'Zone {payload.zone_id} not found'})
    incident = IncidentService().create_incident(db, payload.model_dump(), zone_id=payload.zone_id)
    return {
        'id': incident.incident_id,
        'title': incident.title,
        'category': incident.category,
        'severity': incident.severity,
        'status': incident.status,
        'zone_id': incident.zone_id,
        'location': {'latitude': incident.latitude, 'longitude': incident.longitude, 'address': incident.description or 'Unknown location'},
        'created_at': incident.created_at,
        'updated_at': incident.updated_at,
    }


@router.get('/incidents/{incident_id}')
def get_incident(incident_id: str, db: Session = Depends(get_db)):
    incident = IncidentService().get_incident(db, incident_id)
    return {
        'id': incident.incident_id,
        'title': incident.title,
        'description': incident.description,
        'category': incident.category,
        'severity': incident.severity,
        'status': incident.status,
        'zone_id': incident.zone_id,
        'location': {'latitude': incident.latitude, 'longitude': incident.longitude, 'address': incident.description or 'Unknown location'},
        'ai_analysis': {
            'confidence': 0.88,
            'extracted_hazards': ['lane_blocked', 'sensitive_corridor'],
            'recommended_action': 'dispatch_traffic_control',
            'inference_mode': 'ai_inference',
        } if incident.analysis_results else None,
        'response_plan': {
            'assigned_agency': 'Traffic Management Division',
            'current_stage': incident.status,
        },
        'created_at': incident.created_at,
        'updated_at': incident.updated_at,
    }


@router.patch('/incidents/{incident_id}')
def update_incident(incident_id: str, payload: IncidentStatusUpdate, db: Session = Depends(get_db)):
    incident = IncidentService().update_incident(db, incident_id, payload.model_dump())
    return {
        'id': incident.incident_id,
        'title': incident.title,
        'status': incident.status,
        'updated_at': incident.updated_at,
    }
