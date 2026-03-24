# IdeaForge AI 🔥

> From Issue to PR — Fully Autonomous. Zero Developer Effort.

## What is IdeaForge?

IdeaForge is a multi-agent AI system built on GitLab that automatically analyzes GitLab issues, maps codebase impact, generates solutions, performs security checks, and creates Merge Requests — with zero developer input.

## Agents

- Agent 1: Issue Intelligence — Root cause analysis
- Agent 2: Problem Expansion — Codebase impact mapping  
- Agent 3: Solution Generator — 3 solution approaches
- Agent 4: Security Scanner — Vulnerability detection
- Agent 5: PR Generator — Auto Merge Request creation

## Setup

1. Clone the repo
2. Install dependencies:
   pip install groq requests python-dotenv
3. Create .env file:
   GITLAB_TOKEN=your_token
   GROQ_API_KEY=your_key
   GITLAB_PROJECT_ID=your_project_id
4. Run:
   python main.py

## Tech Stack

- Python
- Groq API (Llama 3.3)
- GitLab API
- python-dotenv

## License
MIT

---
*For instructions on how to get started in the hackathon, take a look at the [onboarding issue](../../work_items/1) in this project.*
