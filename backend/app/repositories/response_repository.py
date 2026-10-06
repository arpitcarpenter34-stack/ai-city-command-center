from sqlalchemy.orm import Session

from app.models.response import ResponseLog


class ResponseRepository:
    def create(self, db: Session, response_log: ResponseLog) -> ResponseLog:
        db.add(response_log)
        db.commit()
        db.refresh(response_log)
        return response_log
