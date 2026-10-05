# JVM performance toolbox

- JFR: low-overhead production diagnostics; CPU samples, allocation, locks, I/O, GC, exceptions.
- JDK Mission Control: inspect JFR recordings.
- `jcmd`: runtime flags, class histogram, JFR control, native memory (when enabled).
- heap dump + MAT/other analyzer: retained graph and dominators.
- GC logs: pause causes, heap sizing, promotion, concurrent-cycle behavior.
- async-profiler: CPU/allocation/lock profiles where available.
- JMH: isolated microbenchmarks.

Do not simultaneously change code, JVM flags, heap size, and workload and then claim causality.
