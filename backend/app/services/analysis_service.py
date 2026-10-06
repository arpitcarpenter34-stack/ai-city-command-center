from datetime import datetime, timezone

from sqlalchemy.orm import Session

from app.core.logging import get_logger
from app.fallback.rule_engine import RuleBasedFallback
from app.integrations.ai_client import AIClient
from app.repositories.analysis_repository import AnalysisRepository
from app.schemas.analysis import AnalysisRequest
from app.models.analysis import AIAnalysisResult
from app.services.severity_service import SeverityService

logger = get_logger(__name__)


class AnalysisService:
    def __init__(
        self,
        repository: AnalysisRepository | None = None,
        ai_client: AIClient | None = None,
        fallback: RuleBasedFallback | None = None,
        severity_service: SeverityService | None = None,
    ):
        self.repository = repository or AnalysisRepository()
        self.ai_client = ai_client or AIClient()
        self.fallback = fallback or RuleBasedFallback()
        self.severity_service = severity_service or SeverityService()

    def analyze_incident(self, db: Session, payload: AnalysisRequest) -> dict:
        request = {'raw_text': payload.raw_text, 'source_type': payload.source_type, 'zone_id': payload.zone_id, 'metrics': payload.metrics.model_dump()}
        try:
            result = self.ai_client.analyze(request)
            result['inference_mode'] = result.get('inference_mode', 'ai_inference')
            logger.info('AI analysis completed successfully')
        except Exception:
            result = self.fallback.analyze(payload)
            logger.warning('AI analysis failed; deterministic fallback used')

        result['computed_severity'] = result.get('computed_severity') or self.severity_service.compute(
            result.get('suggested_category', 'unclassified'),
            request.get('metrics', {}).get('density_indicator'),
            0.5,
        )
        analysis = AIAnalysisResult(
            analysis_id=f"ANL-{datetime.now(timezone.utc).strftime('%Y%m%d%H%M%S')}",
            incident_id='INC-0001',
            detected=result['detected'],
            suggested_category=result['suggested_category'],
            confidence_score=result['confidence_score'],
            hazard_features={'hazard_flags': result.get('hazard_flags', [])},
            recommended_action=result['recommended_action'],
            inference_mode=result['inference_mode'],
            latency_ms=100.0,
            analyzed_at=datetime.now(timezone.utc),
        )
        self.repository.create(db, analysis)
        return result
