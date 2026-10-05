---
name: engineering-java-concurrency
description: Java concurrency: executors, CompletableFuture, virtual threads, structured-concurrency availability, synchronization, atomics, cancellation and lifecycle. Use for async/thread-safety work.
---

# Engineering Java Concurrency

Concurrency design begins with ownership and blocking semantics, not with choosing an executor.

## Rules

- Prefer high-level executors/futures/tasks over raw `new Thread()` in application code.
- Every executor has an owner and shutdown path.
- Never block an event-loop/tick/region thread with `join`, `get`, `sleep`, busy-wait, JDBC, file I/O, or HTTP.
- `CompletableFuture` completion stage executors are explicit when thread affinity matters.
- Preserve cancellation/interruption semantics.
- Concurrent collections make individual operations safe; compound check-then-act still needs atomic APIs/locks.
- `volatile` gives visibility/order, not compound atomicity.
- Avoid holding locks across I/O, callbacks, or unknown code.

## Virtual threads

Use virtual threads for large numbers of mostly blocking, thread-per-request style tasks on Java 21+. They do not make CPU work faster and do not remove downstream pool limits. Audit pinning/lock contention and keep database/HTTP connection pools bounded.

Structured concurrency and scoped values have changed status across releases; verify target Java before using them.

Read [references/concurrency-review.md](references/concurrency-review.md).

## Execution

For repository-changing work, read [references/repository-execution.md](references/repository-execution.md) before editing. For explanation-only work, keep to this skill and exact-version official sources.
