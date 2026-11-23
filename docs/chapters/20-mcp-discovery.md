---
title: Discover MCP servers
description: Understand what MCP standardizes and evaluate a server's tools, data flows, and permissions before connecting it.
hero: MCP Servers_ Discovery and Control-2.png
hero_alt: MCP server discovery connects agents to external tools and context, with explicit evaluation and access control before use.
eyebrow: 03 / TOOLS & BOUNDARIES / LESSON 20
---

# Discover MCP servers

The **Model Context Protocol**, or MCP, standardizes how clients connect models to external tools and context. It does not automatically make a server safe, authorize every operation, or guarantee that returned content is reliable.

## Discover capability, not just a name

A server can expose read operations, write operations, or both. Inspect the actual tool descriptions, authentication model, deployment location, and data returned. For a dependency task, a read-only advisory lookup may be enough; repository-wide write access is not a reasonable default.

GitHub's MCP Registry can help discover integrations. Registry presence is a starting point for evaluation, not a substitute for assessing the particular publisher, version, and permissions.

Configuration and defaults vary across IDEs, CLI, and cloud environments. Check your selected client before assuming a server is available.

## Try it: choose the smallest connection

Find a server relevant to your scenario. Without providing credentials, identify one useful tool and one capability you would disable. Describe what information would leave your environment.

!!! success "Checkpoint"
    Your integration proposal names the server, publisher, authentication scope, required tools, and data boundary. "It supports MCP" is not your entire trust argument.

## Go deeper

Read [GitHub's MCP overview](https://docs.github.com/en/copilot/concepts/customizations/mcp), the [MCP specification and introduction](https://modelcontextprotocol.io/introduction), and browse the [GitHub MCP Registry](https://github.com/mcp).
