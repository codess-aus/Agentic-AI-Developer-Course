---
title: Pull request governance
description: Layer templates, required checks, owners, rulesets, and environments into a reviewable acceptance path.
hero: GitHub PR Governance at a Glance.png
hero_alt: Pull request governance layers a visible plan, automated checks, code ownership, branch policy, and deployment gates.
eyebrow: 02 / ARCHITECTURE / LESSON 11
---

# Pull request governance

A pull request is an architectural control point when review and policy actually constrain acceptance. A template alone is only a request for information.

## Layer the controls

Start with a template asking for the goal, plan, scope, risks, evidence, and rollback. Add a required check for any mechanically testable expectations. A nonempty plan section is useful hygiene, but cannot prove a plan is good.

Use CODEOWNERS to route sensitive paths. The **last matching pattern wins**, so put broad defaults before more specific rules. Require code-owner approval through repository settings, and protect the ownership file and workflow definitions themselves.

Require appropriate status checks and reviews on the target branch. Review bypass actors deliberately. Use a protected environment for deployment: merge approval and production approval are separate decisions.

## Try it: trace one sensitive change

In your practice repository, map a proposed workflow edit to its code owner, required checks, branch rules, and deployment gate. If you have admin access, inspect the active rules rather than enabling speculative settings.

!!! success "Checkpoint"
    You can explain who would review a change that weakens CI, and which rule prevents that same change from bypassing review.

## Go deeper

Compare [CODEOWNERS behavior](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners) with [rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets). Protecting policy changes is as important as protecting application code.
