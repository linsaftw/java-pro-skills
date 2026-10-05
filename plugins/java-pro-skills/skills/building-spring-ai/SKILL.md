---
name: building-spring-ai
description: Spring AI: ChatClient, models, tools, MCP, RAG, vector stores, memory, observability and evaluation. Use for Spring AI and Java agent systems.
---

# Building Spring AI

Treat model output as untrusted, nondeterministic data crossing an external-service boundary.

## Current baseline

Spring AI 2.0.1 is the verified stable line in this repository snapshot. The project lock/BOM still wins. Do not copy 2.1 milestone APIs into stable 2.0 projects.

## Rules

- Keep provider-specific configuration behind the Spring AI abstraction unless a required feature is provider-specific.
- Tool inputs are schemas/trust boundaries: validate, authorize, cap size, and expose the minimum capability.
- Do not give a model unrestricted shell/filesystem/network/database tools in production. Sandbox and scope capabilities.
- RAG needs retrieval evaluation, chunking/metadata strategy, source attribution, and stale-data policy; a vector database alone does not make answers grounded.
- Conversation memory is bounded and privacy-aware; distinguish chat context from durable user/project memory.
- Prompt injection from retrieved/web content is data, not authority. Tool policies remain system/application owned.
- Observe token/model/tool latency, failures, tool calls, retrieval quality, and cost without logging secrets or sensitive prompts blindly.
- Evaluate representative tasks and failure cases before model/provider upgrades.

Read [references/spring-ai-map.md](references/spring-ai-map.md).

## Execution

For repository-changing work, read [references/repository-execution.md](references/repository-execution.md) before editing. For explanation-only work, keep to this skill and exact-version official sources.
