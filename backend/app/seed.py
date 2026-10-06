import json
from pathlib import Path

from app.core.database import Base, SessionLocal, engine
from app.models.incident import Incident
from app.models.zone import Zone


def seed_database() -> None:
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        if db.query(Zone).count() == 0:
            root = Path(__file__).resolve().parents[2]
            with (root / 'data' / 'sample' / 'zones.json').open('r', encoding='utf-8') as handle:
                for record in json.load(handle):
                    db.add(Zone(**record))
            if db.query(Incident).count() == 0:
                with (root / 'data' / 'sample' / 'incidents.json').open('r', encoding='utf-8') as handle:
                    for record in json.load(handle):
                        db.add(Incident(**record))
            db.commit()
    finally:
        db.close()


if __name__ == '__main__':
    seed_database()
    print('Sample data loaded')
