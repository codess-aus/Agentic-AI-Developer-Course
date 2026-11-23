---
title: Operate at scale
description: Diagnose coordination failures, missing evidence, stalled approvals, and flapping workflows before expanding autonomy.
hero: Operate Reliably at GitHub Scale.png
hero_alt: Reliable operations combine visible workflow health, bounded recovery, escalation, and controls that keep multiple agents from destabilizing delivery.
eyebrow: 04 / ORCHESTRATION / LESSON 27
---

# Operate at scale

A collection of individually capable agents can still form an unreliable system. At scale, coordination failures often matter more than a single bad edit.

## Recognize the signals

**Partial execution:** a proposal exists but validation never ran. **Stalled work:** approvals or dependencies never arrive. **Conflicting outputs:** agents produce incompatible proposals. **Flapping:** jobs repeatedly restart, cancel, or invalidate one another.

Inspect the pull request timeline, trigger event, token behavior, workflow history, current commit, and artifact availability before rerunning anything. A missing check may be a trigger or configuration problem, not an agent coding failure.

Do not resolve blocked policy by casually adding a bypass actor. Diagnose whether the proposed workflow and policy are compatible, and involve the policy owner for any exception.

## Try it: diagnose before retrying

A bot opens a pull request but no validation appears. Write an investigation order covering event filters, token-trigger behavior, workflow approval, permissions, and skipped jobs. Name the evidence that would confirm each explanation.

!!! success "Checkpoint"
    Your response changes the failing mechanism, not the strength of the agent's prompt. An absent check remains an unresolved acceptance blocker.

## Go deeper

Use [monitoring workflows](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows) and [triggering workflows](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/trigger-a-workflow) to investigate operational failures.
