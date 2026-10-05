---
name: developing-minecraft-proxies
description: Velocity/Bungee-style proxy development: events, forwarding, trust, auth boundaries, routing and backend messaging. Use for proxy plugins or cross-server integration.
---

# Developing Minecraft Proxies

Proxy and backend are separate trust/execution domains.

## Rules

- Use exact proxy API docs/version; do not assume Bukkit classes/lifecycle on a proxy.
- Never treat username/profile lookup as proof that the connecting client owns an account.
- Separate detection/hints, cryptographic/trusted proof, routing decision, persistence, and backend execution.
- Forward identity only through the proxy platform’s authenticated forwarding mechanism; do not trust arbitrary plugin messages from clients/backends.
- Plugin-message payloads are versioned, bounded, authenticated/authorized where security-sensitive, and validated before allocation/deserialization.
- Network/event-loop threads do bounded nonblocking work. Database/HTTP/file work goes to owned async execution.
- Backend game mutations happen on the backend’s correct Bukkit/Paper/Folia owner, not proxy thread assumptions.
- Reconnect/server-switch lifecycle invalidates per-connection state.

## Execution

For repository-changing work, read [references/repository-execution.md](references/repository-execution.md) before editing. For explanation-only work, keep to this skill and exact-version official sources.
