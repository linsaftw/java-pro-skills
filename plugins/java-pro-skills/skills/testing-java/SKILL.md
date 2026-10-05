---
name: testing-java
description: Java testing with JUnit, assertions, Mockito, parameter/property tests, integration/Testcontainers and deterministic concurrency. Use for JVM test design or regression coverage.
---

# Testing Java

Tests prove externally relevant behavior at the cheapest realistic boundary.

## Defaults

- JUnit Jupiter unless the repository already uses another engine.
- One behavior per test; assertions may be grouped only when they prove one outcome.
- Mock collaborators, not value objects or the unit itself.
- Prefer fakes/real lightweight implementations over deep mocks.
- Do not use `Thread.sleep` for synchronization. Use latches/barriers/futures/virtual time or await a real condition with a deadline.
- Parameterize boundary/value tables instead of copy-pasting tests.
- For persistence, serialization, SQL dialect, networking, or container behavior, use integration tests against the real technology when the difference matters.
- A bug fix gets a regression test that reproduces the defect if the behavior is practical to automate.

## Test layers

`pure unit -> component/slice -> integration with real infrastructure -> end-to-end smoke`

Read [references/testing-toolbox.md](references/testing-toolbox.md).

## Execution

For repository-changing work, read [references/repository-execution.md](references/repository-execution.md) before editing. For explanation-only work, keep to this skill and exact-version official sources.
