---
title: Map agents to the SDLC
description: Give each agent a bounded lifecycle responsibility with observable inputs, outputs, and ownership.
hero: Mapping Agent Responsibilities Across the SDLC.png
hero_alt: Planning, implementation, validation, acceptance, and deployment are mapped to GitHub artifacts and explicit ownership boundaries.
eyebrow: 02 / ARCHITECTURE / LESSON 08
---

# Map agents to the SDLC

An agent should not inherit the entire software development lifecycle just because it can use a terminal. Assign a specific responsibility and a clear finish line.

## Name the role and artifact

| Stage | Agent contribution | Reviewable record |
| --- | --- | --- |
| Planning | Scope and success criteria | Issue or proposed plan |
| Implementation | Focused changes | Branch and commits |
| Validation | Test and scan results | Checks and artifacts |
| Acceptance | Address review feedback | Reviews and policy decisions |
| Deployment | Prepare release evidence | Protected deployment record |

For this workshop, the implementation agent finishes at a reviewable proposal. It does not own the approval decision or production deployment.

Path instructions help communicate scope, but do not prevent writes by themselves. Required reviews detect sensitive changes before merge; scoped credentials and execution environments limit actions earlier.

## Try it: write a role card

Define a dependency agent's allowed files, forbidden areas, required evidence, and escalation owner. Contrast it with a refactoring agent that may edit source files but must not alter dependency manifests or workflows.

!!! success "Checkpoint"
    Each role has a non-overlapping responsibility where possible. Any shared files have a named owner and an explicit coordination rule.

## Go deeper

Read [About code owners](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners). Remember that requesting review and preventing a write are different controls.
