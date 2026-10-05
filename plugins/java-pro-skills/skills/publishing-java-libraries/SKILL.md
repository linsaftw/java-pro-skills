---
name: publishing-java-libraries
description: Publish Java libraries/plugins with API compatibility, SemVer, metadata, sources/Javadocs, signing, BOMs, reproducibility and release automation. Use for reusable artifact releases.
---

# Publishing Java Libraries

A published artifact is a compatibility contract.

## Rules

- Separate public API from implementation packages; document supported Java/runtime/framework baselines.
- Semantic versioning reflects source/binary/behavior contract, not commit size.
- Publish sources and Javadocs where ecosystem expects them; metadata includes license, SCM, project URL, developers/organization as intentionally public information only.
- Never publish local paths, credentials, private repository URLs, internal hostnames, or generated secrets.
- Use dependency scopes so consumers do not inherit implementation details unnecessarily.
- Shaded/relocated dependencies stay private; public signatures must not expose relocated types.
- Run binary/source compatibility checks for mature libraries when feasible.
- Release from a clean, tagged, reproducible commit with CI-proven tests.

## Execution

For repository-changing work, read [references/repository-execution.md](references/repository-execution.md) before editing. For explanation-only work, keep to this skill and exact-version official sources.
