# Digital Twin Filip Implementation Plan

## Purpose

`digital-twin-filip` is the portable twin package for Filip.

It should contain:

- Filip-specific identity
- skills, prompts, templates, and workflows
- portable long-term memory
- capability definitions
- input and output contracts
- deployment overlay definitions for different factories

It should not contain factory-scoped customer data or factory-owned artifacts.

## Relationship to Other Projects

This repo is not the factory runtime.

The intended boundaries are:

- `digital-twin-factory`: control plane and runtime
- `digital-twin-filip`: Filip's portable twin package
- `agent-kernel`: current upstream content source to draw from, without modifying it further

This repo should become the clean packaging layer that makes Filip deployable into multiple factories.

## Core Design Rule

Do not create a separate full twin repo for every factory by default.

Instead, use:

- one portable twin repo
- one or more deployment overlays
- factory-scoped runtime data stored in the factory platform

This keeps identity portable and operations manageable.

## What Belongs In This Repo

### Portable Twin Identity

- biography and role framing
- working principles
- domain strengths
- communication style
- decision style
- reusable mental models

### Portable Twin Capabilities

- strategy review
- architecture review
- project review
- planning
- diagnostic analysis
- artifact analysis

### Portable Twin Memory

- generalized lessons
- approved reusable patterns
- durable heuristics
- exported memory snapshots

### Deployment Overlays

- per-factory limits
- per-factory model overrides
- per-factory channel settings
- per-factory visibility rules
- per-factory memory namespace mapping

## What Must Not Belong In This Repo

- customer documents
- uploaded proprietary files
- raw conversation transcripts from a factory
- factory-owned reports
- secrets
- API tokens
- raw job artifacts
- unredacted factory memory

## Memory Separation Rules

### Portable Memory

Portable memory is exportable and moves with Filip between factories.

Examples:

- frameworks
- generalized operating patterns
- improved abstractions
- reusable critique styles
- approved non-proprietary lessons

### Factory Memory

Factory memory stays in the factory runtime and is never committed here.

Examples:

- client uploads
- factory chat logs
- project-specific notes
- internal reports
- operational decisions
- private URLs
- customer-specific analysis

### Memory Promotion Workflow

When factory experience produces something worth keeping, do not copy raw material directly into portable memory.

Use this workflow:

1. identify candidate learning
2. abstract it into a general lesson
3. remove proprietary references
4. review and approve it
5. record it as portable memory

## Packaging Strategy

This repo should eventually define a formal package contract for the factory platform.

Recommended core files:

- `digital-twin.yaml`
- `CAPABILITIES.md`
- `INPUT_CONTRACTS.md`
- `OUTPUT_CONTRACTS.md`
- `MEMORY_POLICY.md`
- `deployments/`
- `exports/`
- `evals/`

## Recommended Repo Layout

```text
digital-twin-filip/
  README.md
  IMPLEMENTATION_PLAN.md
  twin/
    digital-twin.yaml
    identity.md
    capabilities.md
    input-contracts.md
    output-contracts.md
    memory-policy.md
  memory/
    portable/
    exports/
  deployments/
    default/
      deployment.yaml
      limits.yaml
      channels.yaml
      policies.yaml
    templates/
      deployment-template.yaml
  evals/
  docs/
    packaging.md
    deployment-overlays.md
    memory-governance.md
```

## Deployment Overlay Model

Each factory-specific deployment should be an overlay, not a forked twin.

A deployment overlay should define:

- `factory_id`
- `deployment_id`
- `memory_namespace`
- `enabled_channels`
- `allowed_models`
- `model_preferences`
- `daily_token_limit`
- `max_cost_per_day`
- `allowed_input_types`
- `allowed_output_types`
- `analysis_only`
- `review_requirements`

Example naming:

- twin id: `filip`
- deployment ids: `filip@acme`, `filip@internal-lab`
- internal slug: `filip__acme`

## Upstream Content Strategy

Since `agent-kernel` will not be modified further for this effort, treat it as an upstream source of content and structure.

Recommended approach:

- manually bring over the needed identity, skills, prompts, templates, and docs
- record the source commit or release reference used
- avoid hidden drift by documenting what was imported

Later, if needed, add a formal sync process. For now, keep it simple and explicit.

## Delivery Plan

### Immediate

- define the twin manifest
- define the memory policy
- define capability contracts
- define deployment overlay schema
- define initial portable memory structure

### Soon

- import the relevant Filip-specific content from `agent-kernel`
- create the first deployment overlay for the first factory
- add eval cases
- define export package format

### Later

- add memory promotion workflow tooling
- add more factory overlays
- add more structured capability metadata
- add agent API contracts once the platform is ready

## Additional Recommendations

- Keep this repo person-specific and portable.
- Keep factory data out of this repo completely.
- Keep deployment overlays small and declarative.
- Prefer configuration over code for limits and channel policy.
- Treat exports as a first-class feature, not an afterthought.

## Immediate Next Documents To Create

- `twin/digital-twin.yaml`
- `twin/capabilities.md`
- `twin/input-contracts.md`
- `twin/output-contracts.md`
- `twin/memory-policy.md`
- `deployments/templates/deployment-template.yaml`
- `docs/packaging.md`
- `docs/deployment-overlays.md`
- `docs/memory-governance.md`
