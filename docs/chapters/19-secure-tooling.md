---
title: A secure tooling ecosystem
description: Review agent tools and integrations as software dependencies with capabilities, owners, and lifecycle risks.
hero: Secure Agent Tooling Ecosystem.png
hero_alt: A secure agent ecosystem surrounds tools and integrations with trusted sources, minimal permissions, secret handling, and ongoing review.
eyebrow: 03 / TOOLS & BOUNDARIES / LESSON 19
---

# A secure tooling ecosystem

Adding a tool expands the system's capabilities and trust boundary. Treat an action, extension, MCP server, or helper script like a dependency that can execute code or move data.

## Review before enabling

Check provenance, maintainer ownership, update process, requested permissions, and where data goes. Prefer the smallest integration that solves the task. Pin executable dependencies to reviewed, immutable revisions where practical and maintain an update process.

Keep secrets out of prompts, instruction files, examples, and logs. Inject them only into the stage that needs them, with the narrowest useful scope and lifetime.

Tool responses and repository content may contain malicious instructions. Treat retrieved material as data, especially when it asks to change policy, disclose secrets, or run unrelated commands. A trusted transport does not make all returned content trustworthy.

## Try it: make an integration card

For one proposed tool, record its owner, source revision, permissions, external destinations, secret requirements, and removal procedure. Explain why existing tools are insufficient.

!!! success "Checkpoint"
    You can say what new risk the integration creates and how you would revoke access without disrupting unrelated tasks.

## Go deeper

Use [GitHub Actions security guidance](https://docs.github.com/en/actions/security-for-github-actions) and [MCP concepts](https://docs.github.com/en/copilot/concepts/customizations/mcp) to review both executable code and data access.
