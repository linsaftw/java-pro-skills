---
name: tuning-java-performance
description: JVM performance with JFR/JMC, CPU/allocation/GC/heap evidence, I/O, algorithms and benchmarking. Use for latency, throughput, memory, startup or CPU regressions.
---

# Tuning Java Performance

Measure before tuning. Fix algorithmic and allocation problems before JVM-flag folklore.

## Workflow

1. Define metric and workload: p50/p95/p99 latency, throughput, allocation rate, CPU, live set, pause time, startup, or footprint.
2. Reproduce with representative load and capture JFR/metrics/GC logs.
3. Find the dominant cost by evidence.
4. Fix highest-level cause first: algorithm/query/I/O/contention/allocation.
5. Re-measure with the same workload.

## Rules

- Rising live set after full/concurrent-cycle collection suggests retention, not “GC needs more RAM”.
- High allocation rate can create GC pressure even with a stable live set.
- Cache only when hit rate/value justify retained memory; bound and expire it.
- Avoid per-item object churn in known hot loops only after profiling proves it matters.
- JMH for microbenchmarks; never benchmark with ad-hoc wall-clock loops without warmup/fork discipline.
- Container memory/CPU limits change JVM ergonomics; inspect actual runtime flags and limits.

Read [references/performance-toolbox.md](references/performance-toolbox.md).

## Execution

For repository-changing work, read [references/repository-execution.md](references/repository-execution.md) before editing. For explanation-only work, keep to this skill and exact-version official sources.
