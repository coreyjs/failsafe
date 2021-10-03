import pytest
from failsafe.client import Client

def test_client():
    assert Client(api_key='Hello') is not None
