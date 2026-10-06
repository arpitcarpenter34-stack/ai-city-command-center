from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.incident import Incident
from app.schemas.response import ResponseAdd
from app.services.response_service import ResponseService

router = APIRouter()


@router.patch('/incidents/{incident_id}/response')
@router.post('/incidents/{incident_id}/response')
def update_response(incident_id: str, payload: ResponseAdd, db: Session = Depends(get_db)):
    incident = db.query(Incident).filter(Incident.incident_id == incident_id).first()
    if not incident:
        raise HTTPException(status_code=404, detail={'status': 'error', 'error_code': 'RESOURCE_NOT_FOUND', 'message': f'Incident {incident_id} not found'})
    previous_status = incident.status
    incident.status = payload.status
    incident.updated_at = datetime.now()
    db.commit()
    response_log = ResponseService().create_response(db, incident_id, payload.model_dump())
    return {
        'incident_id': incident_id,
        'previous_status': previous_status,
        'current_status': payload.status,
        'assigned_unit': payload.assigned_unit,
        'updated_at': incident.updated_at,
        'response_id': response_log.response_id,
    }
