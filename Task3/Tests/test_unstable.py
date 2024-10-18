import requests
import pytest

@pytest.fixture
def unstable_url():
    return "http://127.0.0.1:8000/unstable"

@pytest.fixture
def unstable_response(unstable_url):
    response = requests.get(unstable_url)
    return response.status_code, response.content.decode('utf-8').strip('"')


class TestUnstable():
    def test_unstable_get(self, unstable_response):
        code, content = unstable_response

        assert 200 == code
        assert "HAPPY" == content

