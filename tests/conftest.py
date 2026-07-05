"""Test configuration for FHIR Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "fhir-agent", "category": "Healthcare"}
