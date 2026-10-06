import httpx

from app.core.config import settings
from app.core.logging import get_logger

logger = get_logger(__name__)


class AIClient:
    def __init__(self, base_url: str | None = None, timeout: float | None = None):
        self.base_url = base_url or settings.AI_SERVICE_URL
        self.timeout = timeout or settings.AI_TIMEOUT_SECONDS

    def analyze(self, payload: dict) -> dict:
        try:
            response = httpx.post(
                f'{self.base_url.rstrip("/")}/analyze',
                json=payload,
                timeout=self.timeout,
            )
            response.raise_for_status()
            data = response.json()
            required = {'detected', 'suggested_category', 'confidence_score', 'hazard_flags', 'computed_severity', 'recommended_action', 'inference_mode'}
            missing = required.difference(data.keys())
            if missing:
                raise ValueError(f'Malformed AI response missing keys: {sorted(missing)}')
            return data
        except (httpx.TimeoutException, httpx.ConnectError, httpx.HTTPError, ValueError) as exc:
            logger.warning('AI request failed; using fallback: %s', exc)
            raise
