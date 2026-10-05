---
name: developing-minecraft-mods
description: Minecraft Java mod development with Fabric/Loom, mappings, registries, networking, data generation, mixins and client/server separation. Use for Fabric-style mods, not server plugins.
---

# Developing Minecraft Mods

Do not apply Bukkit plugin assumptions to mods. Confirm loader, Minecraft version, mappings, and client/server target first.

## Fabric rules

- Use the project Gradle wrapper and Fabric Loom/toolchain versions already locked.
- Keep client-only code out of dedicated-server classloading paths.
- Prefer public Fabric/vanilla extension APIs before mixins; mixins are precise patches with version-sensitive targets.
- Registries, codecs/data components, networking, rendering, and data generation are strongly Minecraft-version-dependent: verify exact current Fabric docs/source.
- Treat packet payloads as untrusted/bounded and execute world/entity mutation on the game thread required by the target API.
- Data generation should be deterministic and committed/verified according to project convention.

Current Fabric documentation uses the 26.2 generation and JDK 25 for recent Minecraft development; project version wins.

## Execution

For repository-changing work, read [references/repository-execution.md](references/repository-execution.md) before editing. For explanation-only work, keep to this skill and exact-version official sources.
