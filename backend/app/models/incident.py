from datetime import datetime, timezone

from sqlalchemy import CheckConstraint, DateTime, Float, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class Incident(Base):
    __tablename__ = 'incidents'
    __table_args__ = (
        CheckConstraint('latitude BETWEEN -90 AND 90', name='incident_lat_range'),
        CheckConstraint('longitude BETWEEN -180 AND 180', name='incident_lon_range'),
    )

    incident_id: Mapped[str] = mapped_column(String(64), primary_key=True, index=True)
    zone_id: Mapped[str | None] = mapped_column(String(40), ForeignKey('zones.zone_id'), nullable=True, index=True)
    title: Mapped[str] = mapped_column(String(150), nullable=False)
    description: Mapped[str | None] = mapped_column(String, nullable=True)
    category: Mapped[str] = mapped_column(String(50), nullable=False)
    severity: Mapped[str] = mapped_column(String(20), nullable=False)
    status: Mapped[str] = mapped_column(String(30), nullable=False, default='detected')
    latitude: Mapped[float] = mapped_column(Float, nullable=False)
    longitude: Mapped[float] = mapped_column(Float, nullable=False)
    source_type: Mapped[str] = mapped_column(String(40), nullable=False, default='manual_operator')
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)

    zone = relationship('Zone', back_populates='incidents')
    analysis_results = relationship('AIAnalysisResult', back_populates='incident', cascade='all, delete-orphan')
    alerts = relationship('Alert', back_populates='incident', cascade='all, delete-orphan')
    responses = relationship('ResponseLog', back_populates='incident', cascade='all, delete-orphan')
