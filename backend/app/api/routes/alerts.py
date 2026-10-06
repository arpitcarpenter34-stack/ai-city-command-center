from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.alert import AlertCreate, AlertListResponse
from app.services.alert_service import AlertService

router = APIRouter()


@router.get('/alerts')
def list_alerts(acknowledged: bool | None = Query(default=None), db: Session = Depends(get_db)):
    alerts = AlertService().list_alerts(db, acknowledged=acknowledged)
    return {
        'active_alerts_count': len(alerts),
        'alerts': [
            {
                'alert_id': alert.alert_id,
                'incident_id': alert.incident_id,
                'severity': alert.severity,
                'headline': alert.headline,
                'message': alert.message,
                'acknowledged': alert.is_acknowledged,
                'created_at': alert.triggered_at,
            }
            for alert in alerts
        ],
    }


@router.post('/alerts')
def create_alert(payload: AlertCreate, db: Session = Depends(get_db)):
    alert = AlertService().create_alert(db, payload.model_dump())
    return {
        'alert_id': alert.alert_id,
        'incident_id': alert.incident_id,
        'severity': alert.severity,
        'headline': alert.headline,
        'message': alert.message,
        'acknowledged': alert.is_acknowledged,
        'created_at': alert.triggered_at,
    }
