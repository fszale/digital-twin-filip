# Twin Packaging

Use this guide when editing the portable twin package.

## Required Alignment Targets

- `twin/digital-twin.yaml`
- `twin/capabilities.md`
- `twin/input-contracts.md`
- `twin/output-contracts.md`
- `twin/memory-policy.md`
- `deployments/templates/deployment-template.yaml`

## Rules

- preserve analysis-only in v1
- preserve exportable portable memory
- preserve non-exportable factory-scoped memory
- keep names aligned with `digital-twin-factory` contracts
