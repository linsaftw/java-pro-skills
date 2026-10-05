---
name: developing-spring
description: Spring Boot/Framework development across supported generations: DI, configuration, auto-configuration, lifecycle, validation, caching and migration. Use for general Spring work.
---

# Developing Spring

The project BOM/parent decides the Spring API surface. Do not copy Boot 4 examples into Boot 3 or vice versa without checking.

## Defaults

- Constructor injection for required dependencies.
- Typed `@ConfigurationProperties` for nontrivial configuration; validate at startup.
- Keep controllers/adapters thin; business invariants live in application/domain services.
- Prefer framework auto-configuration until a concrete need requires overriding it.
- Avoid `ApplicationContext` service-location from domain code.
- Keep blocking and reactive stacks distinct; do not wrap blocking JDBC in Reactor and call it reactive.
- Use Actuator/Micrometer conventions rather than custom health/metrics endpoints unless necessary.
- Use Spring Modulith when it directly helps enforce/observe modular-monolith boundaries; do not add it merely for architecture branding.

Read [references/spring-version-map.md](references/spring-version-map.md).

## Execution

For repository-changing work, read [references/repository-execution.md](references/repository-execution.md) before editing. For explanation-only work, keep to this skill and exact-version official sources.
