# Salesforce Variant

Esta variante de ForgeSeed está orientada a proyectos basados en Salesforce.

## Incluye
- plantilla de repo especializada
- `AGENTS.md` adaptado a Apex, LWC, Flows y modelo de seguridad
- skills específicas para desarrollo y revisión Salesforce
- workflow base de CI para `sf` CLI
- estructura inicial de `force-app/` y `manifest/`
- runbooks y documentación técnica orientados a Salesforce

## Archivos de arranque
- `scaffold_salesforce_project.py`
- `new-salesforce-project.bat`
- `CUSTOMIZE_TEMPLATE.md`

## Uso rápido
Desde la raíz del repositorio:

```bash
python scaffold_salesforce_project.py "Mi Proyecto Salesforce" --dest "C:\Work" --description "Proyecto Salesforce" --author "Ernesto" --init-git
```

## Objetivo
Que un proyecto Salesforce nuevo empiece ya con una base coherente para:
- arquitectura
- validación
- skills de Codex
- despliegue
- seguridad
- documentación
