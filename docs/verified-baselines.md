# Verified baselines — 2026-10-05

These are **research snapshot anchors**, not automatic upgrade targets. Project lockfiles/BOMs/toolchains win.

| Domain | Verified fact | Official source |
|---|---|---|
| Java | Java SE 27 release generation is September 2026; class-file major 71. Java 25 remains the LTS line in Oracle support roadmap. | https://openjdk.org/ ; https://www.oracle.com/java/technologies/java-se-support-roadmap.html |
| Spring Boot | Current project page: 4.1.1. | https://spring.io/projects/spring-boot |
| Spring Framework | Current project page: 7.0.8. | https://spring.io/projects/spring-framework |
| Spring AI | Stable 2.0.1; 2.1.0-M1 is milestone/preview. | https://spring.io/projects/spring-ai ; https://docs.spring.io/spring-ai/reference/ |
| Maven | 3.10.0 GA; Maven 4.0.0-rc-7 is not GA. | https://maven.apache.org/docs/history.html |
| Gradle | 9.8.0 released 2026-09-24 and supports Java 27 daemon/toolchains. | https://docs.gradle.org/9.8.0/release-notes.html |
| Android | Android 17 = API 37. | https://developer.android.com/about/versions/17 |
| AGP | AGP 9.4 is current stable (September 2026), supports max API 37, and documents Gradle 9.6.0 / JDK 17 as its compatibility baseline. | https://developer.android.com/build/releases/agp-9-4-0-release-notes |
| JUnit | Stable release notes include JUnit 6.1.2 (2026-07-12). | https://docs.junit.org/6.1.2/release-notes.html |
| Paper | Current project-setup docs show Paper API 26.2 generation and Java 25 toolchain; runtime docs map 26.1+ to Java 25. | https://docs.papermc.io/paper/dev/project-setup/ ; https://docs.papermc.io/paper/getting-started/ |
| Spigot | Spigot Maven docs list 1.21.11-R0.1-SNAPSHOT in the current legacy numeric line. | https://www.spigotmc.org/wiki/spigot-maven/ |
| Fabric | Current developer docs are on 26.2 generation; recent setup docs require JDK 25 for 26.1. | https://docs.fabricmc.net/develop/ |
| Quarkus | 3.40 LTS recommended for production in current release table. | https://quarkus.io/releases/ |
| Micronaut | Framework 5.2.0 released 2026-09-27. | https://micronaut.io/ |
| Jakarta EE | Platform 11, Java 17 minimum. | https://jakarta.ee/specifications/platform/11/ |

Do not update application dependencies just because this table is newer. Compatibility and scope come first.
