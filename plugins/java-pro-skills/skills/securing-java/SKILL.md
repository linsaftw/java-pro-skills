---
name: securing-java
description: Java security: validation, auth boundaries, crypto, secrets, deserialization, injection, SSRF, TLS and dependency risk. Use for security review or untrusted-input boundaries.
---

# Securing Java

Security decisions follow data from untrusted input to privileged effect.

## Rules

- Validate at trust boundaries; authorize the resource/action server-side after identity is established.
- Parameterize SQL. Never concatenate untrusted input into SQL, shell commands, LDAP, templates, or file paths.
- Canonicalize/contain filesystem access under an allowed root; defend against traversal and symlink surprises when relevant.
- For outbound URLs, enforce scheme/host/address policy and re-check redirects to mitigate SSRF.
- Avoid native Java serialization for untrusted data. Prefer explicit schemas/codecs with limits.
- Use modern password hashing/KDF libraries and platform guidance; never invent crypto.
- Store secrets outside source and logs; redact tokens/passwords/keys and sensitive headers.
- TLS verification stays enabled; trust-all managers are test-only and never production defaults.
- Bound request/body/decompression/collection sizes before expensive processing.
- Dependency upgrades for CVEs are scoped changes with compatibility verification, not blind latest bumps.

Read [references/security-review.md](references/security-review.md).

## Execution

For repository-changing work, read [references/repository-execution.md](references/repository-execution.md) before editing. For explanation-only work, keep to this skill and exact-version official sources.
