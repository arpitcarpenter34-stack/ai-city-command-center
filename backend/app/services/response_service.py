from datetime import datetime, timezone

from sqlalchemy.orm import Session

from app.models.response import ResponseLog
from app.repositories.response_repository import ResponseRepository


class ResponseService:
    def __init__(self, repository: ResponseRepository | None = None):
        self.repository = repository or ResponseRepository()

    def create_response(self, db: Session, incident_id: str, payload: dict) -> ResponseLog:
        response_log = ResponseLog(
            response_id=f"RSP-{datetime.now(timezone.utc).strftime('%Y%m%d%H%M%S')}",
            incident_id=incident_id,
            stage=payload['status'],
            assigned_agency='Municipal Operations',
            assigned_unit=payload.get('assigned_unit'),
            action_note=payload.get('action_note'),
            timestamp=datetime.now(timezone.utc),
        )
        return self.repository.create(db, response_log)
