# Documentation des Plugins de Type "Models" pour Kisstomato Studio

Les plugins de type "Models" sont au cœur de Kisstomato Studio. Ils définissent les différents types de projets ou de composants de projet que Studio peut comprendre, gérer et pour lesquels il peut générer du code ou une structure. Chaque plugin "Model" encapsule la logique, la configuration, les templates et potentiellement les éléments d'interface utilisateur nécessaires pour un type de projet spécifique (par exemple, une application web Flask, un site HTML statique, un script Python, ou même un autre "modèle Kisstomato").

## Objectif

L'objectif principal d'un plugin "Model" est de fournir un cadre complet pour :

*   **Définir un schéma :** Décrire la structure, les éléments configurables et les propriétés d'un type de projet.
*   **Initialiser un projet :** Fournir une structure de données initiale lorsqu'un utilisateur crée un nouveau projet de ce type.
*   **Générer le code/la structure :** Transformer la configuration d'un projet (définie par vous) en une arborescence de fichiers et de répertoires fonctionnels.
*   **Personnaliser l'interface utilisateur :** Optionnellement, ajouter des contrôles ou des vues spécifiques à l'interface de Kisstomato Studio lorsque l'on travaille sur un projet de ce type.

## Structure d'un Plugin "Model"

Chaque plugin "Model" réside dans son propre répertoire à l'intérieur de `eel/plugins/models/`. Le nom de ce répertoire sert d'identifiant unique au plugin (`<pluginName>`).

eel/ └── plugins/ └── models/ └──


## Composants Clés

### 1. `configuration.json` (Obligatoire)

Ce fichier JSON définit les métadonnées et le schéma du type de projet.

*   **`title` (String) :** Nom lisible par l'humain du type de modèle. Affiché dans l'interface utilisateur de Kisstomato Studio. (Exemple : `"title": "Application HTML Maker"`)
*   **`elements` (Array, Optionnel) :** Pour les modèles complexes, ce tableau définit les types d'éléments hiérarchiques qui peuvent être créés et configurés par vous. Chaque objet élément peut contenir :
    *   `id` (String) : Identifiant unique pour ce type d'élément.
    *   `text` (String) : Libellé affiché dans l'interface.
    *   `icon` (String) : Classe d'icône (par exemple, Font Awesome) pour l'affichage.
    *   `children-type` (Array de Strings) : Liste des `id` d'éléments qui peuvent être enfants de ce type d'élément.
    *   `items` (Array d'Objets) : Définit les propriétés configurables pour cet élément. Chaque objet propriété a :
        *   `id` (String) : Nom de la propriété (utilisé comme clé dans les données JSON du projet).
        *   `text` (String) : Libellé affiché pour la propriété.
        *   `type` (String) : Type de champ pour la saisie de la valeur (ex: `string`, `text`, `list`, `checkbox`, `color`, `icon`, `object`). Ces types peuvent correspondre à des champs HTML standard ou à des [plugins "Fields"](./fields_plugins.md) personnalisés.
        *   Attributs spécifiques au type (ex: `min`, `max` pour `range`, `items` pour `list` avec des paires `text`/`value`).

    _Pour les modèles simples (comme `python_script`), ce fichier peut ne contenir que le `title`._

### 2. `model.py` (Obligatoire)

Ce fichier Python contient la logique backend pour l'initialisation d'un nouveau projet de ce type. Il doit implémenter la fonction suivante :

*   `getJsonCreateNewProject(data)` :
    *   **Rôle :** Modifier et retourner la structure de données initiale pour un nouveau projet.
    *   **Paramètres :**
        *   `data` (dict) : Un dictionnaire, potentiellement pré-rempli par Kisstomato Studio, représentant le nouveau projet.
    *   **Comportement :** Cette fonction doit ajouter ou modifier des clés dans le dictionnaire `data` pour établir la structure de base du projet. Cela peut inclure la création d'une arborescence de nœuds par défaut (comme dans `html_maker` qui crée des nœuds racines "Pages" et "Contenus") ou simplement l'ajout de quelques propriétés initiales.
    *   **Retourne :** (dict) Le dictionnaire `data` modifié.

### 3. `generation.py` (Fortement Recommandé pour les modèles génératifs)

Ce fichier Python contient la logique pour générer les fichiers et répertoires du projet. Il expose typiquement une fonction principale de génération.

*   Fonction de Génération (nom par convention, ex: `generateCode(oData)`, `generateHtmlCode(oData)`) :
    *   **Rôle :** Orchestrer la création du projet sur le système de fichiers.
    *   **Paramètres :**
        *   `oData` (dict) : Un dictionnaire contenant les informations nécessaires pour la génération, fourni par Kisstomato Studio. Cela inclut typiquement :
            *   `file` (String) : Chemin vers le fichier JSON du projet (contenant la configuration définie par vous).
            *   `dir-out` (String) : Répertoire de destination final pour le projet généré.
            *   `dir-temp` (String) : Répertoire temporaire pour assembler les fichiers avant de les déplacer vers `dir-out`.
    *   **Comportement :**
        1.  Lit la configuration du projet à partir du `file` JSON.
        2.  Utilise un moteur de templates (généralement Jinja2) pour traiter les fichiers du répertoire `templates/` du plugin, en les remplissant avec les données du projet.
        3.  Crée l'arborescence des fichiers et des répertoires dans `dir-temp`.
        4.  Copie les fichiers statiques du répertoire `assets/` du plugin vers `dir-temp`.
        5.  Fusionne le contenu de `dir-temp` vers `dir-out`. Des stratégies de fusion peuvent être implémentées pour gérer les fichiers existants (par exemple, en protégeant des sections spécifiques via des commentaires).
    *   **Retourne :** (String) Un rapport ou un message de statut sur l'opération de génération.

### 4. `js/front.js` (Optionnel)

Ce fichier JavaScript permet au plugin d'interagir avec l'interface utilisateur de Kisstomato Studio ou de l'enrichir lorsque vous travaillez sur un projet de ce type de modèle.

*   **Cas d'usage courants :**
    *   Ajouter des boutons à la barre d'outils ou à d'autres zones de l'interface (par exemple, un bouton "Générer le code" qui déclenche la fonction de `generation.py`).
    *   Implémenter des vues ou des interactions personnalisées spécifiques au type de modèle.
    *   Manipuler le DOM de la page de projet pour afficher des informations supplémentaires.

### 5. `templates/` (Optionnel, mais essentiel pour la génération)

Ce répertoire contient les fichiers modèles (ex: `.html`, `.py`, `.json` templates) qui sont traités par le moteur de templates (Jinja2) dans `generation.py`. Les placeholders dans ces templates sont remplacés par les données du projet lors de la génération.

### 6. `assets/` (Optionnel)

Contient des fichiers statiques (images, CSS, bibliothèques JS, etc.) qui font partie intégrante du projet généré et doivent être copiés tels quels dans le répertoire de sortie.

### 7. `classes/`, `helpers/` (Optionnel)

Ces répertoires peuvent contenir des modules et des classes Python pour organiser et structurer le code utilisé dans `model.py` et `generation.py`, améliorant ainsi la lisibilité et la maintenabilité du plugin.

## Workflow d'Intégration

1.  **Découverte :** Kisstomato Studio scanne `eel/plugins/models/` pour trouver les plugins disponibles. Le `title` de `configuration.json` est utilisé pour les afficher.
2.  **Création de Projet :**
    *   Vous choisissez un type de modèle.
    *   Studio appelle `model.py:getJsonCreateNewProject()` du plugin pour obtenir la structure JSON initiale.
    *   Cette structure, combinée au schéma de `configuration.json`, alimente l'interface utilisateur pour la configuration du projet.
3.  **Édition de Projet :** Vous modifiez le projet. Ces modifications sont sauvegardées dans le fichier JSON du projet. L'interface peut être enrichie par `js/front.js`.
4.  **Génération de Code :**
    *   Vous déclenchez l'action de génération (souvent via un bouton ajouté par `js/front.js`).
    *   Studio appelle la fonction principale de `generation.py` du plugin, en lui passant les informations nécessaires.
    *   Le plugin génère les fichiers dans le répertoire de sortie spécifié.

## Conclusion

Les plugins "Models" sont la pierre angulaire de l'extensibilité de Kisstomato Studio pour la gestion de différents types de projets. En comprenant et en implémentant correctement ces composants, les développeurs peuvent adapter Studio à une grande variété de besoins de développement et de workflows de génération de code.
