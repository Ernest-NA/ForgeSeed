---
name: analyze-sharing-model
description: Use this skill when designing or reviewing Salesforce sharing, visibility, and record access behavior.
---

# Goal
Analyze whether the sharing model supports the intended business access rules.

# Steps
1. Identify actors, roles, and record ownership model.
2. Review OWD, role hierarchy, sharing rules, teams, and manual or Apex sharing.
3. Evaluate whether the model matches the business process.
4. Note any reporting or UX side effects.
5. Document risks and recommended changes.

# Constraints
- Avoid local fixes that bypass the intended security model.
- Consider scale and maintainability of sharing logic.
