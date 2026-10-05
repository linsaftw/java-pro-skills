# Contributing

Changes should improve routing quality, factual correctness, token efficiency, or coverage of a real Java/JVM development domain.

## Before editing

1. Read `CLAUDE.md` and the target skill plus its direct references.
2. Inspect current official target-version documentation for volatile APIs and versions.
3. Prefer changing an existing skill over adding overlapping metadata.
4. Keep normative guidance version-agnostic where possible; put dated current facts in `docs/verified-baselines.md`.
5. Do not copy text or implementation bodies from reference repositories.

## Skill contract

- `name`: lowercase letters/numbers/hyphens, maximum 64 characters, no reserved `claude` or `anthropic` term.
- `description`: concise routing description that states what the skill does and when it applies.
- `SKILL.md`: compact operational instructions; target <500 lines.
- Put detailed/versioned material under the same skill's `references/` directory and keep references one hop deep.
- Project source, lockfiles, logs, and exact target-version official APIs always override skill memory.

## Verification

```bash
python3 scripts/validate_repo.py
python3 scripts/list_skills.py
```

If a routing description changes, update `evals/routing.tsv` with at least three representative activation prompts and add overlap/negative cases when another skill could plausibly win.
