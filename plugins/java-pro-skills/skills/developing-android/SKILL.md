---
name: developing-android
description: Android development: SDK/AGP compatibility, Kotlin/Java, Compose/Views, lifecycle, coroutines, storage, networking, permissions and performance. Use for Android implementation.
---

# Developing Android

Android is Kotlin-first today, but Java interoperability remains a first-class constraint in mixed codebases.

## Baseline snapshot

Android 17 is API 37 in the 2026 snapshot. AGP 9.4 is the verified stable 2026 baseline for API 37 and documents Gradle 9.6.0 / JDK 17 compatibility. Resolve the project’s exact AGP/Kotlin matrix before using version-specific APIs. The project’s AGP version is authoritative.

## Rules

- UI state has one owner, survives configuration/recomposition appropriately, and separates transient events from durable state.
- Compose functions are side-effect disciplined; use lifecycle/effect APIs rather than launching uncontrolled work during composition.
- Coroutines have structured scope tied to lifecycle/owner. Do not use `GlobalScope` as application architecture.
- Main thread does UI and short work only; database/network/file/CPU-heavy work leaves it.
- Runtime permissions and behavior changes are gated by actual API/targetSdk requirements, not device-version string folklore.
- Background work uses WorkManager or the exact platform mechanism matching timing/guarantee needs; do not rely on unrestricted background execution.
- Store secrets server-side when possible; app binaries are inspectable.

Read [references/android-versioning.md](references/android-versioning.md).

## Execution

For repository-changing work, read [references/repository-execution.md](references/repository-execution.md) before editing. For explanation-only work, keep to this skill and exact-version official sources.
