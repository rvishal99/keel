## What & why
Briefly: what this changes and the problem it solves. Link the issue (`Closes #…`).

## Changes
-

## Tests
- [ ] Added/updated tests (watched the new test fail first)
- [ ] `KEEL_TEST_DATABASE_URL=… pytest -q` is green
- [ ] For LLM-touching changes: ran the gated live test with a provider key (eval floor holds)

## Checklist
- [ ] Core stays harness-agnostic (harness logic under `adapters/`)
- [ ] Honors the design principles (fail open, warn-not-block, evidence-or-silence, append-only, decisions-are-data)
- [ ] Schema change? included a migration (`ALTER … IF NOT EXISTS`) and noted it
- [ ] No secrets in the diff
- [ ] Docs updated if behavior/config changed
