---
title: Define the task contract
description: Turn a vague goal into explicit inputs, outputs, constraints, and measurable acceptance criteria.
hero: Defining Agent Tasks Clearly.png
hero_alt: A task brief identifies the objective, context, constraints, non-goals, expected outputs, and measurable evidence of completion.
eyebrow: 02 / ARCHITECTURE / LESSON 09
---

# Define the task contract

"Fix the dependency" is not a complete task. A reliable contract names what goes in, what comes out, and what must be true before the work can be accepted.

## Make the goal testable

For the running scenario, the inputs are the advisory, affected package, current dependency files, supported runtime, and test command. The output is a focused pull request with a plan, changed manifest and lockfile, and evidence.

The success criterion is not merely a newer version in the manifest. The resolved dependency graph must no longer contain the affected version, and relevant behavior must still work. Record any advisory exceptions explicitly rather than hiding them.

```markdown
## Goal
Remove the affected version identified by the linked advisory.

## Scope and non-goals
Change the dependency manifest, lockfile, and focused regression tests.
Do not edit workflows, infrastructure, or unrelated packages.

## Acceptance evidence
Record the resolved dependency version and advisory check result.
Run the repository's existing test command and link its output.

## Stop condition
Escalate repeated failures or any required change outside this scope.
```

This brief is a starting point for an issue, not an instruction to edit this workshop's dependencies.

## Try it: remove ambiguity

Replace the generic package and test wording with exact names from your practice repository. Add a rollback approach and identify who may approve scope changes.

!!! success "Checkpoint"
    A reviewer could reject an incomplete solution using your criteria without inventing requirements after the work is done.

## Go deeper

[Creating issue forms](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-issue-forms) can make task intake structured and consistent.
