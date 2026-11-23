---
title: Approvals and acceptance
description: Place approvals at meaningful decision points and bind evidence to the exact code being accepted.
hero: Approvals and PR Governance.png
hero_alt: Agent proposals pass through checks, ownership review, and explicit approval before acceptance, with separate authorization for sensitive deployments.
eyebrow: 02 / ARCHITECTURE / LESSON 12
---

# Approvals and acceptance

Approval is a decision about a specific change with specific evidence. It is not a permanent vote of confidence in an agent.

## Keep decisions current

New commits can invalidate earlier review assumptions. Configure stale-review dismissal or approval of the most recent reviewable push where appropriate. Ensure required checks correspond to the current commit and, where needed, integration with the latest base branch.

Workflow-run approval, pull-request approval, and environment approval serve different purposes. Approving a workflow to execute does not approve its code to merge. Merging does not automatically authorize access to production secrets.

For the workshop scenario, reviewers should see the advisory outcome, resolved version, test evidence, and any behavior changes. If evidence is missing, request it rather than inferring success.

## Try it: handle a late edit

Imagine you approved a dependency-only update, then the agent pushed a workflow change. Write the decision you would make and identify which review or policy setting should force a fresh look.

!!! success "Checkpoint"
    Approval follows the latest relevant change and risk. It cannot be reused to smuggle a new class of action through an earlier decision.

## Go deeper

Review [protected branch settings](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests/about-protected-branches) and [deployment protection rules](https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments).
