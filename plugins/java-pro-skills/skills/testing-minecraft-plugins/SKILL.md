---
name: testing-minecraft-plugins
description: Minecraft plugin tests: pure Java, collaborator mocks, server harnesses, version matrices, packet fixtures and Folia ownership. Use to prove Bukkit/Paper/Folia behavior.
---

# Testing Minecraft Plugins

Test domain logic without a server; test platform contracts on a real or faithful platform boundary.

## Layers

- pure math/domain/config parsing -> ordinary JUnit
- listener/service with platform collaborator -> mock collaborator, not the domain under test
- Bukkit API behavior -> test harness when the harness implements the API involved
- NMS/version/classloading/Folia/PacketEvents lifecycle -> real server/integration matrix when correctness depends on runtime implementation

## Multiversion proof

Compile success against one API does not prove 1.8/current compatibility. At minimum, smoke-load the final JAR on minimum and maximum supported runtime families and execute the touched capability.

## Folia proof

Tests should assert scheduling intent/owner routing in pure bridge tests, then use runtime smoke evidence for real ownership behavior. Never “test” thread safety by sleeping.

## Packet proof

Use captured/constructed packet fixtures and deterministic timeline/state tests. Do not require live network for every codec/state transition, but include an integration smoke path for injection/lifecycle.

## Execution

For repository-changing work, read [references/repository-execution.md](references/repository-execution.md) before editing. For explanation-only work, keep to this skill and exact-version official sources.
