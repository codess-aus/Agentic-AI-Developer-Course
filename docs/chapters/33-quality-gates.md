---
title: Enforce quality gates
description: Select evaluation signals that prove the task outcome and make required evidence binding.
hero: GitHub Quality Gates Infographic.png
hero_alt: Build, test, security, policy, and review signals form quality gates before an agent contribution can be accepted.
eyebrow: 05 / MEMORY & EVALUATION / LESSON 33
---

# Enforce quality gates

Evaluation should prove the task's outcome, not merely confirm that some automation ran.

## Match the signal to the claim

| Claim | Useful evidence |
| --- | --- |
| The update builds | Build result for the proposed commit |
| Behavior is preserved | Relevant automated tests and targeted review |
| The vulnerable version is removed | Resolved dependency graph and advisory evidence |
| Scope stayed bounded | Diff inspection and appropriate policy checks |
| Acceptance is authorized | Required checks and current approvals |

Security signals have different purposes. Code scanning analyzes code, dependency review evaluates dependency changes, and secret scanning looks for exposed credentials. Availability depends on repository and plan settings; select controls that fit the actual risk.

Make relevant checks required. Avoid acceptance paths where a skipped or missing check is mistaken for a validated result.

## Try it: strengthen "done"

Rewrite "CI is green" into three measurable acceptance statements for your dependency update. Name the evidence source for each and verify that it refers to the exact proposed commit.

!!! success "Checkpoint"
    A plausible diff with missing advisory evidence is still incomplete. Reviewers can see what each check does and does not prove.

## Go deeper

Read [dependency review](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-dependency-review) and [code scanning](https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning).
