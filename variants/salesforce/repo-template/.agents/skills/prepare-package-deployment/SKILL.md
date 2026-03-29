---
name: prepare-package-deployment
description: Use this skill when preparing a Salesforce metadata deployment or validation package.
---

# Goal
Prepare a safe, reviewable deployment package and validation plan.

# Steps
1. Identify the exact metadata scope.
2. Review dependencies and target org requirements.
3. Update `package.xml` or deployment manifest as needed.
4. Define validation commands and rollback considerations.
5. Document any post-deploy actions.

# Constraints
- Avoid deploying unrelated metadata.
- Make assumptions about target org configuration explicit.
