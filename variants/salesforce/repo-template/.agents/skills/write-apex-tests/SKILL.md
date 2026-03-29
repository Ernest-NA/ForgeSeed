---
name: write-apex-tests
description: Use this skill when adding or improving Apex tests for changed Salesforce behavior.
---

# Goal
Create Apex tests that validate behavior clearly and reduce regression risk.

# Steps
1. Identify the business behavior that changed.
2. Create focused test data with reusable patterns.
3. Validate success path and key edge cases.
4. Use `Test.startTest()` and `Test.stopTest()` where appropriate.
5. Assert meaningful outcomes, not just coverage.

# Constraints
- Avoid brittle tests tied to irrelevant implementation details.
- Avoid unnecessary `SeeAllData=true`.
