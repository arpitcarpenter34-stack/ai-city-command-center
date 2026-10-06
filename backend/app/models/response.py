from datetime import datetime, timezone

from sqlalchemy import DateTime, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class ResponseLog(Base):
    __tablename__ = 'response_logs'

    response_id: Mapped[str] = mapped_column(String(64), primary_key=True, index=True)
    incident_id: Mapped[str] = mapped_column(String(64), ForeignKey('incidents.incident_id'), nullable=False, index=True)
    stage: Mapped[str] = mapped_column(String(30), nullable=False)
    assigned_agency: Mapped[str | None] = mapped_column(String(120), nullable=True)
    assigned_unit: Mapped[str | None] = mapped_column(String(120), nullable=True)
    action_note: Mapped[str | None] = mapped_column(Text, nullable=True)
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    incident = relationship('Incident', back_populates='responses')
