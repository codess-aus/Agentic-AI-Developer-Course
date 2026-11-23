---
title: Memory, state, and evaluation
description: Separate reusable knowledge, task progress, and proof that the result meets the goal.
hero: Memory, State, and Evaluation for AI Agents.png
hero_alt: Memory preserves useful knowledge, state tracks progress, and evaluation compares agent outcomes with explicit success criteria.
eyebrow: 05 / MEMORY & EVALUATION / LESSON 29
---

# Memory, state, and evaluation

Long-running work needs more than a long conversation. It needs useful context, durable progress records, and a way to determine whether the outcome is correct.

## Ask three separate questions

**Memory:** what should a future task know? Examples include project conventions and reviewed architectural decisions.

**State:** where is this task now? Examples include the current branch, commit, completed steps, remaining work, and unresolved decisions.

**Evaluation:** what proves the result meets the goal? Examples include the resolved dependency version, advisory status, relevant tests, and approval.

Keeping these distinct prevents a stale session summary from being mistaken for current test evidence. Durable artifacts are useful only when their provenance and freshness are clear.

## Try it: sort the information

Classify a test command, failed workflow run, dependency advisory, accepted architecture decision, and "next step: inspect the lockfile". Identify the authoritative home for each and how to check whether it is still current.

!!! success "Checkpoint"
    A task can resume after the conversation ends, but must still revalidate changed assumptions and current code before claiming completion.

## Go deeper

See [Copilot Memory](https://docs.github.com/en/copilot/concepts/prompting-and-context/copilot-memory) for product-specific memory behavior. GitHub issues, pull requests, and workflow records remain useful durable references regardless of whether that feature is available.
