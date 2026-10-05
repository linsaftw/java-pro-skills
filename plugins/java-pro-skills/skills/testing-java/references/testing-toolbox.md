# Testing toolbox

## JUnit
Current 2026 line is JUnit 6.x; many existing projects remain on JUnit 5. Let the project BOM/build decide. Do not upgrade test major versions incidentally.

Use:
- `@ParameterizedTest` for input matrices
- `@TempDir` for filesystem isolation
- timeouts only as safety bounds, not correctness synchronization
- assumptions only for genuine environment capability

## Mockito
- prefer constructor-injected collaborators
- stub only behavior used by the test
- verify externally relevant collaboration, not every internal call
- avoid lenient global stubbing that hides dead test setup

## Testcontainers
Use when database/broker/protocol behavior is part of the contract. Pin compatible images and wait for readiness semantically, not with sleeps.

## Concurrency
Use `CountDownLatch`, `CyclicBarrier`, executors, futures, or deterministic scheduler/test hooks. Always fail with a bounded timeout to avoid hanging CI.

## Property testing
Useful for parsers, codecs, mathematical invariants, value objects, and round-trip serialization. Keep generated domains constrained to valid/interesting states.
