# Repository execution contract

Use only for repository-changing work.

1. **Intake:** read build/wrapper/toolchain/BOM/locks, touched entrypoints/callers, config/resources, tests/fixtures, relevant logs, and dirty state.
2. **Authority:** current source and locked versions win; verify version-sensitive APIs, coordinates, descriptors, behavior, and migrations in exact official target docs/source.
3. **Change:** trace the first bad state or extension point; reuse the existing owner/provider/adapter; make the smallest complete edit; preserve source/bytecode/runtime/platform compatibility; avoid unrelated cleanup.
4. **Lifecycle:** explicit failure; no silent catch, fake success, unbounded retry, or detached work. Close startup/reload/shutdown/cancellation and thread/resource ownership when touched.
5. **Proof:** baseline when practical; run focused tests plus the full relevant gate; separate pre-existing failures from regressions; exercise the minimum supported runtime/platform when compilation cannot prove compatibility.

Flow: `inspect -> trace -> verify API -> reuse owner -> edit -> focused proof -> full gate`.
