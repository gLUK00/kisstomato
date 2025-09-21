# KissTomato JavaFX Application

Cette application JavaFX présente une interface de gestion de projets avec deux pages principales.

## Structure de l'application

- **Page principale** : Affiche une liste de projets sous forme de tableau avec colonnes (nom, description, type de plugin)
- **Page projet** : Affiche un message de bienvenue avec un bouton retour

## Prérequis

- Java 17 ou supérieur
- Maven 3.6+
- JavaFX 21 (inclus via Maven)

## Compilation et exécution

### Avec Maven

```bash
cd java

# Compiler l'application
mvn clean compile

# Lancer l'application
mvn javafx:run

# Créer un JAR autonome
mvn clean package
```

### Avec VS Code

1. **Mode debug** : Utiliser la configuration "Debug KissTomato App" dans le menu Run and Debug
2. **Mode normal** : Utiliser la configuration "Run KissTomato App"
3. **Compilation JAR** : Exécuter la tâche "compile-jar" via Terminal > Run Task

## Configuration VS Code

Pour utiliser les configurations de lancement, vous devez installer l'extension Java pour VS Code :
- Extension Pack for Java (Microsoft)

## Utilisation

1. L'application s'ouvre sur la page principale
2. Double-cliquez sur un projet dans le tableau pour l'ouvrir
3. Sur la page projet, cliquez sur "Retour" pour revenir à la liste

## Structure des fichiers

```
java/
├── pom.xml                          # Configuration Maven
├── .vscode/
│   ├── launch.json                  # Configurations de lancement
│   └── tasks.json                   # Tâches de compilation
└── src/main/
    ├── java/com/kisstomato/
    │   ├── App.java                 # Classe principale
    │   ├── Project.java             # Modèle de données
    │   ├── MainController.java      # Contrôleur page principale
    │   └── ProjectController.java   # Contrôleur page projet
    └── resources/
        ├── main.fxml                # Interface page principale
        └── project.fxml             # Interface page projet
```
