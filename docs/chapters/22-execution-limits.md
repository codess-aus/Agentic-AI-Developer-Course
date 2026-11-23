---
title: Execution limits and protections
description: Bound retries, time, permissions, and triggers so agent tasks terminate predictably.
hero: Agent Execution Limits and Protections.png
hero_alt: Execution protections include bounded retries, failure handling, permission limits, review checkpoints, and traceable recovery.
eyebrow: 03 / TOOLS & BOUNDARIES / LESSON 22
---

# Execution limits and protections

A reliable agent needs a budget as well as a goal: time, attempts, tool access, and a clear stopping condition.

## Prevent runaway execution

Fail explicitly when a required step fails. Retry only transient problems, cap attempts, and preserve the final error. Do not retry policy denials, security incidents, or bad credentials until the underlying issue is understood.

For the workshop, escalate after the same required check fails twice without progress. This is a chosen operating policy, not a GitHub-wide platform limit.

Understand trigger behavior too. Events created using `GITHUB_TOKEN` generally do not start new workflow runs, with documented exceptions such as dispatch events. App tokens and personal tokens can behave differently. Do not assume a bot-created pull request automatically receives the same validation flow.

## Try it: define a stopping policy

For your dependency task, set an execution timeout, retry budget, escalation recipient, and report format. Include the task reference, exact failed check, attempted fixes, current commit, and next recommended action.

!!! success "Checkpoint"
    The task terminates with evidence even when it cannot complete. Changing token types or triggers prompts a fresh check for missing validation and accidental loops.

## Go deeper

Read [triggering workflows](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/trigger-a-workflow) and [workflow syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax) for timeouts, permissions, and event conditions.
