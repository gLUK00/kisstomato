# Python Flask Generator CLI

Générateur de projets Python Flask en ligne de commande pour KissTomato.

## Description

Ce plugin génère des projets Python Flask avec une structure de base comprenant :
- Application Flask de base avec routes
- Configuration de l'application
- Templates Jinja2 avec Bootstrap
- Fichiers de dépendances
- Documentation README

## Structure du plugin

```
plugins/models/python_flask/
├── build/
│   ├── linux.sh              # Script de build Linux
│   └── windows.bat           # Script de build Windows  
├── src/
│   ├── main/java/org/kisstomato/plugins/models/python_flask/
│   │   ├── Main.java         # Classe principale
│   │   ├── CreateNewProject.java  # Création de projets
│   │   └── OpenProject.java  # Ouverture de projets
│   └── resources/templates/  # Templates Freemarker
├── test/                     # Tests du plugin
├── plugin.json              # Configuration du plugin
├── pom.xml                  # Configuration Maven
└── python-flask-generator-cli.jar  # JAR exécutable
```

## Compilation

### Linux
```bash
./build/linux.sh
```

### Windows
```cmd
build\windows.bat
```

## Utilisation

### Créer un nouveau projet
```bash
java -jar python-flask-generator-cli.jar --action=create --data='{"projectName":"MyFlaskApp", "author":"John Doe"}'
```

### Ouvrir un projet existant
```bash
java -jar python-flask-generator-cli.jar --action=open --file='/path/to/project.xml'
```

## Codes de retour

- **0** : Succès
- **1** : Erreur de parsing des arguments

## Structure des projets générés

```
MyFlaskApp/
├── app/
│   ├── templates/           # Templates Jinja2
│   │   ├── base.html       # Template de base avec Bootstrap
│   │   └── index.html      # Page d'accueil
│   └── static/            # Fichiers statiques
│       ├── css/
│       └── js/
├── tests/                 # Tests unitaires
├── app.py                # Point d'entrée de l'application
├── config.py             # Configuration
├── requirements.txt      # Dépendances Python
└── README.md            # Documentation
```

## Développement

### Debug avec VS Code

Le fichier `.vscode/launch.json` contient deux configurations de debug :

1. **Debug Python Flask Plugin - Create Project** : Test de création de projet
2. **Debug Python Flask Plugin - Open Project** : Test d'ouverture de projet

### Technologies utilisées

- **Java 11+** : Langage de développement
- **Maven** : Gestionnaire de dépendances
- **FreeMarker** : Moteur de templates
- **Jackson** : Parsing JSON
- **Maven Shade Plugin** : Création du JAR exécutable

### Dépendances

- `freemarker:2.3.32` : Templates
- `jackson-databind:2.15.2` : JSON
- `junit:4.13.2` : Tests (scope test)

## Tests

Des projets de test peuvent être créés en utilisant :

```bash
java -jar python-flask-generator-cli.jar --action=create --data='{"projectName":"TestFlaskApp", "author":"Developer Test"}'
```

Le projet généré peut ensuite être testé avec :

```bash
cd TestFlaskApp
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou venv\Scripts\activate  # Windows
pip install -r requirements.txt
python app.py
```

L'application sera accessible sur http://localhost:5000

## Intégration KissTomato

Le fichier `plugin.json` configure l'intégration avec KissTomato :

```json
{
    "type": "java-jar",
    "name": "Python Flask Generator",
    "description": "Générateur de projets Python Flask",
    "version": "1.0.0",
    "author": "KissTomato",
    "cmd-create-new-project": "java -jar {path_plugin}/python-flask-generator-cli.jar --action=create --data={data}",
    "cmd-open-project": "java -jar {path_plugin}/python-flask-generator-cli.jar --action=open --file={file}"
}
```

## Maintenance

Pour mettre à jour le plugin :

1. Modifier le code source dans `src/`
2. Recompiler avec le script de build approprié
3. Tester avec des projets de test
4. Mettre à jour la version dans `pom.xml` et `plugin.json`
