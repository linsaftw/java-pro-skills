# Maven / Gradle matrix

Verified snapshot: 2026-10-05.

| Concern | Maven | Gradle |
|---|---|---|
| Current GA snapshot | Maven 3.10.0; Maven 4 is still RC | Gradle 9.8.0 |
| Build model | lifecycle + POM/plugin configuration | task graph + declarative/programmatic model |
| Wrapper | Maven Wrapper | Gradle Wrapper |
| Java toolchains | supported via compiler/toolchain plugins/ecosystem | first-class Java toolchains |
| Dependency constraints | dependencyManagement/BOM | platforms/version catalogs/constraints |
| Android | not standard | required ecosystem default via AGP |
| Minecraft modern docs | supported but Paper discourages Maven in its current setup guide | common/default in Paper/Fabric docs |
| Custom build logic | plugins/extensions | buildSrc/included builds/plugins/tasks |

Decision: preserve current tool unless a concrete requirement is blocked. For new Android use Gradle. For new general Java libraries/services, choose based on team/ecosystem; Maven remains a high-signal default for conventional builds, Gradle for variant-heavy/custom builds.

Official anchors:
- https://maven.apache.org/docs/history.html
- https://maven.apache.org/guides/
- https://docs.gradle.org/current/userguide/userguide.html
- https://docs.gradle.org/current/userguide/compatibility.html
