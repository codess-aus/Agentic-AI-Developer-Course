---
title: Plan, act, evaluate
description: Make the agent loop inspectable, bounded, and driven by objective evidence.
hero: The Agent Lifecycle_ Plan, Act, Evaluate.png
hero_alt: A circular workflow connects planning, tool-driven action, and evaluation, with feedback returning to the plan until the goal or stopping condition is reached.
eyebrow: 01 / FOUNDATIONS / LESSON 03
---

# Plan, act, evaluate

Reliable agent work is a loop, not a single generation. **Plan** the change, **act** within a boundary, and **evaluate** the result against the original goal. Repeat only while the task remains in scope and within its budget.

## Make each phase visible

The plan should explain the intended files, validation, risks, and escalation path. Record this concise decision summary in an issue or pull request. You need an inspectable rationale, not private model reasoning.

Actions should produce attributable changes on a working branch. Evaluation should inspect the actual diff, tests, security signals, and review feedback. A passing build cannot prove that a dependency vulnerability is gone if a transitive dependency still introduces it.

## Try it: make failure useful

Draft a three-row lifecycle table for your dependency update. For each phase, name its artifact, owner, and exit condition. Add a failure branch: if the same check fails twice without progress, stop and provide a handoff containing the error and attempted fixes.

!!! success "Checkpoint"
    Your loop can end in success, an explicit failure, or escalation. It cannot run forever, silently broaden the scope, or declare victory from plausible-looking code.

## Go deeper

Use [workflow artifacts](https://docs.github.com/en/actions/concepts/workflows-and-actions/workflow-artifacts) to preserve test evidence. Enforce acceptance through [required status checks](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests/about-protected-branches), rather than relying on an agent's own completion message.
