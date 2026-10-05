---
name: containerizing-java-services
description: Java containers: runtime images, JVM limits, layered builds, non-root execution, health, signals and graceful shutdown. Use for Docker/Kubernetes JVM deployment.
---

# Containerizing Java Services

Container correctness includes JVM ergonomics, signals, filesystem, identity, and orchestration—not only a Dockerfile that starts.

## Rules

- Use a maintained minimal JRE/JDK base appropriate to the app and licensing policy; pin by version/digest according to supply-chain requirements.
- Run as non-root; make only required paths writable.
- Respect memory/CPU limits and inspect JVM container ergonomics before hardcoding heap percentages.
- Graceful shutdown handles SIGTERM within orchestration grace period and stops accepting new work before resource teardown.
- Readiness/liveness semantics remain distinct.
- Layer dependencies/resources/app classes for cache-efficient builds when useful.
- Do not bake credentials into image layers.
- Generate SBOM/provenance/signing according to deployment policy.
- Native image is a separate compatibility/performance decision; benchmark startup/footprint and verify reflection/resource configuration.

## Execution

For repository-changing work, read [references/repository-execution.md](references/repository-execution.md) before editing. For explanation-only work, keep to this skill and exact-version official sources.
