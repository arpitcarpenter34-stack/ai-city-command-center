from sqlalchemy import Float, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class Zone(Base):
    __tablename__ = 'zones'

    zone_id: Mapped[str] = mapped_column(String(40), primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    district: Mapped[str] = mapped_column(String(120), nullable=False)
    criticality_weight: Mapped[float] = mapped_column(Float, nullable=False)
    status: Mapped[str] = mapped_column(String(50), default='normal', nullable=False)
    center_latitude: Mapped[float] = mapped_column(Float, nullable=False)
    center_longitude: Mapped[float] = mapped_column(Float, nullable=False)

    incidents = relationship('Incident', back_populates='zone')
