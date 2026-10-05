---
name: building-java-projects
description: Maven/Gradle builds, toolchains, dependencies, modules, shading, BOMs, CI and packaging. Use for build design, failures, conflicts or Maven-vs-Gradle.
---

# Building Java Projects

Use the existing build tool unless the task is explicitly a migration. Build-tool rewrites rarely pay for a feature fix.

## Maven vs Gradle

- Maven: declarative lifecycle, strong convention, transparent dependency model, ubiquitous enterprise/plugin ecosystem. Prefer when predictability and standardized builds dominate.
- Gradle: programmable model, strong incremental/build-cache capabilities, Kotlin DSL, excellent Android and modern Minecraft ecosystem adoption. Prefer when build logic/variants/custom orchestration justify it.
- Neither is intrinsically “faster” or “better”; wrapper/version, configuration, cacheability, plugins, and project shape decide.

## Rules

- Commit Maven Wrapper or Gradle Wrapper for reproducible tooling.
- Pin plugin/core dependency versions via parent/BOM/version catalog where appropriate; avoid dynamic versions in release builds.
- Use Java toolchains to decouple build runtime from target compiler where supported.
- Dependency scope matters: API vs implementation, provided/compileOnly, runtime, test.
- Shade/relocate only libraries actually bundled and only when public/runtime type identity will not cross the relocation boundary.
- Do not minimize shaded artifacts when reflection/service loading/resource discovery has not been proven.

Read [references/maven-gradle-matrix.md](references/maven-gradle-matrix.md).

## Execution

For repository-changing work, read [references/repository-execution.md](references/repository-execution.md) before editing. For explanation-only work, keep to this skill and exact-version official sources.
