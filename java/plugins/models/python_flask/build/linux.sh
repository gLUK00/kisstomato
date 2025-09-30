#!/bin/bash

# Script de build pour créer le JAR exécutable python-flask-generator-cli.jar
# Plateforme: Linux

echo "=== Build du plugin Python Flask Generator CLI ==="
echo "Plateforme: Linux"
echo "Date: $(date)"
echo ""

# Répertoire du script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

echo "Répertoire du projet: $PROJECT_DIR"
cd "$PROJECT_DIR"

# Vérifier que Maven est installé
if ! command -v mvn &> /dev/null; then
    echo "ERREUR: Maven n'est pas installé ou n'est pas dans le PATH"
    echo "Veuillez installer Maven: https://maven.apache.org/install.html"
    exit 1
fi

echo "Version de Maven:"
mvn --version
echo ""

# Nettoyer le projet
echo "=== Nettoyage du projet ==="
mvn clean
if [ $? -ne 0 ]; then
    echo "ERREUR: Échec du nettoyage du projet"
    exit 1
fi
echo ""

# Compiler et packager le projet
echo "=== Compilation et packaging ==="
mvn package
if [ $? -ne 0 ]; then
    echo "ERREUR: Échec de la compilation ou du packaging"
    exit 1
fi
echo ""

# Vérifier que le JAR a été créé
JAR_FILE="$PROJECT_DIR/target/python-flask-generator-cli.jar"
if [ -f "$JAR_FILE" ]; then
    echo "=== Succès ! ==="
    echo "JAR créé: $JAR_FILE"
    
    # Copier le JAR à la racine du projet
    cp "$JAR_FILE" "$PROJECT_DIR/"
    echo "JAR copié vers: $PROJECT_DIR/python-flask-generator-cli.jar"
    
    # Afficher la taille du fichier
    echo "Taille du JAR: $(du -h "$PROJECT_DIR/python-flask-generator-cli.jar" | cut -f1)"
    
    # Test rapide du JAR
    echo ""
    echo "=== Test du JAR ==="
    java -jar "$PROJECT_DIR/python-flask-generator-cli.jar" 2>/dev/null
    if [ $? -eq 1 ]; then
        echo "JAR fonctionnel (code de retour attendu pour usage sans arguments)"
    else
        echo "Attention: code de retour inattendu du JAR"
    fi
    
else
    echo "ERREUR: Le JAR n'a pas été créé"
    exit 1
fi

echo ""
echo "=== Build terminé avec succès ==="
echo "Vous pouvez maintenant utiliser le JAR:"
echo "  java -jar python-flask-generator-cli.jar --action=create --data='{\"projectName\":\"MyApp\", \"author\":\"Votre Nom\"}'"
echo "  java -jar python-flask-generator-cli.jar --action=open --file='/path/to/project.xml'"
