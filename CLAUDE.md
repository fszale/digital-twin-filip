# CLAUDE.md

Companion file to [`AGENTS.md`](./AGENTS.md), specific to Claude.

## Read first

- [`README.md`](./README.md) — what this twin is and the roles it ships with.
- [`AGENTS.md`](./AGENTS.md) — what is in scope and out of scope for this repo.
- [`CONTEXT.md`](./CONTEXT.md) — why the twin exists and how it relates to the kernel.
- [`agent-kernel/PHILOSOPHY.md`](https://github.com/fszale/agent-kernel/blob/main/PHILOSOPHY.md) — the principles every role binding respects.

## How to work here

- Read the existing role YAMLs before adding or editing anything. They are the spec, by example.
- Prefer editing an existing role over adding a new one. Roles should only multiply when the principal genuinely operates differently in that context.
- Keep diffs small. A role edit is usually one capability at a time.
- When you reference a skill, double-check it exists in [`agent-kernel/skills/`](https://github.com/fszale/agent-kernel) before committing. Dangling `backed_by_skill` references are the most common decay pattern in this repo.

## Style notes

- Reuse Filip's voice: direct, written-first, slightly dry, allergic to jargon.
- Avoid the words "leverage", "synergy", "robust", "world-class", "ecosystem-wide". They do not belong here.
- Capabilities read as actions the twin performs, not as features.

## When in doubt

Ask "would Filip publish this role with his name on it as something he actually does?" If the answer is no, rewrite or delete.
