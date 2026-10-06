from sqlalchemy.orm import Session

from app.models.zone import Zone


class ZoneRepository:
    def list(self, db: Session) -> list[Zone]:
        return db.query(Zone).order_by(Zone.zone_id).all()

    def get_by_id(self, db: Session, zone_id: str) -> Zone | None:
        return db.query(Zone).filter(Zone.zone_id == zone_id).first()
