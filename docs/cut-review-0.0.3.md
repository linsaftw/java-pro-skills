# 0.0.3 cut-regression review

Purpose: audit what 0.0.2 removed from 0.0.1, restore material that improves coding-agent correctness, and keep the runtime context footprint below 0.0.1.

## Decision rule

A removed block is restored only when it changes an agent decision, prevents a concrete failure mode, or improves proof. Repetition, inventories, persona text, motivational prose, generic “expert” traits, duplicated version trees, and volatile catalogs stay removed.

## Review of 0.0.1 -> 0.0.2 cuts

| Cut | Decision | Reason |
|---|---|---|
| Long routing descriptions | KEEP CUT | They are always-visible routing cost. 0.0.2 retained the discriminating trigger terms. |
| Seven-rule operating contract repeated in every `SKILL.md` | RESTORE VIA REFERENCE | Useful content existed, but duplicating it in every invoked body was wasteful. 0.0.3 restores the useful distinctions in an on-demand reference. |
| `Fast workflow` line | RESTORE VIA REFERENCE | Cheap, useful execution ordering; restored once in the repository-execution reference. |
| Explicit inspection of entrypoints/config/resources/tests/locks | RESTORE | The one-line 0.0.2 contract said “build, locked versions and touched code” but lost the breadth needed to catch integration work. |
| “Current source and locked versions are authority” | KEEP + STRENGTHEN | Already present in 0.0.2; 0.0.3 adds BOM/toolchain and exact-target behavior/migration wording. |
| “Smallest change / reuse owner” | KEEP | Preserved in 0.0.2; retained. |
| Explicit lifecycle/cancellation/resource ownership | RESTORE | This was materially lost by compression and prevents leaks, reload defects, detached work and threading errors. |
| Explicit baseline vs regression distinction | RESTORE | “Run verification gate” was not enough; agents need to separate pre-existing red from new regressions. |
| Minimum supported runtime/platform verification | RESTORE | Compilation cannot prove all cross-JDK, Minecraft, Android or framework runtime behavior. |
| Full per-file inventories of reference repositories | KEEP CUT | Useful during the first audit, but high maintenance/token cost. 0.0.3 restores a compact capability/disposition matrix instead. |
| Long skill catalog prose | KEEP CUT | The live frontmatter is the source of truth; generated catalog is sufficient. |
| Empty references and duplicate framework-version trees | KEEP CUT | No execution value. |

## Restored execution contract

Every skill now contains only a short pointer in its invoked body. Repository-changing tasks read `references/repository-execution.md`; explanation-only tasks do not. The reference restores:

- build/wrapper/toolchain/BOM/dependency-lock inspection;
- entrypoints/callers/config/resources/tests/logs/dirty-state intake;
- exact target-version API authority;
- first-bad-state or extension-point tracing;
- existing owner/provider/adapter reuse;
- compatibility preservation;
- explicit failure semantics;
- lifecycle, cancellation, threading and resource ownership;
- baseline classification, focused proof and full relevant gate;
- minimum supported runtime/platform proof when compile-time evidence is insufficient.

## What remains intentionally absent

- personality/roleplay instructions;
- forced model selection;
- generic SOLID/design-pattern checklists in every skill;
- duplicated Java/Spring/Minecraft advice across unrelated skills;
- exhaustive API/member catalogs that become stale;
- arbitrary “always use X” framework/style claims without project evidence;
- release-specific defaults in core instructions when exact target discovery is possible.

## Acceptance criteria

0.0.3 passes only if:

1. all 33 domain skill bodies remain present;
2. routing descriptions do not regress toward 0.0.1 size;
3. each skill exposes the same compact repository-execution reference;
4. invoked `SKILL.md` aggregate remains below 0.0.1;
5. `SKILL.md + execution reference` aggregate remains below the old repeated 0.0.1 bodies or provides a clearly justified progressive-disclosure improvement;
6. routing, install, privacy and version checks still pass.

## Measured result

Compared with 0.0.1:

- routing-description characters: **10,300 -> 5,586 (-45.8%)**;
- aggregate `SKILL.md` body characters (frontmatter excluded by comparator): **79,884 -> 44,663 (-44.1%)**;
- aggregate body words: **10,616 -> 5,451 (-48.7%)**;
- on-demand repository-execution reference: **1,131 characters / 135 words**;
- **33/33** individual skills remain smaller than their 0.0.1 counterpart even when adding the execution reference to the invoked 0.0.3 skill;
- normalized domain guidance is **32/33 exact** against 0.0.1; the only intentional change remains `developing-android`, updated for the newer verified Android/AGP baseline.

This is the desired outcome: restore decision-critical context without restoring the repeated prompt cost.
