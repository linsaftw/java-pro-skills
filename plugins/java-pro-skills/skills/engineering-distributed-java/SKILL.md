---
name: engineering-distributed-java
description: Distributed Java: idempotency, retries, timeouts, backpressure, messaging, sagas/outbox, consistency and failure isolation. Use for microservices and remote/event-driven systems.
---

# Engineering Distributed Java

Every network call can be slow, fail, duplicate, reorder, or succeed remotely after the local caller times out.

## Rules

- Set connect/request/read/deadline budgets; propagate deadlines where supported.
- Retry only transient failures and only when operation semantics are safe/idempotent. Add bounded attempts, backoff, jitter, and a total deadline.
- Circuit breakers protect dependencies; they do not repair incorrect retry storms.
- Use idempotency keys/durable deduplication for externally retried side effects.
- Transactional outbox bridges DB commit to message publication more safely than “save then publish”.
- Sagas compensate business effects; they are not distributed ACID.
- Version APIs/events compatibly and deploy consumers/producers in a safe order.
- Backpressure/queue capacity is finite; define overload behavior before production.
- Cache invalidation/consistency policy is explicit.

## Execution

For repository-changing work, read [references/repository-execution.md](references/repository-execution.md) before editing. For explanation-only work, keep to this skill and exact-version official sources.
