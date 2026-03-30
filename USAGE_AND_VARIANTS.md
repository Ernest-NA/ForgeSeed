# ForgeSeed Usage and Variants

## Available variants

ForgeSeed does **not** use separate branches for each template type.

The operating model is:
- generic template in `repo-template/`
- Salesforce template in `variants/salesforce/repo-template/`

You should generate **only the variant that matches the project**, instead of cloning ForgeSeed and deleting folders manually.

## Commands to use

### Generic project
Use the base template.

```bash
python scaffold_project.py "My Project" --dest "C:\Work" --description "Project description" --author "Your Name" --init-git
```

Windows launcher:

```text
new-codex-project.bat
```

### Salesforce project
Use the Salesforce variant.

```bash
python scaffold_salesforce_project.py "My Salesforce Project" --dest "C:\Work" --description "Salesforce project" --author "Your Name" --init-git
```

With explicit package name:

```bash
python scaffold_salesforce_project.py "My Salesforce Project" --dest "C:\Work" --description "Salesforce project" --author "Your Name" --package-name "my_package" --init-git
```

Windows launcher:

```text
new-salesforce-project.bat
```

## What each generator creates

### Generic generator
Creates a repository with:
- `AGENTS.md`
- `.agents/skills/`
- `.github/`
- `docs/`
- `src/`
- `tests/`
- `notion/`

### Salesforce generator
Creates a repository with:
- `AGENTS.md`
- `sfdx-project.json`
- `manifest/package.xml`
- `force-app/`
- `.agents/skills/`
- `.github/`
- `docs/`

## Operational rules
- Use `scaffold_project.py` for normal software projects.
- Use `scaffold_salesforce_project.py` for Salesforce projects.
- Do not use another branch to distinguish generic and Salesforce templates.
- Do not clone ForgeSeed and delete folders manually for each project.
- Generate the correct variant directly.
