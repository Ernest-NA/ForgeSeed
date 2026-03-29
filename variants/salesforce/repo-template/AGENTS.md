# AGENTS.md

## Project context
- Project name: __PROJECT_NAME__
- Slug: __PROJECT_SLUG__
- Description: __PROJECT_DESCRIPTION__
- Owner: __AUTHOR__
- Salesforce package name: __PACKAGE_NAME__

## Operating model
This repository is designed for Salesforce delivery using:
- Apex
- Lightning Web Components
- Flows
- permission-based security
- sf CLI driven validation and deployment

## Working rules
- Prefer small, reviewable diffs.
- Respect existing metadata structure and naming conventions.
- Do not weaken security checks, CRUD/FLS validation, or sharing behavior.
- Update tests and docs when behavior changes.
- Avoid introducing parallel patterns when a project standard already exists.

## Expected workflow
1. Read the relevant docs in `docs/`.
2. Select the relevant skill from `.agents/skills/`.
3. Implement the smallest safe change.
4. Update Apex tests or UI validation where applicable.
5. Summarize files changed, org impact, and follow-up items.

## Repository map
- `force-app/`: metadata source
- `manifest/`: package manifests
- `.agents/skills/`: Salesforce-focused workflows
- `.github/`: CI and collaboration templates
- `docs/`: architecture and runbooks

## Done means
- Scope implemented.
- Validation steps documented.
- Security implications checked.
- Tests added or updated where applicable.
- Deployment and rollback considerations called out when relevant.
