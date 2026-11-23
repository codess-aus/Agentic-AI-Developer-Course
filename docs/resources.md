---
title: Resources and connections
description: The two GH-600 presenter-script learning paths, deeper GitHub documentation and blogs, and Michelle's public links.
---

# Keep exploring

<p class="workshop-lead">Go from the workshop's mental models to the official training, current platform documentation, and practical stories from the community.</p>

## The two presenter-script references

These are the two learning paths cited in the original **GH-600 presenter scripts** file. The workshop uses their topics as a guide and adds original explanations, activities, and operational caveats.

<div class="workshop-cards" markdown>

<div class="workshop-card" markdown>
### Developing in Agentic AI Systems, Part 1 of 2
Foundations, architecture and SDLC integration, tooling, MCP, and execution environments.

[Open Microsoft Learn Part 1 →](https://learn.microsoft.com/en-us/training/paths/gh-developing-agentic-systems-1)
</div>

<div class="workshop-card" markdown>
### Developing in agentic AI systems, Part 2 of 2
Multi-agent orchestration, memory and evaluation, governance, and operational reliability.

[Open Microsoft Learn Part 2 →](https://learn.microsoft.com/en-us/training/paths/github-agentic-systems-part-two/github-agentic-systems-part-two)
</div>

</div>

The [official GH-600 course overview](https://learn.microsoft.com/en-us/training/courses/gh-600t00) describes the training scope and intended audience. The [original presenter script](https://github.com/codess-aus/Agentic-AI-Developer-Course/blob/main/GH-600%20presenter%20scripts.md) remains in this repository.

## GitHub documentation by topic

| Topic | Start here | Use it to answer |
| --- | --- | --- |
| Copilot surfaces and environments | [Copilot on GitHub](https://docs.github.com/en/copilot/concepts/copilot-surfaces/copilot-on-github) | Where does this session run, and what can it do? |
| Custom instructions | [Repository instructions](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions) | How do I share stable project guidance? |
| Specialized roles | [Custom agents](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-custom-agents) | Which role and tools fit the task? |
| External tools | [MCP concepts](https://docs.github.com/en/copilot/concepts/customizations/mcp) | What changes when I connect a server? |
| Reusable context | [Copilot Memory](https://docs.github.com/en/copilot/concepts/prompting-and-context/copilot-memory) | What memory behavior does this product support? |
| Identity and access | [GITHUB_TOKEN](https://docs.github.com/en/actions/tutorials/authenticate-with-github_token) | Which job actually needs write access? |
| Workflow data | [Job outputs](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/pass-job-outputs) | How do stages exchange structured values? |
| Coordination | [Concurrency](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/control-workflow-concurrency) | What happens when runs overlap? |
| Evidence | [Workflow artifacts](https://docs.github.com/en/actions/concepts/workflows-and-actions/workflow-artifacts) | How do I preserve commit-specific reports? |
| Acceptance policy | [Rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets) | What makes review and checks enforceable? |
| Ownership | [CODEOWNERS](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners) | Who reviews sensitive changes? |
| Deployment | [Environments](https://docs.github.com/en/actions/concepts/workflows-and-actions/deployment-environments) | Where should production authorization happen? |
| Supply-chain evidence | [Dependency review](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-dependency-review) | Did the dependency change introduce risk? |
| Workflow security | [Security for GitHub Actions](https://docs.github.com/en/actions/security-for-github-actions) | How do I handle untrusted code and inputs? |

## Read the GitHub Blog

[Agent mode 101](https://github.blog/ai-and-ml/github-copilot/agent-mode-101-all-about-github-copilots-powerful-mode/) explains the goal-driven, iterative experience of IDE agent mode.

[Coding agent 101](https://github.blog/ai-and-ml/github-copilot/github-copilot-coding-agent-101-getting-started-with-agentic-workflows-on-github/) introduces the asynchronous pull-request contributor model. These introductory articles provide context; consult the current documentation for interfaces, availability, and security boundaries.

Explore [GitHub Agentic Workflows](https://github.github.io/gh-aw/) for a separate, outcome-oriented automation approach, and the [GitHub MCP Registry](https://github.com/mcp) for discoverable integrations. Neither replaces a review of capabilities, permissions, and provenance.

## Connect with Michelle

Learn more with **Michelle Mei-Ling Sandford**, and keep Coda company along the way.

[Scaling Guacamole · blog](https://www.scaling-guacamole.com){ .md-button .md-button--primary }
[Michelle's website](https://codess-aus.github.io/Codess/){ .md-button }

| Find Michelle | Public profile |
| --- | --- |
| GitHub | [@codess-aus](https://github.com/codess-aus) |
| LinkedIn | [Michelle Sandford](https://www.linkedin.com/in/michellesandford/) |
| Bluesky | [@codess-aus.bsky.social](https://bsky.app/profile/codess-aus.bsky.social) |
| YouTube | [Michelle Sandford](https://www.youtube.com/c/MichelleSandford) |

## About this workshop

The slide artwork and presenter script are supplied by this repository. Lesson text and exercises expand on those themes with links to original sources rather than reproducing the official training.

The site uses [MkDocs](https://www.mkdocs.org/), [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/), and self-hosted [Mona Sans](https://github.com/github/mona-sans), distributed under the [SIL Open Font License](assets/fonts/OFL.txt). Source licensing is recorded in the repository's [LICENSE](https://github.com/codess-aus/Agentic-AI-Developer-Course/blob/main/LICENSE).

Use the theme switch for light or dark mode. Lessons have text equivalents for the slide concepts, keyboard navigation, visible focus states, and full-size slide links. Product features and administrative controls vary by plan and organization policy; always verify the current documentation before applying a workshop pattern to production.
