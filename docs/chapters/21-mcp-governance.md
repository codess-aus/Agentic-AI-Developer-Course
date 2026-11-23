---
title: Govern MCP access
description: Separate server discovery, client policy, tool authorization, credentials, and network controls.
hero: MCP Governance_ Servers, Registries and Allow Lists-1.png
hero_alt: MCP governance combines server review, registry policy, allowlists, tool selection, and least-privilege credentials.
eyebrow: 03 / TOOLS & BOUNDARIES / LESSON 21
---

# Govern MCP access

Discovery answers "what can I connect?" Governance answers "what may this task use, under which identity, with which data?"

## Use multiple boundaries

An approved registry or server list controls which integrations can be selected where supported. A tool allowlist narrows the operations exposed to the agent. Credential scope limits the underlying service account. Network restrictions constrain reachable destinations.

These are different layers. Approving a server does not authorize all its tools. Hiding a write tool does not remove a broadly scoped secret from an unrestricted runtime. A policy may also apply only to particular subscriptions or managed surfaces.

Assign an owner to every approved integration. Review updates, tool-description changes, permissions, and data handling. Revoke unused access instead of letting the list grow indefinitely.

## Try it: write an approval decision

Decide whether your advisory lookup server should be approved. Include the allowed operations, denied capabilities, credential owner, review date, and evidence needed after a server update. Describe how to disable it during an incident.

!!! success "Checkpoint"
    Your policy can be implemented in the chosen client and organization settings. Anything unsupported is called out rather than described as already enforced.

## Go deeper

[GitHub's MCP documentation](https://docs.github.com/en/copilot/concepts/customizations/mcp) explains surface-specific behavior and policy scope. Check current administrative settings before promising organization-wide coverage.
