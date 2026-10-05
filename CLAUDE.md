# Repository instructions for coding agents

This repository is a public Agent Skills collection. Preserve privacy and source accuracy.

## Before editing a skill

1. Read the target `SKILL.md` and its direct references.
2. Read `docs/agent-research-playbook.md`.
3. If the change names a current version/API, verify it against an official source and update `docs/verified-baselines.md` only when the baseline itself changes.
4. Run `python3 scripts/validate_repo.py`.

## Hard rules

- No personal/private data, local paths, secrets, internal hostnames, uploaded file IDs, or private product references.
- Skill `name` cannot contain `claude` or `anthropic`; these are reserved by current Agent Skills validation.
- Description is third-person, <=1024 chars, and says both what the skill does and when to use it.
- `SKILL.md` stays <500 lines. Split detail into direct `references/` files.
- No volatile “latest” API claims in normative instructions without a dated source. Prefer project-version-first rules.
- Do not copy implementation text from audited repositories. Generalize facts and architecture; preserve licenses.
- One production concern per skill. Add a new skill only if routing improves enough to justify metadata/context cost.
