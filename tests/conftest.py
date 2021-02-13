# pylint: disable=redefined-outer-name
"""
    PEX conftest. Configuration used by all tests
"""
import pytest
from src.pex.app import app as flask_app


@pytest.fixture
def app():
    """
    App Fixture
    """
    yield flask_app


@pytest.fixture
def client(app):
    """
    Client fixture
    """
    return app.test_client()
