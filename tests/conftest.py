import copy
import pytest


# Capture a deep copy of the initial in-memory activities state
from src import app as app_module

_INITIAL_ACTIVITIES = copy.deepcopy(app_module.activities)


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset the in-memory activities dict before each test."""
    # Clear and repopulate the module-level dict so route handlers keep the same object
    app_module.activities.clear()
    app_module.activities.update(copy.deepcopy(_INITIAL_ACTIVITIES))
    yield


@pytest.fixture
def client():
    from fastapi.testclient import TestClient

    with TestClient(app_module.app) as c:
        yield c
