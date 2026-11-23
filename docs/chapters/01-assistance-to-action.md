---
title: From assistance to action
description: Recognize the goal, tools, durable changes, and feedback loop that make development work agentic.
hero: From Assistance to Action_ Agentic AI.png
hero_alt: A purple illustrated guide contrasts receiving AI help with delegating a goal that leads to tool use, repository changes, and evaluated outcomes.
eyebrow: 01 / FOUNDATIONS / LESSON 01
---

# From assistance to action

An agentic development system does not stop at an answer. It works toward a goal, chooses actions using tools, inspects the results, and adjusts its approach. Its work can leave durable artifacts: branches, commits, issues, pull requests, and test reports.

## Follow the work, not the label

A chat interface can provide advice in one interaction and perform agentic work in another. The distinction is the behavior and granted capabilities, not the presence of a chatbot or a particular model.

For our dependency-remediation scenario, advice is a suggested upgrade command. Agentic work includes inspecting the manifest, changing the dependency and lockfile, running relevant tests, and preparing a reviewable contribution. The system must still know when to stop or escalate.

## Try it: draw the boundary

Write a four-line delegation brief in your practice issue: the goal, permitted tools, expected repository artifacts, and the evidence required before completion. Explicitly exclude merge and deployment authority.

!!! success "Checkpoint"
    Someone else can identify what the system will change, how it will evaluate the result, and which decision remains human-owned. A confident response alone is not completion evidence.

## Go deeper

[GitHub Blog: Agent mode 101](https://github.blog/ai-and-ml/github-copilot/agent-mode-101-all-about-github-copilots-powerful-mode/) explains the iterative tool loop in IDE agent mode. Compare that interactive experience with [Copilot on GitHub](https://docs.github.com/en/copilot/concepts/copilot-surfaces/copilot-on-github), where execution environment and available capabilities can differ.
