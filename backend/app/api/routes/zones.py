from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.services.zone_service import ZoneService

router = APIRouter()


@router.get('/zones')
def list_zones(db: Session = Depends(get_db)):
    zones = ZoneService().list_zones(db)
    return {
        'zones': [
            {
                'zone_id': zone.zone_id,
                'name': zone.name,
                'criticality_weight': zone.criticality_weight,
                'status': zone.status,
                'active_incidents': len(zone.incidents),
                'center_coordinates': {
                    'latitude': zone.center_latitude,
                    'longitude': zone.center_longitude,
                },
            }
            for zone in zones
        ]
    }
