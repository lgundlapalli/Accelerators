# Project MARS — Capability Mapping
**Project:** Abbott Health Store — Pedialyte DTC
**Date:** 2026-05-04
**Source Documents:** Abbott-Health-Store-Pedialyte-DTC-PRD-2026-05-01.docx, abbott-dtc-pedialyte-ecommerce-evaluation-2026-05-01-v2.docx

---

| # | Business Capability | Category | Technical Enabler | Component | Layer |
|---|---|---|---|---|---|
| 1 | Product Catalog Browsing | Experience | Headless CMS / PIM | Product Listing & Detail Pages | Experience Layer |
| 2 | Product Search & Filtering | Experience | Search Engine (Algolia / Elasticsearch) | Search Service | Experience Layer |
| 3 | Shopping Cart Management | Experience | Session / Cart State Service | Cart UI + Cart API | Experience Layer |
| 4 | Cart Persistence | Data | Persistent Cart Store | Cart State DB (Redis / DB) | Data Layer |
| 5 | 3-Step Checkout Flow | Experience | Checkout Orchestration Service | Checkout UI + Checkout API | Experience Layer |
| 6 | Payment Processing | Integration | Payment Gateway (Stripe / Braintree) | Payment Service | Integration Layer |
| 7 | Payment Tokenization (no saved cards) | Security & Governance | PCI-DSS Tokenization (gateway-side) | Token Vault (external) | Security & Governance |
| 8 | Order Creation & Confirmation | Process | Order Management Service | Order API + Confirmation Email | Application Services Layer |
| 9 | Order Routing to Fulfillment | Integration | Fulfillment Integration Adapter | Fulfillment Connector / Webhook | Integration Layer |
| 10 | Fulfillment Status Sync | Integration | Webhook / Polling Adapter | Order Status Updater | Integration Layer |
| 11 | Subscribe & Save Enrollment | Process | Subscription Engine | Subscription API | Application Services Layer |
| 12 | Recurring Order Scheduling | Process | Job Scheduler (Azure Scheduler / cron) | Recurring Order Job | Application Services Layer |
| 13 | Subscription Management (pause/cancel/edit) | Experience | Subscription Management Service | Account Dashboard — Subscription UI | Experience Layer |
| 14 | Subscribe & Save Discount Application | Process | Pricing / Promotion Engine | Discount Rules Service | Application Services Layer |
| 15 | Loyalty Points Accrual | Process | Loyalty Engine | Points Ledger Service | Application Services Layer |
| 16 | Loyalty Points Redemption | Process | Loyalty Engine | Redemption API + Promo Code Service | Application Services Layer |
| 17 | Loyalty Balance Display | Experience | Loyalty Read API | Account Dashboard — Loyalty UI | Experience Layer |
| 18 | Customer Account Registration | Process | Identity & Access Management (IAM) | Registration Service | Application Services Layer |
| 19 | Customer Authentication (Login / Logout) | Security & Governance | IAM / Auth Provider (Azure AD B2C) | Auth Service (OAuth2 / OIDC) | Security & Governance |
| 20 | Password Reset & MFA | Security & Governance | IAM / Auth Provider | Credential Management Service | Security & Governance |
| 21 | Session Management | Security & Governance | Token-based Session (JWT) | Session Handler | Security & Governance |
| 22 | Account Dashboard — Order History | Experience | Order Read API | Order History UI | Experience Layer |
| 23 | Customer Profile Management | Experience | Profile Service | Profile UI + Profile API | Experience Layer |
| 24 | Customer PII Storage | Data | Encrypted Relational DB | Customer Profile Store | Data Layer |
| 25 | Order Data Persistence | Data | Relational DB (Azure SQL / PostgreSQL) | Order Store | Data Layer |
| 26 | Product Data Management | Data | PIM / CMS Data Store | Product Catalog DB | Data Layer |
| 27 | Loyalty Points Ledger Storage | Data | Transactional DB | Loyalty Ledger Store | Data Layer |
| 28 | Subscription Data Persistence | Data | Relational DB | Subscription Store | Data Layer |
| 29 | Mobile Responsive UI | Experience | Responsive Design Framework (React + Tailwind) | Frontend SPA / SSR App | Experience Layer |
| 30 | Transactional Email Notifications | Integration | Email Service Provider (SendGrid / Azure Comms) | Notification Service | Integration Layer |
| 31 | Revenue & Conversion Analytics | Integration | Analytics Platform (GA4 / Segment) | Analytics Event Pipeline | Integration Layer |
| 32 | Business Reporting & KPI Tracking | Data | Data Warehouse / BI Tool | Reporting Store + Dashboard | Data Layer |
| 33 | Event / Audit Logging | Security & Governance | Centralized Log Aggregator (Azure Monitor) | Audit Log Service | Security & Governance |
| 34 | API Gateway & Routing | Platform | API Gateway (Azure APIM / Kong) | API Gateway | Infrastructure Layer |
| 35 | CDN & Asset Delivery | Platform | CDN (Azure Front Door) | CDN Layer | Infrastructure Layer |
| 36 | Application Hosting & Scaling | Platform | Container Orchestration (AKS / Azure App Service) | Compute Hosting | Infrastructure Layer |
| 37 | CI/CD Pipeline | Platform | DevOps Toolchain (Azure DevOps / GitHub Actions) | Build & Deploy Pipeline | Infrastructure Layer |
| 38 | Secrets & Config Management | Security & Governance | Secrets Manager (Azure Key Vault) | Config & Secrets Store | Security & Governance |
| 39 | Data Encryption at Rest & in Transit | Security & Governance | TLS + DB Encryption | Encryption Layer | Security & Governance |
| 40 | SOC2 / PII Compliance Controls | Security & Governance | Policy Engine + Data Masking | Compliance & Privacy Controls | Security & Governance |
| 41 | Rate Limiting & Bot Protection | Security & Governance | WAF / Rate Limiter (Azure WAF) | Edge Security Layer | Security & Governance |
| 42 | Inventory Availability Check | Integration | Inventory Service / Fulfillment API | Inventory Availability Adapter | Integration Layer |
| 43 | Pricing Service | Process | Pricing Engine | Price Calculation Service | Application Services Layer |
| 44 | Tax Calculation | Integration | Tax Service (Avalara / TaxJar) | Tax Calculation Adapter | Integration Layer |
| 45 | Shipping Estimation | Integration | Shipping Carrier API (UPS / FedEx) | Shipping Rate Adapter | Integration Layer |
