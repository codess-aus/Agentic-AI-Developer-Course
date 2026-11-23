---
title: Workflow orchestration
description: Choose sequential, parallel, or fan-out/fan-in execution based on real dependencies and shared state.
hero: Workflows and Automation Infographic.png
hero_alt: Event-driven workflows coordinate sequential and parallel tasks, combining their outputs through explicit dependencies and controlled automation.
eyebrow: 04 / ORCHESTRATION / LESSON 24
---

# Workflow orchestration

Orchestration defines when work runs, what it depends on, and how results move between participants. Make that coordination visible in workflows and artifacts.

## Choose the pattern

Use **sequential** work when one stage needs another's output: plan, implementation, validation, approval. A dependent job should declare `needs`, not hope the producer finished first.

Use **parallel** work when tasks are independent and isolated. Two read-only analyses can often run together. Two writers touching the same lockfile cannot safely be treated as independent.

Use **fan-out/fan-in** when several bounded analyses contribute to one decision. The combining stage should verify that every required result exists and refers to the same task and commit.

Cross-workflow triggers need particular care: an unprivileged result must not become an unchecked path to a privileged token or secret.

## Try it: draw a dependency graph

Arrange dependency analysis, migration-note research, implementation, tests, and review in a graph. Mark the independent research that can run together and the evidence required before the final decision.

!!! success "Checkpoint"
    Missing or failed inputs block the combining stage. Parallelism does not let a downstream action race ahead of validation.

## Go deeper

Consult [workflow syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax) and [workflow security](https://docs.github.com/en/actions/security-for-github-actions) before connecting workflows with different trust levels.
