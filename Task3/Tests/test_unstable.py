import requests
import pytest

@pytest.fixture
def unstable_url():
    return "http://127.0.0.1:8000/unstable"

@pytest.fixture
def unstable_response(unstable_url):
    response = requests.get(unstable_url)
    return response

@pytest.fixture
def unstable_response_content(unstable_url):
    response = requests.get(unstable_url)
    return response.content.decode('utf-8').strip('"')

class TestUnstable():
    def test_unstable_get(self, unstable_response, unstable_response_content):

        assert 200 == unstable_response.status_code
        assert "HAPPY" == unstable_response_content

