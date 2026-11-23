---
title: Design the architecture
description: Design a visible path from task definition to accepted change before adding more autonomy.
hero: Designing Agent Architecture with Michelle and Coda.png
hero_alt: Michelle and Coda map an agent architecture around defined tasks, bounded execution, validation evidence, and human control.
eyebrow: 02 / ARCHITECTURE / LESSON 07
---

# Design the architecture

Architecture is the path work follows through your system. Before choosing tools or adding agents, decide where intent is recorded, where changes happen, how validation runs, and who accepts the result.

## Separate responsibilities

A useful starting design has four parts: an issue containing the task contract, a planner producing an inspectable proposal, an implementer working on a branch, and validation attached to a pull request. People and configured policy decide acceptance.

These are responsibilities, not necessarily four separate processes. One bounded agent can handle several steps. Splitting a small task across many agents adds coordination cost without automatically improving quality.

A **plan** is the reviewable artifact. **Planning** is the capability that creates or revises it. Keep the artifact durable even if the session disappears.

## Try it: sketch a minimal system

Draw the dependency-remediation flow using five boxes: issue, plan, branch, checks, review. Label every arrow with its trigger and identity. Mark where write access first becomes necessary and where a human can stop progress.

!!! success "Checkpoint"
    The architecture explains how a failed test returns work to the implementer without letting that implementer weaken the acceptance policy.

## Go deeper

[Copilot customization](https://docs.github.com/en/copilot/concepts/customization) describes ways to provide context and specialization. Use specialization to support your architecture, not as a substitute for repository controls.
