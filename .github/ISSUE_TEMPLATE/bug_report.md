---
name: Bug report
about: Something isn't working as expected
title: "bug: "
labels: bug
---

## What happened
A clear description of the bug (observed vs expected).

## Repro
Minimal steps / the MCP call or hook input that triggers it:
```
# e.g. the tools/call body or the PreToolUse stdin JSON
```

## Environment
- Keel commit:
- How you run it (local / docker-compose / Cloud Run):
- LLM provider (`KEEL_LLM_PROVIDER`) and model:
- Harness (Claude Code / Codex / …) + version, if relevant:

## Evidence
Logs, tracebacks, request IDs, screenshots (omit secrets/tokens).
