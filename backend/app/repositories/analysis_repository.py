from sqlalchemy.orm import Session

from app.models.analysis import AIAnalysisResult


class AnalysisRepository:
    def create(self, db: Session, analysis: AIAnalysisResult) -> AIAnalysisResult:
        db.add(analysis)
        db.commit()
        db.refresh(analysis)
        return analysis
