---
name: add-new-role-spec
description: Add a new role binding to digital-twin-filip in a way that preserves the kernel contract and stays consistent with existing roles.
---

# Add a new role spec

Use this workflow when Filip starts operating in a meaningfully new context (e.g. "Board Advisor", "Diligence Partner") and a dedicated role binding is justified.

## Preconditions

- The role represents work Filip *actually does*, not work he aspires to do.
- The role is materially different from existing roles (Principal Operator, Fractional CTO, Engineering Acceleration Advisor, Manufacturing AI Advisor). If it overlaps >70% with an existing role, extend that role instead.
- Every capability the role needs already exists in [`agent-kernel`](https://github.com/fszale/agent-kernel)/skills/, **or** you have a plan to add it upstream first.

## Steps

1. **Pick a slug.** Lowercase kebab-case, matches how Filip introduces the role in conversation (`board-advisor`, not `strategic_board_partner_v2`).
2. **Copy the closest existing role.** `cp roles/principal-operator.yaml roles/<slug>.yaml`. Keep the YAML key order identical.
3. **Set the metadata.**
   - `id`: same as the slug
   - `display_name`: Title Case
   - `twin`: `digital-twin-filip` (always)
   - `spec_version`: `1`
   - `agent_spec_template`: `agent-kernel/templates/agent-spec-domain-template.yaml`
4. **Write the `context` block.** 2–4 sentences. Plain language. What the role is hired to do, who it works with, what good looks like.
5. **List `active_capabilities`.** Each entry has `id` (kebab-case), `description` (one paragraph, action-oriented), and `backed_by_skill` (kernel path). Aim for 3–6 capabilities. More than 8 means you are conflating two roles.
6. **Verify every `backed_by_skill` resolves.** Open [`agent-kernel`](https://github.com/fszale/agent-kernel) and confirm the skill exists. If any are missing, stop and add them upstream first.
7. **Update [`README.md`](../../../README.md)'s role table.** One line: role + what it does.
8. **Update [`CONTEXT.md`](../../../CONTEXT.md)** if the new role changes the "what changes / what does not" section.
9. **Open a PR** with subject `Add <slug> role binding`. Body should include: why this role exists, the principal context that produced it, and the kernel skills it draws from.

## Out of scope

- Editing skills (do that in `agent-kernel`)
- Editing identity or guardrails (those are kernel-level, shared across all roles)
- Adding runtime behavior (that belongs in `agent-factory`)

## Done looks like

- New `roles/<slug>.yaml` exists, validates against the template, and every `backed_by_skill` resolves.
- README role table updated.
- A reader can open the new role and answer in under two minutes: what is this for, what does it do, where do its capabilities come from.
