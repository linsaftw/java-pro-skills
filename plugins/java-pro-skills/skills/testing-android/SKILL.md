---
name: testing-android
description: Android tests: JVM, Robolectric, instrumentation, Compose UI, coroutine testing, fakes, accessibility and Macrobenchmark. Use for Android test design or flaky/performance tests.
---

# Testing Android

Use the cheapest environment that implements the behavior being asserted.

- pure ViewModel/domain/mappers -> JVM unit tests
- Android framework behavior that Robolectric faithfully models -> Robolectric
- real device/emulator API behavior -> instrumentation
- Compose UI semantics/interactions -> Compose test APIs
- database migrations -> migration tests using real schema files/databases
- startup/jank -> Macrobenchmark/Baseline Profile tooling, not unit-test timers

Use coroutine test schedulers (`runTest`) rather than real delays. Inject clocks/dispatchers at boundaries where determinism matters. UI tests interact through stable semantics/test tags only when user-visible semantics are insufficient.

## Execution

For repository-changing work, read [references/repository-execution.md](references/repository-execution.md) before editing. For explanation-only work, keep to this skill and exact-version official sources.
