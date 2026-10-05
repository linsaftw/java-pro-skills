---
name: persisting-java-data
description: Java persistence: JDBC, JPA/Hibernate, transactions, migrations, pooling, locking, batching and database tests. Use for SQL/JPA/Flyway/Liquibase or persistence bugs.
---

# Persisting Java Data

Database correctness is schema + transaction + query behavior, not entity annotations alone.

## Rules

- Keep domain invariants above persistence details; repositories expose domain-oriented operations, not raw ORM mechanics everywhere.
- Transactions wrap one consistency boundary. Avoid remote network calls while holding a DB transaction unless explicitly designed.
- Never rely on lazy loading outside a known persistence context.
- Avoid N+1 by measuring generated queries and selecting fetch strategy deliberately.
- Use keyset pagination for large ordered feeds when offset cost/consistency becomes material.
- Use optimistic locking for concurrent edits where lost updates matter; pessimistic locks only with understood contention/deadlock behavior.
- Batch writes intentionally and monitor JDBC driver/database limits.
- Schema migrations are forward, deterministic, reviewed, and deploy-safe; destructive changes use expand/migrate/contract when rolling deployment matters.

Read [references/jpa-and-migrations.md](references/jpa-and-migrations.md).

## Execution

For repository-changing work, read [references/repository-execution.md](references/repository-execution.md) before editing. For explanation-only work, keep to this skill and exact-version official sources.
