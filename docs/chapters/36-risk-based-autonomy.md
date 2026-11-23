---
title: Risk-based autonomy
description: Match permitted actions to impact, reversibility, and exposure rather than giving every task the same freedom.
hero: Risk based autonomy and action boundaries.png
hero_alt: Increasing levels of autonomy are matched to risk, with stronger checks and human authorization for high-impact actions.
eyebrow: 06 / GOVERNANCE / LESSON 36
---

# Risk-based autonomy

Risk depends on what changes, how easily it can be undone, and how quickly it affects users or systems. A two-line workflow edit can be riskier than a large documentation change.

## Define levels deliberately

| Level | Suitable boundary |
| --- | --- |
| Read-only | Inspect and recommend without repository writes |
| Propose-only | Prepare a branch or pull request, without acceptance authority |
| Guarded execution | Run explicitly authorized tests or staging operations |
| Human-authorized | Gate production, secrets, and other consequential actions |

These are workshop design categories, not universal Copilot modes. For this course, keep agent-authored changes propose-only. Any future low-risk auto-merge policy should be an explicit organizational decision, backed by appropriate validation.

Do not let the agent's own unverified risk label authorize itself. Evaluate changed paths, capabilities, and policy using deterministic checks and appropriate owners.

## Try it: classify the actions

Rank reading an advisory, updating a lockfile, editing CI, changing authentication, and deploying to production. Explain the required evidence and authorization for each.

!!! success "Checkpoint"
    Autonomy grows only when controls and outcomes justify it. A smaller diff does not automatically receive a lower risk rating.

## Go deeper

Use [deployment environments](https://docs.github.com/en/actions/concepts/workflows-and-actions/deployment-environments) and [token permissions](https://docs.github.com/en/actions/tutorials/authenticate-with-github_token) to translate risk decisions into enforceable capabilities.
