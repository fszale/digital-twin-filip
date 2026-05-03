# AGENTS.md

Guidance for AI coding agents working in `digital-twin-filip`.

## Scope of this repo

This repo holds **role bindings**, not runtime code. Every file under `roles/` is a YAML manifest that conforms to the kernel's `agent-spec-domain-template.yaml` shape. The actual capabilities live in [`agent-kernel`](https://github.com/fszale/agent-kernel)'s skill catalog; the runtime that loads them lives in [`agent-factory`](https://github.com/fszale/agent-factory).

## What you can do here

- Edit the root docs (`README.md`, `AGENTS.md`, `CLAUDE.md`, `CONTEXT.md`) for clarity, accuracy, and freshness.
- Add a new role binding under `roles/` by following [`.agents/workflows/add-new-role-spec/`](./.agents/workflows/add-new-role-spec/).
- Update an existing role's `active_capabilities` when the kernel adds a skill that the role legitimately needs.
- Add or revise repo-specific skills under `.agents/skills/`.

## What you should not do here

- Do not invent skills here. If a role needs a new capability, add the skill upstream in `agent-kernel/skills/` first, then bind it from a role.
- Do not change the kernel contract from inside this repo. The four-file twin shape is owned by `agent-kernel`.
- Do not add runtime code, tests, or build tooling. This repo is declarative.
- Do not edit roles to chase aesthetic consistency at the cost of accuracy. Each role is allowed to look slightly different where the principal really does work differently in that mode.

## Tone

Write like Filip would. Short sentences. Plain language. No hype, no marketing voice. The audience is engineers and the principals they work for.

## When you finish

A reader should be able to answer in under five minutes:

1. What is a digital twin in this ecosystem?
2. Which roles does this twin currently support?
3. How would I add a new role?

If a doc no longer helps with one of those, fix it or remove it.
