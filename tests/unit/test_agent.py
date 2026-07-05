"""FHIR Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_query_fhir_resource():
    """Test Query FHIR server for patient, observation, or other resources."""
    tools = AgentTools()
    result = await tools.query_fhir_resource(resource_type="test", search_params="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_create_fhir_resource():
    """Test Create a FHIR resource from clinical data."""
    tools = AgentTools()
    result = await tools.create_fhir_resource(resource_type="test", data="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_validate_fhir_resource():
    """Test Validate a FHIR resource against profiles and implementation guides."""
    tools = AgentTools()
    result = await tools.validate_fhir_resource(resource="test", profile="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_map_data_format():
    """Test Map data between FHIR, HL7v2, CDA, and proprietary formats."""
    tools = AgentTools()
    result = await tools.map_data_format(source_format="test", target_format="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.fhir_agent_agent import FhirAgentAgent
    agent = FhirAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
