---
name: building-spring-data-messaging
description: Spring persistence and messaging: Data/JPA, transactions, Kafka/JMS/AMQP, outbox, idempotency, Batch and caching. Use for repositories, consumers, producers or batch.
---

# Building Spring Data and Messaging

Keep database commit semantics and broker delivery semantics explicit; “exactly once” is never assumed from framework annotations.

## Data

- Let repository abstractions simplify common access, but use explicit queries where behavior/performance matters.
- Design indexes and transaction boundaries with queries.
- Cache is not source of truth unless the architecture explicitly makes it one.

## Messaging

- Consumers must tolerate redelivery. Make side effects idempotent or deduplicate with durable state when required.
- A DB transaction and broker publish are separate resources unless a proven transaction mechanism coordinates them; transactional outbox is a common robust default.
- Acknowledge/commit offsets only according to the desired processing guarantee.
- Dead-letter policy includes reason, retry count/backoff, observability, and operator recovery.
- Schema/event evolution is versioned and backward/forward compatibility is considered before deployment.

## Batch

Chunk size, restartability, checkpoint state, item idempotency, and transaction boundaries are first-class. Do not process unbounded datasets into memory.

## Execution

For repository-changing work, read [references/repository-execution.md](references/repository-execution.md) before editing. For explanation-only work, keep to this skill and exact-version official sources.
