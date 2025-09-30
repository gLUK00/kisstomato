{% extends "base.html" %}

{% block content %}
<div class="row">
    <div class="col-lg-8 mx-auto">
        <h2>À propos de ${projectName}</h2>
        
        <div class="card">
            <div class="card-body">
                <h5 class="card-title">Informations sur le projet</h5>
                
                <table class="table table-borderless">
                    <tbody>
                        <tr>
                            <th scope="row">Nom du projet :</th>
                            <td>${projectName}</td>
                        </tr>
                        <tr>
                            <th scope="row">Auteur :</th>
                            <td>${author}</td>
                        </tr>
                        <tr>
                            <th scope="row">Framework :</th>
                            <td>Flask (Python)</td>
                        </tr>
                        <tr>
                            <th scope="row">Générateur :</th>
                            <td>KissTomato Python Flask Generator</td>
                        </tr>
                    </tbody>
                </table>
                
                <hr>
                
                <h6>Technologies utilisées :</h6>
                <ul>
                    <li><strong>Flask</strong> - Framework web Python</li>
                    <li><strong>Jinja2</strong> - Moteur de templates</li>
                    <li><strong>Bootstrap 5</strong> - Framework CSS</li>
                    <li><strong>Werkzeug</strong> - Serveur WSGI</li>
                </ul>
                
                <div class="mt-4">
                    <a href="{{ url_for('index') }}" class="btn btn-secondary">← Retour à l'accueil</a>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}
