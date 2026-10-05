---
name: reviewing-java
description: Review Java for correctness, API contracts, maintainability, concurrency, ownership, compatibility, security and regressions. Use for PR/code/generated-patch audits.
---

# Reviewing Java

Review in causal order: correctness -> contracts -> concurrency/lifecycle -> compatibility -> security -> performance -> readability.

## Review method

1. Read the diff plus direct callers and tests; do not review an isolated method when its contract is elsewhere.
2. Identify behavior changed, public/internal API changed, state ownership changed, and failure paths.
3. Check null/empty/error semantics and resource closure.
4. Trace concurrency publication, atomicity, cancellation, shutdown, and boundedness when shared state/executors/futures are touched.
5. Check Java target and dependency API availability.
6. Look for security boundary changes: validation, authz, path/network/deserialization/SQL/command injection, secret exposure.
7. Demand tests that fail on the old behavior and pass on the new behavior for bug fixes.

## Reject common generated-code defects

- invented library methods or annotations
- catch-and-ignore or log-and-rethrow duplicates
- fake async (`completedFuture` around unfinished work)
- unbounded caches/queues/retries
- `Thread.sleep` tests
- mocks of the class under test or persistence layer in integration tests
- broad refactor mixed into a targeted fix
- returning `null` from a newly designed optional/collection API

## Execution

For repository-changing work, read [references/repository-execution.md](references/repository-execution.md) before editing. For explanation-only work, keep to this skill and exact-version official sources.
