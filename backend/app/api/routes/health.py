from datetime import datetime, timezone

from fastapi import APIRouter

router = APIRouter()


@router.get('/health')
def get_health():
    return {
        'status': 'healthy',
        'timestamp': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'subsystems': {
            'backend': 'online',
            'ai_engine': 'available',
            'data_layer': 'ready',
        },
    }
