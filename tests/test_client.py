import pytest
from failsafe.client import Client


@pytest.fixture(scope='function')
def client():
    yield Client(api_key='12345')


def test_client(client):
    assert client is not None
    assert client.session.api_key == '12345'


def test_client_has_session(client):
    assert client.session is not None
