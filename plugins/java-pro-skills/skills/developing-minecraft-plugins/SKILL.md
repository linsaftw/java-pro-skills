---
name: developing-minecraft-plugins
description: Bukkit/Spigot/Paper plugin development: lifecycle, events, commands, config, services, persistence, schedulers and thread safety. Use for general Minecraft server plugins.
---

# Developing Minecraft Plugins

First identify the runtime contract: Bukkit/Spigot/Paper, Minecraft versions, Java target, Folia support, proxy topology, and optional dependencies.

## Core rules

- `JavaPlugin`/bootstrap is composition root, not a service locator.
- Register listeners/commands/services once with explicit owners; close executors/resources on disable.
- Do not block server/tick/region/entity threads with DB, file, HTTP, or long compute.
- Capture immutable data on the legal game thread, perform I/O async, then return to the correct game owner before mutation.
- Avoid static global plugin state when constructor injection is practical.
- Configuration has defaults, validation, migration/reload semantics, and user-facing error messages.
- Permissions/commands are complete contracts: descriptor/registration, aliases, sender constraints, tab completion, and messages.
- Prefer public APIs. NMS/CraftBukkit is an isolated compatibility adapter only when public APIs cannot satisfy the requirement.

For 1.8-to-current support, activate `supporting-minecraft-versions`. For Folia, activate `scheduling-minecraft-folia`.

## Execution

For repository-changing work, read [references/repository-execution.md](references/repository-execution.md) before editing. For explanation-only work, keep to this skill and exact-version official sources.
