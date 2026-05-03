# digital-twin-filip

The reference twin for the SolidCage [`agent-kernel`](https://github.com/fszale/agent-kernel) — a working digital twin of [Filip Szalewicz](https://solidcage.com), AI-First Transformation Consultant.

This repo is the canonical proof point: the same kernel, four files per role, one principal, multiple roles. When the kernel changes shape, this twin is the first thing that has to keep working.

## What lives here

- `README.md` — this file
- `AGENTS.md` — instructions for AI coding agents that work in this repo
- `CLAUDE.md` — Claude-specific guidance that complements `AGENTS.md`
- `CONTEXT.md` — historical and strategic context behind the twin
- `.agents/skills/` — reusable agent behaviors specific to this repo
- `.agents/workflows/` — step-by-step procedures (e.g. add a new role spec)
- `roles/` — one YAML per role binding (Principal Operator, Fractional CTO, Engineering Acceleration Advisor, Manufacturing AI Advisor)

## The twin in one paragraph

`digital-twin-filip` is one principal (Filip) wearing several hats. Each `roles/*.yaml` is a role binding that pins the same identity, voice, and guardrails to a different working context. The runtime that loads these bindings is [`agent-factory`](https://github.com/fszale/agent-factory). The kernel they all conform to lives in [`agent-kernel`](https://github.com/fszale/agent-kernel).

## Roles

| Role | What it does |
| --- | --- |
| `principal-operator` | Runs the operating cadence of a small team — priorities, blockers, decisions, follow-ups |
| `fractional-cto` | Platform engineering, due diligence, AI transformation advisory |
| `engineering-acceleration-advisor` | Cycle-time + throughput diagnosis and remediation |
| `manufacturing-ai-advisor` | Industrial AI, OT/IT integration, factory-floor agentic workflows |

Every role is the same shape because the kernel says so. Adding a fifth role is a 30-minute exercise; see [`.agents/workflows/add-new-role-spec/`](./.agents/workflows/add-new-role-spec/).

## Sibling repos

| Repo | Role |
| --- | --- |
| [`agent-kernel`](https://github.com/fszale/agent-kernel) | Methodology, skill catalog, twin-builder mirror |
| [`agent-factory`](https://github.com/fszale/agent-factory) | Runtime that loads kernel packages with HITL governance |
| [`digital-twin-factory`](https://github.com/fszale/digital-twin-factory) | Demo portal that showcases this twin and the role-binding model |
| [`operational-intelligence-lab`](https://github.com/fszale/operational-intelligence-lab) | Rate-of-Improvement tracker for twin telemetry |
| [`agent-roi-generator`](https://github.com/fszale/agent-roi-generator) | ROI + readiness intake for prospective twin engagements |
| [`agentic-playbook`](https://github.com/fszale/agentic-playbook) | Audience-specific guides and ecosystem map |

## Live tools

The same SolidCage Replit Deployment hosts every tool that surfaces this twin,
served under the `apps.solidcage.com` custom domain:

- Digital Twin Factory Demo Portal — <https://apps.solidcage.com/twin-portal/>
- Twin Builder Wizard — <https://apps.solidcage.com/twin-portal/twin-builder>
- Agent Factory Admin Dashboard — <https://apps.solidcage.com/twin-portal/admin>
- Agent ROI Generator + Readiness Scorecard — <https://apps.solidcage.com/agent-roi-generator/>
- OI Lab Rate-of-Improvement Tracker — <https://apps.solidcage.com/oi-tracker/>
- The Agentic OS Playbook (deck) — <https://apps.solidcage.com/decks/agentic-os-playbook>
- The ROI of AI Employees (deck) — <https://apps.solidcage.com/decks/roi-ai-employees>
- Digital Twin Factories (deck) — <https://apps.solidcage.com/decks/digital-twin-factories>

## Want it done for you?

The kernel is open and self-serve. If you would rather have a twin deployed, governed, and iterated on by the person who designed the methodology, book Filip at <https://solidcage.com>.
