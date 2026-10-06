from datetime import datetime, timezone

from sqlalchemy import Boolean, DateTime, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class Alert(Base):
    __tablename__ = 'alerts'

    alert_id: Mapped[str] = mapped_column(String(64), primary_key=True, index=True)
    incident_id: Mapped[str] = mapped_column(String(64), ForeignKey('incidents.incident_id'), nullable=False, index=True)
    severity: Mapped[str] = mapped_column(String(20), nullable=False)
    headline: Mapped[str] = mapped_column(String(120), nullable=False)
    message: Mapped[str] = mapped_column(Text, nullable=False)
    is_acknowledged: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    triggered_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    incident = relationship('Incident', back_populates='alerts')
