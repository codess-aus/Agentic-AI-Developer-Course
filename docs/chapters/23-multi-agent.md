---
title: Multi-agent responsibilities
description: Add agents only where separate responsibilities and independent evidence justify the coordination cost.
hero: Multi-Agent Orchestration Infographic.png
hero_alt: Specialized agents coordinate planning, implementation, and validation through explicit roles and reviewable GitHub artifacts.
eyebrow: 04 / ORCHESTRATION / LESSON 23
---

# Multi-agent responsibilities

More agents do not automatically mean better results. Each additional participant creates another handoff, identity, context boundary, and possible conflict.

## Separate by responsibility

A dependency agent can own manifest and lockfile changes. A documentation agent can update migration guidance. A validation role can inspect test and advisory evidence. All should refer to the same task contract.

Avoid having multiple agents independently rewrite the same files or redefine success. A reviewer produced by the same model can offer useful feedback, but is not an independent authorization boundary. Required human review and objective checks still matter.

Start with one agent. Split only when a responsibility benefits from separate context, permissions, or genuinely independent work.

## Try it: create a responsibility matrix

For each role, record the allowed files, output artifact, dependent inputs, identity, and escalation owner. Mark shared files such as lockfiles and assign a single writer.

!!! success "Checkpoint"
    Every handoff has an owner and an artifact. Two agents cannot both claim authority to accept the final result or silently change the original requirements.

## Go deeper

Read [custom agent concepts](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-custom-agents) alongside [workflow dependencies](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#jobsjob_idneeds). Role descriptions and execution ordering solve different problems.
