from fastapi.testclient import TestClient
from fastapi_app.main import app
import json

client = TestClient(app)

def test_insert_group():
    data = {
    "cuatrimestre": 1,
    "no_grupo": 2,
    "hora_entrada_minima": "12:00:00",
    "hora_salida_maxima": "20:00:00",
    "ciclo_escolar": 1,
    "carrera": 1
    }
    response = client.post(
        "grupos/",
        data=json.dumps(data),
    )
    assert response.status_code == 202
    assert response.json() == { "message" : "Grupo agregado correctamente" }