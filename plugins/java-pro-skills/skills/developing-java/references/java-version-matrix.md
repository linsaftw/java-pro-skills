# Java version matrix (8-27)

This is a routing matrix, not a substitute for target-version Javadocs. Stable language/platform milestones only are treated as safe defaults; preview/incubator features are labeled.

| Java | Selected additions relevant to application code |
|---|---|
| 8 | lambdas, streams, default/static interface methods, `java.time`, `CompletableFuture`, repeatable/type annotations |
| 9 | JPMS modules, JShell, collection factory methods, `Flow`, private interface methods |
| 10 | local variable type inference (`var`) |
| 11 LTS | standardized HTTP Client, single-file source launch, `var` in lambda parameters, useful `String`/`Files` APIs |
| 12-13 | mostly incremental platform work; switch expressions/text blocks were preview during this era |
| 14 | switch expressions final; records and pattern matching for `instanceof` preview; helpful NPEs |
| 15 | text blocks final; hidden classes; records/sealed types still preview |
| 16 | records final; pattern matching for `instanceof` final; `jpackage` final |
| 17 LTS | sealed classes final; stronger encapsulation; enhanced PRNG APIs |
| 18 | UTF-8 default charset; simple web server; Javadoc code snippets |
| 19-20 | virtual threads, record patterns, structured concurrency, scoped values progressed as previews/incubators |
| 21 LTS | virtual threads final; record patterns final; pattern matching for `switch` final; sequenced collections; preview features still require opt-in |
| 22 | Foreign Function & Memory API final; unnamed variables/patterns final; multi-file source launch; several APIs remained preview |
| 23 | Markdown documentation comments; generational ZGC default; module imports/primitive patterns/structured concurrency/scoped values remained preview |
| 24 | Class-File API and Stream Gatherers finalized; recent language/concurrency work continued through preview cycles |
| 25 LTS | module import declarations finalized; Key Derivation Function API finalized; other features must be checked against JDK 25 JEP status before use |
| 26 | March 2026 feature release. Treat new language/VM features such as value-class work as target-version-specific and verify preview/final status before use. |
| 27 | September 2026 release generation; class-file major version 71. Verify each new feature against JDK 27 release/JEP status before production use. |

## Compatibility rules

- `--release N` is the preferred compiler contract when supported: it limits both language level and linked standard-library API surface.
- Runtime JDK >= compilation target does not make dependencies compatible with older targets.
- Multi-release JARs are an advanced packaging tool, not the default answer to cross-JDK support.
- Annotation processors, bytecode tooling, Gradle/Maven runtime JDK, test runtime, and application target may each have different JDK constraints.
- Preview class files require `--enable-preview` at both compile and runtime and are tied to a specific Java release.

## Official anchors

- https://openjdk.org/projects/jdk/
- https://openjdk.org/jeps/0
- https://docs.oracle.com/en/java/javase/
- https://www.oracle.com/java/technologies/java-se-support-roadmap.html
