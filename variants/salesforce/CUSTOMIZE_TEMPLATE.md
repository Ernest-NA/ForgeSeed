# Cómo personalizar la variante Salesforce

Tokens sustituidos automáticamente:
- `__PROJECT_NAME__`
- `__PROJECT_SLUG__`
- `__PROJECT_DESCRIPTION__`
- `__AUTHOR__`
- `__PACKAGE_NAME__`

## Revisiones obligatorias
- `AGENTS.md`
- `sfdx-project.json`
- `manifest/package.xml`
- `.github/workflows/ci.yml`
- `docs/architecture/system-overview.md`
- `docs/runbooks/local-setup.md`
- `.agents/skills/*`

## Qué debes adaptar sí o sí
1. Package name
2. Namespace si aplica
3. Estructura de metadata real
4. Convenciones de tests Apex
5. Estrategia de despliegue
6. Conexión de CI con orgs y secretos
7. Modelo de seguridad y sharing

## Flujo recomendado
1. Generar proyecto con `scaffold_salesforce_project.py`
2. Revisar `AGENTS.md`
3. Ajustar package y manifest
4. Añadir metadata real en `force-app/`
5. Configurar CI
6. Autenticarse con `sf` CLI
7. Hacer primer commit
