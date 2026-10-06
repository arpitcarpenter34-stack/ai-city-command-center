from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.analysis import AnalysisRequest
from app.services.analysis_service import AnalysisService

router = APIRouter()


@router.post('/analysis')
def run_analysis(payload: AnalysisRequest, db: Session = Depends(get_db)):
    return AnalysisService().analyze_incident(db, payload)
