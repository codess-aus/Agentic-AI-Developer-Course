---
title: Reliable workflow handoffs
description: Pass structured values between jobs, select the right context, and guard event-specific work.
hero: Reliable Agent Workflows Infographic.png
hero_alt: Reliable workflows use explicit inputs and outputs, event-aware conditions, least-privilege jobs, validation, and controlled handoffs.
eyebrow: 02 / ARCHITECTURE / LESSON 13
---

# Reliable workflow handoffs

Workflow logs are for people. **Outputs** are contracts between steps and jobs. Environment variables configure execution; they do not automatically become cross-job state.

## Make dependencies explicit

This complete, read-only demonstration publishes a value and consumes it in a dependent job. Save it as a workflow only in your practice repository.

```yaml
name: Handoff demonstration
on: workflow_dispatch
permissions:
  contents: read
jobs:
  plan:
    runs-on: ubuntu-latest
    outputs:
      scope: ${{ steps.contract.outputs.scope }}
    steps:
      - id: contract
        run: echo "scope=dependency-only" >> "$GITHUB_OUTPUT"
  inspect:
    needs: plan
    runs-on: ubuntu-latest
    steps:
      - name: Inspect the handoff
        env:
          TASK_SCOPE: ${{ needs.plan.outputs.scope }}
        # Pass data through the environment instead of interpolating it into shell code.
        run: printf 'Received scope: %s\n' "$TASK_SCOPE"
```

Use `github` for event metadata, `vars` for nonsensitive configuration, and `secrets` for sensitive values. Guard pull-request-only jobs when a workflow also supports manual or scheduled triggers. Treat issue titles, branch names, and other external values as untrusted data.

## Try it: follow the value

Run the demonstration manually. Locate the step output, job output, `needs` dependency, and receiving environment variable.

!!! success "Checkpoint"
    The receiving job cannot run before its producer. No downstream step needs to scrape logs to discover the scope.

## Go deeper

Read [passing job outputs](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/pass-job-outputs) and [script injection guidance](https://docs.github.com/en/actions/concepts/security/script-injections).
