---
name: topy-billing
description: Inspect TOPY billing state, credit balance, transactions, subscriptions, and portal/checkout flows. Use when the user wants to check limits or purchase access.
---

# TOPY Billing

## Intent

Read billing state and initiate subscription or credit-purchase flows.

## Allowed operations

- View entitlements
- View credit balance
- View credit transactions
- Start a credit purchase intent
- List subscription plans
- Start subscription checkout
- Open the billing portal

## Route map

- `GET /api/v1/billing/entitlements`
- `GET /api/v1/billing/credits/balance`
- `GET /api/v1/billing/credits/transactions?limit=N`
- `POST /api/v1/billing/credits/purchase-intent`
- `GET /api/v1/billing/subscriptions/plans`
- `POST /api/v1/billing/subscriptions/checkout`
- `POST /api/v1/billing/subscriptions/portal`

## Rules

- Prefer reading billing state before any expensive operation.
- Use the billing response as the source of truth for credits and plan limits.
- Keep checkout and portal flows user-driven.

## Failure behavior

- If the user lacks credit or entitlement, surface the exact backend response.
- If the portal or checkout flow fails, stop and do not retry automatically.
