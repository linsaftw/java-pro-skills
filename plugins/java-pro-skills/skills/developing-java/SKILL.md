---
name: developing-java
description: General Java language/API development with version-aware syntax, libraries, types, exceptions, collections and modern features. Use for Java implementation or feature-version questions.
---

# Developing Java

Use this as the default Java language skill. Keep source/target/runtime distinct.

## Decisions

- Establish `source`, `target`/`release`, runtime JDK, and library baseline from the build before using syntax or APIs.
- Prefer immutable state, final fields where practical, constructor injection, explicit ownership, small cohesive types, and value objects with `equals`, `hashCode`, and `toString` when identity is value-based.
- Use `Optional` for an intentionally optional return value, empty collections for no elements, and exceptions for failed contracts. Do not introduce new APIs that return `null` without a framework contract requiring it.
- Use try-with-resources for owned closeables. Preserve interruption with `Thread.currentThread().interrupt()` when catching `InterruptedException`.
- Avoid speculative abstraction. Extract when there is a real second use, policy boundary, test seam, or version/platform seam.
- Prefer standard library APIs before dependencies.
- Never use a preview feature unless the project explicitly enables preview compilation and runtime and accepts the deployment constraint.

## Version use

Read [references/java-version-matrix.md](references/java-version-matrix.md) whenever syntax/API availability affects correctness. For APIs not listed there, check target-version Javadocs rather than guessing from memory.

## Verification

Compile with the project wrapper/tool and inspect emitted target/release settings. When compatibility matters, test on the minimum supported runtime, not only the developer JDK.

## Execution

For repository-changing work, read [references/repository-execution.md](references/repository-execution.md) before editing. For explanation-only work, keep to this skill and exact-version official sources.
