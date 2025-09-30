package org.kisstomato.plugins.models.python_flask;

import freemarker.template.Configuration;
import freemarker.template.Template;
import freemarker.template.TemplateException;

import java.io.*;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.HashMap;
import java.util.Map;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;

/**
 * Classe pour créer un nouveau projet Python Flask
 */
public class CreateNewProject {
    
    public static void execute(String jsonData) throws Exception {
        System.out.println("Création d'un nouveau projet Python Flask...");
        
        // Parse JSON data
        ObjectMapper mapper = new ObjectMapper();
        JsonNode projectData = mapper.readTree(jsonData);
        
        String projectName = projectData.get("projectName").asText();
        String author = projectData.get("author").asText();
        
        if (projectName == null || projectName.trim().isEmpty()) {
            throw new IllegalArgumentException("Le nom du projet ne peut pas être vide");
        }
        
        System.out.println("Nom du projet: " + projectName);
        System.out.println("Auteur: " + author);
        
        // Créer le répertoire du projet
        Path projectPath = Paths.get(projectName);
        if (Files.exists(projectPath)) {
            throw new IllegalArgumentException("Le répertoire '" + projectName + "' existe déjà");
        }
        
        Files.createDirectories(projectPath);
        
        // Préparer les données pour les templates
        Map<String, Object> templateData = new HashMap<>();
        templateData.put("projectName", projectName);
        templateData.put("author", author);
        templateData.put("packageName", projectName.toLowerCase().replaceAll("[^a-z0-9]", "_"));
        
        // Configuration Freemarker
        Configuration cfg = new Configuration(Configuration.VERSION_2_3_31);
        cfg.setDefaultEncoding("UTF-8");
        
        // Pour le moment, générer les fichiers sans templates Freemarker
        // (les templates sont intégrés dans les méthodes Java)
        generateProjectStructure(projectPath, cfg, templateData);
        
        System.out.println("Projet '" + projectName + "' créé avec succès dans le répertoire: " + projectPath.toAbsolutePath());
    }
    
    private static String getTemplatesPath() {
        // Récupérer le chemin du JAR ou du répertoire de classes
        String jarPath = CreateNewProject.class.getProtectionDomain()
            .getCodeSource().getLocation().getPath();
        
        File jarFile = new File(jarPath);
        if (jarFile.isDirectory()) {
            // Mode développement
            return jarFile.getParent() + "/src/resources/templates";
        } else {
            // Mode JAR - extraire les templates dans un répertoire temporaire
            return extractTemplatesFromJar();
        }
    }
    
    private static String extractTemplatesFromJar() {
        // Pour l'instant, retourner un chemin par défaut
        // Dans une implémentation complète, il faudrait extraire les templates du JAR
        return "templates";
    }
    
    private static void generateProjectStructure(Path projectPath, Configuration cfg, Map<String, Object> data) 
            throws IOException, TemplateException {
        
        // Créer les répertoires de base
        Files.createDirectories(projectPath.resolve("app"));
        Files.createDirectories(projectPath.resolve("app/templates"));
        Files.createDirectories(projectPath.resolve("app/static/css"));
        Files.createDirectories(projectPath.resolve("app/static/js"));
        Files.createDirectories(projectPath.resolve("tests"));
        
        // Générer app.py
        generateFileFromTemplate(cfg, "app.py.ftl", projectPath.resolve("app.py"), data);
        
        // Générer requirements.txt
        generateFileFromTemplate(cfg, "requirements.txt.ftl", projectPath.resolve("requirements.txt"), data);
        
        // Générer README.md
        generateFileFromTemplate(cfg, "README.md.ftl", projectPath.resolve("README.md"), data);
        
        // Générer config.py
        generateFileFromTemplate(cfg, "config.py.ftl", projectPath.resolve("config.py"), data);
        
        // Générer template HTML de base
        generateFileFromTemplate(cfg, "base.html.ftl", projectPath.resolve("app/templates/base.html"), data);
        
        // Générer index.html
        generateFileFromTemplate(cfg, "index.html.ftl", projectPath.resolve("app/templates/index.html"), data);
    }
    
    private static void generateFileFromTemplate(Configuration cfg, String templateName, 
            Path outputPath, Map<String, Object> data) throws IOException, TemplateException {
        
        // Pour l'instant, créer directement les fichiers basiques
        // Plus tard, on pourrait utiliser les templates du JAR
        System.out.println("Génération: " + outputPath.getFileName());
        createBasicFile(outputPath, templateName, data);
    }
    
    private static void createBasicFile(Path outputPath, String templateName, Map<String, Object> data) throws IOException {
        String content = "";
        String projectName = (String) data.get("projectName");
        String author = (String) data.get("author");
        
        switch (templateName) {
            case "app.py.ftl":
                content = "from flask import Flask, render_template\n\n" +
                         "app = Flask(__name__)\n\n" +
                         "@app.route('/')\n" +
                         "def index():\n" +
                         "    return render_template('index.html', title='" + projectName + "')\n\n" +
                         "if __name__ == '__main__':\n" +
                         "    app.run(debug=True)\n";
                break;
                
            case "requirements.txt.ftl":
                content = "Flask==2.3.3\n" +
                         "Werkzeug==2.3.7\n";
                break;
                
            case "README.md.ftl":
                content = "# " + projectName + "\n\n" +
                         "Projet Python Flask créé par " + author + "\n\n" +
                         "## Installation\n\n" +
                         "```bash\n" +
                         "pip install -r requirements.txt\n" +
                         "```\n\n" +
                         "## Exécution\n\n" +
                         "```bash\n" +
                         "python app.py\n" +
                         "```\n";
                break;
                
            case "config.py.ftl":
                content = "import os\n\n" +
                         "class Config:\n" +
                         "    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'\n" +
                         "    DEBUG = True\n";
                break;
                
            case "base.html.ftl":
                content = "<!DOCTYPE html>\n" +
                         "<html lang=\"fr\">\n" +
                         "<head>\n" +
                         "    <meta charset=\"UTF-8\">\n" +
                         "    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n" +
                         "    <title>{% block title %}{{ title }}{% endblock %}</title>\n" +
                         "</head>\n" +
                         "<body>\n" +
                         "    <header>\n" +
                         "        <h1>" + projectName + "</h1>\n" +
                         "    </header>\n" +
                         "    <main>\n" +
                         "        {% block content %}{% endblock %}\n" +
                         "    </main>\n" +
                         "</body>\n" +
                         "</html>\n";
                break;
                
            case "index.html.ftl":
                content = "{% extends \"base.html\" %}\n\n" +
                         "{% block content %}\n" +
                         "<h2>Bienvenue dans " + projectName + "</h2>\n" +
                         "<p>Votre application Flask est prête !</p>\n" +
                         "{% endblock %}\n";
                break;
        }
        
        Files.write(outputPath, content.getBytes());
    }
}
