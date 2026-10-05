---
name: scheduling-minecraft-folia
description: Folia scheduling by entity, region, global and async ownership with Bukkit/Paper fallback and real teleport futures. Use for Folia support or scheduler/threading bugs.
---

# Scheduling Minecraft Folia

Folia has ownership domains, not one universal main thread.

## Operation -> owner

- player/entity mutation -> entity scheduler
- block/chunk/location/world-region mutation/read requiring ownership -> region scheduler
- truly global server work -> global region scheduler
- DB/file/HTTP/compression/heavy detached compute -> async scheduler/executor
- classic Bukkit/Spigot fallback -> legal synchronous Bukkit context for game mutation

## Hard rules

- Scheduler is chosen by **owned state**, not by “sync vs async” convenience.
- Entity scheduler follows entity movement/teleports; region scheduler does not substitute for entity ownership.
- Packet/network callbacks do not mutate Bukkit world/entity state.
- No raw detached threads. Owned executor pools are only for pure non-Bukkit work and must shut down.
- Preserve real `CompletableFuture<Boolean>` from async teleports; never return an already-completed fake success.
- For broad legacy support, isolate Folia-only classes from old-server classloading and resolve capability once.
- Declaring `folia-supported: true` is necessary but not proof of correctness.

Read [references/folia-ownership.md](references/folia-ownership.md).

## Execution

For repository-changing work, read [references/repository-execution.md](references/repository-execution.md) before editing. For explanation-only work, keep to this skill and exact-version official sources.
