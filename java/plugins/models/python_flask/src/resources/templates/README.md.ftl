# ${projectName}

Application Flask créée par ${author}.

## Description

Votre nouvelle application Flask est prête à être développée !

## Installation

1. Créer un environnement virtuel :
```bash
python -m venv venv
```

2. Activer l'environnement virtuel :

**Sur Linux/Mac :**
```bash
source venv/bin/activate
```

**Sur Windows :**
```bash
venv\Scripts\activate
```

3. Installer les dépendances :
```bash
pip install -r requirements.txt
```

## Exécution

Pour démarrer l'application en mode développement :

```bash
python app.py
```

L'application sera accessible à l'adresse : http://localhost:5000

## Structure du projet

```
${packageName}/
├── app.py                 # Point d'entrée de l'application
├── config.py             # Configuration de l'application  
├── requirements.txt      # Dépendances Python
├── README.md            # Ce fichier
├── app/
│   ├── templates/       # Templates Jinja2
│   │   ├── base.html
│   │   ├── index.html
│   │   └── about.html
│   └── static/          # Fichiers statiques (CSS, JS, images)
│       ├── css/
│       └── js/
└── tests/               # Tests unitaires
```

## Développement

- Modifiez `app.py` pour ajouter de nouvelles routes
- Ajoutez vos templates HTML dans `app/templates/`
- Placez vos fichiers CSS et JavaScript dans `app/static/`
- Configurez l'application dans `config.py`

## Production

Pour déployer en production, consultez la documentation Flask :
https://flask.palletsprojects.com/en/2.3.x/deploying/
