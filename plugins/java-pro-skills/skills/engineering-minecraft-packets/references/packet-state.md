# Packet-state doctrine

A robust per-viewer key often needs:
`viewer UUID + connection epoch + world/dimension epoch + entity id + entity generation`.

Client-visible world replication consumes outbound chunk/block updates and makes them visible according to the project’s acknowledgement/timing model. It does not query Bukkit world from a packet thread as authoritative packet-time truth.

Client-visible entity replication:
- spawn initializes generation
- relative moves add deltas, not absolute coordinates
- teleport replaces absolute position
- destroy invalidates the matching generation
- join/respawn/world change clears stale IDs
- delayed tasks carry expected epoch/generation and discard on mismatch

State consumers declare maximum snapshot age and fallback authority. Unavailable/stale evidence is not fabricated.

PacketEvents official anchors:
- https://docs.packetevents.com/
- https://javadocs.packetevents.com/
- https://github.com/retrooper/packetevents
