---
name: developing-kotlin-jvm
description: Kotlin/JVM and Java interop: nullability, data/value/sealed types, coroutines, collections, Gradle and mixed modules. Use for Kotlin JVM or Java-Kotlin code.
---

# Developing Kotlin/JVM

Kotlin convenience must preserve Java/JVM contracts when code crosses languages or frameworks.

## Rules

- Nullability annotations/platform types at Java boundaries need explicit treatment; do not blindly trust platform types.
- Data classes are value-oriented; do not use them casually as mutable JPA entities.
- Coroutines are not Java threads; blocking calls still block the underlying dispatcher thread.
- Use structured concurrency and owner scopes; avoid `GlobalScope`.
- Public Java-facing APIs should consider generated signatures, default arguments, companion/static exposure, checked exceptions, wildcards, and SAM interoperability.
- Keep Kotlin/Java target/toolchain aligned with framework/Android build requirements.
- Prefer immutable collections/interfaces at boundaries; understand Kotlin read-only vs truly immutable distinction.

## Execution

For repository-changing work, read [references/repository-execution.md](references/repository-execution.md) before editing. For explanation-only work, keep to this skill and exact-version official sources.
