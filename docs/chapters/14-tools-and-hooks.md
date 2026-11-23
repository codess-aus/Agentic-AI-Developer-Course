---
title: Tools, hooks, and security
description: Treat tool calls as capabilities and use supported hooks as one layer of defense.
hero: Tools, Hooks, and Security Infographic.png
hero_alt: Tools provide agent capabilities while pre-tool, post-tool, and error hooks support checks, logging, and escalation around execution.
eyebrow: 03 / TOOLS & BOUNDARIES / LESSON 14
---

# Tools, hooks, and security

Tools turn a language model's proposed action into a real effect. Reading a file, executing a command, calling an API, and deploying an application have different risk profiles.

## Constrain capabilities first

Inventory the tools your agent can access and remove those the task does not need. Keep credentials scoped to the task. Prefer a read-only analysis stage followed by an explicitly authorized write stage.

Where your client supports them, hooks can run checks around tool execution. A pre-tool hook may block a prohibited operation; a post-tool hook can record results; an error hook can support escalation. Exact events and blocking behavior vary by product.

Hooks are not a complete sandbox. Shell-command filtering is difficult to make comprehensive, and a hook cannot constrain credentials used outside its scope. Combine it with permissions, isolation, and platform policy.

## Try it: classify the tools

List the operations needed for your dependency task. Mark each read, write, execute, or deploy. For every write or execution capability, explain the constraint and evidence you need. Identify one operation that should be denied entirely.

!!! success "Checkpoint"
    Removing a dangerous tool actually removes the capability from the task. It does not merely add a sentence asking the model to behave.

## Go deeper

Start with [Copilot customization](https://docs.github.com/en/copilot/concepts/customization) and verify hook support for your selected surface before implementing a guardrail.
