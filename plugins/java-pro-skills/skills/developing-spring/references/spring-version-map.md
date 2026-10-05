# Spring version map

Verified snapshot: 2026-10-05.

- Spring Boot current stable page: 4.1.1.
- Spring Framework current stable page: 7.0.8.
- Spring AI current stable: 2.0.1 and supports Boot 4.0.x/4.1.x; 2.1.0-M1 is preview and targets a newer Boot milestone, so do not use it as stable default.
- Existing Boot 3 / Framework 6 applications remain common. Preserve their BOM and API contracts unless migration is requested.

Migration rule: read the official Spring Boot release notes/migration guide for the exact source and destination lines. Never infer package/API changes solely from major version numbers.

Official anchors:
- https://spring.io/projects/spring-boot
- https://spring.io/projects/spring-framework
- https://docs.spring.io/spring-boot/
- https://docs.spring.io/spring-framework/reference/
