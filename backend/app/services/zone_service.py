from sqlalchemy.orm import Session

from app.models.zone import Zone
from app.repositories.zone_repository import ZoneRepository


class ZoneService:
    def __init__(self, repository: ZoneRepository | None = None):
        self.repository = repository or ZoneRepository()

    def list_zones(self, db: Session) -> list[Zone]:
        return self.repository.list(db)
