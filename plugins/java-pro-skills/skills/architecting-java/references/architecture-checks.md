# Architecture review checks

- What is the business capability?
- Which component owns each mutable state/invariant?
- Are dependency directions acyclic?
- Is framework code leaking into domain logic unnecessarily?
- Are DTOs/API schemas accidentally used as persistence/domain entities?
- Is there one transaction boundary for each consistency requirement?
- Are retries/idempotency placed at an external side-effect boundary?
- Is a new interface actually a policy/provider seam, or merely an interface with one implementation?
- Can the feature be tested without booting unrelated infrastructure?
- Are lifecycle start/stop/reload semantics explicit?
- Are queues, caches, histories, and executor pools bounded and owned?
- Would a modular monolith solve the problem more cheaply than a network boundary?
