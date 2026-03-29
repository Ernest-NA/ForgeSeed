---
name: write-tests
description: Use this skill when adding or improving automated tests for changed or critical behavior.
---

# Goal
Create clear tests that validate behavior and are easy to maintain.

# Steps
1. Identify the behavior under test.
2. Prefer tests close to the affected module boundary.
3. Cover happy path, key edge case, and failure mode where appropriate.
4. Keep assertions precise and readable.

# Constraints
- Do not overmock.
- Avoid brittle implementation-detail assertions.
