# Migration checklist

## Baseline
- capture wrapper/tool versions and exact baseline command
- capture current tests and representative runtime smoke path
- inventory JVM args, agents, reflective libraries, JNI/native libs, annotation processors
- inventory deployment JDK and container/base image

## Dependency gate
- framework major support for destination JDK
- build tool and plugins support destination JDK
- bytecode instrumentation/coverage tools support destination class version
- test engines/mocking libraries support destination JDK
- JDBC drivers/native clients supported

## Source gate
- removed/deprecated JDK APIs
- reflection/module-access failures
- `javax` vs `jakarta` namespace based on owning specification
- date/time/default charset/locale behavior
- finalization/cleaner/resource lifecycle
- changed security providers/algorithms/TLS defaults

## Runtime gate
- start with minimal JVM flags; remove cargo-cult GC flags
- capture JFR/GC evidence before tuning
- verify startup, steady-state, shutdown hooks, signals
- validate memory limits inside containers

## Proof
- compile against intended API level
- run unit/integration tests
- run on minimum and production runtime versions if different
- compare behavior/performance using the same workload
