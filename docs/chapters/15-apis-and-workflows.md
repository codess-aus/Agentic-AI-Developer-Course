---
title: APIs and workflows
description: Understand how authenticated API calls, deterministic workflows, and agentic automation fit together.
hero: GitHub Agents_ APIs, Workflows and Collaboration.png
hero_alt: GitHub APIs connect agent actions to issues and pull requests while Actions workflows provide validation and collaboration records.
eyebrow: 03 / TOOLS & BOUNDARIES / LESSON 15
---

# APIs and workflows

Agents work through authenticated interfaces. The important questions are which identity makes each request, which permissions it holds, and where the result is recorded.

## Distinguish the execution layers

The REST and GraphQL APIs expose repository operations such as reading issues or updating pull requests. A token bounds the request; an agent's intention does not expand that token's access.

GitHub Actions runs explicit jobs in response to configured events. It is well suited to repeatable validation and deployment. Agentic automation can add interpretation for bounded, open-ended work, but should not make a deterministic test suite optional.

If you explore GitHub Agentic Workflows, consult its current documentation for Markdown definitions, compilation, and controlled outputs. It is a distinct technology, not another name for every workflow that invokes an agent.

## Try it: trace one operation

For "post a remediation summary", identify the API operation, required repository scope, token source, triggering event, and durable result. Compare that with "push a fix": it needs a different capability and should not inherit unrelated deployment access.

!!! success "Checkpoint"
    You can draw the line from identity to permission to action to evidence, and can explain why a read-only analysis token cannot publish a code change.

## Go deeper

Read [GITHUB_TOKEN authentication](https://docs.github.com/en/actions/tutorials/authenticate-with-github_token), the [REST API documentation](https://docs.github.com/en/rest), and [GitHub Agentic Workflows](https://github.github.io/gh-aw/).
