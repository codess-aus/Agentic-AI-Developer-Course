---
title: Responsibility and traceability
description: Keep human accountability explicit and design a reconstructable trail for every agent contribution.
hero: Agentic Systems Responsibility Infographic.png
hero_alt: Responsibility stays with people who define tasks, grant permissions, configure safeguards, and approve outcomes; agent actions need a traceable evidence trail.
eyebrow: 01 / FOUNDATIONS / LESSON 04
---

# Responsibility and traceability

Delegating work does not delegate accountability. People remain responsible for task scope, permissions, controls, review, and the consequences of accepting a change.

## Recognize the anti-patterns

Planless execution hides intent. Excess permissions increase the blast radius. Missing decision summaries make changes hard to understand. Blind trust in a green check mistakes partial validation for a complete engineering judgment.

Counter each failure with a concrete mechanism: a reviewable task contract, a narrowly scoped identity, durable decision records, and checks combined with appropriate review. Avoid asking for hidden chain-of-thought; ask for assumptions, decisions, evidence, and unresolved risks.

## Try it: reconstruct an incident

Imagine the dependency update passes tests but breaks startup in production. List the records you would need to investigate: the original goal, changed commit, test run, reviewer decision, deployment artifact, and rollback action. Assign an owner to each missing record.

!!! success "Checkpoint"
    Another maintainer could reconstruct what changed and why without access to the agent's chat history. They can identify both the contributor and the person who accepted the risk.

## Go deeper

[About pull request reviews](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/about-pull-request-reviews) explains the decision record. [Organization audit logs](https://docs.github.com/en/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/reviewing-the-audit-log-for-your-organization) provide additional administrative evidence, subject to access and retention.
