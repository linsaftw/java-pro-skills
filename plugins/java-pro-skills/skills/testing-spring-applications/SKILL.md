---
name: testing-spring-applications
description: Spring tests: unit, slices, MockMvc/WebTestClient, Security, JPA, Testcontainers, WebSocket/STOMP and full-context tests. Use for Spring test design or migration.
---

# Testing Spring Applications

Load the smallest Spring context that proves the behavior.

## Routing

- pure service/domain logic -> no Spring context
- MVC controller -> MVC test slice / framework-supported MVC test client for the project version
- WebFlux controller/reactive flow -> WebTestClient + StepVerifier where signals matter
- repository/JPA -> `@DataJpaTest` + real database when dialect behavior matters
- security -> Spring Security test support with explicit auth/CSRF/JWT/OIDC cases
- WebSocket/STOMP -> real server port when transport behavior is under test
- wiring/configuration -> targeted context runner or `@SpringBootTest`

## JPA trap

When verifying a query/persistence effect, flush and clear the persistence context so the assertion cannot pass from first-level cache state. Do not use the repository under test as the only fixture creator when that could mask the same bug.

## Version rule

Spring Boot 3 and 4 testing APIs differ in places. Inspect the exact target docs/imports instead of assuming the newest example compiles.

## Execution

For repository-changing work, read [references/repository-execution.md](references/repository-execution.md) before editing. For explanation-only work, keep to this skill and exact-version official sources.
