# Comparative reference audit

Purpose: retain the useful lessons from the supplied skill repositories without shipping their text or bloating runtime skill context. Source repositories are inspiration/evidence; `java-pro-skills` guidance is independently written.

## Compact disposition matrix

| Reference source | Strong material retained | Weaknesses rejected / corrected |
|---|---|---|
| `claude-code-java` | Java review, migration, concurrency, persistence, security, performance and architecture task decomposition | Long monolithic bodies, repeated generic doctrine, limited Minecraft/Android depth |
| `claude-skills` | Broad ecosystem taxonomy and useful adjacent JVM/cloud/testing ideas | Persona-first skills, cross-language noise, shallow Java specificity |
| `java-skills` | Architecture/process boundaries, Java-focused organization | Small coverage surface; insufficient Spring/Minecraft/Android/version depth |
| `spring-boot-skills` | Deep Spring Boot 3/4 topic coverage and version-specific migration knowledge | Whole-topic duplication by Spring generation; replaced with target-version routing inside one skill family |
| `spring-testing-skills` | Strong test-slice, integration, security, persistence and container testing ideas | Spring-only scope; generalized where appropriate and kept specialized where behavior differs |
| `spring-ai-agent-utils` | Agent/RAG/MCP implementation patterns and utility concerns | Utility-library structure rather than a skill taxonomy; exact APIs remain target-version verified |
| `ag-opencode-skills` | Clear `When to use` / `When NOT to use` idea, category/index validation, related-skill thinking, large routing taxonomy | Persona padding, forced model choice, “use proactively” routing, broad stale claims such as Java 21+/Spring Boot 3.x as universal defaults, monolithic Java/Minecraft scope |

## Concepts retained across the collection

### Java/JVM

- target/source/runtime distinction and feature-version lookup;
- architecture/review/testing/concurrency/performance/security/persistence as separate activation intents;
- modernization as a version-aware migration task, not “use latest Java”;
- Maven/Gradle/toolchain/dependency ownership as a build skill;
- observability/debugging/container/distributed-system concerns as production skills.

### Spring

- Boot/Framework baseline discovery before API choices;
- MVC vs WebFlux and blocking/reactive boundary separation;
- Security as its own skill;
- focused testing layers rather than unconditional full-context tests;
- data/messaging and Spring AI as distinct task families;
- no duplicated Boot 3/Boot 4 skill trees.

### Minecraft

- Bukkit/Spigot/Paper/Folia plugin engineering as a first-class Java domain;
- legacy-to-current compatibility through capability isolation and classloading-safe adapters;
- Folia ownership-specific scheduling;
- PacketEvents/network-thread rules separated from Bukkit gameplay ownership;
- Adventure/MiniMessage/text compatibility;
- proxy/auth/trust boundaries;
- plugin testing and runtime version matrices.

The multi-version plugin rules are intentionally stronger than generic community-skill advice: capability detection is preferred over scattered presentation-version checks, and modern-only types must not leak into always-loaded legacy-safe classes. The Folia rules classify work by entity, region, global or async ownership rather than treating Folia as “another async scheduler.”

### Android / Kotlin / build

- Android is its own versioned platform skill rather than generic Java mobile advice;
- Kotlin/JVM interop and language choices remain separate from Java core;
- Maven and Gradle are both supported; project wrapper/build source wins rather than repository preference.

## Lessons from the `ag-opencode-skills` inspirational source

Useful ideas adopted or reinforced:

1. **Explicit skill schema validation.** Keep machine-checkable name/description constraints and routing corpora.
2. **Positive and negative routing intent.** A skill should be selected for a concrete task, not because it declares itself “proactive.”
3. **Related-domain boundaries.** Java, Spring, performance, concurrency, persistence and Minecraft should not collapse into one `java-pro` monolith.
4. **Examples are valuable only when they test routing or a hard API contract.** Generic persona examples are not worth permanent context.
5. **Index/catalog generation should derive from live metadata.** Avoid hand-maintained duplicate inventories.

Rejected patterns:

- setting `model: opus` inside knowledge skills;
- broad “master/expert” persona preambles;
- assuming Java 21+, Spring Boot 3.x, Paper-modern APIs, or specific build systems for every project;
- recommending reflection/NMS as a default cross-version strategy when a stable API/capability adapter exists;
- unconditional architecture patterns such as repository/service/factory/event-bus layers;
- “always WebSearch” prose inside every domain skill; source/version lookup is conditional on volatility and correctness need.

## Maintenance rule

When a future inspirational repository is supplied, record only:

`source -> useful capability -> gap/defect -> retained concept -> destination skill/reference`

Do not restore per-file inventories unless a specific audit requires them. This keeps maintainers informed without converting the public repository into a mirror of other skill packs.
