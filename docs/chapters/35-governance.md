---
title: Governance and guardrails
description: Make permitted behavior enforceable and keep accountability visible as agent capabilities grow.
hero: Governance and Guardrails for AI Agents.png
hero_alt: Governance surrounds AI agent work with policies, approvals, security boundaries, evidence, and human accountability.
eyebrow: 06 / GOVERNANCE / LESSON 35
---

# Governance and guardrails

The governance question is not only "what can the agent do?" It is "what should this task be authorized to do, and how will we prove the boundary held?"

## Build a layered system

Permissions constrain accessible resources. Execution isolation limits exposure. Checks evaluate results. Reviews authorize consequential changes. Logs and artifacts make decisions reconstructable.

Each layer covers a different failure mode. Documentation communicates intent, but cannot revoke a token. Passing tests provide evidence, but do not grant deployment permission. Approval records a judgment, but does not repair a missing security check.

Governance should support useful work while preventing unacceptable consequences. Make low-risk tasks straightforward and high-risk decisions explicit, rather than adding the same friction everywhere.

## Try it: connect a risk to a control

Choose three risks for your dependency agent: changing workflows, exposing credentials, and submitting incomplete evidence. For each, identify the preventive boundary, detective signal, accountable owner, and recovery action.

!!! success "Checkpoint"
    Your controls are configured mechanisms with owners, not only promises in a prompt. Their limits and availability are documented honestly.

## Go deeper

Review [rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets) and [Actions security](https://docs.github.com/en/actions/security-for-github-actions) as complementary parts of the control plane.
