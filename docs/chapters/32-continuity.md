---
title: Continue across tools
description: Re-anchor work to shared task references when moving between IDE, CLI, and cloud execution.
hero: Agent Memory Continuity Across Tools.png
hero_alt: Shared issue, pull request, branch, commit, and workflow references connect IDE, CLI, and cloud environments without conflicting copies of state.
eyebrow: 05 / MEMORY & EVALUATION / LESSON 32
---

# Continue across tools

Continuity comes from shared references and verified state. A tool switch should not create a new, contradictory version of the task.

## Share identifiers, then verify

Use the repository, issue, pull request, branch, commit SHA, and workflow run as the handoff contract. A new environment can use those references to recover context rather than trusting an unverified narrative.

Check that the working tree is on the intended branch, the remote proposal has not changed, the requirements are current, and evidence matches the latest relevant commit. Treat "tests passed" without a run reference as an incomplete claim.

Some Copilot environments support session continuity across clients. Others do not. Even when a session transfers automatically, permissions, runtime setup, and repository state still need verification.

## Try it: hand off without a transcript

Write a concise handoff that another person could use from a different client. Include authoritative references and the next action, not an entire chat export. Ask them to identify which checks must be rerun if they change the code.

!!! success "Checkpoint"
    The new environment continues the same task with the same acceptance criteria, while independently confirming the current state and available capabilities.

## Go deeper

Consult [Copilot session and environment concepts](https://docs.github.com/en/copilot/concepts/copilot-surfaces/copilot-on-github) for current continuity support. Durable repository references keep the workflow portable.
