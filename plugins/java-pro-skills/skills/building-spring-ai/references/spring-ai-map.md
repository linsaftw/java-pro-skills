# Spring AI capability map

Spring AI 2.0.x includes portable model APIs, ChatClient, tool calling, advisors, vector stores, ETL/RAG support, observability, evaluation utilities, and MCP integration.

Agent utility design lessons worth reusing without coupling to any one library:
- filesystem/shell/web tools need explicit sandbox and timeout contracts
- tool-call listeners/audit hooks are essential for operational visibility
- task/subagent delegation needs bounded scope and result contracts
- interruption/deadline/budget controls belong outside the model
- skill loading should use progressive disclosure
- durable memory needs type, ownership, retention, and consolidation policy

Official anchors:
- https://spring.io/projects/spring-ai
- https://docs.spring.io/spring-ai/reference/
