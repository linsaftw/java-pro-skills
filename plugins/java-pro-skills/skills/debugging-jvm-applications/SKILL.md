---
name: debugging-jvm-applications
description: JVM debugging with logs, stack/thread dumps, JFR, heap evidence, dependency/classloading diagnostics and first-bad-state tracing. Use for crashes, hangs, linkage errors or leaks.
---

# Debugging JVM Applications

Trace the first bad state, not the loudest downstream symptom.

## Workflow

1. Preserve exact error, versions, command, environment, and reproduction.
2. Classify: compile, linkage/classloading, startup/config, logic, concurrency, resource, performance, external dependency.
3. Reduce to earliest failing boundary and inspect its inputs/state.
4. Compare expected contract to actual source/runtime dependency.
5. Instrument narrowly when evidence is missing.
6. Fix root cause and lock it with a regression test or diagnostic assertion.

## Linkage quick map

- `ClassNotFoundException`: requested dynamic load not found.
- `NoClassDefFoundError`: class linkage/initialization failed or dependency unavailable at runtime.
- `NoSuchMethodError`/`NoSuchFieldError`: compiled against a different binary API than runtime.
- `UnsupportedClassVersionError`: class file is newer than runtime JVM.
- `IncompatibleClassChangeError`: binary shape changed incompatibly.

Inspect actual runtime classpath/dependency tree before editing source.

## Execution

For repository-changing work, read [references/repository-execution.md](references/repository-execution.md) before editing. For explanation-only work, keep to this skill and exact-version official sources.
