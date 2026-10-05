# JPA, SQL, and migration checks

## JPA/Hibernate
- entity equality must respect lifecycle/proxy semantics
- avoid Lombok-generated equality/toString across lazy associations
- inspect fetch plans and SQL
- flush behavior can expose constraint errors before commit
- bulk update/delete bypasses normal persistence-context entity synchronization; clear/refresh as required

## Transactions
- know proxy/interceptor boundary of `@Transactional`
- self-invocation may bypass proxy-based interception depending on framework mode
- checked/unchecked rollback rules are framework configuration, not Java language guarantees
- isolation level must match invariant

## Migrations
- never edit an already-applied production migration unless tooling/process explicitly permits checksum repair
- make indexes/constraints part of the migration contract
- large backfills may need bounded online jobs rather than one migration transaction
- test migrations from a representative previous schema, not only empty database creation
