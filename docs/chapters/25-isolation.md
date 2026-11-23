---
title: Isolate parallel work
description: Use separate branches and job identities, appropriate concurrency, and deliberate conflict resolution.
hero: Purple GitHub Agent Workflow Infographic.png
hero_alt: A purple GitHub workflow connects isolated agent branches, pull requests, checks, and human review before integration.
eyebrow: 04 / ORCHESTRATION / LESSON 25
---

# Isolate parallel work

Isolation keeps concurrent tasks attributable and recoverable. Give each writing task a working branch, a focused proposal, and a distinct execution context with minimal permissions.

## Control overlap

For replaceable pull-request validation, group concurrency by workflow and branch or pull request. Including the workflow name prevents unrelated workflows from cancelling one another. Cancelling obsolete validation can save time.

Deployments are different: interrupting an active deployment can leave partial state. Serialize them deliberately rather than copying cancellation settings from test jobs. Concurrency behavior and queuing guarantees should be checked against current Actions documentation.

Conflicts are not only textual. Two cleanly merging updates may introduce incompatible behavior, duplicate work, or touch areas requiring different approvals. Required integration tests and ownership review help detect these semantic and policy conflicts.

## Try it: arbitrate a conflict

Imagine one agent updates a package while another changes its API usage. Define a merge order, identify the shared test, and name the owner who resolves incompatible assumptions. Escalate after repeated conflict-resolution attempts rather than rebasing indefinitely.

!!! success "Checkpoint"
    Timing does not decide which proposal wins. The resolution is based on requirements, integration evidence, and ownership.

## Go deeper

Read [control workflow concurrency](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/control-workflow-concurrency) and consider a [merge queue](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue) for busy protected branches.
