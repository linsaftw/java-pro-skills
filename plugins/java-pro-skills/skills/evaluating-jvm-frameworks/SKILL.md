---
name: evaluating-jvm-frameworks
description: Compare JVM frameworks/runtimes such as Spring, Quarkus, Micronaut, Jakarta EE and GraalVM. Use for framework selection, native-image or deployment tradeoffs.
---

# Evaluating JVM Frameworks

Choose from workload, team, ecosystem, operational constraints, and deployment model—not benchmark headlines.

## Snapshot

- Quarkus current recommended production LTS in the 2026-10 snapshot: 3.40 LTS.
- Micronaut Framework 5.2.0 was released 2026-09-27.
- Jakarta EE 11 requires Java 17+ and standardizes records, virtual-thread-aware support, and Jakarta Data 1.0.
- Spring Boot remains the largest general-purpose ecosystem option and is covered by dedicated skills.

## Decision axes

- library/integration ecosystem and team knowledge
- DI/configuration programming model
- startup and memory requirements
- native-image importance vs JVM steady-state
- standards portability (Jakarta EE) vs framework-specific productivity
- build-time code generation/annotation processing constraints
- reactive/event-loop vs blocking/virtual-thread architecture
- observability/testing/dev-mode tooling
- support/LTS cadence

Native image changes reflection/resources/dynamic proxy/JNI assumptions. Do not promise native compatibility without a real native build/test.

## Execution

For repository-changing work, read [references/repository-execution.md](references/repository-execution.md) before editing. For explanation-only work, keep to this skill and exact-version official sources.
