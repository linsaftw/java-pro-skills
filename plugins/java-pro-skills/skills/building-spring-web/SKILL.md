---
name: building-spring-web
description: Spring MVC/WebFlux APIs: validation, DTOs, Problem Details, pagination, versioning, clients, resilience and streaming. Use for controllers, HTTP clients or reactive web.
---

# Building Spring Web

Choose servlet MVC or reactive WebFlux from workload and existing stack; mixing models casually creates harder systems.

## HTTP API rules

- DTOs at the transport boundary; do not expose persistence entities as API contracts.
- Bean validation handles structural input constraints; domain service enforces business invariants.
- Use precise HTTP semantics, status codes, content types, cache/idempotency headers where relevant.
- Use RFC Problem Details support for machine-readable errors when available in the project line; keep stable application error codes separate from human text.
- Bound pagination, body size, upload size, decompression, and streaming buffers.
- Timeouts are explicit on outbound clients. Retries only for safe/idempotent operations or with an idempotency design.

## MVC vs WebFlux

MVC works well for conventional blocking stacks and virtual-thread deployments. WebFlux is appropriate for end-to-end nonblocking pipelines and streaming/high-concurrency cases. Never call blocking JPA/JDBC/file APIs on Reactor event-loop threads.

## Execution

For repository-changing work, read [references/repository-execution.md](references/repository-execution.md) before editing. For explanation-only work, keep to this skill and exact-version official sources.
