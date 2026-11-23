---
title: Evidence and handoffs
description: Make intent, attribution, evidence, and the next responsible owner visible at every transition.
hero: Observability and Outcomes Infographic.png
hero_alt: Observable agent work links intent, actor identity, commits, checks, artifacts, and decisions to measurable outcomes.
eyebrow: 04 / ORCHESTRATION / LESSON 26
---

# Evidence and handoffs

Observability should answer four questions: who acted, what they changed or decided, what evidence supports it, and who owns the next step.

## Make the record useful

Use consistent pull request sections for objective, plan, evidence, decisions, risks, and handoff. Link to the exact commit and workflow run rather than saying "tests passed earlier".

A label or title can help route work, but it is not proof of identity. Use authenticated actor information and workflow records for attribution.

Upload structured reports and test artifacts when they aid diagnosis. Set retention deliberately. Artifacts expire and may be deleted; they are not an unlimited archive or a reason to include secrets.

## Try it: write a handoff note

Create a note for an unresolved dependency-test failure. Include the issue, branch, commit SHA, workflow run, failed test, attempted fixes, unresolved hypothesis, and next owner. Avoid copying pages of logs when a concise excerpt and reference are sufficient.

!!! success "Checkpoint"
    A maintainer can resume the investigation without your session. The note distinguishes observed facts from hypotheses and does not present a missing artifact as evidence of success.

## Go deeper

Use [workflow artifacts](https://docs.github.com/en/actions/concepts/workflows-and-actions/workflow-artifacts) and [workflow run logs](https://docs.github.com/en/actions/how-tos/monitor-workflows/use-workflow-run-logs) to design evidence that outlasts the live agent session.
