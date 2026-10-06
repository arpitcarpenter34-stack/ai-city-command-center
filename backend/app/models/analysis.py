from datetime import datetime, timezone

from sqlalchemy import DateTime, Float, ForeignKey, JSON, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class AIAnalysisResult(Base):
    __tablename__ = 'ai_analysis_results'

    analysis_id: Mapped[str] = mapped_column(String(64), primary_key=True, index=True)
    incident_id: Mapped[str] = mapped_column(String(64), ForeignKey('incidents.incident_id'), nullable=False, index=True)
    detected: Mapped[bool] = mapped_column(nullable=False)
    suggested_category: Mapped[str] = mapped_column(String(50), nullable=False)
    confidence_score: Mapped[float] = mapped_column(Float, nullable=False)
    hazard_features: Mapped[dict] = mapped_column(JSON, nullable=True)
    recommended_action: Mapped[str] = mapped_column(String(120), nullable=False)
    inference_mode: Mapped[str] = mapped_column(String(40), nullable=False)
    latency_ms: Mapped[float] = mapped_column(Float, nullable=False)
    analyzed_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    incident = relationship('Incident', back_populates='analysis_results')
