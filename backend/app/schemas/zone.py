from pydantic import BaseModel, Field


class ZoneCenter(BaseModel):
    latitude: float = Field(..., ge=-90.0, le=90.0)
    longitude: float = Field(..., ge=-180.0, le=180.0)


class ZoneOut(BaseModel):
    zone_id: str
    name: str
    district: str
    criticality_weight: float = Field(..., ge=0.0, le=1.0)
    status: str
    center_coordinates: ZoneCenter


class ZoneListResponse(BaseModel):
    zones: list[ZoneOut]
