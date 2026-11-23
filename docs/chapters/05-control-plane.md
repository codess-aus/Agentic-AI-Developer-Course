---
title: GitHub as the control plane
description: Separate artifacts that record agent activity from controls that constrain acceptance and deployment.
hero: GitHub’s Agentic Development Control Plane.png
hero_alt: GitHub connects issues, branches, pull requests, Actions, checks, reviews, and policy as a shared system of record and enforcement plane.
eyebrow: 01 / FOUNDATIONS / LESSON 05
---

# GitHub as the control plane

GitHub is a **system of record** when it captures intent, changes, evidence, and decisions. It becomes a **control plane** when configured policies constrain what can merge, run, or deploy.

## Recording is not enforcement

An issue records requirements. A branch and commits record implementation. A pull request brings the proposal, checks, and review together. Workflow runs and artifacts record validation.

Rulesets, required checks, required reviews, token permissions, and deployment environments add enforcement. A checklist saying "security reviewed" is not equivalent to a required security-owner approval. CODEOWNERS alone routes review; requiring that review is a separate configuration.

Controls only help where enabled and applicable. Verify your plan, repository visibility, organization policy, and bypass actors rather than assuming defaults protect you.

## Try it: inspect your repository

Create two columns: "records" and "enforcement". Place your issue, pull request template, test workflow, required check setting, CODEOWNERS file, and environment reviewers in the right column. Some artifacts support both, but explain which setting makes a control binding.

!!! success "Checkpoint"
    You can name the exact gate that blocks an unreviewed agent contribution. If the answer is only "the prompt says not to", you have guidance, not enforcement.

## Go deeper

Read [About rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets) and [deployment environments](https://docs.github.com/en/actions/concepts/workflows-and-actions/deployment-environments).
