@echo off
setlocal

echo ============================================
echo   ForgeSeed Salesforce Project Creator
echo ============================================
echo.

set /p PROJECT_NAME=Nombre del proyecto Salesforce: 
set /p DEST_PATH=Ruta destino (ej: C:\Work): 
set /p DESCRIPTION=Descripcion corta: 
set /p AUTHOR=Autor/Owner: 
set /p PACKAGE_NAME=Package name (opcional): 

if "%PROJECT_NAME%"=="" (
  echo Debes indicar un nombre de proyecto.
  pause
  exit /b 1
)

if "%DEST_PATH%"=="" (
  set DEST_PATH=.
)

if "%DESCRIPTION%"=="" (
  set DESCRIPTION=New Salesforce project
)

if "%AUTHOR%"=="" (
  set AUTHOR=%USERNAME%
)

if "%PACKAGE_NAME%"=="" (
  python "%~dp0scaffold_salesforce_project.py" "%PROJECT_NAME%" --dest "%DEST_PATH%" --description "%DESCRIPTION%" --author "%AUTHOR%" --init-git
) else (
  python "%~dp0scaffold_salesforce_project.py" "%PROJECT_NAME%" --dest "%DEST_PATH%" --description "%DESCRIPTION%" --author "%AUTHOR%" --package-name "%PACKAGE_NAME%" --init-git
)

echo.
pause
