# 🔥 IdeaForge AI

> **From Issue to PR — Fully Autonomous. Zero Developer Effort.**

[![GitLab Duo Agent Platform](https://img.shields.io/badge/GitLab%20Duo-Agent%20Platform-orange?style=for-the-badge&logo=gitlab)](https://docs.gitlab.com/ee/user/duo_workflow/)
[![Powered by Anthropic](https://img.shields.io/badge/Powered%20by-Anthropic%20Claude-blue?style=for-the-badge)](https://www.anthropic.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](./LICENSE)

---

## 🎯 What is IdeaForge?

IdeaForge is a **multi-agent AI flow** built natively on the **GitLab Duo Agent Platform**.
Assign it to any GitLab issue and watch five AI agents collaborate to:

1. Analyze the root cause
2. Map every affected file in the codebase
3. Generate three solution approaches and implement the best one
4. Run a full OWASP security scan
5. Open a production-ready Merge Request

**One trigger. Five agents. One MR. Zero developer effort.**

---

## 🎬 Demo Video

📺 [Watch the 3-minute demo on YouTube](https://youtu.be/your-demo-link)

---

## 🧠 Architecture: Five-Agent Sequential Pipeline

```
Issue Assigned to IdeaForge Flow
            │
            ▼
  ┌─────────────────────┐
  │   Agent 1           │
  │  Issue Intelligence │  → Root cause, severity, complexity, risk, acceptance criteria
  └──────────┬──────────┘
             │ passes: INTELLIGENCE_REPORT
             ▼
  ┌─────────────────────┐
  │   Agent 2           │
  │  Problem Expansion  │  → Reads actual files, maps call chains, identifies every change
  └──────────┬──────────┘
             │ passes: IMPACT_MAP
             ▼
  ┌─────────────────────┐
  │   Agent 3           │
  │  Solution Generator │  → 3 scored approaches, full production-ready code + tests
  └──────────┬──────────┘
             │ passes: SOLUTION_REPORT
             ▼
  ┌─────────────────────┐
  │   Agent 4           │
  │  Security Scanner   │  → OWASP Top 10 scan. CRITICAL finding = BLOCK (no MR created)
  └──────────┬──────────┘
             │ passes: SECURITY_REPORT
             ▼
  ┌─────────────────────┐
  │   Agent 5           │
  │  PR Generator       │  → Branch + commits + fully documented MR + issue comment
  └─────────────────────┘
```

Each agent receives the **complete output of all previous agents** as context. Nothing is lost between steps.

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

# Commit
cd /your/project
git add .gitlab/ AGENTS.md
git commit -m "feat: add IdeaForge multi-agent flow"
git push
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

### Step 4: Watch it work

You'll see five progress comments appear on the issue:

```
🔍 IdeaForge Step 1/5 — Issue Intelligence Complete
   Root cause identified. Proceeding to codebase mapping... ⚙️

🗺️ IdeaForge Step 2/5 — Codebase Mapped
   4 files identified for changes. Generating solution... 💡

💡 IdeaForge Step 3/5 — Solution Generated
   "Minimal Patch" selected from 3 candidates. Running security scan... 🛡️

🛡️ IdeaForge Step 4/5 — Security Scan Complete
   Decision: PROCEED | Issues: Critical=0 High=0 Medium=1
   Creating Merge Request... 🚀

🔥 IdeaForge Complete!
   👉 Review the MR: https://gitlab.com/your/project/-/merge_requests/42
```

---

## 📁 Repository Structure

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

IdeaForge has a **hard security gate**:

- Agent 4 runs an OWASP Top 10 scan on every generated solution
- Any **CRITICAL** finding → pipeline stops, MR is NOT created
- The issue receives a detailed comment with all findings and remediation steps
- Developers fix the issues, re-trigger IdeaForge — clean pipeline, clean MR

This makes IdeaForge safer than most human-written PR workflows.

---

## 🔬 Technical Implementation

| Aspect | Details |
|--------|---------|
| **Platform** | GitLab Duo Agent Platform (native — no external infra) |
| **Schema** | Flow Registry v1 (`version: "v1"`, `environment: ambient`) |
| **AI Model** | Anthropic Claude (via GitLab Duo Agent Platform default) |
| **Trigger** | Assign flow to issue OR mention `@ideaforge` |
| **Agents** | 5 `AgentComponent` entries in one YAML file |
| **Context passing** | `from: "component:{agent}.output"` inputs |
| **Total files** | 4 files — maximum simplicity, zero external dependencies |

### Tools used across the pipeline

| Tool | Used by |
|------|---------|
| `get_issue` | Agents 1, 2, 5 |
| `list_repository_tree` | Agents 2, 5 |
| `get_repository_file` | Agents 2, 3, 4 |
| `find_files` | Agents 2, 3 |
| `blob_search` | Agents 2, 3, 4 |
| `create_file` | Agent 5 |
| `create_commit` | Agent 5 |
| `create_branch` | Agent 5 |
| `create_merge_request` | Agent 5 |
| `create_issue_note` | All agents (progress comments) |

---

## 📊 What Makes IdeaForge Different

| Feature | GitHub Copilot | Devin | **IdeaForge** |
|---------|---------------|-------|----------------|
| Reads actual issue | ❌ | ✅ | ✅ |
| Maps codebase impact | ❌ | ✅ | ✅ |
| 3-approach generation with scoring | ❌ | ❌ | ✅ |
| OWASP security scan | ❌ | ❌ | ✅ |
| Hard security gate (BLOCK) | ❌ | ❌ | ✅ |
| Full documented MR | ❌ | ✅ | ✅ |
| Native GitLab — no external infra | ❌ | ❌ | ✅ |
| Monthly cost | $19+ | $500 | **Free** |

---

## 📄 License

MIT — see [LICENSE](./LICENSE)

---

*🔥 IdeaForge — Because your backlog shouldn't wait for a developer to have time.*
