# Digital Twin Filip Context

## What This Repo Is

`digital-twin-filip` is the portable digital twin package for Filip.

It is meant to be imported into `digital-twin-factory` and deployed into one or more factories using deployment overlays.

## Current Scope

V1 is:

- analysis-only
- portable
- contract-driven
- optimized for review, planning, strategy, and artifact analysis

## Important Boundaries

- portable twin identity belongs here
- portable memory belongs here
- factory-scoped data does not belong here
- deployment overlays may exist here as templates or portable defaults

## Important Files

- `twin/digital-twin.yaml`
- `twin/capabilities.md`
- `twin/input-contracts.md`
- `twin/output-contracts.md`
- `twin/memory-policy.md`
- `deployments/templates/deployment-template.yaml`
- `docs/architecture.md`

## Important Directories

- `twin/`: portable twin contract and identity
- `deployments/templates/`: factory deployment overlay templates
- `docs/`: architecture and packaging docs
- `diagrams/`: Mermaid source diagrams
- `.agents/`: repo-specific agent guidance
- `scripts/`: doc and diagram maintenance utilities
