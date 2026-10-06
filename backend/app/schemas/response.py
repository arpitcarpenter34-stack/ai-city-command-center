from datetime import datetime

from pydantic import BaseModel, Field


class ResponseAdd(BaseModel):
    status: str = Field(..., pattern='^(investigating|dispatched|in_progress|resolved)$')
    action_note: str | None = None
    assigned_unit: str | None = None


class ResponseOut(BaseModel):
    incident_id: str
    previous_status: str
    current_status: str
    assigned_unit: str | None = None
    updated_at: datetime
