package org.kisstomato.plugins.models.python_flask;

import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.NodeList;

/**
 * Classe pour ouvrir un projet Python Flask existant
 */
public class OpenProject {
    
    public static void execute(String filePath) throws Exception {
        System.out.println("Ouverture du projet Python Flask: " + filePath);
        
        Path projectFile = Paths.get(filePath);
        
        // Vérifier que le fichier existe
        if (!Files.exists(projectFile)) {
            throw new IllegalArgumentException("Le fichier projet n'existe pas: " + filePath);
        }
        
        // Vérifier que c'est bien un fichier XML
        if (!filePath.toLowerCase().endsWith(".xml")) {
            throw new IllegalArgumentException("Le fichier projet doit avoir l'extension .xml");
        }
        
        // Parser le fichier XML du projet
        ProjectInfo projectInfo = parseProjectFile(projectFile.toFile());
        
        System.out.println("Projet chargé:");
        System.out.println("  Nom: " + projectInfo.getName());
        System.out.println("  Auteur: " + projectInfo.getAuthor());
        System.out.println("  Répertoire: " + projectInfo.getPath());
        System.out.println("  Version: " + projectInfo.getVersion());
        
        // Vérifier que le répertoire du projet existe
        Path projectPath = Paths.get(projectInfo.getPath());
        if (!Files.exists(projectPath)) {
            throw new IllegalArgumentException("Le répertoire du projet n'existe pas: " + projectInfo.getPath());
        }
        
        // Vérifier la structure du projet Flask
        validateFlaskProject(projectPath);
        
        System.out.println("Projet Python Flask ouvert avec succès !");
    }
    
    private static ProjectInfo parseProjectFile(File projectFile) throws Exception {
        DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
        DocumentBuilder builder = factory.newDocumentBuilder();
        Document document = builder.parse(projectFile);
        
        Element root = document.getDocumentElement();
        
        ProjectInfo info = new ProjectInfo();
        
        // Extraire les informations du projet
        info.setName(getElementText(root, "name"));
        info.setAuthor(getElementText(root, "author"));
        info.setPath(getElementText(root, "path"));
        info.setVersion(getElementText(root, "version"));
        info.setDescription(getElementText(root, "description"));
        
        // Valider les champs requis
        if (info.getName() == null || info.getName().trim().isEmpty()) {
            throw new IllegalArgumentException("Le nom du projet est requis dans le fichier XML");
        }
        
        if (info.getPath() == null || info.getPath().trim().isEmpty()) {
            throw new IllegalArgumentException("Le chemin du projet est requis dans le fichier XML");
        }
        
        return info;
    }
    
    private static String getElementText(Element parent, String tagName) {
        NodeList nodeList = parent.getElementsByTagName(tagName);
        if (nodeList.getLength() > 0) {
            return nodeList.item(0).getTextContent();
        }
        return null;
    }
    
    private static void validateFlaskProject(Path projectPath) throws Exception {
        System.out.println("Validation de la structure du projet Flask...");
        
        // Vérifier les fichiers/répertoires essentiels
        boolean hasAppPy = Files.exists(projectPath.resolve("app.py"));
        boolean hasRequirements = Files.exists(projectPath.resolve("requirements.txt"));
        boolean hasAppDir = Files.exists(projectPath.resolve("app")) && Files.isDirectory(projectPath.resolve("app"));
        
        if (!hasAppPy) {
            System.out.println("Attention: fichier app.py manquant");
        }
        
        if (!hasRequirements) {
            System.out.println("Attention: fichier requirements.txt manquant");
        }
        
        if (!hasAppDir) {
            System.out.println("Attention: répertoire app/ manquant");
        } else {
            // Vérifier la structure dans app/
            boolean hasTemplates = Files.exists(projectPath.resolve("app/templates")) 
                && Files.isDirectory(projectPath.resolve("app/templates"));
            boolean hasStatic = Files.exists(projectPath.resolve("app/static")) 
                && Files.isDirectory(projectPath.resolve("app/static"));
                
            if (!hasTemplates) {
                System.out.println("Attention: répertoire app/templates/ manquant");
            }
            
            if (!hasStatic) {
                System.out.println("Attention: répertoire app/static/ manquant");
            }
        }
        
        if (hasAppPy && hasRequirements) {
            System.out.println("Structure du projet Flask validée !");
        } else {
            System.out.println("La structure du projet Flask semble incomplète mais le projet peut être ouvert.");
        }
    }
    
    /**
     * Classe pour stocker les informations du projet
     */
    private static class ProjectInfo {
        private String name;
        private String author;
        private String path;
        private String version;
        private String description;
        
        public String getName() { return name; }
        public void setName(String name) { this.name = name; }
        
        public String getAuthor() { return author; }
        public void setAuthor(String author) { this.author = author; }
        
        public String getPath() { return path; }
        public void setPath(String path) { this.path = path; }
        
        public String getVersion() { return version; }
        public void setVersion(String version) { this.version = version; }
        
        public String getDescription() { return description; }
        public void setDescription(String description) { this.description = description; }
    }
}
