---
title: Plan before acting
description: Choose when to review intent and distinguish planning guidance from an enforced read-only boundary.
hero: Planning and Task Design Infographic.png
hero_alt: Good tasks have a clear objective, acceptance criteria, constraints, non-goals, and validation; vague goals and unrestricted tools are shown as pitfalls.
eyebrow: 02 / ARCHITECTURE / LESSON 10
---

# Plan before acting

Separate **intent**, **execution**, and **validation**. Reviewers should understand what the agent intends to do before they are asked to accept the result.

## Choose the right review point

**Plan-first** work reviews an issue or proposal before implementation starts. Use it for authentication, workflow, infrastructure, or other consequential changes. A planning stage can use read-only tools and hand off only after approval.

**Plan plus execution** allows an initial implementation alongside the plan, while policy still blocks merge. This can suit small, reversible changes where an early diff helps discussion.

A prompt that says "do not edit" expresses intent. A read-only environment or tool allowlist enforces a capability boundary. Use both when a plan must be approved before any change.

## Try it: critique the plan

Ask for a plan to remediate the dependency without editing files. Check whether it identifies the affected graph, expected files, test commands, rollback, and stopping conditions. Remove write tools if your chosen client supports that boundary.

!!! success "Checkpoint"
    The plan explains the next actions and evidence without pretending implementation already succeeded. New scope or uncertainty is surfaced for a decision.

## Go deeper

Use the [current Copilot documentation](https://docs.github.com/en/copilot/concepts/copilot-surfaces/copilot-on-github) to check which planning and execution experiences your surface supports. Do not assume that a custom agent definition itself creates a separate security sandbox.
