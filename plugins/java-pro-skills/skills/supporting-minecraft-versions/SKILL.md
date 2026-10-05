---
name: supporting-minecraft-versions
description: Bukkit/Spigot/Paper multiversion support from legacy to current: classloading isolation, capabilities and compatibility adapters. Use for 1.8+ compatibility or linkage failures.
---

# Supporting Minecraft Versions

Multi-version support is primarily a **JVM classloading/API-shape** problem.

## Hard rules

- Prefer capability detection over parsing server brand/version strings.
- Never reference a modern-only type from an always-loaded legacy-safe class in imports, fields, method descriptors, casts, `instanceof`, annotations, or static initialization. A branch cannot protect linkage that occurs before the branch.
- Centralize compatibility by domain: scheduler, materials/sounds/entities, text, block state/collision, persistence/custom data, items/profiles/potions, teleport, packets.
- Resolve aliases/capabilities once at startup and cache immutable results.
- Required capabilities fail clearly; optional cosmetics degrade explicitly.
- Cross-version business logic consumes plugin-owned neutral models, not `BlockData`, `MaterialData`, NMS, or Folia types directly.

## Major eras

- pre-1.13: legacy material/data model
- 1.13+: flattening and BlockData era
- 1.14+: PersistentDataContainer becomes available
- modern Paper: Adventure/native APIs expand, but Spigot/legacy compatibility still requires isolation
- Folia: ownership-aware scheduling, not a version-string branch
- current Paper generation has moved beyond the old `1.21.x` naming in docs; always inspect exact current API coordinate/Java requirement.

Read [references/multiversion-hotspots.md](references/multiversion-hotspots.md).

## Execution

For repository-changing work, read [references/repository-execution.md](references/repository-execution.md) before editing. For explanation-only work, keep to this skill and exact-version official sources.
