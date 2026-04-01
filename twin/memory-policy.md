# Memory Policy

## Purpose

Define how memory is handled for `digital-twin-filip` when deployed into `digital-twin-factory`.

This policy exists to preserve twin portability while protecting factory-confidential data.

## Core Principle

There are two kinds of memory:

- portable memory
- factory-scoped memory

Portable memory may travel with Filip between factories.

Factory-scoped memory stays in the factory unless explicitly redacted and approved.

## Portable Memory

Portable memory includes:

- durable identity
- generalized frameworks
- reusable mental models
- refined prompt patterns
- reviewed portable skill patches
- generalized lessons
- approved non-proprietary heuristics

Portable memory may be exported with the twin.

## Factory-Scoped Memory

Factory-scoped memory includes:

- uploaded customer artifacts
- conversation transcripts
- project-specific notes
- internal reports
- proprietary instructions
- customer names, contacts, and confidential details
- raw derived artifacts

Factory-scoped memory must remain in the deployment namespace by default.

## Promotion Rule

Factory experience may influence portable memory only through an explicit promotion workflow.

Required steps:

1. identify candidate learning
2. abstract it into a general lesson
3. remove proprietary details
4. review for confidentiality and usefulness
5. approve promotion
6. record promotion event

Raw factory materials must never be copied directly into portable memory.

Approved promotions may take one of two forms:

- `portable_memory_entry`
- `portable_skill_patch`

`portable_skill_patch` is the preferred format when the learning is a reusable procedure rather than a fact or heuristic.

## Export Rule

When the twin leaves a factory, export only:

- portable memory
- approved generalized learnings
- twin identity metadata

Do not export by default:

- raw transcripts
- customer artifacts
- factory reports
- secrets
- private project notes

## Self-Improvement Rule

Deployment-local self-improvement is allowed for:

- prompt ranking
- retrieval tuning
- artifact formatting preferences
- model profile preferences within allowed lists
- local priority tuning among enabled portable skills

Portable memory changes are not auto-approved.

Portable skill changes are also not auto-approved.

## Human Review Requirements

Human review is required for:

- any portable memory promotion
- any export beyond the standard portable set
- any disputed classification of memory scope

## Practical Heuristic

Ask this question:

- is this a general lesson Filip should carry anywhere, or is it knowledge gained from a specific factory's confidential context?

If it depends on factory-specific context, it stays factory-scoped.
