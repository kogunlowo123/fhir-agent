#!/bin/bash
set -euo pipefail
echo "Setting up FHIR Agent..."
pip install -e ".[dev]"
echo "Setup complete!"
