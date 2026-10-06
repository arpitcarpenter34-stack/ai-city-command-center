from datetime import datetime, timezone

from sqlalchemy.orm import Session

from app.models.alert import Alert
from app.repositories.alert_repository import AlertRepository


class AlertService:
    def __init__(self, repository: AlertRepository | None = None):
        self.repository = repository or AlertRepository()

    def list_alerts(self, db: Session, acknowledged: bool | None = None) -> list[Alert]:
        return self.repository.list(db, acknowledged=acknowledged)

    def create_alert(self, db: Session, payload: dict) -> Alert:
        alert = Alert(
            alert_id=f"ALT-{datetime.now(timezone.utc).strftime('%Y%m%d%H%M%S')}",
            incident_id=payload['incident_id'],
            severity=payload['severity'],
            headline=payload['headline'],
            message=payload['message'],
            is_acknowledged=False,
            triggered_at=datetime.now(timezone.utc),
        )
        return self.repository.create(db, alert)
