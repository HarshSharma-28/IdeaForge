# IdeaForge Architecture — Deep Technical Documentation

## Overview

IdeaForge is a sequential multi-agent flow where each agent builds on the structured output of its predecessor. Context is explicitly threaded through the pipeline — no agent operates in isolation.

---

## Agent Communication Protocol

Each agent produces a structured report using a delimiter-based format:

```
{AGENT_REPORT_TYPE}
─────────────────────────────
{structured content}
─────────────────────────────
END_{AGENT_REPORT_TYPE}
```

The IdeaForge Flow passes these reports as Jinja2 template variables into each subsequent agent's prompt:

```yaml
prompt: |
  INTELLIGENCE REPORT:
  {{ steps.issue_intelligence.output }}

  IMPACT MAP:
  {{ steps.problem_expansion.output }}
```

This ensures:
1. Full context is available to every agent
2. Agents can parse structured data from predecessors
3. No information is lost between pipeline stages

---

## Agent 1: Issue Intelligence — Design Decisions

### Why 5-Whys Methodology?
Surface-level bug fixes address symptoms, not causes. The 5-Whys forces the agent to trace causality chains, ensuring the solution targets the actual root cause rather than applying a band-aid.

### Why Classification Matters
The `type` and `complexity` fields downstream guide Agent 3's solution selection. A `simple` bug patch shouldn't trigger a full architectural refactor. A `complex` feature shouldn't be patched.

### Acceptance Criteria Extraction
Many issues lack clear acceptance criteria. By extracting or inferring them, IdeaForge ensures the solution is verifiable. These criteria feed directly into Agent 3's test generation.

---

## Agent 2: Problem Expansion — Design Decisions

### Why Read Actual Files?
Generic code generation without reading the target codebase produces code that:
- Doesn't match the project's style
- Imports the wrong packages
- Uses different naming conventions
- Misses existing utility functions that should be reused

Agent 2 forces grounding in reality.

### Call Chain Tracing
The agent traces at minimum 2 levels deep. This catches cascading failures: a change to a utility function may break 5 callers that don't appear in the issue description.

### Tech Stack Auto-Detection
Rather than requiring configuration, IdeaForge reads standard dependency files:
- `package.json` → Node.js, identifies test framework (jest, mocha, vitest)
- `requirements.txt` / `pyproject.toml` → Python, identifies test framework (pytest, unittest)
- `pom.xml` → Java/Maven
- `go.mod` → Go
- `Cargo.toml` → Rust
- `Gemfile` → Ruby

This eliminates setup friction entirely.

---

## Agent 3: Solution Generator — Design Decisions

### Three-Approach Generation
Single-solution generation is fragile — the model may fixate on one approach. Three approaches with explicit scoring force consideration of alternatives:

| Criterion | Weight | Rationale |
|-----------|--------|-----------|
| Correctness | 30% | Wrong code is worse than no code |
| Maintainability | 25% | Code is read more than written |
| Performance | 20% | Premature optimization is evil but perf regressions are too |
| Minimal footprint | 15% | New code = new bugs |
| Testability | 10% | If it can't be tested, it can't be trusted |

### No Truncation Policy
The single biggest failure mode in AI code generation is truncated output. The instruction `NEVER truncate code` is explicitly stated and reinforced with the note that `// ... rest of code` is FORBIDDEN. This is a deliberate attempt to force complete output.

### Style Matching
Agent 3 is instructed to re-read files before writing solutions. This ensures:
- Same indentation (tabs vs. spaces, 2 vs. 4 spaces)
- Same naming convention (camelCase vs. snake_case)
- Same error handling pattern (try/catch vs. Result types vs. callbacks)
- Same import style (named vs. default, relative vs. absolute)

---

## Agent 4: Security Scanner — Design Decisions

### Hard Block Mechanism
The security gate is binary and enforced at the flow level. If `pipeline_decision: BLOCK`, Agent 5 is instructed to stop and comment on the issue instead of creating an MR.

This is a critical differentiator from most automated code generation tools which have no security layer.

### OWASP Top 10 Alignment
By explicitly mapping findings to OWASP categories, the security report becomes actionable and educational — developers learn what class of vulnerability was avoided.

### False Positive Discipline
The agent is instructed to require a concrete exploit scenario for every finding. This prevents noise:
- Every CRITICAL must have: "An attacker could..."
- Uncertain findings are marked INFO, not CRITICAL

### Exploit Scenario Format
Each finding includes a concrete exploit scenario, making the security report immediately useful to a developer without requiring deep security expertise.

---

## Agent 5: PR Generator — Design Decisions

### Branch Naming Convention
`ideaforge/{issue-id}-{slugified-title}` is deterministic and human-readable:
- Easy to find in branch lists
- Links back to originating issue
- Consistent across all IdeaForge MRs

### MR Description Structure
The MR description is structured for multiple audiences:
- **Developers** → What changed, why, how to test
- **Reviewers** → Security findings, alternative approaches considered
- **Product** → Plain English problem statement
- **Future developers** → Rollback plan, architecture decisions

### Checkbox List
The checklist in the MR description serves a dual purpose:
- Pre-checked items show what IdeaForge did automatically
- Unchecked items (CI passing, human review) make it clear what humans still need to do

### Error Resilience
If the MR creation fails partway through, Agent 5 is instructed to post the complete file contents as issue comments. This ensures the work is never lost even if the automation fails at the last mile.

---

## Flow-Level Design

### Sequential vs. Parallel Execution
The agents run sequentially by design:
- Agent 2 needs Agent 1's output to know where to look
- Agent 3 needs Agent 2's output to know what files to read and change
- Agent 4 needs Agent 3's output to have code to scan
- Agent 5 needs Agent 4's security decision

Parallelism was considered but rejected — the quality gain from full context passing outweighs the speed gain from parallel execution.

### Real-Time Issue Comments
Each agent posts a progress comment to the issue upon completion. This provides:
- Visibility into what IdeaForge is doing
- A record of the pipeline execution
- Early warning if an agent is blocked

### Trigger Design
`issue_labeled: ideaforge` was chosen as the trigger over `issue_created` for two reasons:
1. Not every issue should be automated — labeling is an explicit opt-in
2. The developer may want to enrich the issue description before triggering IdeaForge

---

## Failure Modes and Mitigations

| Failure Mode | Mitigation |
|-------------|------------|
| Issue too vague to analyze | Agent 1 flags ambiguity explicitly in report |
| Codebase too large to fully read | Agent 2 prioritizes based on intelligence report focus areas |
| Solution code is incomplete | Agent 5 detects truncation and notes it in MR description |
| Security scan finds critical issue | Pipeline hard-blocks before MR creation |
| Branch creation fails | Agent 5 posts code as issue comments as fallback |
| MR creation fails | Agent 5 posts complete solution in issue comment |

---

## Why This Wins

IdeaForge addresses the core "AI Paradox" identified by the hackathon:

> *AI writes code. That's expected now. The real opportunity? Everything else.*

Every agent addresses a different "everything else":
- Agent 1 → **Planning** (understanding the issue)
- Agent 2 → **Architecture** (knowing the codebase)  
- Agent 3 → **Engineering** (writing the code)
- Agent 4 → **Security** (catching vulnerabilities)
- Agent 5 → **Operations** (shipping the work)

The result is not just a code generator. It's a complete, autonomous engineering workflow.
