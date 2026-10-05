---
name: observing-java-services
description: Java observability: logging, exception policy, metrics, tracing, health/readiness, correlation and audit events. Use for production diagnostics or OpenTelemetry/Micrometer.
---

# Observing Java Services

Observability should answer what failed, for whom, where, how often, and whether the system is healthy without leaking secrets.

## Rules

- Exceptions carry context upward; log at the boundary that owns handling. Do not log and rethrow the same failure repeatedly.
- Structured logs use stable event names/fields; avoid parsing prose as a monitoring API.
- Correlation/request IDs propagate across async/message boundaries deliberately.
- Metrics measure rates, latency distributions, saturation, queue depth, errors, and business-critical outcomes. Avoid unbounded label cardinality.
- Tracing is useful across service/remote boundaries; sampling must match traffic and incident needs.
- Liveness answers “process should be restarted?”; readiness answers “can receive traffic?”. Do not make liveness depend on every downstream service.
- Audit logs are security/business records with stricter integrity/retention semantics than debug logs.

## Execution

For repository-changing work, read [references/repository-execution.md](references/repository-execution.md) before editing. For explanation-only work, keep to this skill and exact-version official sources.
