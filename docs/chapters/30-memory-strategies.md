---
title: Memory strategies
description: Keep working context focused, reusable knowledge curated, and authoritative records outside the session.
hero: Agent Memory Strategies Infographic.png
hero_alt: Short-term context, curated long-term knowledge, and external GitHub records form complementary memory layers with deliberate maintenance.
eyebrow: 05 / MEMORY & EVALUATION / LESSON 30
---

# Memory strategies

More context is not always better context. Repeated, stale, or contradictory information makes it harder for an agent to stay aligned.

## Use three layers

**Working context** supports the current task: recent feedback, relevant files, and immediate next steps. Keep it focused.

**Curated reusable knowledge** captures stable conventions and consequential decisions. Give it a source, owner, and review process. Repository instructions are useful for contributor-wide guidance.

**External records** hold authoritative requirements, proposals, and validation evidence. Link to the issue or workflow run instead of copying the same claim into every prompt.

Never put credentials, personal details, or sensitive customer data into memory merely because they might be convenient later. Retention and access should match the information's purpose.

## Try it: trim a handoff

Rewrite a long task transcript into a short summary containing the goal reference, accepted decisions, current commit, evidence links, and next action. Remove transient commands, duplicated requirements, and superseded guesses.

!!! success "Checkpoint"
    The summary helps navigation without becoming a competing source of truth. A future reader can verify every important claim.

## Go deeper

Use [repository instructions](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions) for stable project guidance and [workflow artifacts](https://docs.github.com/en/actions/concepts/workflows-and-actions/workflow-artifacts) for task-specific results.
