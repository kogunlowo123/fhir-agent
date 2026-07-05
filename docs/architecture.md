# FHIR Agent Architecture

FHIR interoperability agent that manages healthcare data exchange using FHIR R4 standards, maps between data formats, validates FHIR resources, and enables seamless integration between healthcare systems.

## Domain Tools

- **query_fhir_resource**: Query FHIR server for patient, observation, or other resources
- **create_fhir_resource**: Create a FHIR resource from clinical data
- **validate_fhir_resource**: Validate a FHIR resource against profiles and implementation guides
- **map_data_format**: Map data between FHIR, HL7v2, CDA, and proprietary formats
- **bulk_export**: Initiate FHIR bulk data export for analytics