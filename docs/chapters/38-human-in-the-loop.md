---
title: Humans at decision points
description: Put human judgment where consequences matter and give reviewers enough evidence to make a real decision.
hero: Human-in-the-Loop Workflows with Michelle and Coda.png
hero_alt: Michelle and Coda represent human oversight at merge, deployment, and sensitive-access decisions while routine agent work proceeds within guardrails.
eyebrow: 06 / GOVERNANCE / LESSON 38
---

# Humans at decision points

Human oversight should be targeted, informed, and accountable. Asking for approval on every harmless read encourages fatigue without necessarily improving safety.

## Make approval meaningful

Place people at consequential transitions: accepting a change, expanding scope, accessing sensitive resources, or deploying to production. Let bounded analysis and routine validation run without unnecessary interruptions.

Give reviewers a small diff, clear intent, evidence tied to the current commit, known risks, and a rollback plan when appropriate. Route to people with the relevant ownership and context.

Watch for rubber-stamping. Long queues and poor evidence can turn review into a button press to unblock automation. Measure whether review catches meaningful issues, not just how quickly an approval arrives.

## Try it: prepare the review packet

Create a short approval request for your dependency update. Explain what changed, what proved the vulnerability was resolved, what behavior was tested, and what remains uncertain. State the decision requested explicitly.

!!! success "Checkpoint"
    The reviewer can approve, request changes, or escalate based on evidence. A missed deadline or absent reviewer does not silently convert into authorization.

## Go deeper

Compare [pull request reviews](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/about-pull-request-reviews) with [deployment protection rules](https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments). They protect different decisions.
