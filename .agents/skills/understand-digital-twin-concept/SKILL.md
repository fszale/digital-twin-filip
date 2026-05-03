---
name: understand-digital-twin-concept
description: Explain what a digital twin means in the SolidCage ecosystem so you can reason correctly about role bindings without inventing definitions.
---

# Understand the digital twin concept

A digital twin in this ecosystem is **one principal's identity, voice, and guardrails, pinned once and projected into multiple working contexts**. It is not a chatbot persona, a fine-tuned model, or a per-task assistant.

## Three precise claims

1. **Same identity, multiple roles.** A twin is a single principal. Roles are different hats the same principal wears (e.g. Filip as Principal Operator vs. Filip as Manufacturing AI Advisor). The identity, voice, and guardrails are shared; the role context and capability set differ.
2. **Skills come from the kernel, not the twin.** Capabilities are references into [`agent-kernel`](https://github.com/fszale/agent-kernel)'s catalog. If a role needs a capability the kernel does not have, add the skill upstream first.
3. **Guardrails are load-bearing.** A twin without guardrails is a generic assistant, not a twin. The principal's *will not delegate* list is as important as their *will do* list.

## What a twin is not

- Not a fine-tuned model. The kernel is composition over training.
- Not a single autonomous agent. Twins run with HITL via `agent-factory`.
- Not a chatbot. Twins do work; they do not perform conversation as the deliverable.

## How to talk about a twin externally

- "A digital twin of <Principal> for <role context>."
- Avoid "AI clone", "AI version of you", "your AI self". The kernel deliberately avoids identity-replacement framing.
- The principal is always in the loop. Marketing language that suggests otherwise is wrong about the product.

## Where the canonical definition lives

[`agent-kernel/README.md`](https://github.com/fszale/agent-kernel/blob/main/README.md) and [`agent-kernel/PHILOSOPHY.md`](https://github.com/fszale/agent-kernel/blob/main/PHILOSOPHY.md). When in doubt, defer to those.
