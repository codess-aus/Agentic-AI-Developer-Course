---
title: Cloud agent boundaries
description: Verify the selected cloud environment rather than assuming every Copilot session has identical restrictions.
hero: Cloud Agent Boundaries Infographic.png
hero_alt: Cloud agent work is enclosed by platform and repository controls, with reviewable proposals and explicit limits around sensitive actions.
eyebrow: 03 / TOOLS & BOUNDARIES / LESSON 17
---

# Cloud agent boundaries

"Runs in the cloud" is not a complete security model. Copilot environments differ, and product capabilities evolve. Verify the environment selected for the task.

## Know which model you are using

GitHub's current documentation distinguishes GitHub Actions-based sessions from cloud sandbox sessions. Their repository scoping, customization, continuity, and setup capabilities are not identical.

The presenter script emphasizes a repository-scoped, pull-request-based contributor model. Keep that model as a deliberate workshop constraint, but do not claim every cloud session is inherently single-repository, Actions-based, or unable to perform other authorized operations.

Read the current plan and organization policies, available credentials, network controls, and review settings. No product label replaces that inspection.

## Try it: compare environments

Make a two-column comparison of the environment you use and the environment described in the current GitHub documentation. Record repository access, session continuity, network restrictions, and how proposed changes reach review.

!!! success "Checkpoint"
    You can distinguish a platform guarantee from a repository policy and from a workshop recommendation. Unknown boundaries are investigated before the task receives sensitive access.

## Go deeper

Use the [current environment comparison](https://docs.github.com/en/copilot/concepts/copilot-surfaces/copilot-on-github#comparison-of-github-actions-based-sessions-and-cloud-sandboxes) as your source of truth. Recheck it when changing clients or execution environments.
