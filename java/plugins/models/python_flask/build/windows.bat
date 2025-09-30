@echo off
setlocal enabledelayedexpansion

REM Script de build pour créer le JAR exécutable python-flask-generator-cli.jar
REM Plateforme: Windows

echo === Build du plugin Python Flask Generator CLI ===
echo Plateforme: Windows
echo Date: %date% %time%
echo.

REM Répertoire du script
set SCRIPT_DIR=%~dp0
set PROJECT_DIR=%SCRIPT_DIR%..

echo Répertoire du projet: %PROJECT_DIR%
cd /d "%PROJECT_DIR%"

REM Vérifier que Maven est installé
mvn --version >nul 2>&1
if !errorlevel! neq 0 (
    echo ERREUR: Maven n'est pas installé ou n'est pas dans le PATH
    echo Veuillez installer Maven: https://maven.apache.org/install.html
    pause
    exit /b 1
)

echo Version de Maven:
mvn --version
echo.

REM Nettoyer le projet
echo === Nettoyage du projet ===
mvn clean
if !errorlevel! neq 0 (
    echo ERREUR: Échec du nettoyage du projet
    pause
    exit /b 1
)
echo.

REM Compiler et packager le projet
echo === Compilation et packaging ===
mvn package
if !errorlevel! neq 0 (
    echo ERREUR: Échec de la compilation ou du packaging
    pause
    exit /b 1
)
echo.

REM Vérifier que le JAR a été créé
set JAR_FILE=%PROJECT_DIR%\target\python-flask-generator-cli.jar
if exist "%JAR_FILE%" (
    echo === Succès ! ===
    echo JAR créé: %JAR_FILE%
    
    REM Copier le JAR à la racine du projet
    copy "%JAR_FILE%" "%PROJECT_DIR%\"
    echo JAR copié vers: %PROJECT_DIR%\python-flask-generator-cli.jar
    
    REM Afficher la taille du fichier
    for %%I in ("%PROJECT_DIR%\python-flask-generator-cli.jar") do echo Taille du JAR: %%~zI octets
    
    REM Test rapide du JAR
    echo.
    echo === Test du JAR ===
    java -jar "%PROJECT_DIR%\python-flask-generator-cli.jar" >nul 2>&1
    if !errorlevel! equ 1 (
        echo JAR fonctionnel ^(code de retour attendu pour usage sans arguments^)
    ) else (
        echo Attention: code de retour inattendu du JAR
    )
    
) else (
    echo ERREUR: Le JAR n'a pas été créé
    pause
    exit /b 1
)

echo.
echo === Build terminé avec succès ===
echo Vous pouvez maintenant utiliser le JAR:
echo   java -jar python-flask-generator-cli.jar --action=create --data="{\"projectName\":\"MyApp\", \"author\":\"Votre Nom\"}"
echo   java -jar python-flask-generator-cli.jar --action=open --file="C:\path\to\project.xml"
echo.
pause
