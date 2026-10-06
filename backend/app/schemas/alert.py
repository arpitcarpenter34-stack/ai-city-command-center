from datetime import datetime

from pydantic import BaseModel, Field


class AlertCreate(BaseModel):
    incident_id: str
    severity: str = Field(..., pattern='^(critical|high|medium)$')
    headline: str = Field(..., min_length=1, max_length=120)
    message: str = Field(..., min_length=1)


class AlertOut(BaseModel):
    alert_id: str
    incident_id: str
    severity: str
    headline: str
    message: str
    acknowledged: bool
    created_at: datetime


class AlertListResponse(BaseModel):
    active_alerts_count: int
    alerts: list[AlertOut]
