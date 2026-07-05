# FHIR Agent

[![CI](https://github.com/kogunlowo123/fhir-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/fhir-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Healthcare | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

FHIR interoperability agent that manages healthcare data exchange using FHIR R4 standards, maps between data formats, validates FHIR resources, and enables seamless integration between healthcare systems.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `query_fhir_resource` | Query FHIR server for patient, observation, or other resources |
| `create_fhir_resource` | Create a FHIR resource from clinical data |
| `validate_fhir_resource` | Validate a FHIR resource against profiles and implementation guides |
| `map_data_format` | Map data between FHIR, HL7v2, CDA, and proprietary formats |
| `bulk_export` | Initiate FHIR bulk data export for analytics |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/fhir/process` | Process request |
| `POST` | `/api/v1/fhir/query` | Query data |
| `POST` | `/api/v1/fhir/validate` | Validate |
| `POST` | `/api/v1/fhir/report` | Generate report |
| `GET` | `/api/v1/fhir/audit` | Get audit trail |

## Features

- Fhir
- Compliance
- Interoperability

## Integrations

- Epic Ehr
- Cerner Ehr
- Allscripts
- Fhir Server
- Clearinghouse

## Architecture

```
fhir-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── fhir_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**EHR + Healthcare Platform + LLM**

---

Built as part of the Enterprise AI Agent Platform.
