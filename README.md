# Java Pro Skills

**`java-pro-skills`** is a curated, source-first Claude Code Agent Skills collection for professional Java/JVM development.

Repository: https://github.com/linsaftw/java-meta-skills  
Release: **0.0.3**

It covers Java, Spring, Bukkit/Spigot/Paper/Folia, PacketEvents, Minecraft proxies/mods, Android, Kotlin/JVM, Maven/Gradle, testing, security, persistence, performance, distributed systems and production operations.

## Why this exists

Public Java skill packs tend to be either broad but shallow, deep but monolithic, duplicated by framework version, or weak on Minecraft/Android/JVM-runtime engineering. `java-pro-skills` uses progressive disclosure: concise routing metadata, small task-specific `SKILL.md` bodies, and direct reference files only when deeper version/domain detail is needed.

Current Claude Code documentation states that skill names/descriptions are present for routing while full skill content is loaded on demand. Version 0.0.3 keeps the 0.0.2 routing/body compression, then restores execution details that the first optimization pass compressed too aggressively through an on-demand repository-execution reference.

## Coverage

| Area | Coverage |
|---|---|
| Java core | language/versioning, modernization, architecture, review, testing, concurrency, performance, security, persistence, builds, observability, debugging, publishing, containers, distributed systems |
| Spring | Boot/Framework, MVC/WebFlux, Security, testing, data/messaging, Spring AI/MCP/RAG |
| Minecraft | Bukkit/Spigot/Paper, legacy-to-current multiversion, Folia, PacketEvents/protocol, Adventure/MiniMessage, Velocity/Bungee-style proxies, testing, Fabric mods |
| Android/JVM | Android, Android testing, Kotlin/JVM, Quarkus/Micronaut/Jakarta/GraalVM evaluation |

Skill count: **33**.

## Install with Claude Code

Add the repository as a marketplace:

```text
/plugin marketplace add linsaftw/java-meta-skills
/plugin install java-pro-skills@java-pro-skills
```

The GitHub repository has not yet been renamed; the public plugin/marketplace identity in this release is `java-pro-skills`.

For repository-local installation, copy the canonical plugin skills into `.claude/skills/`:

```bash
./scripts/install.sh --project /path/to/project
```

For user-level installation:

```bash
./scripts/install.sh --user
```

## Token-efficiency contract

0.0.3 preserves the two-budget optimization and adds a cut-regression rule:

- **Always-loaded routing metadata:** descriptions are short, trigger-oriented and non-overlapping.
- **On-demand skill bodies:** universal source/version/verification doctrine is compressed; domain rules remain local.
- **Deep detail:** version matrices/checklists live in direct `references/` files instead of every skill body.
- **Recovered execution context:** repository-changing tasks load a compact execution reference; explanation-only invocations do not pay that cost.
- **No framework-version duplicate trees:** Spring 3/4 behavior is selected from the inspected project version.
- **No giant volatile API catalogs:** exact APIs are verified against the project target and official source.

See [`docs/token-efficiency-audit-0.0.2.md`](docs/token-efficiency-audit-0.0.2.md) and [`docs/cut-review-0.0.3.md`](docs/cut-review-0.0.3.md).

## Discovery keywords

Java Claude skills, Java agent skills, Spring Claude skills, Spring Boot skills, Bukkit Claude skills, Spigot Claude skills, Paper Claude skills, Folia development, Minecraft Claude skills, Minecraft development skills, PacketEvents skills, Android Claude skills, Kotlin JVM skills, Maven skills, Gradle skills.

These terms are repository-discovery text. Individual skill names remain concise domain/action names.

## Source policy

Use evidence in this order:

1. Current project source, build files, lock/BOM/toolchain and dirty state.
2. Runtime logs, tests, configuration and reproduction evidence.
3. Exact official target-version documentation/Javadocs/source.
4. Mature reference implementations for architecture/failure modes where licensing permits.
5. Skill guidance.
6. Model memory only as a search hint.

Research snapshot: [`docs/verified-baselines.md`](docs/verified-baselines.md).  
Reference audit: [`docs/reference-repository-audit.md`](docs/reference-repository-audit.md).

## Validate

```bash
python3 scripts/validate_repo.py
python3 scripts/measure_context.py
python3 scripts/list_skills.py
```

## Versioning

`0.0.1 -> 0.0.2 -> ... -> 0.0.9 -> 0.1.0 -> 0.1.1 ...`

Use `python3 scripts/bump_version.py` for the next release.

## Privacy

The public repository must contain no credentials, private project identifiers, uploaded-file IDs, local machine paths, internal hosts, private emails, or proprietary source. Audited repositories are inspiration/reference material only; shipped guidance is independently written and generalized.

## License

MIT. External projects and documentation retain their own licenses.
