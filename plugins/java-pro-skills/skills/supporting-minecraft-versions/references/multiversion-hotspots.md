# Minecraft multi-version hotspots

Audit these before claiming broad compatibility:

- materials and pre/post-flattening aliases/data
- sounds, particles/effects, entity type renames
- `MaterialData` vs `BlockData`
- collision shapes/bounding boxes
- signs and sided sign APIs
- Adventure/components/titles/action bars
- PersistentDataContainer vs legacy storage
- skull/profile APIs
- offhand/equipment slots
- potions
- command APIs/permission messages
- passenger/entity behavior
- async teleport/futures
- Paper-only APIs
- Folia schedulers
- NMS/mappings/package layout

Classloading test: launch the produced JAR on the **minimum supported server/JVM**, not only compile against a legacy API.
