# Agent research playbook

Use this when a skill lacks an exact API/version fact.

1. Read the repository build/lock/BOM first. Extract exact Java/framework/plugin versions and the wrapper command.
2. Search repository source for the existing abstraction/owner before adding anything.
3. Read target-version official docs/Javadocs/source. Prefer a versioned page over a generic “current” page.
4. If official docs are incomplete, inspect dependency source/artifact metadata.
5. Community references are for undocumented behavior and operational experience; corroborate before coding.
6. Record unstable facts with date/version in the patch or docs; do not encode “latest” as a timeless rule.
7. For Minecraft, separate server version, client protocol version, Java runtime, API artifact, proxy translation, and dependency version.
8. For Android, resolve AGP/Gradle/JDK/Kotlin/compileSdk/targetSdk as a compatibility matrix.
9. For Spring, resolve Boot BOM -> Framework/Security/Data/third-party versions before choosing APIs.
10. For Java preview features, verify JEP status and compile/runtime `--enable-preview` requirement for the exact release.
