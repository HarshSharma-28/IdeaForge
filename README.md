# 🔥 IdeaForge AI

> **From Issue to PR — Fully Autonomous. Zero Developer Effort.**

[![GitLab Duo Agent Platform](https://img.shields.io/badge/GitLab%20Duo-Agent%20Platform-orange?style=for-the-badge&logo=gitlab)](https://docs.gitlab.com/ee/user/duo_workflow/)
[![Powered by Anthropic](https://img.shields.io/badge/Powered%20by-Anthropic%20Claude-blue?style=for-the-badge)](https://www.anthropic.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](./LICENSE)

---

## 🎯 What is IdeaForge?

IdeaForge is a **multi-agent AI system** built natively on the **GitLab Duo Agent Platform** that transforms a GitLab issue into a production-ready Merge Request — entirely autonomously.

**One label. Five agents. One Merge Request. Zero developer effort.**

When a developer labels any GitLab issue with `ideaforge` or assigns it to the IdeaForge flow, a coordinated team of five AI agents springs into action. They read the issue, explore the codebase, write the code, scan for security vulnerabilities, and open a fully documented MR — all within minutes.

This isn't a chatbot. This is a **digital engineering teammate** that does the work.

---

## 🎬 Demo Video

📺 [Watch the 3-minute demo on YouTube](https://youtu.be/your-demo-link)

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

## 🧠 Architecture: Five-Agent Sequential Pipeline

```
GitLab Issue
     │
     │ (labeled: ideaforge or assigned to flow)
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

Each agent receives the **complete output of all previous agents** as context. Nothing is lost between steps.

---

## 🤖 Meet the Agents

### Agent 1: Issue Intelligence
**"I understand what's broken."**

Performs deep root-cause analysis using 5-Whys methodology. Classifies the issue (bug/feature/security/etc.), estimates complexity, maps affected system areas, extracts acceptance criteria, and produces a structured intelligence report that drives every downstream agent.

### Agent 2: Problem Expansion
**"I know every file that needs to change."**

Explores the actual codebase — not a guess. Lists directories, reads dependency files, searches code for relevant patterns, reads every potentially affected file, traces call chains 2 levels deep, and identifies every test that needs updating.

### Agent 3: Solution Generator
**"I write the code. All of it."**

Reads actual file contents, understands existing code style, and generates THREE complete solution approaches. Scores each on correctness, maintainability, performance, minimal footprint, and testability. Implements the optimal approach with complete, untruncated code for every file — including tests.

### Agent 4: Security Scanner
**"I stop bad code before it ships."**

Performs a comprehensive OWASP Top 10 security audit of the generated solution. Checks for injection vulnerabilities, auth gaps, sensitive data exposure, crypto weaknesses, and business logic flaws. Issues a binary decision: PROCEED or BLOCK. Critical findings halt the pipeline entirely.

### Agent 5: PR Generator
**"I open the MR. You just review it."**

The final agent. Checks the security decision, creates a new branch with a semantic name, commits each file with conventional commit messages, and opens a fully documented Merge Request with problem statement, solution rationale, security summary, testing instructions, and rollback plan. Then closes the loop by commenting on the original issue.

---

## 🚀 Quick Start

### Step 1: Add IdeaForge to your project

Copy the `.gitlab/` directory and `AGENTS.md` to your project root:

```bash
# Clone IdeaForge
git clone https://gitlab.com/gitlab-ai-hackathon/ideaforge.git

# Copy the flow files into your project
cp -r ideaforge/.gitlab/ /your/project/
cp ideaforge/AGENTS.md /your/project/
```

### Step 2: Register the flow in GitLab

1. Go to your project → **Automate → Flows → New Flow**
2. Set the configuration path to: `.gitlab/duo/flows/ideaforge.yaml`
3. Name it: `IdeaForge`
4. Save

### Step 3: Trigger IdeaForge on any issue

Go to any issue in your project and either:
- **Assign** the IdeaForge flow to the issue (via the Assignee field)
- Comment: `@ideaforge` in the issue
- Add the label `ideaforge`

---

## 🏗️ Repository Structure

```
.
├── AGENTS.md                        # Context file — all Duo agents read this automatically
├── README.md                        # This file
├── LICENSE                          # MIT License
└── .gitlab/
    └── duo/
        ├── agent-config.yml         # Flow execution config (runner setup)
        └── flows/
            └── ideaforge.yaml       # The complete 5-agent pipeline (Flow Registry v1)
```

---

## 🛡️ Security-First Design

IdeaForge has a **hard security gate** built in:

- Agent 4 runs an OWASP Top 10 scan on every generated solution.
- If Agent 4 finds **any CRITICAL vulnerability** → Pipeline BLOCKED, MR not created.
- Developers are notified with exact findings and remediation steps.
- Any **CRITICAL** finding → pipeline stops, MR is NOT created.
- The issue receives a detailed comment with all findings and remediation steps.
- Developers fix the issues, re-trigger IdeaForge — clean pipeline, clean MR.

This makes IdeaForge safer than most human-written PR workflows.

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
| 🔌 **Easiest to Use** | One label or comment. That's the entire UX. |

---

## 🔬 Technical Implementation

| Aspect | Details |
|--------|---------|
| **Platform** | GitLab Duo Agent Platform (native — no external infra) |
| **Schema** | Flow Registry v1 (`version: "v1"`, `environment: ambient`) |
| **AI Model** | Anthropic Claude (via GitLab Duo Agent Platform default) |
| **Trigger** | Assign flow to issue, mention `@ideaforge`, or label `ideaforge` |
| **Agents** | 5 `AgentComponent` entries in one YAML file |
| **Context passing** | `from: "component:{agent}.output"` inputs |
| **Total files** | 4-5 files — maximum simplicity, zero external dependencies |

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

## 📄 License

MIT License — see [LICENSE](./LICENSE) for details.

---

## 🙏 Acknowledgments

Built on the **GitLab Duo Agent Platform** using **Anthropic Claude** as the intelligence layer.
Submitted to the **GitLab AI Hackathon 2026** by **Harsh Sharma**.

---

*🔥 IdeaForge — Because your backlog shouldn't wait for a developer to have time.*
