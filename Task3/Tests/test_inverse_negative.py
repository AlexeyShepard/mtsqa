import pytest
import requests
import json

from models import InverseData

@pytest.fixture
def inverse_url():
    return "http://127.0.0.1:8000/inverse"

@pytest.fixture()
def inverse_data():
    return InverseData().model_dump(exclude_none=True)

@pytest.fixture()
def inverse_response(inverse_url, inverse_data):
    response = requests.post(inverse_url, json=inverse_data)
    return response.status_code, json.loads(response.content.decode("utf-8"))

class TestInverseNegative():
    def test_inverse_post(self, inverse_response):
        status_code, content = inverse_response

        assert content == {}
        assert status_code == 400