# Kisstomato Studio

Kisstomato Studio est un outil de développement de bureau conçu pour faciliter la gestion et la génération de code pour des "projets Kisstomato". Il offre une interface graphique conviviale construite avec des technologies web, tout en exploitant la puissance de Python pour sa logique principale.

## Aperçu Général

*   **Type d'application :** Environnement de Développement Spécialisé / Outil de Productivité pour Développeurs.
*   **Technologie principale :** Python, utilisant la bibliothèque Eel pour lier le backend Python à une interface utilisateur HTML/JS.
*   **Interface Utilisateur :** Basée sur HTML, CSS (avec Bootstrap), et JavaScript (avec jQuery), s'exécutant dans une fenêtre d'application native.

## Fonctionnalités Clés

*   **Gestion de Projets Kisstomato :**
    *   Permet de créer de nouveaux projets Kisstomato.
    *   Ouvre des projets Kisstomato existants à partir de leurs fichiers de définition.
    *   Référence des projets existants pour les intégrer dans l'environnement de travail.
    *   Les projets sont typiquement définis par des fichiers de configuration au format JSON.

*   **Génération de Code :**
    *   Intègre un moteur de génération de code capable de produire des structures de fichiers et du contenu basé sur les modèles et les configurations du projet.
    *   La nature exacte du code généré est déterminée par les plugins installés et activés.

*   **Interface Graphique Intuitive :**
    *   Offre une page d'accueil pour la sélection et la création de projets.
    *   Propose un espace de travail dédié (probablement via `project.html`) une fois un projet chargé.
    *   Utilise des dialogues système natifs pour les opérations de fichiers (ouvrir, enregistrer), assurant une bonne intégration avec l'OS.

*   **Système de Plugins Extensible :**
    *   L'architecture de Kisstomato Studio est conçue autour d'un système de plugins.
    *   Ces plugins étendent les capacités de l'outil, notamment en ce qui concerne les types de code qui peuvent être générés et les spécificités des différents "modèles" de projets Kisstomato.
    *   Cela permet à l'outil de s'adapter à divers besoins de développement sans modifier le noyau de l'application.

## Architecture Technique

*   **Backend :** Développé en Python, il gère la logique métier, la lecture des configurations, l'interaction avec le système de fichiers et le moteur de génération de code.
*   **Frontend :** L'interface utilisateur est construite avec des fichiers HTML, CSS et JavaScript. La communication entre le frontend et le backend Python est assurée par Eel.
*   **Configuration :** Utilise des fichiers JSON (par exemple, `configuration.json`) pour les paramètres de l'application et la définition des chemins vers les projets.

## Utilisation Typique

Vous lanceriez Kisstomato Studio pour :
1.  Sélectionner un projet Kisstomato existant ou en créer un nouveau.
2.  Travailler sur la structure et les définitions du projet via l'interface graphique.
3.  Utiliser les fonctionnalités de génération de code pour produire des artefacts de projet, en fonction des plugins configurés pour ce projet.

## Documentation sur les plugins

Vous trouverez ci-dessous la documentation relative au développement et à l'extension de Kisstomato Studio :

*   [Documentation des Plugins de Type "Fields"](./docs/plugin_field.md)
*   [Documentation des Plugins de Type "Models"](./docs/plugin_model.md)

Kisstomato Studio vise à simplifier les tâches répétitives et à structurer le développement au sein de l'écosystème Kisstomato.
