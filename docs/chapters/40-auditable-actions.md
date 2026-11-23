---
title: Auditable Actions
description: Preserve commit-specific execution evidence and approval records without leaking secrets or assuming infinite retention.
hero: Observable GitHub Actions Infographic.png
hero_alt: Observable Actions link triggers, actor identity, job logs, test reports, artifacts, and approval records into an auditable execution trail.
eyebrow: 06 / GOVERNANCE / LESSON 40
---

# Auditable Actions

An auditable workflow can explain what happened, against which code, under which identity, and with whose authorization.

## Design evidence before execution

Record the task reference, commit SHA, workflow run, relevant test or scan reports, decision summary, and approval events. For deployment, include the artifact version and environment decision.

Set artifact retention to match operational needs and applicable policy. Keep secrets and sensitive payloads out of reports. Access control and redaction matter as much as retention.

Evidence collection should still run when a test fails, where safe, so diagnosis is possible. But uploading a report must not turn a failed validation into a successful result. A required report that does not exist should fail explicitly rather than quietly producing an empty artifact.

## Try it: audit a hypothetical run

Your pull request claims "all checks passed", but its linked report comes from an earlier commit. Identify what must be rerun and how the workflow should label evidence to prevent confusion.

!!! success "Checkpoint"
    Reviewers can bind evidence to the exact proposed change. Missing, stale, or inaccessible evidence is treated as an unresolved gap, not an invitation to trust the summary.

## Go deeper

Use [workflow artifacts](https://docs.github.com/en/actions/concepts/workflows-and-actions/workflow-artifacts), [run logs](https://docs.github.com/en/actions/how-tos/monitor-workflows/use-workflow-run-logs), and [organization audit logs](https://docs.github.com/en/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/reviewing-the-audit-log-for-your-organization) for complementary records.
