---
name: enterprise-architect/api-documentation
description: Document RESTful, GraphQL, or event/message API contracts and design guidelines.
---

## Purpose
Produces structured API documentation covering contracts, schemas, authentication, error handling, and versioning for REST, GraphQL, or event-driven APIs. Use this when publishing an API for internal or external consumers or formalizing an existing API contract.

## Context Brief
> To complete this I'll need: API type (REST/GraphQL/event), resources/operations being documented, authentication method, consumers
> Share what you have and I'll ask about anything missing.

## Gap Questions
Ask these one at a time, only if not already provided by the user:
1. What type of API? (REST / GraphQL / Event/Message)
2. What are the main resources or operations?
3. How is the API authenticated?
4. Who are the consumers (internal services, mobile apps, third parties)?
5. Are there versioning requirements?

## Process
1. Establish API type and document the conventions and base URL.
2. For REST: document each resource with endpoints, HTTP methods, request/response schemas, and status codes.
3. For GraphQL: document types, queries, mutations, and subscriptions with example payloads.
4. For events: document event types, schemas, producers, consumers, and ordering guarantees.
5. Document authentication, error handling patterns, and rate limiting policies.

## Output
Produce OpenAPI-aligned markdown documentation with example requests and responses.
Apply all rules in `references/behavioral-guidelines.md` and `references/quality-standards.md`.
Save to `docs/architecture/api/`.
