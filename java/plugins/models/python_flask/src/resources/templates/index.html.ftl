{% extends "base.html" %}

{% block content %}
<div class="row">
    <div class="col-lg-8 mx-auto">
        <div class="text-center">
            <h1 class="display-4">Bienvenue dans ${projectName}</h1>
            <p class="lead">Votre application Flask est prête à être développée !</p>
        </div>
        
        <div class="card mt-4">
            <div class="card-body">
                <h5 class="card-title">🚀 Démarrage rapide</h5>
                <p class="card-text">
                    Votre application Flask a été générée avec succès. 
                    Vous pouvez maintenant commencer à développer vos fonctionnalités.
                </p>
                
                <h6 class="mt-3">Prochaines étapes :</h6>
                <ul>
                    <li>Modifiez <code>app.py</code> pour ajouter de nouvelles routes</li>
                    <li>Personnalisez les templates dans <code>app/templates/</code></li>
                    <li>Ajoutez vos styles CSS dans <code>app/static/css/</code></li>
                    <li>Configurez votre application dans <code>config.py</code></li>
                </ul>
                
                <a href="{{ url_for('about') }}" class="btn btn-primary">En savoir plus</a>
            </div>
        </div>
    </div>
</div>
{% endblock %}
