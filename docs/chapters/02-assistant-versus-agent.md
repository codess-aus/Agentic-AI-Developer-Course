---
title: Assistant versus agent
description: Compare advisory help with delegated execution without confusing autonomy with accountability.
hero: Assistant vs Agent in GitHub.png
hero_alt: An assistant offers suggestions while an agent follows a goal through repository actions and checks; human review remains part of acceptance.
eyebrow: 01 / FOUNDATIONS / LESSON 02
---

# Assistant versus agent

An **assistant** helps you decide or write. An **agent** can move a delegated task forward using tools. Neither behavior implies that the result is correct, safe, or ready to merge.

## Compare the same task

| Dependency update | Assistant-style help | Agentic execution |
| --- | --- | --- |
| Understand the alert | Explains affected versions | Inspects the alert and dependency graph |
| Prepare a change | Suggests commands and edits | Updates allowed files on a working branch |
| Validate | Recommends tests | Runs tests and reads their output |
| Respond to failure | Explains an error you paste | Revises within its limits or escalates |
| Accept the result | You own the decision | People and configured policy still own acceptance |

This is a teaching distinction, not a permanent classification of products. What matters is what the current session can actually do.

## Try it: compare two requests

First request an explanation of how to update a dependency. Then, in a disposable repository, draft a second request delegating the update with a narrow scope and a required test command. Compare expected outputs before allowing any execution.

!!! success "Checkpoint"
    Your second request names an artifact and an observable success condition, not just "fix it". It also names the stopping point: a proposal ready for review, not permission to merge.

## Go deeper

Read [GitHub Blog: Coding agent 101](https://github.blog/ai-and-ml/github-copilot/github-copilot-coding-agent-101-getting-started-with-agentic-workflows-on-github/) for the asynchronous pull-request model. Treat its interface details as historical context and consult [current Copilot documentation](https://docs.github.com/en/copilot/concepts/copilot-surfaces/copilot-on-github) for today's surfaces.
