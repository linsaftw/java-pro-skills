# Folia ownership examples

| Work | Folia owner |
|---|---|
| set player inventory/health/velocity | entity |
| teleport/correct player | entity + teleport API semantics |
| set block/state at location | region |
| spawn world entity at location | region for location preparation; then entity ownership for entity mutation |
| iterate global trigger then mutate every player | global trigger may enumerate; schedule each mutation on entity owner |
| SQL/HTTP/file | async, using immutable captured data |
| console/global server task | global region |

Two-phase I/O pattern:
1. owner thread reads the minimum live state
2. build immutable DTO
3. async I/O
4. owner scheduler applies result if entity/world/session is still valid

Never block an owner thread waiting for the async phase.
