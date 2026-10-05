# Design principles

## Skill boundary

Create a skill only when it has a distinct activation intent. If two topics are normally selected by the same user request, keep one skill and route internally after source/version inspection.

## Context budget

Claude Code routing sees skill metadata before activation; the full body is loaded when relevant. Optimize in this order:

1. precise, non-overlapping `description`;
2. dense task decisions in `SKILL.md`;
3. direct `references/` only for deeper stable detail;
4. official docs/source for volatile API catalogs.

Do not repeat generic “expert”, workflow or source-truth prose across every skill unless the rule changes execution materially.

## Source/version authority

Repository build/BOM/wrapper/configuration wins. Version-sensitive methods, coordinates, descriptors and behavior must be checked against official documentation/Javadocs/source for that exact line. Dated research baselines are navigation hints, never upgrade commands.

## Architecture restraint

Reuse the project’s existing owner/provider/adapter before adding another abstraction. A pattern is not a requirement. Framework-version differences are not a reason to duplicate the whole skill tree.

## Verification

A change is not proven by plausible code. Use the repository-proven build/test/check gate and distinguish baseline failures from regressions. Runtime-only platform behavior remains unverified until exercised in the relevant environment.

## Publication safety

No credentials, private identifiers, internal endpoints, local/container paths, uploaded-file IDs or proprietary source. External material can contribute facts, failure modes and architecture concepts subject to licensing; shipped prose must be independently written.

## Cut-regression rule

Optimization is not deletion-by-default. After compressing a skill, compare against the previous release and recover any removed rule that changes source intake, architecture ownership, compatibility, lifecycle/failure semantics, or verification. Prefer restoring that rule behind progressive disclosure instead of duplicating it in every activated body.
