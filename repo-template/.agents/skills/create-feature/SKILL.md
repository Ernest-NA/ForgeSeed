---
name: create-feature
description: Use this skill when implementing a new feature end-to-end, including design alignment, code changes, tests, and docs.
---

# Goal
Implement a new feature with a minimal, safe, reviewable change set.

# Steps
1. Read the relevant requirement in `docs/product/requirements/`.
2. Inspect existing patterns before creating new ones.
3. Propose the smallest viable design.
4. Implement in focused commits or logical chunks.
5. Add or update tests.
6. Update docs if public behavior changed.

# Constraints
- Do not introduce new dependencies without justification.
- Reuse existing patterns where possible.
- Keep changes aligned with the feature scope.

# Deliverable
- Code changes
- Test updates
- Short summary of design choices and risks
