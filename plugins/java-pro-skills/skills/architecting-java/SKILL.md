---
name: architecting-java
description: Java architecture: modules, dependency direction, DDD, ports/adapters, SOLID, lifecycle and state ownership. Use for structural design or refactors.
---

# Architecting Java

Architecture exists to protect domain rules and change boundaries, not to maximize interfaces.

## Default decision rules

- Start with a modular monolith unless independent deployment/scaling/ownership is proven.
- Organize by domain capability before technical layer at repository scale; keep infrastructure dependencies pointing inward through narrow ports only where a real replaceable boundary exists.
- One mutable state concept has one authoritative owner.
- Constructor injection for required collaborators. Avoid service locators and global mutable singletons.
- Domain models should not depend on HTTP, Spring MVC, Bukkit, SQL clients, or message-broker classes unless the domain is explicitly that platform integration.
- Transactions belong around business invariants, not arbitrary repository methods.
- Events are useful when they decouple post-commit effects; they are not a substitute for direct calls inside one consistency boundary.

## Choosing structure

- Small CRUD: simple controller/service/repository layering can be enough.
- Complex domain rules: domain module + application service + ports/adapters.
- Independent subdomains: modular boundaries with contract tests.
- Microservices: only with demonstrated independent deployment/ownership/scaling need and operational capacity.

Read [references/architecture-checks.md](references/architecture-checks.md) for review questions.

## Execution

For repository-changing work, read [references/repository-execution.md](references/repository-execution.md) before editing. For explanation-only work, keep to this skill and exact-version official sources.
