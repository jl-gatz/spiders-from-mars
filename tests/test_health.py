from http import HTTPStatus

from fastapi.testclient import TestClient

from process_miner.api.main import app


def test_healthcheck():
    client = TestClient(app)
    response = client.get('/health/')
    assert response.status_code == HTTPStatus.OK
    data = response.json()
    assert data == {'status': 'ok', 'service': 'process-miner', 'mode': 'api'}
