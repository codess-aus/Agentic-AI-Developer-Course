# Developing in Agentic AI Systems: Content

### References: 
- [Developing in Agentic AI Systems Part 1 of 2](https://learn.microsoft.com/en-us/training/paths/gh-developing-agentic-systems-1)
- [Developing in agentic AI systems part 2 of 2](https://learn.microsoft.com/en-us/training/paths/github-agentic-systems-part-two/github-agentic-systems-part-two)

## What makes an AI system agentic in a development context

## What's the difference between an AI assistant and an AI agent?

An assistant is reactive. It waits for you to decide what happens next. It can suggest code, explain an error, or summarize a set of changes, and that's genuinely useful. But it doesn't move the work forward on its own. You're still the one doing each step in the repository.

An agent is goal-driven. You give it a task, and it works out an approach and takes the steps to get it done. It uses tools to do that, like the GitHub API, CI workflows, and the ability to write to the repository. That means it produces real, lasting results: branches, commits, and pull requests. And it doesn't stop at the first attempt. It iterates based on feedback from checks, reviews, and security scans, until the work meets the bar.

On GitHub, that usually looks like a pull-request workflow. The agent makes its changes on a branch, opens a pull request, and then waits. Reviews and validation happen before anything merges.

So the agent does the work, and people and policy still decide what gets accepted.

## Assistant versus agent

So how can you tell whether an AI system is acting as an assistant or as an agent?

It's acting as an assistant when it gives you suggestions or explanations, but doesn't take any action in the repository. You still have to apply every step yourself.

It's acting as an agent when it can hold onto a goal across several steps, decide what to do next along the way, use tools, create or change lasting artifacts like branches, commits, and pull requests, and keep improving its work based on feedback.

On GitHub, you can see agent behavior in the same places you already look. Branches and commits show what changed. Pull requests show what's being proposed, why, and for review. Workflows and checks show the evidence. And review comments and approvals show what people accepted or rejected. An agent doesn't replace your workflow. It joins it, as another participant.

Here's the difference in practice. Imagine a security alert comes in about an outdated dependency.

With an assistant, you ask: how do I safely update this dependency? It gives you the commands to run, a checklist of risks, and some suggested code changes. All helpful. But you still create the branch, make the changes, and open the pull request yourself.

With an agent, it handles the task itself. It creates a branch. It updates the dependency and the lockfile. It opens a pull request with a summary and a plan. Then it waits for the CI checks and review feedback, and revises the change if needed.

Same alert, same goal. The difference is who moves the work forward. And in both cases, people still decide what gets merged.

## Explain the agent lifecycle: plan, act, evaluate

Agents don't make one decision and stop. They work in cycles. The core model is plan, act, evaluate. It's a loop. The agent keeps planning, acting, and evaluating until the task meets its success criteria.

Plan. First, the agent works out what the goal is and what steps it'll take to get there. In a good system, that plan isn't hidden inside the agent. It's written down where people can review it, like a structured plan in the pull request description, or a linked issue or checklist that sets out the scope and success criteria. A plan is easiest to review when it says three things: what will change, how you'll know it worked, and how to roll back or escalate if it doesn't.

Act. Next, the agent carries out the plan in the repository. It creates a branch, pushes commits, opens a pull request, and responds to review feedback. This keeps execution bounded. Everything happens in one repository, on a branch, through a pull request, never as uncontrolled changes straight to main.

Evaluate. Then the agent, and the people supervising it, check the results using signals from GitHub itself. Status checks show whether it builds and passes tests. Code review shows whether people approve. And security signals, like code scanning, secret scanning, dependency alerts, and push protection, show whether it's safe. With rulesets or branch protection, those checks have to pass before anything merges, so evaluation becomes an enforced gate, not a suggestion. The key lesson: judge the work by these signals, not by how confident the agent sounds.

And evaluation isn't the end. If checks fail, risks remain, or requirements aren't met, the loop continues. Say an agent proposes a dependency update. The plan names the package, the action updates the files, and CI and security checks evaluate it. If a workflow fails, or the vulnerability is still there, the work isn't done. The agent revises the plan, adjusts the change, or hands it to a person.

A good agent system makes every phase visible. The plan can be inspected, the actions stay inside repository workflows, and evaluation uses objective signals. Take any of those away, and trust goes with it.

## Identify responsibilities, risks, anti-patterns, and traceability needs

As agents get more capable, it's tempting to think responsibility moves to the system. It doesn't. Agents can do the work, but people stay accountable for the outcome, and for the controls around it.

When an agent opens a pull request, it's taking part in the workflow, not taking ownership. The people accountable are the ones who defined the task, set the permissions, chose and configured the controls, and approved the change. The pull request model makes that explicit. The agent proposes. People decide.

Early agent systems tend to fail in four predictable ways.

Planless execution. The agent starts changing code with no clear approach anyone can inspect. The fix: require a plan section in the pull request template, and require review before merge.

Over-permissioned agents. The agent's token can do far more than it needs to. The fix: least-privilege tokens, environments with required reviewers, and limits on who can trigger workflows.

Hidden reasoning. You only see the final diff, not the plan, the assumptions, or the decisions behind it. The fix: require a plan, link the workflow runs, and record decisions in pull request comments.

Blind trust in automation. "CI passed, ship it." But checks only catch what they're designed to catch. A passing build doesn't mean the change is complete, appropriate, or low risk. The fix: combine checks with code owners, required reviews, and approvals based on risk.

To supervise an agent well, you need more than the final diff. You need a trail. At minimum: a stated goal, an inspectable plan, a bounded set of changes on a branch, automated evidence from workflow runs, a human review and approval, and a clear outcome, whether that's a merge, a revert, or an escalation. That isn't just for compliance. When something breaks, you need to know what changed, who approved it, and why.

Imagine an agent's security fix passes CI, but later causes a regression. Don't just ask whether the agent got it wrong. Ask whether the system made the mistake understandable and preventable. Was there a visible plan? Did the right people review it? Did the checks match the risk? And can you reconstruct what happened?

The takeaway: agents change who does the work, not who owns the outcome.

## Describe GitHub as the system of record and control plane

Agents need more than a place to store code. They need an environment that captures intent, records what happened, enforces validation, and applies policy. In this learning path, that environment is GitHub. And it plays two roles.

First, GitHub is the system of record. It holds the artifacts where development work is proposed and evaluated. Repositories and branches. Commits and pull requests. Issues and discussions, which capture context and intent. Workflow runs and artifacts, which provide evidence. And review history, which records decisions. These artifacts support development, and they let you inspect what an agent did afterwards.

Second, GitHub is the control plane. When it's configured, it provides enforcement points that shape what agents can and can't do. Pull requests make agent work reviewable before it merges. Required reviews add a human approval gate. Required status checks turn CI evidence into enforceable policy. Code owners route changes to the right experts based on the files they touch. Rulesets and branch protection apply consistent guardrails. And environments control approvals for deployments and access to secrets.

One caveat: enforcement only works when these controls are switched on, and that's usually an admin task.

GitHub Actions belongs in the control plane too, and permissions matter as much as checks. Set the workflow token to read-only by default. Give higher permissions only to the jobs that need them. And use environments and approvals for sensitive secrets and deployments. For agents, what the agent can do often comes down to what its token and tool credentials can do.

Here's how it works in practice. An agent opens a pull request with a security fix. A person may need to approve its workflows before they run, so privileged workflows don't run automatically on untrusted code. Then GitHub makes the change visible in the pull request. Code owners route it to the right reviewers. Required checks and workflows evaluate it. Merging is blocked until every policy requirement is met. And if a job needs protected secrets or a deployment, it waits for an approver.

That's what it means to call GitHub the control plane. It's where enforcement happens.

The takeaway: GitHub isn't just where agent work is stored. It's where it's supervised, validated, and governed.

## Apply the contributor model to agent-generated work

Here's a reliable way to evaluate agent output: stop treating it as something different from normal development work. Treat it as a contribution.

On GitHub, the pull request is the natural unit of contribution. And whether a person or an agent wrote it, a pull request should answer the same questions. Does it solve the intended problem? Is the scope appropriate, and explained? Do the required checks pass? Are the right owners reviewing the areas it touches? And does it fit your standards, architecture, and policy?

This model protects you from two opposite mistakes. Excessive suspicion, where you reject work just because AI wrote it. And excessive trust, where you accept work just because automation produced it. The contributor model says: judge the work by the standards of your workflow, not by the novelty of the author.

When you review an agent's pull request, use a simple checklist. Intent: is there a clear goal and a visible plan? Scope: do the changed files match the plan? Evidence: do the required checks pass, with logs and artifacts available? Ownership: have the code owners reviewed the sensitive areas? Policy: does it respect your rulesets, branch rules, and environments? And fallback: for high-risk changes, is the rollback or escalation path clear?

Here's an example. An agent submits a pull request that updates a dependency, but it also changes some configuration files. Under the contributor model, you don't just ask whether the code compiles. You ask whether those extra changes are justified, whether the checks cover the risk they introduce, whether the right owners reviewed them, and whether the change fits your repository and deployment policies.

So what does good look like? A well-supervised agent contribution is understandable, with a clear goal and plan. It's bounded, with scoped changes and least privilege. It's reviewable, with the right owners and evidence. It follows policy. And it's reconstructable, with an audit trail.

None of that is a special standard for AI. It's the standard of any healthy engineering workflow, applied consistently.

The takeaway: treating agents as contributors keeps your engineering discipline intact. Evaluation stays grounded in pull requests, checks, reviews, policy, and human judgment, not in hype or fear.

## Designing agent architecture and SDLC integration

Agentic systems are changing how software gets built and maintained. Teams no longer rely only on developers to write and update code. They're adopting systems that can interpret a goal, propose a solution, and take action inside a repository.

On GitHub, an agent might create a branch, change some files, and open a pull request. Then it keeps improving that work, based on feedback from tests, security scans, and code reviews.

But capability alone doesn't make an agent reliable. Without a clear architecture, an agent can act too early, produce changes nobody can follow, or run without enough validation. In production, those failures carry real risk, to code quality, to security, and to operational stability.

So designing an agent system on GitHub isn't about giving the agent more freedom. It's about defining how work flows through the system, using things GitHub can enforce, like pull requests, workflows, and repository rules. A well-designed architecture makes sure every agent action leaves a visible record, is validated by objective signals, and is only accepted when it meets your policies.

Before we go further, two terms come up a lot, and they sound alike, so let's separate them.

A plan is an artifact. It's a written, structured description of the changes the agent intends to make, usually in the pull request description. It sets out the goal, the scope, the steps, the risks, and how the work will be validated.

Planning is a capability. It's the process the agent uses to create or refine that plan, based on a task, an issue, or your input. Planning can start from different places, like a GitHub issue or the Agents interface.

So planning is what the agent does. The plan is what it produces, and what you review.

## Map agent responsibilities to the SDLC

Agents shouldn't roam across the entire development lifecycle without limits. Treat an agent like a general-purpose developer, and it's hard to predict, hard to contain, and hard to audit.

A more reliable approach is to map each agent to specific stages of the lifecycle, the stages where GitHub can enforce boundaries. Most teams start with implementation and validation, because pull requests and workflows give you natural control points there.

Think of the lifecycle in four stages, each with its own place in GitHub.

In planning, the agent drafts the scope, the steps, and the success criteria. That lives in issues, pull request descriptions and comments, or the Agents tab.

In implementation, the agent creates a branch, makes changes, and opens or updates a pull request. That lives in the branch, the commits, and the pull request.

In validation, checks run, artifacts are attached, and the agent iterates on failures. That lives in workflow runs, checks, and artifacts.

And deployment is usually restricted, with approvals required for anything sensitive. That lives in environments and deployment approvals.

Then set clear boundaries. Scope agents early, limiting which folders they can change through policy and code ownership. That keeps the blast radius small. Treat changes to workflows and infrastructure as higher risk than changes to application code. And always work through pull requests, even for automation, never straight to the default branch.

The boundary that ties it all together is simple. Agents propose. People and policy accept. The agent prepares the work and submits it as a pull request. Your repository rules and your reviewers decide whether it's merged or deployed.

Here's how that looks for a dependency remediation agent, scoped to implementation. It spots a vulnerable dependency, maybe from a security alert or an issue. It creates a branch. It updates the dependency and the lockfile. And it opens a pull request with a structured plan and the signals that will show it worked.

And at that point, its job is done. Validation and acceptance happen through checks, reviews, and policy, not through the agent.

The takeaway: give each agent a defined stage, a defined scope, and a pull request as its finish line.

## Define inputs, outputs, and success criteria

For predictable results, give every agent task three parts. Inputs: what the agent needs, like the issue context, constraints, and boundaries. Outputs: what the agent produces, which is a plan, a pull request, and evidence. And success criteria: how you'll judge the result, through checks, scans, and review.

Skip that structure, and you'll get changes that look plausible but don't actually solve the problem.

Here's a task contract for fixing a vulnerability.

The inputs are a security alert or issue describing the vulnerability. A clear scope: the agent can change source code and dependency files, but not infrastructure, unless someone explicitly asks. And constraints: no workflow changes without platform team review, no secrets, and no pushing straight to main.

The output is a pull request containing three things. A structured plan in the description. A bounded set of commits on the agent's own branch. And links to the workflow runs as evidence.

And the success criteria are four things. The required checks pass, for build, test, and lint. The security issue is actually resolved, so the vulnerable version is gone. The scope matches the intent, with no unexpected files changed. And for higher-risk changes, there's a recorded rollback or escalation path.

Notice that "CI passed" is on the list, but it isn't enough on its own. Success criteria should reflect what the task was really for. Not "the tests passed", but "the vulnerability is resolved".

Then make those criteria enforceable. A common approach is a workflow that runs on every pull request to main. One job runs the tests. Another runs CodeQL security analysis. Set that workflow as a required check, using rulesets or branch protection, and the pull request can't merge until it passes. Success is enforced by the system, not assumed by the agent.

Here's what happens when success criteria are vague. The agent can "complete" the task in a way that looks right, but misses the point. It updates the dependency, but the vulnerable version is still reachable through another package that depends on it. Or it makes broad changes that are hard to validate.

The takeaway: define what goes in, what comes out, and what success really means, then let GitHub enforce it.

## Separate planning, reasoning, and execution

Reliable agent systems keep three things separate. Planning: what will be done, and why. Execution: the actual changes to the repository. And validation: the evidence that the result meets the success criteria.

Mix planning and execution together, and reviewers only see the final diff. They lose the chance to check intent early, spot misunderstandings quickly, and control scope before anything changes.

GitHub supports this naturally. The plan lives in a pull request description or issue comment, execution in commits on a branch, and validation in checks, scans, artifacts, and reviews.

Planning can start in different places, like assigning an issue to Copilot, or the Agents tab. But it all ends up in a pull request. So the real design choice isn't where the plan starts. It's when a person validates it, relative to the code being written. You have two options.

Option A is plan-first. The agent opens a pull request with only the plan, and no code. Reviewers discuss it, refine it, and approve it. Only then does the agent start implementing. Intent is validated before any code exists.

Option B is plan plus execution. The agent opens one pull request with both a plan and its first code changes, and keeps updating both as it goes. Required checks, code owner reviews, and branch protection still block the merge until everything's satisfied.

Both are safe when your protections are set up properly. The difference is when change enters the system. Plan-first means no code until intent is approved. That's best for high-risk work, like workflows, infrastructure, authentication, and production. Plan plus execution is faster, but code appears before the plan is agreed. It can't merge, but it can mean wasted changes and extra review effort. That's fine for low-risk, easily reversible work where speed matters.

However you choose, enforce the boundary with tools, not instructions. Give planning agents read-only tools, so they physically can't edit files. Hand off to a separate implementation agent only once the plan is approved. Or use a plan mode that pauses before any changes are made. Telling an agent not to edit is guidance. Tool limits are enforcement.

The takeaway: work is always reviewed. Separation lets you review intent before you accept impact.

## Pull requests are architectural control points

When an AI agent writes code in GitHub, the pull request is where you stay in control. The agent never pushes straight to main. It works on its own branch, opens a pull request with its plan, and that pull request can only merge once your policies are met.

Five layers make this work.

First, a pull request template. It pre-fills every pull request with the same sections: goal, scope, steps, success criteria, risks, and rollback. Reviewers always know where to look. But a template only asks. Anyone, human or agent, can delete it.

So second, a required status check. A small GitHub Actions workflow reads the pull request description and fails if the plan is missing or the goal is empty. Once an admin marks that check as required, "please include a plan" stops being a habit and becomes a guarantee. People still judge whether it's a good plan.

Third, CODEOWNERS. This file maps folders to the teams responsible for them. Touch the security folder and the security team is asked to review automatically. One catch: the last matching line wins, so put your catch-all rule first and your sensitive paths after it. And make sure your workflows folder has an owner too, so an agent can't quietly weaken the checks that govern it.

Fourth, rulesets. Require a pull request before merging. Require approvals, including from code owners. Dismiss approvals when new commits are pushed, so late changes get reviewed again. Require the status checks to pass. And keep the bypass list empty. Never put an agent on it.

Fifth, environment gates. Merging isn't the same as deploying. Point your deployment job at a protected environment like production, and it pauses until a named reviewer approves. Production secrets are only released after that approval.

Here's the risk to watch for. If an agent can skip checks, merge without review, or deploy without approval, your safety model is gone. That isn't a model problem. It's a workflow design problem.

The takeaway: pull requests aren't just for collaboration. With templates, checks, code owners, rulesets and environment gates, they're how you control what agents can change, and what they can ship.

## Build reliable workflows: outputs, contexts, triggers, and cross-job handoffs

Reliable agent workflows come down to four ideas: match autonomy to risk, pass data through outputs, use the right context, and guard your triggers.

First, autonomy must be designed, not assumed. Not every change carries the same risk, so don't apply the same rules everywhere. Low-risk changes, like documentation or formatting, can merge automatically once the required checks pass. Medium-risk changes, like source code or dependency updates, need a pull request, passing checks, and at least one review. High-risk changes, like infrastructure or workflow files, need code owners, multiple reviewers, and stricter rulesets. And critical actions, like production deployments or secrets, go behind an environment approval. The agent can prepare the change, but only a person can let it run.

That's how environment approvals work. Point a job at a protected environment like production, and the job pauses until a named reviewer approves it.

Second, treat outputs as contracts. If a later step or job needs a value, don't bury it in the logs. Publish it as an output. Step outputs pass values between steps in the same job. Job outputs pass values to other jobs, and the receiving job declares which job it needs. Environment variables are for configuring how something runs. They're not a substitute for passing structured data.

Third, use the right context. The github context tells you about the run itself: what triggered it, which branch, which pull request. The vars context holds configuration values you manage centrally and reuse across workflows. The env context holds environment variables for the job or step. And sensitive values belong in secrets, never in vars.

Fourth, guard your triggers. A workflow built for pull requests often has other triggers too, like a manual run or a schedule. If one of those starts the run, pull request steps, like posting a comment, can fail or behave unexpectedly. The fix is a job-level condition that only runs the job when the event is actually a pull request. The workflow can still have other triggers. The pull request work just won't run without a pull request.

The takeaway: reliable workflows treat plans and signals as structured outputs, and guard them with logic that knows which event started the run.

## Control and operate agents: observability, tools, MCP, secrets, hooks, and reliability

Running agents safely comes down to four things: evidence, reliability, boundaries, and hooks.

First, evidence. Every meaningful action an agent takes should leave something you can review. In GitHub, that's the pull request with its plan, the commit history, the workflow runs for each required check, uploaded artifacts like test reports, and the review outcomes. Upload artifacts so the evidence outlasts the logs, and link to them from an Evidence section in the pull request. Every artifact should trace back to a specific workflow run and a specific commit, so you can always answer: which run produced this, and against what code?

Second, reliability. Assume failure. Agents will misunderstand tasks and tests will fail. So set a clear iteration policy. If a required check fails, the agent can fix its branch and try again. If the same check fails twice, it stops and hands over to a person, with what failed, what it tried, the evidence, and a suggested next step. That prevents endless loops. For high-risk changes, include rollback notes, and deploy from a specific commit or tag, not whatever's latest on a branch.

Third, boundaries. Use allowlists for tools. Give planning and review agents read-only tools, and save write access for the agents that implement. MCP servers add more tools, so enable only the specific tools you need, and review new ones like a high-risk dependency. Keep secrets out of instruction files, config files, and workflow YAML. Inject them at runtime, scope them by environment, and remember the agent's environment has its own secrets. It doesn't automatically inherit your CI secrets. And give workflows least-privilege permissions: read-only by default, elevated only where needed.

Fourth, hooks. Hooks are scripts that run at set points while an agent works: before a tool runs, after it runs, or when an error occurs. A pre-tool hook can block a dangerous command before it executes. A post-tool hook can log what happened for auditing. An error hook can trigger an alert. Hooks don't ask the model to follow a rule. They enforce it in code.

The takeaway: you can't control what you can't see. Make agent work visible, plan for failure, keep permissions tight, and enforce the rules in code.

## How agents interact with GitHub APIs and workflows

Agents on GitHub don't work around the platform. They work through it, using the same branches, pull requests, issues, and automation that developers use. Three layers make that possible: APIs, Actions workflows, and agentic workflows.

First, APIs. When an agent changes code, it follows the same steps a developer would. It picks a base branch, creates a working branch, edits files, commits, and opens a pull request. Each step is an API call, and every call is authenticated with a token, like a GitHub App token or the workflow's built-in token. So everything an agent does is limited by permissions and recorded for audit.

Second, GitHub Actions, the execution layer. Workflows run jobs in isolated environments when something triggers them: an event like a push or pull request, a manual run, or an API call. Agents rely on workflows to run tests, validate changes, and deploy. Copilot's cloud agent itself runs inside a GitHub Actions environment, so workflows are its foundation.

Third, agentic workflows. A traditional workflow spells out every step in YAML. An agentic workflow describes the outcome you want in plain Markdown, and a coding agent works out how to get there. The file has two parts. The frontmatter at the top sets the boundaries: when it runs, what it can read, which tools it can use, and its safe outputs, the only actions it's allowed to take, like creating an issue with a set label. The Markdown below explains the task, for example: "Write a daily status report for maintainers, with highlights, risks, and next steps." The file is compiled into a standard workflow that Actions runs. Agentic workflows suit open-ended but bounded tasks like triage, reporting, documentation, and CI failure analysis. They don't replace your CI/CD pipeline. They extend it.

While an agent works, you can follow its session log, see each action, steer it with feedback, and review the final pull request.

So the end-to-end flow is: assign a task, the agent plans, creates a branch and commits, opens a pull request, workflows validate it, and a person reviews it.

The takeaway: agent work on GitHub is scoped to a repository, controlled by permissions, run through workflows, and reviewable in pull requests.

## Execution context and boundaries

Once an agent can take actions, the next question is where those actions happen. That's the execution context: the repository the agent works in, the branch it works on, the workflow that runs it, and the permissions it's given. Each one is a boundary.

First, the repository. An agent works inside one repository. It reads and changes that code, and works with that repository's issues, pull requests, and workflows. It can't reach other repositories unless you grant access.

Within that repository, custom agents narrow things further. A custom agent is a file in the dot-github agents folder. It lists the tools the agent can use, like read and search, and its instructions say what to focus on. A security reviewer, for example, might only get read-only tools.

Second, the branch. Agents don't work on main. Copilot's cloud agent creates its own branch from the base branch you choose, makes its changes there, and those changes reach main only through a reviewed pull request. Notice who enforces this. It isn't the custom agent. It's the system running the agent. A custom agent decides what the agent does. The platform decides where it does it.

Third, the workflow. Agent tasks run inside GitHub Actions workflows. A workflow defines what triggers the run, which steps execute, and which environment they run in. Each run starts clean, can be repeated, and captures its logs. You can even run Copilot CLI inside your own workflow, on a schedule or on demand, giving it only the tools it needs.

Fourth, permissions. Every workflow gets a token, and that token decides what the agent can do: read code, write code, open pull requests, use secrets. Define permissions explicitly and keep them as small as possible.

GitHub Agentic Workflows build all of this in. The agent gets a read-only token and no secrets. It runs in a sandboxed container, with outbound network access limited to an allowlist. It can only propose actions, and a separate, gated step checks them for threats before anything is written.

The takeaway: an agent is only as safe as the boundaries around it. Scope it to a repository, isolate it on a branch, run it through workflows, and keep its permissions tight.

## Define multi-agent responsibilities in the SDLC

A multi-agent system only works when every agent has a clear job. When roles overlap, the failures are predictable: duplicated work, pull requests that conflict, and nobody quite sure who owns what.

So start with one simple rule. Agents propose. People and policy accept. Agents can open pull requests and produce evidence, but your repository's rules and your reviewers decide what merges.

Next, map each stage of the development lifecycle to an agent responsibility, and to something in GitHub you can actually review.

In planning, an agent defines the goal, scope, success criteria, and risks. You review that in the plan section of the pull request.

In implementation, an agent makes changes on its own branch. You review the branch, the commits, and the pull request.

In validation, an agent produces evidence. You review the workflow runs, the checks, and the uploaded artifacts.

Acceptance belongs to policy and people: code owners, reviews, and required checks.

And deployment is gated by environments and approvals.

Then draw the boundaries. Be specific about what each agent is allowed to change. The dependency agent changes dependency manifests and lockfiles, and nothing else. The refactoring agent works in the source folder, but never touches dependencies, lockfiles, or workflows. That stops a refactor from turning into an open-ended change that collides with other automation. The security agent validates results and writes reports that point to checks and scan results. It can propose fixes, but it doesn't wander into refactoring unless the task is specifically to fix a security issue.

Now picture the opposite. Every agent acts like a general developer with access to the whole repository, including workflows and infrastructure. You get constant collisions, reviews going to the wrong people, and risk nobody controls.

Finally, don't rely on instructions alone. Back each boundary with something GitHub enforces: code owners on each path, and a required check that fails if an agent changes files outside its lane.

The takeaway: define each agent's responsibilities precisely enough that GitHub itself can enforce them.

## Agent execution limits and protections

Agents can act in your repositories, but always inside limits the platform sets and safeguards you add. Let's take those in turn.

First, the platform limits. Copilot's cloud agent can only reach the repository it's working in. It makes its changes on a separate branch, never directly on main. And it doesn't merge its own work. A person decides whether the changes become a pull request, gets them revised, or throws them away. Around that, your repository and organization settings control which workflows and actions can run, and what the workflow token is allowed to do.

That token has one more useful limit. Most actions taken with the built-in workflow token don't start new workflow runs. That stops an agent from accidentally triggering itself in a loop. GitHub App tokens and personal access tokens can trigger new runs, which is more flexible, but you have to design carefully to avoid loops.

Second, the safeguards you add. Think of five.

Fail fast. When a step fails, stop the workflow and log a clear error, so you never end up with half-finished changes.

Retry, but only for temporary problems like a network blip. Cap the number of attempts, and if the last one fails, fail the run. Don't let a retry loop hide a real failure.

Make rollback easy. Because agent work lives on a branch behind a pull request, rolling back usually just means closing the pull request. If something bad has already merged, revert the commit.

Escalate to people. Require reviews, assign reviewers automatically, and notify maintainers when an agent gets stuck.

Keep everything traceable. Workflow logs, commit history, and pull request discussions show what each agent did and why. Clear commit messages help.

Third, protect deployments. If agent changes feed a deployment, use environments. They pause for approval, keep secrets locked until then, and control where code can deploy.

And while an agent is running, you can watch its session log, inspect each action, and steer it with follow-up prompts.

Put together, that makes agent execution resilient, controlled, auditable, and governed by people.

The takeaway: agents prepare the changes. You stay responsible for reviewing and finalizing them.

## Orchestrate agents using GitHub workflows

Once each agent has a clear role, the next question is how they work together. That's orchestration: when each agent runs, in what order, and how work passes from one to the next. In GitHub, you express that through workflows that respond to events, so the coordination is visible in pull requests, runs, checks, and logs.

The usual triggers are a schedule, for regular work like reports or dependency checks; pull request events, for validation; and one workflow finishing, when another should start after it.

There are three patterns to know.

First, sequential. Some work has to happen in order. The dependency agent opens a pull request. CI runs the build and tests. Security validation runs only once CI has passed. A person approves. And only then can it merge. Use this whenever one step depends on the result of the one before.

Second, parallel. Agents can work at the same time, but only if they can't collide. A documentation agent and a refactoring agent can run together if they work in separate folders. The rule is isolation. If two agents can edit the same files, running them in parallel adds instability, not speed.

A common version is fan-out, fan-in. Two agents, say a spec analyzer and a risk reviewer, run side by side. A third job waits for both to finish, then merges their findings into one plan. Add a concurrency group so two merge jobs never overlap on the same branch.

Third, coordinate through artifacts. Agents talking directly to each other is fragile. Instead, run the agent with read-only permissions, and have it produce a structured output, like a plan or a report, saved as an artifact. Then a separate, controlled step applies only the actions you allow, like opening an issue. That keeps a clear line between thinking and writing, and leaves evidence reviewers can check.

What if coordination happens outside GitHub? Then there's no trail. Nobody can see why the system did what it did, and trust drops.

The takeaway: orchestrate through workflows and shared artifacts so everything stays visible. Run in sequence when steps depend on each other, and in parallel only when agents are isolated.

## Isolate execution: branches, workflows, permissions, and concurrency

Execution isolation means every agent works in its own space. It doesn't share a branch, a workflow, or permissions with any other agent. That isn't only about avoiding merge conflicts. When agents share an execution context, failures are hard to trace, and the system can thrash, re-running over and over. Isolation makes it safe to run agents in parallel, and makes it clear who did what.

There are four layers.

First, branches. Each agent works on its own branch and opens its own pull request. A naming convention helps: agent, slash, dependency, slash, ticket number. Reviewers can see at a glance which agent made the change and why.

Second, workflows. Give each agent its own workflow, or at least its own job. Then its triggers, permissions, and outputs are easy to reason about, and changing one agent's workflow doesn't accidentally break another.

Third, permissions. Give each workflow only what it needs. For example, a workflow that comments on pull requests gets write access to pull requests, but read-only access to code, so it can't push commits.

Fourth, concurrency. Even with all that, runs can overlap in time. Picture an agent pushing to a pull request three times in a minute. Without controls, you get three overlapping runs, all competing. A concurrency group fixes that. Name the group after the workflow and the branch, and turn on cancel in progress. Now only the newest run on that branch continues, while other workflows and other branches still run in parallel.

Be careful with the group name. Groups apply across the whole repository. If you name it after the branch alone, unrelated workflows on that branch end up cancelling each other. And for deployments, don't cancel a run halfway through. Queue them instead.

What happens without isolation? Agents share a branch, commits interleave, nobody's sure who owns what, and the same failures keep repeating. Rolling back and auditing both get much harder.

The takeaway: isolation is the foundation of a stable multi-agent system. Separate branches, separate workflows, minimal permissions, and concurrency controls, especially when pull requests update often.

## Detect and resolve conflicts using GitHub-native arbitration

Even with good isolation, conflicts will happen when several agents work in the same repository. And they're not just conflicts in code. There are four kinds to watch for.

Merge conflicts, where two changes touch the same lines in the same files.

Semantic conflicts, where everything merges cleanly, but the combined changes break the behavior.

Policy conflicts, where changes touch protected areas that need different reviews or approvals.

And duplicate effort, where two agents open two pull requests that solve the same problem in different ways.

A stable system does two things: it spots conflicts early, and it resolves them by rules, not by luck.

Spotting them early starts with a merge validation check. GitHub already shows merge conflicts on a pull request, but many teams add a step that test-merges the branch with main. Make that a required check, and a conflict fails the pull request straight away. Nobody has to notice it by eye.

Next, route by ownership. CODEOWNERS sends changes to the right reviewers based on the files they touch. If an agent changes security code, the security team reviews it. If it changes workflows or infrastructure, the platform team does. That's your arbitration. The people who own the area decide.

Then set escalation thresholds, so automation stops before it starts going round in circles. Escalate to a person when a pull request still conflicts after two rebase attempts, when a required check fails twice with the same error, or when two agents propose fixes that can't both be right. The escalation should come with a short report: what conflicted, what was tried, and what the options are.

Without rules like these, timing decides the outcome, not correctness. Whichever pull request merges first wins, and reviewers are left untangling the mess afterwards. That makes the whole system less predictable and harder to coordinate.

The takeaway: detect conflicts early with automated checks, resolve them deliberately through ownership routing, and escalate to a person when the same conflict or failure happens twice.

## Make the system observable: attribution, evidence, and handoffs

Observability means being able to see what your system is doing at every step. Every meaningful action an agent takes can be inspected, explained, and checked afterwards. As you add more agents, that stops being nice to have. It becomes the foundation for coordination, debugging, and governance.

The good news is that GitHub builds this into the way you already work. You don't need hidden logs or external tools. Pull requests, workflow runs, logs, and artifacts already give you the trail.

With several agents, reviewers need answers to four questions. Which agent made this change? What did it decide? What evidence supports that? And what happened next? So set a simple goal: every meaningful step leaves a lasting trace in GitHub. A pull request that explains the intent. Checks and workflow runs that produce evidence. Artifacts and logs that explain the outcome. And clear attribution.

Attribution comes from consistent naming. Start pull request titles with the agent's name, like agent dependency. Add a label for each agent. And use the same sections in every pull request body.

A standard structure works well: the objective, the plan, the evidence, the decisions and handoffs, and the risks and rollback. The decisions section records what was decided, why, and who owns it next if it needs to be escalated. That way every handoff is explicit, not assumed.

For evidence that lasts, have the agent save a structured report and upload it as a workflow artifact. Later, when you're investigating what happened, go to the workflow run, scroll to the Artifacts section, and download the report. It's often your best evidence, even when the live logs are incomplete. And if an artifact has gone missing, the organization audit log shows who deleted it, when, and from which repository.

Why does this matter so much? Without observability, nobody shares an understanding of what happened or why. Reviewers can't verify decisions, debugging becomes slow and reactive, and the system becomes unpredictable. Invisible work is an operational risk.

The takeaway: observability isn't optional. It's what keeps a multi-agent system reviewable and operable.

Even with good observability, things will still fail. Next, we'll look at how to diagnose those failures and recover safely.

## Operate reliably at scale: diagnose failures and recover safely

In a multi-agent system, failure is expected, not exceptional. And most failures aren't one agent getting something wrong. They're coordination failures: each agent works, but the system stalls or goes unstable.

Watch for four patterns. Partial execution, where a pull request exists but the evidence or validation is missing. Stalled workflows, where checks keep failing or approvals never arrive. Conflicting outputs, where pull requests compete and block each other. And flapping, where workflows keep re-running and never settle.

To diagnose them, use what GitHub already records. The pull request timeline shows what changed and when. Check results show what failed, and how often. Workflow run history shows patterns of failures and cancellations. And artifacts explain the outcomes. If an agent session seems stuck, you can follow its log live from the GitHub CLI.

Recovery comes down to three strategies. Bounded retries: an agent can fix its own branch, but only a limited number of times. Escalation: if the same required check fails twice, automation stops and hands over to a person, with links and a short summary. And rollback readiness: keep pull requests small and scoped, so reverting is safe.

Some blocks are deliberate. A pre-tool hook can block a risky action, like deleting infrastructure, before it runs, and hand it to a human for review.

Configuration can cause failures too. If an agent has model invocation turned off, another agent can't call it automatically, so an orchestration that depends on it will break. In editors like VS Code, a planner agent can list which subagents it's allowed to call, and use handoffs to pass work to an implementer, then a reviewer.

Rules can block agents as well. If a ruleset requires signed commits, Copilot's pushes may be blocked. You can add Copilot as a bypass actor for that ruleset, so the rule still applies to everyone else.

And for high-risk actions like production deployments, environments add an approval gate.

A system that assumes success fails unpredictably: workflows loop, failures pile up, and people step in too late. So assume failure, limit retries, escalate when automation can't converge, and keep every change reversible.

The takeaway: reliable multi-agent systems are built to detect failure, recover from it, and iterate safely.

## Memory, state, and evaluation

As agents get more capable, we hand them bigger jobs. Tasks that take many steps, use several tools, cross different environments, and often don't finish in a single session.

That raises a new challenge. To do that kind of work well, an agent has to remember what matters, keep track of how far it's got, and stay focused on the original goal, even when the work is spread over hours or days.

On GitHub, that's especially important, because agents aren't just answering questions. They're creating branches, opening pull requests, running workflows, and working with files and artifacts in your repository. Their work has real effects, and it builds up over time.

So in this section, we'll look at three questions. Memory: what should an agent remember, and how? State: how is progress saved, so work can pick up where it left off? And evaluation: how do we judge whether the results are actually good?

## Implement agent memory strategies

Agents need structured memory to work reliably. One long stream of context isn't enough. Memory should be organized so the agent can focus on the task in front of it, while still reaching important information when it needs it.

Think of memory in three layers.

Short-term memory is the working context for the current task: recent instructions, feedback, and the next few steps. It's useful while the agent works, but it's gone when the session ends.

Long-term memory is curated knowledge the agent can reuse across tasks, like key decisions, patterns, and lessons learned. It's more stable, and usually summarized.

External memory lives outside the agent, in durable systems. On GitHub, that's your issues, pull requests, documentation, and workflow outputs. Because it lasts and anyone can review it, external memory is your source of truth.

Next, decide where each kind of information belongs. Requirements and acceptance criteria go in the issue or the pull request description, so the agent can always check its work against the goal. Plans and decisions go there too, so work can carry on without anyone reinterpreting earlier steps. And repeatable processes become instructions or reusable skills, so you don't redefine them for every task.

Then be selective. Only keep what affects the outcome: requirements and constraints, decisions that shape the implementation, and how the work will be tested. Leave out temporary steps and duplicated context. Less memory means less confusion, and less chance of the agent acting on something out of date.

Give every type of information one home. Requirements live in the issue. Decisions live in the pull request or the documentation. Validation rules live in the repository instructions. And results live in workflow logs and artifacts. One home per type means no conflicting versions, and an agent that stays aligned from one session to the next.

Finally, maintain it. Temporary outputs like logs and artifacts should expire. Clear out what's no longer useful. Summarize long histories into key points and links. And define reset rules for when requirements change or old assumptions stop being true.

The takeaway: good agent memory is structured and selective. Short-term memory supports the current task, long-term memory keeps what's worth reusing, and external memory is the durable source of truth.

## Persist agent state and manage context drift

Memory tells an agent what matters. State tracks what's been done, what was decided, and what's left to do.

On GitHub, state doesn't live in one place. It's spread across the issue, the pull request, the commits, and the workflow runs. Together, they're the agent's persistent memory. The issue holds the requirements and acceptance criteria. The agent creates a branch and opens a pull request. Each commit marks progress. And workflows run on every push to validate the changes.

The pull request is the anchor. Its description should hold the task, the acceptance criteria or a link to the issue, the plan, and updates as the work moves on. When a decision changes, update the description. GitHub pulls the commits, checks, and discussion into the pull request, so it's the one place to see where things stand.

That's what lets an agent resume without starting over. When work pauses, the agent opens the existing pull request, rereads the description and the issue, looks at the commits already made, checks the workflow results, and carries on from there. Nothing gets done twice.

Over long tasks, watch for context drift. That's when the agent's work slowly stops matching the original goal or earlier decisions. Signs include changes that miss the acceptance criteria, commits that contradict earlier decisions, and checks that fail or go missing. The fix is to realign with the source of truth. Reread the issue and the pull request, compare the changes with the acceptance criteria, update the description, and re-run the workflows.

State needs maintenance too. Workflow logs and artifacts are kept for ninety days by default, and you can change that. Delete artifacts that are stale or redundant, but remember deletion is permanent. Summarize long histories in the pull request, linking to key commits and runs instead of copying them. And reset when things change, like when requirements shift or you take a new approach. Rewrite the description, or close the pull request and start a fresh one, and record the new direction first.

Finally, make checks required, so nothing merges until the workflows pass.

The takeaway: pull requests, commits, and workflow runs hold the agent's state. Use them to resume reliably, catch drift early, and keep memory accurate over time.

## Ensure continuity of agent memory and state across tools and environments

Agent work rarely stays in one place. An agent might start in your IDE, carry on through the command line, and finish in a GitHub-hosted environment. Memory and state have to follow it, and that means relying on GitHub, not on the current session.

First, share state through references, not copies. A pull request number, a branch name, a commit SHA, a workflow run link, an issue URL. Any tool can use those to find exactly the same state. So start from an issue, open a pull request, and make that pull request the central reference. Your IDE, your CLI, and the GitHub website can all open it, and nothing needs to be handed over between sessions.

Second, make GitHub the source of truth. Requirements live in issues. Decisions and progress live in pull requests. Validation rules live in repository instructions. Results live in workflow runs and artifacts. Don't keep anything important only in a prompt or a chat history. If it matters, write it to the issue or the pull request.

Third, prevent conflicting context. That's when the same information exists in two places with different values. Give each type of information one home, and update the original rather than making a new copy. For example, don't restate acceptance criteria in every prompt. Update the issue.

Fourth, prevent stale context. That's when the agent acts on information that's out of date. Maybe the branch has fallen behind main, the workflow results no longer match the code, or the requirements changed and nobody updated the issue. So before continuing, bring the branch up to date, check the latest commits and runs, and keep issues and pull requests current. Branch protection can help, by requiring branches to be up to date before they merge.

Workflows tie all this together. Run them on every pull request and push, re-run them after changes, and treat their results as the final word on the current state.

So whenever the agent switches environments, it re-anchors to the pull request and continues from there.

The takeaway: continuity comes from shared, durable state. Use GitHub as the source of truth, refer to it the same way from every tool, and agents stay aligned across sessions.

## Define evaluation signals and enforce quality gates

How do you know an agent's work is actually done, and done well? You decide in advance, and then you let GitHub enforce it.

Start with clear success criteria. Write them in the issue, and reference them in the pull request. They describe what has to be true for the task to be complete. For example: the feature behaves as expected, the tests pass, and no new security issues have been introduced. With criteria like these, both the agent and the reviewer can check the work against the same standard.

The pull request is where evaluation happens. Every time the agent pushes a change, workflows run automatically. They run the tests, lint the code, and build the application. The results show up as status checks on the pull request, with the detail in the Checks tab. Each run also produces logs and artifacts, like test results and reports, which are kept for ninety days by default. Link to them from the pull request so reviewers can see the evidence.

Security belongs in that evaluation too. Turn on code scanning to find vulnerabilities, dependency review to catch risky packages, and secret scanning with push protection to stop credentials from leaking. Treat any security failure as a blocker, not a suggestion.

Then make the checks mandatory. In your branch protection rules, require status checks to pass before merging, and choose which checks count. You can also require branches to be up to date with main. Add at least one approving review, and block direct pushes to protected branches. Now nothing gets merged just because someone was in a hurry.

Put it all together, and the flow looks like this. An issue defines the task and the success criteria. The agent creates a branch and opens a pull request. Workflows run automatically, and their results appear as checks. The required checks must pass. A reviewer approves. And only then does the pull request merge.

The takeaway: evaluation is how you know agent work is complete and correct. Define success up front, and use workflows, required checks, security scanning, and reviews so every change meets that standard before it merges.

## Analyze agent failures and improve behavior

Agents won't always get it right first time. That's normal. What matters is that you learn from each failure and make the agent better next time.

Start with the evidence. On GitHub, failures leave a trail. Open the pull request and review the recent changes, check the Checks tab for failed workflows, and read the logs to find the error.

Then compare intent with results. The intent is in the issue, with its requirements and acceptance criteria, and in the pull request description, with its plan and decisions. The results are in the commits, the code changes, and the workflow outputs. Put the two side by side and ask: did the agent misunderstand the task, build the wrong solution, or fail while running or validating it?

Next, classify the root cause. Most failures fall into one of three groups.

Reasoning errors. The agent made a wrong assumption or decision. It misread the requirements or ignored the acceptance criteria.

Tool misuse. The agent used workflows, commands, or repository operations incorrectly. A workflow was misconfigured, or a script was wrong.

Context issues. The agent worked from information that was missing, out of date, or contradictory. It used an old pull request state, missed an earlier decision, or found conflicting information in different places.

Each cause has its own fix. For reasoning errors, improve the prompts and instructions. Clarify the acceptance criteria, add constraints, and update the repository instruction files. For context issues, fix memory and state. Record decisions clearly in the issue or pull request, remove outdated information, and keep one source of truth. For tool misuse, fix the configuration. Update the workflow files, check they trigger on the right events, and verify permissions and required checks.

Then close the loop. Run the agent, observe what fails, find the root cause, apply the fix, and run it again. GitHub makes that easy, because you can re-run workflows and inspect the logs.

And keep every improvement traceable. Record changes in the pull request, link the related commits and runs, and keep each change small enough to review.

The takeaway: failures are part of the process. Use GitHub's evidence to find the root cause, then improve the prompts, memory, or tools, so the agent gets more reliable every time.

## Governance, guardrails, and operations

As agent systems get more capable, the most important design question changes. It's no longer what can an agent do. It's what should it be allowed to do.

In real software teams, agents don't operate in a vacuum. They work within security requirements, compliance obligations, operational risk management, and organizational policies.

Without governance, even a well-designed agent can cause serious problems. It can make unauthorized changes to critical code. It can trigger unsafe deployments. It can end up with too many permissions, or expose sensitive data. And when something goes wrong, there may be no clear record of who did what, or why.

The good news is that on GitHub, governance isn't a separate system you bolt on. It's built into the way you already work. It's enforced directly through repository controls, workflows, and policies that agents can't simply ignore.

In this section, we'll look at how to use those controls to decide what agents are allowed to do, and to keep every action safe, accountable, and traceable.

## Define risk-based autonomy and action boundaries

Not every action an agent takes carries the same risk. Treat them all the same, and you either slow everything down or leave yourself exposed. Risk-based autonomy means giving agents freedom that matches the impact of what they're doing, and how easily it can be undone.

Risk depends on three things: where the change lands, how easily it can be reversed, and how quickly it affects users or systems. Editing a README barely matters. Changing a workflow file affects your entire pipeline. That's why workflows, infrastructure, and security folders should be treated as high risk by default. They're small diffs with big consequences.

Think of autonomy in four levels. Read-only, where the agent can inspect, summarize, and recommend, but can't change anything. Propose-only, where it can create branches and pull requests, but can't merge or deploy. Execute with guardrails, where it can run pre-approved workflows like tests, builds, and staging deploys. And human-authorized, where high-impact actions, like a production deploy, a workflow change, or access to secrets, only happen after a person approves.

Map those levels to risk. Low-risk work, like docs and formatting, can be fully automated. Medium-risk work, like dependency updates or safe refactors, goes through a pull request with required checks. High-risk work, like infrastructure or workflow changes, needs code owners, explicit approvals, and stronger checks. And critical actions, like production deploys or production secrets, go behind an environment gate with named reviewers and an audit trail. The rule of thumb: automate only what you can undo.

Make it enforceable. If an agent's plan includes a risk rating, don't rely on its explanation. Have it output the rating in a machine-readable form, and let the workflow route on it. Low risk runs automatically. Anything higher waits for approval.

For terminal agents like Copilot CLI, tool access is the boundary. Allow only the tools a task needs. Summarizing commits needs Git, not write access.

Finally, grow autonomy step by step. Start with the agent only opening pull requests. Then let it merge low-risk changes once checks pass. Then deploy to staging. And only deploy to production through environment approval.

The takeaway: autonomy should be defined, not assumed. Automate low-risk, reversible work, and require validation or approval for everything else.

## Enforce governance with GitHub controls

Once you've defined what agents can do, those rules have to hold, in a way that can't be bypassed. GitHub gives you five controls to do that: rulesets and branch protection, required checks, code owners, environments, and guardrail workflows.

First, rulesets and branch protection. On protected branches like main, require a pull request to merge, require checks to pass, and require approving reviews, with more approvals for riskier changes. Require code owner review for sensitive paths. Block direct pushes, force pushes, and branch deletion.

Second, required checks. Each one should map to a governance goal. Builds and unit tests cover quality. Security scans cover risk. Policy checks cover changes to workflows and infrastructure. And treat renaming or removing a required check as high risk. If your checks drift, your governance drifts with them.

Third, code owners. Assign security code to the security team, and workflows and infrastructure to the platform team. But make sure code owner review is actually required. Otherwise, code owners are just a suggestion.

Fourth, environments. Use them to require reviewers for production deploys, keep production secrets available only to production, and keep a clear record of who approved what. Any workflow that touches production secrets is critical risk, so gate it.

Fifth, guardrails. For agents running locally, like Copilot CLI, a pre-tool hook can block dangerous commands, like running as root or piping a download straight into a shell, before they ever execute. Logging and warnings don't stop anything. A hook does. And in the repository, a guardrail workflow can enforce rules settings alone can't express. For example, it can make sure an agent's pull request is never merged without at least one approval from a real person, not a bot.

Put together, that's layered enforcement. Permissions constrain what happens before an action. Checks validate it as it happens. Logs and artifacts trace it afterwards.

Why automate all this? Because agents work at speed and scale, and governance that depends on people remembering the rules will fail. Controls that only live in documentation are an anti-pattern. If the platform can't enforce it, it will be bypassed.

The takeaway: on GitHub, governance runs on policy, not trust.

## Design human-in-the-loop workflows

Even with strong controls, some moments still need human judgment. The goal isn't to add friction everywhere. It's to put people where it matters most, so high-impact actions stay under control while low-risk work keeps moving.

Agents can produce changes quickly, but they don't carry responsibility for the outcome. People do. People weigh risk, context, and trade-offs, especially for decisions automated checks can't fully validate.

Here's how a human-in-the-loop workflow usually runs. The agent opens a pull request, including its plan and a risk level. Checks validate the changes. Code owners are automatically asked to review where needed. And the pull request merges only once the approvals and checks are in place.

The key is where you put people. Put them at decision points: merging, deploying, and accessing secrets. Don't put them at every step, like analysis, formatting, and routine checks.

Production deployments are the most important decision point. Use a production environment with required reviewers, so every deploy is explicitly approved, recorded, and owned by someone accountable. And make sure production deploys never overlap. With a concurrency group, only one runs at a time, which avoids race conditions and conflicting releases.

You can apply the same thinking to tools. Low-risk actions, like reading and searching, can be automated. Higher-risk actions, like editing files or running commands, still need approval at the moment they're used. That keeps everyday work fast, without giving away control.

Watch out for governance fatigue. If every review is slow and painful, people start rubber-stamping. So make review easy. Require evidence, like tests, scans, and artifacts, so reviewers can check quickly. Route reviews through code owners, so reviewers have the right context. Keep pull requests small and focused. And require a rollback plan for high-impact changes.

The takeaway: human oversight should be targeted and intentional. Put people at the high-impact decisions, like merge, deploy, and access to sensitive resources, and let low-risk work run on its own. That way you keep speed and accountability.

Approvals protect decisions. Next, we'll look at permissions, which define what agents can access in the first place.

## Control agent capabilities using least privilege

Once you've decided where people make decisions, the next question is what agents can actually access. That's set by permissions.

Least privilege means giving an agent only the minimum permissions it needs for a specific task, and nothing more. It sounds simple, but it matters enormously. Permissions define what an agent can really do, whatever its instructions say and whatever it intends. Give it a broad token, and a small mistake can turn into a big incident, with unintended changes spreading across the system. Keep permissions tight, and the blast radius stays small, so problems are easier to contain and recover from.

Here's how to put it into practice.

Start with minimal defaults. At the workflow level, set access to read-only. Only allow write access where it's genuinely needed, and document why.

Then elevate permissions only where they're needed, job by job. Picture a workflow with two jobs. The first analyzes the code, so it only needs read access. The second creates or updates a pull request, so that job, and only that job, gets write access. The analysis job never holds permissions it doesn't use.

Treat write access to pull requests as an elevated capability too. Grant it only when a workflow has to create or update pull requests.

Then add three more controls. Use environments to restrict access to secrets. Keep high-risk jobs separate, so they never share permissions with low-risk ones. And use as few third-party actions as you can, pinned to specific versions.

Why does this matter so much? Because an agent can only damage what it can reach. Least privilege is what keeps a mistake in one place from becoming a problem everywhere.

The takeaway: permissions are the true boundary of an agent's power. They decide what it can actually do, whatever its instructions say. Keep them minimal and scoped, and you reduce risk, contain failures, and stay in control as your system grows.

And even a well-controlled system has to prove what it did. That's where evidence comes in, next.

## Make actions observable, traceable, and auditable

Once agents are working inside your boundaries, you need to be able to see what they're doing. What happened? Why did it happen? And who approved it? If you can answer those three questions, it's much easier to debug problems and to trust the system.

GitHub captures that evidence as part of the normal workflow, through pull requests, workflow runs, logs, and artifacts. So the rule is simple: every meaningful action leaves a trace that a reviewer can inspect.

For each meaningful action, that trace should include five things. The pull request and its commit history. The workflow results, including the job logs, when it ran, and who or what ran it. Uploaded artifacts, like the plan, the test results, and an execution report. The approval and merge events. And, for production, the environment approval record.

Treat this as a design requirement, not a nice-to-have. Without durable evidence, you can't reliably debug failures. You can't investigate incidents. You can't prove compliance. And over time, you can't trust autonomous changes.

So make your critical workflows evidence-first. Each one should produce test results, scan reports, a machine-readable plan, and a machine-readable summary of what was executed. Upload them as artifacts, so they're easy to find, and keep them long enough to support audits and incident response.

And here's the most important rule. Treat missing evidence as a failure. If a change can't be audited, it shouldn't be merged.

Why does this matter so much? Because when actions aren't visible or traceable, everything gets harder. Debugging becomes slow and reactive, because there's no reliable record of what happened. Compliance can't be demonstrated, because decisions and approvals can't be audited. And trust breaks down, because nobody can explain or validate the changes. If a system can't show what happened and why, it can't be operated safely at scale.

The takeaway: observability is what makes accountability and trust possible. Make every action visible, traceable, and explainable, and your system stays debuggable, auditable, and reliable as it grows.

And remember, governance isn't static. Next, we'll look at how it needs to evolve over time.

## Maintain governance and operational reliability

Systems change over time, and so do the risks. Controls that worked well on day one can quietly drift or go out of date. So governance isn't something you set up once. It's something you keep running.

Start with the agent lifecycle. Agents are deployed, monitored, updated, and eventually retired, and their guardrails evolve alongside them. That means every agent needs a clear owner, a runbook, and a regular review.

Then watch for governance drift. It's inevitable. A required check gets renamed or removed. Review rules get relaxed. Code owners go out of date. Permissions creep wider. Secrets move into broader scopes. None of these changes looks dramatic on its own, but together they open gaps. That's why reviews need to be built into how you operate.

Prevent ambiguity before it becomes risk. Before you hand a task to an agent, define it clearly: acceptance criteria, constraints and non-goals, the files or paths involved, and how it'll be validated and rolled out. If you can't define a task precisely, it shouldn't run autonomously.

When things go wrong, recover in a predictable way. Retry temporary failures, but only a limited number of times. Escalate when failures repeat. Roll back quickly, using small pull requests and safe reverts. And when it's a security failure, investigate. Don't just retry.

Put it on a cadence. Weekly, review failed runs and common policy violations. Monthly, review workflow permissions and secret scopes. Quarterly, audit your rulesets, code owners, environment reviewers, and how long you keep evidence.

And know the failure patterns to look for. Unbounded autonomy, like production deploys with no approval. Excess permissions, like a token that can write everywhere and read every secret. A missing audit trail, with only console logs and no artifacts. Bypass paths, like direct pushes to main or disabled checks. And rubber-stamping, where approvals become a click to unblock. The fixes are the controls we've covered: environments and reviewers, least privilege, evidence-first workflows, rulesets, and smaller, better-evidenced pull requests.

The takeaway: governance needs continuous monitoring and improvement. Treat it as an ongoing operational responsibility, not a one-time setup, and your system stays secure and reliable as it scales.

