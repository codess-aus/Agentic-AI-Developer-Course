---
title: Developing in Agentic AI Systems
description: A practical, slide-led workshop for designing, supervising, and governing AI agents on GitHub.
hero: Developing in Agentic AI Systems.png
hero_alt: Michelle, Coda the dog, and a purple robot connect code, checks, and delivery tools. Michelle's shirt reads "I'm the Human in the loop".
eyebrow: THE AGENTIC AI FIELD GUIDE
---

# Capable agents. Thoughtful humans.

<p class="workshop-lead">Build systems that do more than suggest code. Learn to give AI agents a clear goal, safe boundaries, and evidence that their work actually works.</p>

<div class="workshop-stats" role="group" aria-label="Workshop at a glance">
  <span>6 modules</span>
  <span>41 slide-led lessons</span>
  <span>Self-paced + hands-on</span>
  <span>GitHub as your control plane</span>
</div>

[Start the workshop →](chapters/01-assistance-to-action.md){ .md-button .md-button--primary }
[Explore the resources](resources.md){ .md-button }

## Your field guide

Join **Michelle and Coda** for a practical journey from agent fundamentals to operating governed, multi-agent workflows. Every lesson begins with its original slide, explains the ideas in accessible text, and gives you a small activity with a concrete outcome.

The central principle runs through everything: **agents propose; people and policy accept**. More autonomy should mean better boundaries and stronger evidence, not less accountability.

<div class="workshop-cards" markdown>

<div class="workshop-card" markdown>
### 01 / Understand the fundamentals
Distinguish assistants from agents, explore the plan-act-evaluate loop, and learn why GitHub is both a record and a control plane.

[Explore foundations →](chapters/01-assistance-to-action.md)
</div>

<div class="workshop-card" markdown>
### 02 / Design the architecture
Turn an ambiguous goal into a task contract, a reviewable plan, and a pull request backed by meaningful checks.

[Design your system →](chapters/07-architecture.md)
</div>

<div class="workshop-card" markdown>
### 03 / Connect tools safely
Understand execution contexts, custom agents, hooks, MCP servers, credentials, and the difference between guidance and enforcement.

[Explore tools and boundaries →](chapters/14-tools-and-hooks.md)
</div>

<div class="workshop-card" markdown>
### 04 / Coordinate the work
Give agents distinct roles, isolate parallel changes, build observable handoffs, and recover when workflows fail.

[Coordinate your agents →](chapters/23-multi-agent.md)
</div>

<div class="workshop-card" markdown>
### 05 / Remember and evaluate
Persist useful state, resume across tools, catch context drift, and improve your system using objective evaluation signals.

[Build continuity →](chapters/29-memory-state-evaluation.md)
</div>

<div class="workshop-card" markdown>
### 06 / Govern for the long run
Match autonomy to risk, apply least privilege, place humans at consequential decisions, and maintain an audit trail.

[Put governance into practice →](chapters/35-governance.md)
</div>

</div>

## Browse every chapter

Jump straight to any lesson by its slide.

<!-- chapter-gallery -->

## Before you begin

You should be comfortable with repositories, branches, pull requests, and basic CI/CD concepts. Bring a GitHub account and a **disposable practice repository** with a small application and a test command you can run.

A Copilot subscription and enabled agent features are useful for live exercises, but you can complete the design activities without them. Repository administration is needed for rulesets, environments, and some policy settings. Availability varies by plan and organization policy.

!!! tip "One scenario, increasing depth"
    Use a dependency-remediation task throughout the workshop: update one vulnerable dependency, preserve behavior, prove the vulnerable version is no longer present, and submit a focused pull request. Never experiment with production secrets or infrastructure.

## How to work through it

Read the slide and lesson, try the activity, then compare your output with the checkpoint. Use **Previous**, **Home**, and **Next** at the bottom of every page, the module navigation, or search to move around. The light/dark switch follows your system preference until you choose a mode.

The original [GH-600 presenter script](https://github.com/codess-aus/Agentic-AI-Developer-Course/blob/main/GH-600%20presenter%20scripts.md) guides this workshop. The [Resources page](resources.md) links both Microsoft Learn paths, deeper GitHub reading, Michelle's blog, and her socials. This is a companion workshop, not a replacement for the official training or an assurance of certification readiness.

!!! note "Read product boundaries in context"
    Copilot capabilities evolve across IDE, CLI, GitHub Actions-based, and cloud sandbox environments. Branch-only changes, propose-only agents, and human deployment approval are workshop design choices unless the current product documentation explicitly guarantees them.
