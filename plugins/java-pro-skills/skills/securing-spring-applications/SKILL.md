---
name: securing-spring-applications
description: Spring Security: filter chains, OAuth2/OIDC, JWT, CSRF/CORS, sessions, method authorization and tests. Use for Spring authentication or authorization.
---

# Securing Spring Applications

Authorization is a business boundary, not only a URL matcher.

## Rules

- Use the project’s Spring Security major-version APIs; verify DSL changes against exact docs.
- Authenticate once from a trusted mechanism, then authorize the specific action/resource server-side.
- Prefer explicit `SecurityFilterChain` configuration over legacy patterns no longer supported by the target version.
- JWT signature validation is not enough: validate issuer/audience/time and map authorities deliberately.
- Browser session/cookie applications need CSRF protection unless the architecture genuinely removes ambient credentials.
- CORS is a browser policy, not authentication.
- Method security complements endpoint rules for domain-sensitive operations.
- Passwords use adaptive password encoders; never reversible encryption or raw hashes.
- Test both allowed and denied paths, including missing/invalid identity and cross-resource access.

## Execution

For repository-changing work, read [references/repository-execution.md](references/repository-execution.md) before editing. For explanation-only work, keep to this skill and exact-version official sources.
