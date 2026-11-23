---
title: Least privilege
description: Give each job and tool only the permissions needed for its specific action and lifetime.
hero: Least Privilege, Thoughtfully Applied.png
hero_alt: Narrow, task-specific access limits an agent's reach, with separate read-only analysis and explicitly authorized write capabilities.
eyebrow: 06 / GOVERNANCE / LESSON 39
---

# Least privilege

Permissions define the agent's reachable blast radius. Start with the minimum capability and elevate only the stage that needs it.

## Separate analysis from publication

An analysis job usually does not need write access. A job that posts a pull request comment may need `pull-requests: write`, but not code writes or production credentials. Permission requirements also depend on the exact API operation and trigger.

```yaml
# Workflow-level defaults remain read-only.
permissions:
  contents: read

jobs:
  analyze:
    runs-on: ubuntu-latest
    steps:
      - run: echo "Read-only analysis stage"

  # A real publisher would consume validated results and use a trusted implementation.
  publish:
    needs: analyze
    runs-on: ubuntu-latest
    permissions:
      contents: read
      pull-requests: write
    steps:
      - run: echo "Only this job has pull request write permission"
```

This is a permissions fragment, not a complete workflow or a recommendation to give untrusted pull-request code a write token. Fork and event restrictions still apply.

## Try it: justify every grant

List each token permission your task needs and the exact operation requiring it. Remove unused grants and identify where credentials should expire or be revoked.

!!! success "Checkpoint"
    Read-only stages never receive unnecessary write credentials. Publishing is a separately reviewed capability, not a side effect of analysis.

## Go deeper

Read [GITHUB_TOKEN permissions](https://docs.github.com/en/actions/tutorials/authenticate-with-github_token) and [security hardening guidance](https://docs.github.com/en/actions/security-for-github-actions).
