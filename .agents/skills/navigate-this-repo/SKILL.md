---
name: navigate-this-repo
description: Orient yourself in digital-twin-filip — where the role bindings live, what shape they follow, and which sibling repos own related concerns.
---

# Navigate this repo

Use this skill when you are an AI agent (or a new human reader) opening `digital-twin-filip` for the first time.

## Read order

1. [`README.md`](../../../README.md) — top-level overview, role table, live tools, sibling repos.
2. [`CONTEXT.md`](../../../CONTEXT.md) — why the twin exists.
3. One role YAML, e.g. [`roles/principal-operator.yaml`](../../../roles/principal-operator.yaml) — the spec, by example.
4. [`AGENTS.md`](../../../AGENTS.md) — what you are allowed to change here vs. upstream.

## Mental model

- This repo is **declarative**. There is no runtime code.
- Every role is the same shape: id, display_name, twin, spec_version, agent_spec_template, context, active_capabilities.
- Each `active_capabilities[].backed_by_skill` is a path that resolves into [`agent-kernel`](https://github.com/fszale/agent-kernel)'s skill catalog. If the skill does not exist there, the role binding is broken.

## Where things actually live

| Concern | Repo |
| --- | --- |
| Twin identity, voice, guardrails template | `agent-kernel` |
| Skill catalog | `agent-kernel/skills/` |
| Role bindings (this repo) | `digital-twin-filip/roles/` |
| Runtime loader, HITL, audit | `agent-factory` |
| ROI + readiness for prospective twins | `agent-roi-generator` |
| Telemetry for deployed twins | `operational-intelligence-lab` |

## Stop conditions

You should leave this repo and open the right sibling when:

- The change touches *runtime behavior* → `agent-factory`
- The change touches *what a skill does* → `agent-kernel`
- The change touches *measurement of outcomes* → `operational-intelligence-lab`
