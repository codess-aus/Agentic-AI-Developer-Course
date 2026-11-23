---
title: Improve the system
description: Classify failures, change the responsible mechanism, and compare outcomes on a repeatable task.
hero: GitHub Agent Improvement Loop Infographic.png
hero_alt: An improvement cycle observes agent outcomes, classifies failures, adjusts instructions or tools, and evaluates the next run using evidence.
eyebrow: 05 / MEMORY & EVALUATION / LESSON 34
---

# Improve the system

An agent failure is useful only if it leads to a specific, verifiable improvement. "Use a better prompt" is not a diagnosis.

## Classify before changing

**Task or decision error:** the system misunderstood the goal or chose an invalid approach. Clarify acceptance criteria and relevant constraints.

**Tool or configuration error:** the command, workflow, trigger, or permissions were wrong. Fix the integration rather than adding repetitive instructions.

**Context error:** requirements, repository state, or prior decisions were missing or stale. Repair the authoritative record and resume process.

Record a minimal reproducible case and compare the old and new behavior against the same criteria. Keep changes small enough to attribute an improvement. Watch for tradeoffs such as higher latency, more review burden, or newly expanded permissions.

## Try it: design one experiment

Choose a failed dependency-remediation attempt. State the observed failure, likely cause, single change you will make, and outcome that would demonstrate improvement. Preserve the relevant commit and run references.

!!! success "Checkpoint"
    You can explain why the change addresses the failure mechanism and show evidence that it works without weakening the acceptance standard.

## Go deeper

Use [workflow run logs](https://docs.github.com/en/actions/how-tos/monitor-workflows/use-workflow-run-logs) and the [original Microsoft Learn paths](../resources.md#the-two-presenter-script-references) to connect diagnosis, state management, and evaluation.
