---
name: topy-billing
description: Inspect TOPY billing state, credit balance, transactions, subscriptions, and portal/checkout flows using TOPY_AI_KEY. Use when the user wants to check limits or purchase access.
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

- `GET https://topy.ai/api/v1/billing/entitlements`
- `GET https://topy.ai/api/v1/billing/credits/balance`
- `GET https://topy.ai/api/v1/billing/credits/transactions?limit=N`
- `POST https://topy.ai/api/v1/billing/credits/purchase-intent`
- `GET https://topy.ai/api/v1/billing/subscriptions/plans`
- `POST https://topy.ai/api/v1/billing/subscriptions/checkout`
- `POST https://topy.ai/api/v1/billing/subscriptions/portal`

## API and auth

See [references/auth-and-api.md](../topy-ai-ceo-core/references/auth-and-api.md) for the shared convention.

## Rules

- Before any API call, verify that `TOPY_AI_KEY` is available.
- Use `https://topy.ai/api` as the base URL for all calls.
- Prefer reading billing state before any expensive operation.
- Use the billing response as the source of truth for credits and plan limits.
- Keep checkout and portal flows user-driven.

## Failure behavior

- If `TOPY_AI_KEY` is missing, stop and route the user to `topy-init`.
- If the user lacks credit or entitlement, surface the exact backend response.
- If the portal or checkout flow fails, stop and do not retry automatically.
