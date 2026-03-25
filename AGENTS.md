# IdeaForge AI — Project Context for GitLab Duo

## What This Project Is
IdeaForge is a multi-agent AI pipeline built on the GitLab Duo Agent Platform.
It autonomously transforms any GitLab issue into a production-ready Merge Request
using five sequential AI agents.

## Pipeline Overview
When triggered, five agents run in sequence:
1. **Issue Intelligence** — Root cause analysis of the issue
2. **Problem Expansion** — Deep codebase exploration and file impact mapping
3. **Solution Generator** — Three-approach code generation, best one fully implemented
4. **Security Scanner** — OWASP Top 10 audit with hard BLOCK capability
5. **PR Generator** — Branch creation, commits, and full Merge Request

## How to Trigger IdeaForge
Assign the IdeaForge flow to any issue in your project via:
- GitLab UI: Issue → Assign → select IdeaForge flow
- Comment: `/assign @ideaforge` on any issue

## Agent Behavior Standards
All agents in this pipeline MUST:
- Post progress comments to the issue after completing each step
- Never truncate code — write complete file contents always
- Never skip tests — every code change requires corresponding test updates
- Respect the structured report format (delimited with `─────`)
- Pass full context to the next agent via structured reports

## Security Rules (Non-Negotiable)
- Agent 4 (Security Scanner) is a hard gate: CRITICAL findings = pipeline BLOCK
- No code reaches a Merge Request without passing the security scan
- Every security finding must include a concrete exploit scenario

## Code Quality Standards
- Match existing code style of the target repository exactly
- Use conventional commits: type(scope): description
- No new dependencies without explicit justification
- Acceptance criteria from the issue must be testable and met

## Output Artifacts
The final output of IdeaForge is always:
- A new branch: `ideaforge/{issue-iid}-{slug}`
- A fully documented Merge Request
- Progress comments on the original issue

## Repository Structure
```
.
├── AGENTS.md                            # This file — context for all Duo agents
├── README.md                            # Project documentation
├── LICENSE                              # MIT License
└── .gitlab/
    └── duo/
        ├── agent-config.yml             # Flow execution configuration
        └── flows/
            └── ideaforge.yaml           # Complete 5-agent pipeline (v1 format)
```
