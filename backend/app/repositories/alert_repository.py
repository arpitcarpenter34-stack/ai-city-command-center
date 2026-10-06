from sqlalchemy.orm import Session

from app.models.alert import Alert


class AlertRepository:
    def list(self, db: Session, acknowledged: bool | None = None) -> list[Alert]:
        query = db.query(Alert)
        if acknowledged is not None:
            query = query.filter(Alert.is_acknowledged == acknowledged)
        return query.order_by(Alert.triggered_at.desc()).all()

    def create(self, db: Session, alert: Alert) -> Alert:
        db.add(alert)
        db.commit()
        db.refresh(alert)
        return alert
