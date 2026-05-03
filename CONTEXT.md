# CONTEXT.md

Historical and strategic context behind `digital-twin-filip`. If you are picking this work up cold, start here.

## Where this came from

In 2024 and 2025, Filip Szalewicz operated as Head of Engineering (serving as fractional CTO across roughly a dozen mid-market technology companies). The advisory work surfaced a pattern: principals wanted an agent that operated *like them*, not a generic assistant. They had a voice, a set of decision frameworks, and a list of things they would never delegate.

`agent-kernel` formalised that pattern into a methodology. `digital-twin-filip` is the working proof: Filip's own twin, deployed against his real workload, exercised every day across multiple roles.

## Why one twin, multiple roles

Most "personal AI" projects build one assistant per task. The kernel takes the opposite stance: a principal is one identity wearing several hats. Pinning the identity, voice, and guardrails once and varying only the role context keeps the twin coherent across very different contexts (board prep vs. factory-floor diagnostics) without re-training or forking.

Each YAML in `roles/` is therefore intentionally thin. The heavy lifting (skills, guardrails, identity) is centralised in the kernel.

## Sibling repos

| Repo | Role |
| --- | --- |
| [`agent-kernel`](https://github.com/fszale/agent-kernel) | Methodology + skill catalog this twin draws from |
| [`agent-factory`](https://github.com/fszale/agent-factory) | Runtime that loads role bindings with HITL governance |
| [`digital-twin-factory`](https://github.com/fszale/digital-twin-factory) | Demo portal that showcases this twin and the role-binding model |
| [`operational-intelligence-lab`](https://github.com/fszale/operational-intelligence-lab) | Rate-of-Improvement telemetry for any twin in production |
| [`agent-roi-generator`](https://github.com/fszale/agent-roi-generator) | ROI + readiness intake for prospective twin engagements |
| [`agentic-playbook`](https://github.com/fszale/agentic-playbook) | Audience-specific guides and ecosystem map |

## Strategic positioning

`digital-twin-filip` is the credibility artefact. The methodology being public is what makes the SolidCage sales motion honest — anyone can read exactly how Filip's twin is composed before they ever book him. Principals who would rather have a twin deployed and operated by the person who designed the methodology book at <https://solidcage.com>.

## What changes and what does not

Stable on purpose:

- The four-file kernel contract (`agent-spec.yaml`, `identity.md`, `guardrails.md`, curated skills)
- The principle of one identity, multiple roles
- Guardrails as a first-class artefact, not an afterthought

Evolves:

- The list of roles (4 today; grows when Filip starts operating in a meaningfully new context)
- The capability set per role (driven by what each engagement actually needs)
- The set of skills in the kernel that any role can pull from
