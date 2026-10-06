from sqlalchemy.orm import Session

from app.models.incident import Incident


class IncidentRepository:
    def list(self, db: Session, status: str | None = None, zone_id: str | None = None, severity: str | None = None) -> list[Incident]:
        query = db.query(Incident)
        if status:
            query = query.filter(Incident.status == status)
        if zone_id:
            query = query.filter(Incident.zone_id == zone_id)
        if severity:
            query = query.filter(Incident.severity == severity)
        return query.order_by(Incident.created_at.desc()).all()

    def get_by_id(self, db: Session, incident_id: str) -> Incident | None:
        return db.query(Incident).filter(Incident.incident_id == incident_id).first()

    def create(self, db: Session, incident: Incident) -> Incident:
        db.add(incident)
        db.commit()
        db.refresh(incident)
        return incident

    def update(self, db: Session, incident: Incident) -> Incident:
        db.add(incident)
        db.commit()
        db.refresh(incident)
        return incident
