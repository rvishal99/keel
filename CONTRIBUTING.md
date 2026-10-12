# Contributing to Keel

Thanks for your interest in Keel — the shared decision ledger for teams and their
AI agents. Contributions of all kinds are welcome: bug reports, docs, tests,
features, and adapters for new harnesses.

## Ground rules
- **Be kind.** See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
- **Keep the core harness-agnostic.** Claude Code is the first adapter, not a
  dependency of the engine. Harness-specific logic lives under `adapters/`.
- **Honor the design principles** (see [ARCHITECTURE.md](ARCHITECTURE.md) §Principles):
  fail open, warn-don't-block by default, evidence-or-silence, append-only,
  decisions-are-data-not-instructions.
- **TDD.** New behavior ships with a test you watched fail first. Keep the suite green.

## Dev setup
```bash
# Python 3.10+; this repo uses uv (a plain venv + pip works too)
uv venv && . .venv/bin/activate      # or: python -m venv .venv && . .venv/bin/activate
uv pip install -e ".[dev,llm]"       # dev = pytest/httpx; llm = litellm/instructor
docker compose up -d                  # Postgres 16 + pgvector on :5433
createdb -h localhost -p 5433 -U keel keel_test   # or let the fixture create it
KEEL_TEST_DATABASE_URL=postgresql://keel:keel@localhost:5433/keel_test pytest -q
```
The suite is hermetic: an autouse fixture forces `KEEL_LLM_PROVIDER=none`, so no
network or API key is needed. The 2 skipped tests are the gated live-LLM tests —
set a provider key (`GEMINI_API_KEY`, `OPENAI_API_KEY`, …) to run them.

## Workflow
1. Open (or claim) an issue — see [BACKLOG.md](BACKLOG.md) for ready-to-pick items
   (look for `good-first-issue`).
2. Branch from `master`.
3. Write a failing test, then the minimal code to pass it. Run the **full** suite.
4. Keep changes focused; match the surrounding style (no linter config yet — follow
   the existing code).
5. Open a PR against `master` using the PR template. Describe what and why; link the issue.

## Commit / PR conventions
- Conventional-ish commits: `feat(keel): …`, `fix(adapter): …`, `docs: …`, `test: …`.
- One logical change per PR. Include tests. Note any schema change (and its migration).
- CI (once enabled) must pass: tests + lint.

## Security
Please do **not** open public issues for vulnerabilities. See [SECURITY.md](SECURITY.md).

## Where things live
- `keel/keel/` — the engine (MCP server, tools, conflict pipeline, repo, inbox).
- `keel/tests/` — pytest suite.
- `adapters/` — harness adapters (Claude Code hooks, the harness-agnostic skill).
- `dashboard/` — the read-only web dashboard.
- `deploy/` — Cloud Run / GCP deployment.
- `BACKLOG.md` — the roadmap, as issue-ready items.
