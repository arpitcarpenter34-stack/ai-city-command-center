from datetime import datetime, timezone

from sqlalchemy.orm import Session

from app.core.exceptions import ResourceNotFoundError
from app.models.incident import Incident
from app.repositories.incident_repository import IncidentRepository
from app.services.severity_service import SeverityService


class IncidentService:
    def __init__(self, repository: IncidentRepository | None = None, severity_service: SeverityService | None = None):
        self.repository = repository or IncidentRepository()
        self.severity_service = severity_service or SeverityService()

    def list_incidents(self, db: Session, status: str | None = None, zone_id: str | None = None, severity: str | None = None) -> list[Incident]:
        return self.repository.list(db, status=status, zone_id=zone_id, severity=severity)

    def get_incident(self, db: Session, incident_id: str) -> Incident:
        incident = self.repository.get_by_id(db, incident_id)
        if incident is None:
            raise ResourceNotFoundError(f'Incident {incident_id} not found')
        return incident

    def create_incident(self, db: Session, payload: dict, zone_id: str | None = None) -> Incident:
        zone_ref = zone_id or payload.get('zone_id')
        if not zone_ref:
            raise ResourceNotFoundError('Zone identifier missing for incident')
        last = db.query(Incident).order_by(Incident.incident_id.desc()).first()
        number = 1
        if last and last.incident_id.startswith('INC-'):
            try:
                number = int(last.incident_id.split('-')[-1]) + 1
            except ValueError:
                number = 1

        incident = Incident(
            incident_id=f'INC-{number:04d}',
            zone_id=zone_ref,
            title=payload['title'],
            description=payload.get('description'),
            category=payload['category'],
            severity=payload.get('severity') or self.severity_service.compute(payload['category'], payload.get('density_indicator'), None),
            status=payload.get('status', 'detected'),
            latitude=payload['location']['latitude'],
            longitude=payload['location']['longitude'],
            source_type=payload.get('source_type', 'manual_operator'),
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
        )
        return self.repository.create(db, incident)

    def update_incident(self, db: Session, incident_id: str, payload: dict) -> Incident:
        incident = self.get_incident(db, incident_id)
        for key, value in payload.items():
            if key == 'status':
                incident.status = value
            elif key == 'severity':
                incident.severity = value
            elif key == 'title':
                incident.title = value
            elif key == 'description':
                incident.description = value
            elif key == 'category':
                incident.category = value
            elif key == 'zone_id':
                incident.zone_id = value
            elif key == 'source_type':
                incident.source_type = value
            elif key == 'location':
                incident.latitude = value['latitude']
                incident.longitude = value['longitude']
        incident.updated_at = datetime.now(timezone.utc)
        return self.repository.update(db, incident)
