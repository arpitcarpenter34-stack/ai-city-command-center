from pydantic import BaseModel, Field


class AnalysisMetrics(BaseModel):
    density_indicator: str | None = None


class AnalysisRequest(BaseModel):
    raw_text: str = Field(..., min_length=1)
    source_type: str = Field(..., pattern='^(sensor_feed|sensor_stream|citizen_report|camera_feed|manual_operator)$')
    zone_id: str
    metrics: AnalysisMetrics = Field(default_factory=AnalysisMetrics)


class AnalysisResponse(BaseModel):
    detected: bool
    suggested_category: str
    confidence_score: float = Field(..., ge=0.0, le=1.0)
    hazard_flags: list[str]
    computed_severity: str
    recommended_action: str
    inference_mode: str
