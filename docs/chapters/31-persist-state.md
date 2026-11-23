---
title: Persist state
description: Use the issue and pull request as durable anchors and detect drift before resuming execution.
hero: Persist Agent State in GitHub.png
hero_alt: Issues, pull requests, commits, and workflow runs preserve progress so an agent can resume work and detect context drift.
eyebrow: 05 / MEMORY & EVALUATION / LESSON 31
---

# Persist state

State records what has happened and what remains. Keep it attached to the task, not only inside the current agent session.

## Anchor progress in the proposal

The issue holds the requirements. The pull request links the plan, commits, decisions, and latest evidence. Keep its description current when a decision changes, and preserve important rationale in the discussion or documentation.

Before resuming, read the current issue and pull request, inspect the latest commit, and confirm which checks ran against it. Compare the diff with the original scope. New unrelated files or contradictory decisions are signs of context drift.

Artifact retention varies by repository and organization settings. Do not rely on a fixed default as your archival plan. Keep a durable summary of consequential outcomes and references.

## Try it: simulate an interruption

Pause after planning your dependency change. Write a resume note with task reference, branch, commit, completed work, unresolved questions, and next action. Return later and verify every field against the repository before proceeding.

!!! success "Checkpoint"
    Resuming does not duplicate work or assume old checks apply to new code. Changed requirements trigger an updated plan.

## Go deeper

Review [artifact retention settings](https://docs.github.com/en/organizations/managing-organization-settings/configuring-the-retention-period-for-github-actions-artifacts-and-logs-in-your-organization) and [pull request basics](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests).
