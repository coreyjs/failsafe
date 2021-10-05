import pytest
from failsafe import __version__, api_client
from failsafe.exceptions import AuthenticationError

def test_version():
    assert __version__ == '0.1.0'


def test_creating_api_client():
    client = api_client(api_key='Oryx')
    assert client


def test_creating_api_client_with_missing_key_will_error():
    with pytest.raises(AuthenticationError) as err:
        api_client(api_key=None)
