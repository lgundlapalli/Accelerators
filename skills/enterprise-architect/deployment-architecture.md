---
name: enterprise-architect/deployment-architecture
description: Design infrastructure topology, networking, and cloud deployment architecture.
---

## Purpose
Produces a deployment architecture document covering cloud infrastructure, network topology, environment design, and HA/DR approach. Use this when standing up a new system, migrating to cloud, or hardening an existing deployment for resilience and compliance.

## Context Brief
> To complete this I'll need: cloud provider, deployment model (containers/VMs/serverless), environments needed, network segmentation and security requirements
> Share what you have and I'll ask about anything missing.

## Gap Questions
Ask these one at a time, only if not already provided by the user:
1. Which cloud provider? (AWS / Azure / GCP / on-prem / hybrid)
2. Container, VM, or serverless?
3. What environments are needed (dev/staging/prod)?
4. Are there network segmentation or compliance requirements (VPC, private subnets, firewall rules)?
5. What are the HA and DR requirements?

## Process
1. Define each environment and its purpose, access controls, and promotion rules.
2. Design network topology — VPCs, subnets, peering, and segmentation.
3. Map services to deployment units — containers, functions, or VMs.
4. Address ingress/egress, load balancing, and CDN strategy.
5. Document the HA and DR approach — failover, replication, RTO/RPO targets.

## Output
Produce a deployment topology diagram in Mermaid and an environment summary table.
Apply all rules in `references/behavioral-guidelines.md` and `references/quality-standards.md`.
Save to `docs/architecture/deployment-architecture-[date].md`.
