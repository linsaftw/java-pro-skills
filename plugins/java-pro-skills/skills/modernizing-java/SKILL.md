---
name: modernizing-java
description: Java/JDK migration with bytecode/API compatibility, dependency support, modules, removed APIs and tests. Use for JDK upgrades, javax-to-jakarta or legacy modernization.
---

# Modernizing Java

Migrations are compatibility projects, not syntax cleanup.

## Sequence

1. Record current build JDK, `source`/`target`/`release`, runtime JDK, framework versions, container/server runtime, CI matrix, and production launch flags.
2. Establish the desired **runtime** and desired **bytecode/API target** separately.
3. Run dependency/plugin compatibility checks before source edits. Build plugins and annotation processors often block upgrades before application code does.
4. Fix illegal reflective access, removed JDK modules/APIs, charset assumptions, TLS/crypto defaults, serialization assumptions, and GC/flag changes based on actual errors and release notes.
5. Upgrade framework major versions as separate bounded steps when possible.
6. Only after behavior passes, adopt new language features deliberately.

## High-risk transitions

- 8 -> 11: Java EE/CORBA modules removed from JDK; stronger library/tooling changes.
- 11 -> 17: strong encapsulation and framework generation changes.
- 17 -> 21: virtual threads become available but do not make synchronized/blocking resource bottlenecks disappear.
- Spring/Jakarta transitions: package namespace and framework contracts must be migrated together; do not blind-replace `javax.*` because Java SE packages such as `javax.crypto` remain valid.

Read [references/migration-checklist.md](references/migration-checklist.md) for gates.

## Execution

For repository-changing work, read [references/repository-execution.md](references/repository-execution.md) before editing. For explanation-only work, keep to this skill and exact-version official sources.
