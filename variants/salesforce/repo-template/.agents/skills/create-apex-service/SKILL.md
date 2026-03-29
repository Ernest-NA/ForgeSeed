---
name: create-apex-service
description: Use this skill when implementing or extending an Apex service class or domain service.
---

# Goal
Create Apex service logic that is bulk-safe, readable, and aligned with the project architecture.

# Steps
1. Review the relevant business process and object model.
2. Inspect existing service or selector patterns before adding new classes.
3. Keep SOQL and DML outside loops.
4. Consider sharing, CRUD/FLS, and exception handling.
5. Add or update Apex tests.

# Constraints
- Avoid mixing orchestration and data access concerns.
- Avoid hidden side effects.
