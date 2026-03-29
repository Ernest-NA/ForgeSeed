---
name: review-soql-security
description: Use this skill when reviewing Apex or metadata changes for CRUD, FLS, sharing, and SOQL safety.
---

# Goal
Review Salesforce code and metadata with a security and governor-limit lens.

# Review checklist
- Is CRUD/FLS enforced where needed?
- Is sharing behavior explicit and correct?
- Are SOQL queries selective and outside loops?
- Are DML operations bulk-safe?
- Is sensitive data exposure controlled?

# Output
- Findings ordered by severity
- Security risks
- Governor-limit or query risks
- Suggested remediations
