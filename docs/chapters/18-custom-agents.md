---
title: Custom agents and instructions
description: Use reusable guidance and specialized roles without mistaking customization for a permission system.
hero: Custom Agents and Instructions Infographic.png
hero_alt: Custom agent roles, repository instructions, and selected tools guide specialized work while platform controls provide enforcement.
eyebrow: 03 / TOOLS & BOUNDARIES / LESSON 18
---

# Custom agents and instructions

Customization makes recurring work more consistent. Repository instructions provide shared conventions; a custom agent describes a focused role and, where supported, its tools and handoffs.

## Keep guidance small and durable

Repository-wide guidance belongs in `.github/copilot-instructions.md`. Put stable facts there: how to run tests, which architecture constraints matter, and where to find authoritative documentation. Do not copy entire histories or store credentials.

Custom agent profiles commonly live under `.github/agents/` with an `.agent.md` extension. Supported properties and tool identifiers depend on the surface, so validate the current format rather than copying an incompatible profile.

A role saying "review only" is not enough if the session still has unrestricted execution and write credentials. Reduce capabilities as well as narrowing instructions.

## Try it: define a focused reviewer

Draft a reviewer role that reads the issue, compares the diff with acceptance criteria, inspects test evidence, and reports findings without editing files. Name the minimum tools it needs and the situations it must escalate.

!!! success "Checkpoint"
    The role produces a concrete review artifact. Its instructions do not claim to override organization policy, and no secret is embedded in the profile.

## Go deeper

Read [repository custom instructions](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions) and [custom agents](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-custom-agents).
