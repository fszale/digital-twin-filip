# Architecture

## Purpose

Describe the package structure and memory boundaries for `digital-twin-filip`.

## Package Structure

<!-- DIAGRAM: twin-package-structure START -->
```mermaid
graph TB
    PKG["digital-twin-filip"]
    TWIN["twin/
manifest and contracts"]
    DEPLOY["deployments/
overlay templates"]
    DOCS["docs/
architecture and packaging"]
    AGENT[".agents/
repo guidance"]

    PKG --> TWIN
    PKG --> DEPLOY
    PKG --> DOCS
    PKG --> AGENT

    style PKG fill:#1a4a2e,color:#fff,stroke:#4ade80
    style TWIN fill:#3a2a5c,color:#fff,stroke:#a78bfa
    style DEPLOY fill:#1a3a5c,color:#fff,stroke:#4a9ede
    style DOCS fill:#2a2a2a,color:#fff,stroke:#6b7280
    style AGENT fill:#3a3a1a,color:#fff,stroke:#facc15
```
<!-- DIAGRAM: twin-package-structure END -->

## Memory Boundary

<!-- DIAGRAM: twin-memory-boundary START -->
```mermaid
graph LR
    PORT["Portable Memory
identity, heuristics, approved lessons"] --> TWIN["Digital Twin Filip"]
    FACT["Factory-Scoped Memory
transcripts, artifacts, proprietary context"] --> REVIEW["Promotion Review"]
    REVIEW -->|"approved generalized learning"| PORT

    style PORT fill:#3a2a5c,color:#fff,stroke:#a78bfa
    style TWIN fill:#1a4a2e,color:#fff,stroke:#4ade80
    style FACT fill:#4a1a1a,color:#fff,stroke:#f87171
    style REVIEW fill:#3a3a1a,color:#fff,stroke:#facc15
```
<!-- DIAGRAM: twin-memory-boundary END -->

## Narrative Summary

This repo defines the portable twin, not the runtime platform.

The twin package should carry:

- identity
- capability contracts
- portable memory policy
- deployment overlay templates

The twin package should not carry:

- raw factory memory
- customer artifacts
- factory transcripts
- secrets

## Update Rule

When package structure or memory rules change:

1. update the diagram source in `diagrams/`
2. run `python3 scripts/embed_diagrams.py`
3. update the relevant `twin/` contract files
