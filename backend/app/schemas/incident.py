from datetime import datetime

from pydantic import BaseModel, Field


class IncLocation(BaseModel):
    latitude: float = Field(..., ge=-90.0, le=90.0)
    longitude: float = Field(..., ge=-180.0, le=180.0)
    address: str | None = None


class IncidentCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=150)
    description: str | None = None
    category: str = Field(..., pattern='^(traffic_collision|road_hazard|crowd_surge|fire_emergency|utility_failure|unclassified)$')
    severity: str = Field(..., pattern='^(low|medium|high|critical)$')
    status: str = Field(default='detected', pattern='^(detected|investigating|dispatched|in_progress|resolved)$')
    zone_id: str
    location: IncLocation
    source_type: str = Field(default='manual_operator', pattern='^(sensor_feed|sensor_stream|citizen_report|camera_feed|manual_operator)$')


class IncidentOut(BaseModel):
    id: str
    title: str
    description: str | None = None
    category: str
    severity: str
    status: str
    zone_id: str | None = None
    location: IncLocation
    ai_analysis: dict | None = None
    response_plan: dict | None = None
    created_at: datetime
    updated_at: datetime


class IncidentListItem(BaseModel):
    id: str
    title: str
    category: str
    severity: str
    status: str
    zone_id: str | None = None
    location: IncLocation
    created_at: datetime
    updated_at: datetime


class IncidentListResponse(BaseModel):
    total_count: int
    incidents: list[IncidentListItem]


class IncidentStatusUpdate(BaseModel):
    status: str = Field(..., pattern='^(investigating|dispatched|in_progress|resolved)$')
    action_note: str | None = None
    assigned_unit: str | None = None
