# 🔥 IdeaForge AI

> **From Issue to PR — Fully Autonomous. Zero Developer Effort.**

[![GitLab Duo Agent Platform](https://img.shields.io/badge/GitLab%20Duo-Agent%20Platform-orange?style=for-the-badge&logo=gitlab)](https://docs.gitlab.com/ee/user/duo_workflow/)
[![Powered by Anthropic](https://img.shields.io/badge/Powered%20by-Anthropic%20Claude-blue?style=for-the-badge)](https://www.anthropic.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](./LICENSE)

---

## 🎯 What is IdeaForge?

IdeaForge is a **multi-agent AI system** built natively on the **GitLab Duo Agent Platform** that transforms a GitLab issue into a production-ready Merge Request — entirely autonomously.

**One label. Five agents. One Merge Request. Zero developer effort.**

When a developer labels any GitLab issue with `ideaforge`, a coordinated team of five AI agents springs into action. They read the issue, explore the codebase, write the code, scan for security vulnerabilities, and open a fully documented MR — all within minutes.

This isn't a chatbot. This is a **digital engineering teammate** that does the work.

---

## 🎬 Demo Video

> 📺 [Watch the 3-minute demo on YouTube](https://youtu.be/your-demo-link)

---

## ✨ The Problem IdeaForge Solves

Modern software teams face an **AI Paradox**: AI can write code instantly, but the surrounding work — understanding issues, reading codebases, security review, PR documentation — still requires significant senior developer time.

The result? Issues sit in backlogs. Simple bugs take days. Security scanning is skipped when teams are rushed.

**IdeaForge eliminates this paradox** by automating the entire issue-to-PR lifecycle:

| Without IdeaForge | With IdeaForge |
|-------------------|----------------|
| Developer reads issue (10 min) | Agent reads + analyzes issue |
| Developer explores codebase (30–90 min) | Agent maps every affected file |
| Developer writes solution (1–4 hours) | Agent generates 3 approaches, picks best |
| Developer or reviewer does security check (varies) | Agent runs automated security scan |
| Developer writes PR description (20 min) | Agent creates complete, professional MR |
| **Total: 2–6 hours per issue** | **Total: 3–8 minutes** |

---

## 🧠 Architecture: Five-Agent Pipeline

```
GitLab Issue
     │
     │ (labeled: ideaforge)
     ▼
┌─────────────────────────────────────────────────────────┐
│                  IdeaForge Flow                          │
│                                                          │
│  ┌──────────────┐     ┌──────────────────┐              │
│  │    Agent 1   │────▶│     Agent 2      │              │
│  │   Issue      │     │    Problem       │              │
│  │ Intelligence │     │   Expansion      │              │
│  │              │     │                  │              │
│  │ • Root cause │     │ • File mapping   │              │
│  │ • Classify   │     │ • Call chains    │              │
│  │ • Risk assess│     │ • Stack detect   │              │
│  └──────────────┘     └──────────────────┘              │
│         │                     │                          │
│         └──────────┬──────────┘                          │
│                    ▼                                      │
│           ┌──────────────────┐                           │
│           │     Agent 3      │                           │
│           │    Solution      │                           │
│           │   Generator      │                           │
│           │                  │                           │
│           │ • 3 approaches   │                           │
│           │ • Scored matrix  │                           │
│           │ • Full code impl │                           │
│           │ • Tests written  │                           │
│           └──────────────────┘                           │
│                    │                                      │
│                    ▼                                      │
│           ┌──────────────────┐                           │
│           │     Agent 4      │                           │
│           │    Security      │◀── BLOCK if critical     │
│           │    Scanner       │    vulnerabilities found  │
│           │                  │                           │
│           │ • OWASP Top 10   │                           │
│           │ • Injection scan │                           │
│           │ • Auth check     │                           │
│           │ • Crypto check   │                           │
│           └──────────────────┘                           │
│                    │                                      │
│           (PROCEED / PROCEED_WITH_WARNINGS)              │
│                    ▼                                      │
│           ┌──────────────────┐                           │
│           │     Agent 5      │                           │
│           │  PR Generator    │                           │
│           │                  │                           │
│           │ • Create branch  │                           │
│           │ • Commit files   │                           │
│           │ • Open full MR   │                           │
│           │ • Comment issue  │                           │
│           └──────────────────┘                           │
└─────────────────────────────────────────────────────────┘
                    │
                    ▼
          Production-Ready MR
          (awaiting human review)
```

---

## 🤖 Meet the Agents

### Agent 1: Issue Intelligence
**"I understand what's broken."**

Performs deep root-cause analysis using 5-Whys methodology. Classifies the issue (bug/feature/security/etc.), estimates complexity, maps affected system areas, extracts acceptance criteria, and produces a structured intelligence report that drives every downstream agent.

**Key outputs:** Root cause, severity, complexity score, affected codebase areas, acceptance criteria, risk assessment.

---

### Agent 2: Problem Expansion
**"I know every file that needs to change."**

Explores the actual codebase — not a guess. Lists directories, reads dependency files, searches code for relevant patterns, reads every potentially affected file, traces call chains 2 levels deep, and identifies every test that needs updating.

**Key outputs:** Complete file impact map, tech stack detection, call chain analysis, lines of interest per file.

---

### Agent 3: Solution Generator
**"I write the code. All of it."**

Reads actual file contents, understands existing code style, and generates THREE complete solution approaches. Scores each on correctness, maintainability, performance, minimal footprint, and testability. Implements the optimal approach with complete, untruncated code for every file — including tests.

**Key outputs:** Three scored approaches, complete production-ready implementation, full test coverage, conventional commit messages.

---

### Agent 4: Security Scanner
**"I stop bad code before it ships."**

Performs a comprehensive OWASP Top 10 security audit of the generated solution. Checks for injection vulnerabilities, auth gaps, sensitive data exposure, crypto weaknesses, and business logic flaws. Issues a binary decision: PROCEED or BLOCK. Critical findings halt the pipeline entirely.

**Key outputs:** Severity-classified findings, exploit scenarios, remediation guidance, PROCEED/BLOCK pipeline decision.

---

### Agent 5: PR Generator
**"I open the MR. You just review it."**

The final agent. Checks the security decision, creates a new branch with a semantic name, commits each file with conventional commit messages, and opens a fully documented Merge Request with problem statement, solution rationale, security summary, testing instructions, and rollback plan. Then closes the loop by commenting on the original issue.

**Key outputs:** Named branch, committed code, professional MR, issue resolution comment.

---

## 🚀 Quick Start

### Prerequisites
- GitLab project with GitLab Duo Agent Platform enabled
- Maintainer access to the repository

### Installation

**Step 1:** Copy the `agents/` and `flows/` directories into your repository root.

```bash
cp -r agents/ /your/project/agents/
cp -r flows/ /your/project/flows/
git add agents/ flows/
git commit -m "feat(ideaforge): add IdeaForge multi-agent flow"
git push
```

**Step 2:** Verify the agents are recognized in GitLab Duo settings.

**Step 3:** Label any issue with `ideaforge` and watch the pipeline run.

---

## 📋 Usage

### Trigger IdeaForge on any issue:

1. Open any GitLab issue in your project
2. Add the label `ideaforge`
3. Watch the pipeline comments appear on the issue in real time
4. Review the Merge Request created by Agent 5

### What you'll see:

```
🔍 IdeaForge Step 1/5: Issue Intelligence complete. Root cause identified.
   Proceeding to codebase analysis...

🗺️ IdeaForge Step 2/5: Codebase mapped. 4 affected areas identified.
   Generating solutions...

💡 IdeaForge Step 3/5: Solution generated. Running security scan...

🛡️ IdeaForge Step 4/5: Security scan complete. Decision: PROCEED.
   Creating Merge Request...

🔥 IdeaForge has finished!
   👉 Review the MR here: https://gitlab.com/your/project/-/merge_requests/42
```

---

## 🏗️ Repository Structure

```
.
├── flows/
│   └── ideaforge-flow.yaml          # Main orchestration flow
├── agents/
│   ├── 01-issue-intelligence.yaml  # Root cause analysis
│   ├── 02-problem-expansion.yaml   # Codebase impact mapping
│   ├── 03-solution-generator.yaml  # Code generation
│   ├── 04-security-scanner.yaml    # Security audit
│   └── 05-pr-generator.yaml        # MR creation
├── docs/
│   └── architecture.md              # Deep technical documentation
├── LICENSE                          # MIT License
└── README.md                        # This file
```

---

## 🛡️ Security-First Design

IdeaForge has a **hard security gate** built in:

- If Agent 4 finds **any CRITICAL vulnerability** → Pipeline BLOCKED, MR not created
- Developers are notified with exact findings and remediation steps
- No vulnerable code ever reaches a Merge Request

This makes IdeaForge safer than most human PR workflows.

---

## 🎯 Supported Issue Types

IdeaForge handles any SDLC issue:

| Type | Example |
|------|---------|
| 🐛 Bug Fix | "Login fails when email has uppercase letters" |
| ✨ Feature | "Add rate limiting to the public API" |
| ⚡ Performance | "Dashboard query takes 8 seconds on large datasets" |
| 🔒 Security | "User can access other users' data by changing URL ID" |
| ♻️ Refactor | "Extract payment logic into its own service" |
| 📚 Documentation | "API endpoints lack OpenAPI spec" |
| 🧪 Testing | "User service has no integration tests" |

---

## 🏆 Prize Categories Targeted

| Prize | Justification |
|-------|--------------|
| 🥇 **Grand Prize** | Complete, novel, end-to-end automation of a real developer pain point |
| 🔧 **Most Technically Impressive** | 5-agent orchestration with inter-agent context passing, security gating, and full code generation |
| 💥 **Most Impactful** | Directly addresses the "AI Paradox" — AI writes code but humans still bottleneck everything else |
| 🤝 **GitLab & Anthropic Prize** | All agents use Anthropic Claude via the GitLab Duo Agent Platform |
| 🔌 **Easiest to Use** | One label. That's the entire UX. |

---

## 🔬 Technical Implementation

**Platform:** GitLab Duo Agent Platform (native — no external infrastructure needed)

**AI Model:** Anthropic Claude (default model in GitLab Duo Agent Platform)

**Trigger:** `issue_labeled` event with label `ideaforge`

**Tools used per agent:**
- `read_file` — Read actual file content
- `list_directory` — Explore repository structure
- `search_code` — Find relevant code patterns
- `create_file` — Create new files in solution branch
- `update_file` — Modify existing files
- `create_branch` — Create solution branch
- `create_merge_request` — Open the final MR
- `add_comment_to_issue` — Real-time progress updates

**Context passing:** Each agent receives the complete output of all preceding agents via Jinja2 template variables in the flow's step prompts.

---

## 📊 Comparison with Existing Solutions

| Feature | GitHub Copilot | Devin | Cursor | **IdeaForge** |
|---------|---------------|-------|--------|----------------|
| Reads actual issue | ❌ | ✅ | ❌ | ✅ |
| Maps codebase impact | ❌ | ✅ | ✅ | ✅ |
| Multi-approach generation | ❌ | ❌ | ❌ | ✅ |
| Built-in security scan | ❌ | ❌ | ❌ | ✅ |
| Security gate (hard block) | ❌ | ❌ | ❌ | ✅ |
| Full MR with documentation | ❌ | ✅ | ❌ | ✅ |
| Native GitLab integration | ❌ | ❌ | ❌ | ✅ |
| External infrastructure needed | ✅ | ✅ | ✅ | ❌ |
| Cost | Subscription | $500/mo | Subscription | **Free** |

---

## 🤝 Contributing

IdeaForge is open source under the MIT License. Contributions welcome:

1. Fork the repository
2. Create a feature branch: `git checkout -b feat/your-feature`
3. Commit changes: `git commit -m 'feat: add your feature'`
4. Push: `git push origin feat/your-feature`
5. Open a Merge Request (or just label an issue `ideaforge` 😄)

---

## 📄 License

MIT License — see [LICENSE](./LICENSE) for details.

---

## 🙏 Acknowledgments

Built on the **GitLab Duo Agent Platform** using **Anthropic Claude** as the intelligence layer.
Submitted to the **GitLab AI Hackathon 2026** by **Harsh Sharma**.

---

*🔥 IdeaForge — Because your backlog shouldn't wait for a developer to have time.*
