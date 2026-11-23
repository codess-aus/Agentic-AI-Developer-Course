---
title: Execution boundaries
description: Identify the repository, branch, runtime, network, tools, and identity that bound a real agent task.
hero: AI Agent Execution Boundaries Infographic.png
hero_alt: A development agent operates inside explicit repository, branch, workflow, and permission boundaries rather than unrestricted access.
eyebrow: 03 / TOOLS & BOUNDARIES / LESSON 16
---

# Execution boundaries

An execution context includes the code available to the task, the working branch, the runtime, network access, tools, and credentials. Inspect the actual context before trusting its boundaries.

## Check each layer

**Repository and branch:** which repositories can this environment read or change, and where will edits land? For the workshop, use one disposable repository and a dedicated branch.

**Runtime and network:** is execution local, GitHub Actions-based, or in a cloud sandbox? What services can it contact, and does it share state with other tasks?

**Identity and tools:** which credentials are injected, what can they reach, and can a command bypass the intended tool interface?

A branch isolates proposed changes, but is not a security sandbox. Code executing on a runner can still access whatever the runner and credentials expose.

## Try it: write a boundary statement

Before a task starts, record the repository, branch, execution environment, permitted external services, and token scope. State what is unknown and verify it through settings or documentation.

!!! success "Checkpoint"
    Your boundary statement describes enforced capabilities, not only desired behavior. No production credential is available merely because the agent might need it later.

## Go deeper

[Copilot environments and surfaces](https://docs.github.com/en/copilot/concepts/copilot-surfaces/copilot-on-github) explains why execution characteristics differ. Use [secure Actions guidance](https://docs.github.com/en/actions/security-for-github-actions) for workflows and runners.
