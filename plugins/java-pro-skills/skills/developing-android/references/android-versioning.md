# Android version/toolchain rules

Verified 2026-10-05:
- Android 17 = API level 37.
- Android Gradle Plugin 9.4 is current stable (September 2026), supports max API 37, and documents Gradle 9.6.0 / JDK 17 as its compatibility baseline/defaults.

Do not globally pin those numbers into an existing project. Read the AGP release page matching the project’s exact plugin version because AGP <-> Gradle <-> JDK <-> Kotlin compatibility is a matrix.

When changing `targetSdk`, read behavior changes for every crossed Android release. Compile SDK availability and target behavior are separate decisions.

Official anchors:
- https://developer.android.com/about/versions/17
- https://developer.android.com/build/releases/gradle-plugin
- https://developer.android.com/jetpack/compose
