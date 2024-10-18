import pytest
import requests

from models import InverseData

@pytest.fixture
def inverse_url():
    return "http://127.0.0.1:8000/inverse"

@pytest.fixture()
def inverse_data():
    return InverseData(
        key1="value1"
    ).model_dump()

@pytest.fixture()
def inverse_response(inverse_url, inverse_data):
    response = requests.post(inverse_url, json=inverse_data)
    return response.status_code, response.json()

class TestInversePositive():
    def test_inverse_post(self, inverse_response):
        status_code, content = inverse_response

        assert content == {"value1":"key1"}
        assert status_code == 200