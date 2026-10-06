from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_endpoint():
    response = client.get('/health')
    assert response.status_code == 200
    payload = response.json()
    assert payload['status'] == 'healthy'
    assert payload['subsystems']['backend'] == 'online'


def test_list_incidents_returns_payload():
    response = client.get('/incidents')
    assert response.status_code == 200
    payload = response.json()
    assert 'total_count' in payload
    assert 'incidents' in payload


def test_zones_endpoint_returns_payload():
    response = client.get('/zones')
    assert response.status_code == 200
    payload = response.json()
    assert 'zones' in payload


def test_analysis_endpoint_accepts_alert_payload():
    response = client.post(
        '/analysis',
        json={
            'raw_text': 'Pedestrian congestion surge reported near Stadium Plaza',
            'source_type': 'sensor_feed',
            'zone_id': 'ZONE-05',
            'metrics': {'density_indicator': 'high'},
        },
    )
    assert response.status_code == 200
    payload = response.json()
    assert payload['detected'] in (True, False)
    assert 'suggested_category' in payload
    assert 'computed_severity' in payload
