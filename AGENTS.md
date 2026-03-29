# AGENTS.md

Read [CONTEXT.md](CONTEXT.md) first.

## Repo Purpose

`digital-twin-filip` is the portable twin package for Filip.

This repo should remain:

- person-specific
- portable across factories
- analysis-only in v1
- free of raw factory-confidential data

## Working Rules

1. Do not place factory-specific transcripts or proprietary artifacts in this repo.
2. Keep portable memory distinct from factory-scoped memory.
3. Update `twin/digital-twin.yaml` when capability or contract boundaries change.
4. Keep diagrams and docs synchronized with the scripts in `scripts/`.
5. When editing the package contract, update:
   - `twin/digital-twin.yaml`
   - `twin/capabilities.md`
   - `twin/input-contracts.md`
   - `twin/output-contracts.md`
   - `twin/memory-policy.md`

## First Files To Read

- [CONTEXT.md](CONTEXT.md)
- [docs/architecture.md](docs/architecture.md)
- [twin/digital-twin.yaml](twin/digital-twin.yaml)
- [twin/memory-policy.md](twin/memory-policy.md)

## Agent Workflow Hints

- Use `.agents/skills/project-navigation.md` for orientation.
- Use `.agents/skills/twin-packaging.md` before editing package contracts.
- Use `.agents/workflows/run-doc-checks.md` after changing docs or diagrams.
