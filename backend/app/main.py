from fastapi import FastAPI
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.api.router import api_router
from app.core.database import Base, SessionLocal, engine
from app.core.logging import get_logger
from app.models.alert import Alert  # noqa: F401
from app.models.analysis import AIAnalysisResult  # noqa: F401
from app.models.incident import Incident  # noqa: F401
from app.models.response import ResponseLog  # noqa: F401
from app.models.zone import Zone  # noqa: F401

logger = get_logger(__name__)

app = FastAPI(title='AI City Command Center API', version='0.1.0')
app.include_router(api_router)


def _seed_zones() -> None:
    db: Session = SessionLocal()
    try:
        if db.query(Zone).count() == 0:
            db.add_all(
                [
                    Zone(
                        zone_id='ZONE-01',
                        name='Commercial District',
                        district='Central City',
                        criticality_weight=0.6,
                        status='normal',
                        center_latitude=28.6250,
                        center_longitude=77.2150,
                    ),
                    Zone(
                        zone_id='ZONE-03',
                        name='Central Transit Corridor',
                        district='Transit Core',
                        criticality_weight=0.9,
                        status='elevated_alert',
                        center_latitude=28.6139,
                        center_longitude=77.2090,
                    ),
                    Zone(
                        zone_id='ZONE-05',
                        name='Stadium Plaza',
                        district='North District',
                        criticality_weight=0.8,
                        status='normal',
                        center_latitude=28.6280,
                        center_longitude=77.2200,
                    ),
                ]
            )
            db.commit()
    finally:
        db.close()


@app.on_event('startup')
def startup_event():
    logger.info('Starting AI City Command Center backend')
    Base.metadata.create_all(bind=engine)
    _seed_zones()


Base.metadata.create_all(bind=engine)
_seed_zones()


@app.exception_handler(404)
async def not_found_handler(_request, exc):
    return JSONResponse(status_code=404, content={'status': 'error', 'error_code': 'RESOURCE_NOT_FOUND', 'message': 'Resource not found'})


@app.exception_handler(400)
async def bad_request_handler(_request, exc):
    return JSONResponse(status_code=400, content={'status': 'error', 'error_code': 'VALIDATION_ERROR', 'message': 'Bad request'})
