---
name: formatting-minecraft-text
description: Adventure/MiniMessage text across Paper and legacy Bukkit: components, audiences, serializers, placeholders, lore, titles and shading. Use for Minecraft text/message compatibility.
---

# Formatting Minecraft Text

Keep user-facing text behind one project text authority/bridge.

## Rules

- Internal representation is Adventure `Component` when the project can support it.
- MiniMessage parses trusted/configured formatting; never concatenate untrusted user text into a MiniMessage template without escaping/tag resolvers.
- Legacy `&`/section-code inputs are deserialized at a compatibility boundary; do not repeatedly mix legacy codes and MiniMessage with find/replace hacks.
- For old Bukkit/Spigot, use the appropriate Adventure platform adapter/serializer boundary.
- Shading/relocation is a type-identity decision: if a public/native/PacketEvents API signature expects unrelocated `net.kyori` types, relocated components cannot cross that boundary.
- Item lore can inherit italic style; explicitly control decoration when needed.
- PlaceholderAPI strings are not MiniMessage; integrate through a deliberate resolver/legacy-deserialization boundary.

Read exact Adventure target docs when adding a serializer/platform dependency.

## Execution

For repository-changing work, read [references/repository-execution.md](references/repository-execution.md) before editing. For explanation-only work, keep to this skill and exact-version official sources.
