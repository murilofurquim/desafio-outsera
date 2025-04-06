from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)
client.get("/raspberry-awards")

def test_read_main():
    response = client.get("/raspberry-awards")
    assert response.status_code == 200
    assert response.json() ==   {'max': [{'folowingWin': 2015,
            'interval': 13,
            'previousWin': 2002,
            'producer': 'Matthew Vaughn'}],
   'min': [{'folowingWin': 1991,
            'interval': 1,
            'previousWin': 1990,
            'producer': 'Joel Silver'}]}
