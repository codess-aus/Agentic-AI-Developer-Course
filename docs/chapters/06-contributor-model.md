---
title: The contributor model
description: Evaluate agent-generated changes using the same evidence, ownership, and engineering standards as other contributions.
hero: The Contributor Model for Agent Work.png
hero_alt: An agent submits a contribution through a pull request, while checks, code owners, policy, and human judgment determine whether the work is accepted.
eyebrow: 01 / FOUNDATIONS / LESSON 06
---

# The contributor model

Treat agent-generated work as a contribution, not as an exception to your engineering standards. Avoid both automatic rejection because AI wrote it and automatic trust because a tool produced it.

## Review the work

Ask whether the change solves the stated problem, stays within scope, preserves expected behavior, and comes with relevant evidence. Route sensitive changes to the right owners and check that repository policy actually applies.

For a dependency update, unexpected workflow edits deserve scrutiny even when tests pass. They may change what "passing" means. Review the diff against the plan, not just the pull request summary.

For high-risk work, require an understandable rollback or escalation path. An agent's confident claim cannot replace a reviewer confirming the evidence.

## Try it: practice acceptance

Write a short review for a hypothetical update that changes a lockfile and disables a failing security check. Explain why the extra workflow change is outside the task contract, what evidence is missing, and what the contributor must do before another review.

!!! success "Checkpoint"
    Your review explains an actionable acceptance standard. It neither attacks the author nor lowers the bar because the author is automated.

## Go deeper

Use [reviewing proposed changes](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/reviewing-proposed-changes-in-a-pull-request) as the baseline. In the next module, you will turn that standard into a task contract and architecture.
