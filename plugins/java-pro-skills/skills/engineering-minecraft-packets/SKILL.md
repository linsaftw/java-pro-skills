---
name: engineering-minecraft-packets
description: PacketEvents/protocol engineering: listeners, wrappers, re-encoding, replication, transactions, movement and thread boundaries. Use for packet systems, anti-cheat or client-visible state.
---

# Engineering Minecraft Packets

Packet facts are connection-local and time-dependent. A packet callback is not Bukkit gameplay context.

## PacketEvents rules

- Determine dependency ownership first: external installed plugin vs private bundled/relocated library. Never mix both.
- Match packet type/state/direction before constructing a wrapper.
- Distinguish `serverbound` (client -> server) and `clientbound` (server -> client) explicitly.
- Decode immutable fields, run bounded math/state updates, cancel/mutate packets as needed; do no blocking I/O or unsafe Bukkit mutation in the callback.
- When re-encode-by-default is disabled, wrapper mutation requires `event.markForReEncode(true)`.
- Netty write completion is not client acknowledgement.
- Client protocol version, event server-schema version, and serialization version are different concepts.

## State replication

For reach/collision/anti-cheat/protocol-sensitive products, server Bukkit location is not necessarily what a specific viewer sees. Maintain viewer/session epochs, ordered packet state, staleness policy, and acknowledgement/timeline semantics when exact client-visible state matters.

Read [references/packet-state.md](references/packet-state.md).

## Execution

For repository-changing work, read [references/repository-execution.md](references/repository-execution.md) before editing. For explanation-only work, keep to this skill and exact-version official sources.
