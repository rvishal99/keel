# Security Policy

## Reporting a vulnerability
**Do not open a public GitHub issue for security vulnerabilities.**

Email **contact.vasanml@gmail.com** with:
- a description of the issue and its impact,
- steps to reproduce (a minimal PoC if possible),
- affected version / commit.

We aim to acknowledge within 3 business days and to provide a remediation timeline
after triage. Please give us a reasonable window to fix before any public disclosure;
we'll credit you (if you wish) in the release notes.

## Scope / sensitive areas
Keel handles team decisions and bearer tokens, and injects ledger text into agent
context. Areas of particular interest:
- **Auth:** bearer-token handling, session scoping, (upcoming) OAuth/connect flows.
- **Prompt injection:** ledger text is treated as *data, not instructions* and is
  delimited/guarded when injected into an agent's context; report any bypass.
- **Multi-tenancy:** cross-project/org data leakage via the API or MCP tools.
- **Secrets:** anything that could expose provider API keys or tokens.

## Supported versions
Pre-v1: only the latest `master` is supported. Pin a commit for reproducibility.

## Good hygiene (for operators)
- Keep provider keys (Gemini/OpenAI/…) in a secret manager, never in the repo.
- Set `KEEL_CORS_ORIGINS` to your dashboard origin in production (default `*`).
- Rotate tokens; prefer read-only tokens for the dashboard where possible.
