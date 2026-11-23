---
title: Recover safely
description: Distinguish transient failures from deterministic defects and policy denials, then recover with bounded actions.
hero: Reliable Agent Operations Infographic.png
hero_alt: Reliable agent operations connect failure detection to bounded retries, human escalation, rollback, and a clear audit trail.
eyebrow: 04 / ORCHESTRATION / LESSON 28
---

# Recover safely

Recovery is part of the design, not an improvisation after an agent gets stuck. Keep changes small enough to understand and reversible enough to contain.

## Pick the right response

| Failure | First response |
| --- | --- |
| Temporary service interruption | Retry within a time and attempt budget |
| Reproducible test failure | Diagnose and fix the scoped implementation |
| Permission or policy denial | Stop and involve the authorized owner |
| Suspected credential exposure | Revoke or rotate, investigate, and preserve evidence |
| Bad merged change | Assess impact and prepare a reviewed revert or fix |

Closing an unmerged pull request stops that proposal from merging, but does not undo external side effects. Reverting code also does not automatically reverse database migrations, deployments, or exposed secrets.

## Try it: rehearse the runbook

For your dependency update, define the last known good commit, rollback owner, validation after rollback, and communication channel. Practice on a disposable branch with no deployment side effects.

!!! success "Checkpoint"
    Your runbook states when automation must stop. It restores a verified state instead of hiding the error, skipping the check, or granting broader access.

## Go deeper

Read [reverting a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/reverting-a-pull-request) and [reviewing deployment history](https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/view-deployment-history).
