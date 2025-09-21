package com.kisstomato;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ArrayNode;
import com.fasterxml.jackson.databind.node.ObjectNode;
import javafx.scene.control.Alert;
import javafx.scene.control.ButtonType;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

/**
 * Classe singleton pour gérer la configuration de l'application KissTomato.
 * Cette classe permet de charger, manipuler et sauvegarder la configuration
 * depuis/vers un fichier JSON.
 */
public class ConfigurationManager {
    
    private static ConfigurationManager instance;
    private static final String DEFAULT_CONFIG_FILE = "configuration.json";
    
    private String configFilePath;
    private String basePath;
    private JsonNode configuration;
    private ObjectMapper objectMapper;
    
    /**
     * Constructeur privé pour le pattern singleton
     */
    private ConfigurationManager() {
        this.objectMapper = new ObjectMapper();
        this.configFilePath = DEFAULT_CONFIG_FILE;
    }
    
    /**
     * Obtient l'instance unique du ConfigurationManager
     * @return l'instance singleton
     */
    public static synchronized ConfigurationManager getInstance() {
        if (instance == null) {
            instance = new ConfigurationManager();
        }
        return instance;
    }
    
    /**
     * Initialise la configuration avec le chemin du fichier spécifié
     * @param configFilePath le chemin vers le fichier de configuration (peut être null pour utiliser le défaut)
     */
    public void initialize(String configFilePath) {
        if (configFilePath != null && !configFilePath.trim().isEmpty()) {
            this.configFilePath = configFilePath;
        }
        
        // Détermine le chemin de base
        determineBasePath();
        
        // Charge la configuration
        loadConfiguration();
    }
    
    /**
     * Détermine le chemin de base de l'application
     */
    private void determineBasePath() {
        try {
            // Obtient le chemin du JAR ou du répertoire de classes
            String jarPath = ConfigurationManager.class.getProtectionDomain()
                    .getCodeSource().getLocation().toURI().getPath();
            
            File jarFile = new File(jarPath);
            if (jarFile.isFile()) {
                // Si c'est un JAR, prend le répertoire parent
                this.basePath = jarFile.getParent();
            } else {
                // Si c'est un répertoire (mode développement), remonte au répertoire racine du projet
                this.basePath = Paths.get(jarPath).getParent().getParent().toString();
            }
        } catch (Exception e) {
            // En cas d'erreur, utilise le répertoire courant
            this.basePath = System.getProperty("user.dir");
        }
    }
    
    /**
     * Charge la configuration depuis le fichier JSON
     */
    public void loadConfiguration() {
        try {
            Path configPath = Paths.get(configFilePath);
            
            // Si le chemin n'est pas absolu, le considère comme relatif au basePath
            if (!configPath.isAbsolute()) {
                configPath = Paths.get(basePath, configFilePath);
            }
            
            if (Files.exists(configPath)) {
                String jsonContent = Files.readString(configPath);
                this.configuration = objectMapper.readTree(jsonContent);
            } else {
                // Crée une configuration par défaut si le fichier n'existe pas
                createDefaultConfiguration();
                saveConfiguration();
            }
        } catch (Exception e) {
            showErrorDialog("Erreur de chargement de la configuration", 
                    "Impossible de charger le fichier de configuration : " + configFilePath + 
                    "\nErreur : " + e.getMessage());
            createDefaultConfiguration();
        }
    }
    
    /**
     * Recharge la configuration depuis le fichier
     */
    public void reloadConfiguration() {
        loadConfiguration();
    }
    
    /**
     * Crée une configuration par défaut
     */
    private void createDefaultConfiguration() {
        ObjectNode defaultConfig = objectMapper.createObjectNode();
        ArrayNode projectsArray = objectMapper.createArrayNode();
        defaultConfig.set("projects", projectsArray);
        this.configuration = defaultConfig;
    }
    
    /**
     * Sauvegarde la configuration dans le fichier JSON
     */
    private void saveConfiguration() {
        try {
            Path configPath = Paths.get(configFilePath);
            if (!configPath.isAbsolute()) {
                configPath = Paths.get(basePath, configFilePath);
            }
            
            // Crée les répertoires parents si nécessaire
            Files.createDirectories(configPath.getParent());
            
            // Écrit la configuration formatée
            String jsonString = objectMapper.writerWithDefaultPrettyPrinter()
                    .writeValueAsString(configuration);
            Files.writeString(configPath, jsonString);
            
        } catch (IOException e) {
            showErrorDialog("Erreur de sauvegarde", 
                    "Impossible de sauvegarder la configuration : " + e.getMessage());
        }
    }
    
    /**
     * Obtient la liste des projets depuis la configuration
     * @return la liste des chemins des fichiers de projets
     */
    public List<String> getProjectPaths() {
        List<String> projectPaths = new ArrayList<>();
        
        if (configuration != null && configuration.has("projects")) {
            JsonNode projectsNode = configuration.get("projects");
            if (projectsNode.isArray()) {
                for (JsonNode projectNode : projectsNode) {
                    String projectPath = projectNode.asText();
                    // Remplace {path_base} par le chemin de base réel
                    projectPath = projectPath.replace("{path_base}", basePath);
                    projectPaths.add(projectPath);
                }
            }
        }
        
        return projectPaths;
    }
    
    /**
     * Ajoute un projet à la configuration
     * @param projectPath le chemin du fichier de projet à ajouter
     */
    public void addProject(String projectPath) {
        if (configuration != null) {
            // Remplace le chemin de base par {path_base} pour la portabilité
            String relativePath = projectPath.replace(basePath, "{path_base}");
            
            ArrayNode projectsArray;
            if (configuration.has("projects")) {
                projectsArray = (ArrayNode) configuration.get("projects");
            } else {
                projectsArray = objectMapper.createArrayNode();
                ((ObjectNode) configuration).set("projects", projectsArray);
            }
            
            // Vérifie si le projet n'existe pas déjà
            boolean exists = false;
            for (JsonNode projectNode : projectsArray) {
                if (projectNode.asText().equals(relativePath)) {
                    exists = true;
                    break;
                }
            }
            
            if (!exists) {
                projectsArray.add(relativePath);
                saveConfiguration();
            }
        }
    }
    
    /**
     * Supprime un projet de la configuration
     * @param projectPath le chemin du fichier de projet à supprimer
     */
    public void removeProject(String projectPath) {
        if (configuration != null && configuration.has("projects")) {
            String relativePath = projectPath.replace(basePath, "{path_base}");
            ArrayNode projectsArray = (ArrayNode) configuration.get("projects");
            
            // Cherche et supprime le projet
            for (int i = 0; i < projectsArray.size(); i++) {
                if (projectsArray.get(i).asText().equals(relativePath)) {
                    projectsArray.remove(i);
                    saveConfiguration();
                    break;
                }
            }
        }
    }
    
    /**
     * Obtient le chemin de base de l'application
     * @return le chemin de base
     */
    public String getBasePath() {
        return basePath;
    }
    
    /**
     * Obtient le chemin du fichier de configuration
     * @return le chemin du fichier de configuration
     */
    public String getConfigFilePath() {
        return configFilePath;
    }
    
    /**
     * Vérifie si la configuration est chargée et valide
     * @return true si la configuration est disponible
     */
    public boolean isConfigurationLoaded() {
        return configuration != null;
    }
    
    /**
     * Retourne le contenu brut de la configuration pour débogage
     * @return le contenu JSON sous forme de chaîne
     */
    public String getConfigurationContent() {
        if (configuration != null) {
            try {
                return objectMapper.writerWithDefaultPrettyPrinter()
                        .writeValueAsString(configuration);
            } catch (Exception e) {
                return "Erreur lors de la sérialisation : " + e.getMessage();
            }
        }
        return "Configuration non chargée";
    }
    
    /**
     * Affiche une boîte de dialogue d'erreur
     * @param title le titre de la boîte de dialogue
     * @param message le message d'erreur
     */
    private void showErrorDialog(String title, String message) {
        Alert alert = new Alert(Alert.AlertType.ERROR);
        alert.setTitle(title);
        alert.setHeaderText("Erreur de Configuration");
        alert.setContentText(message);
        
        // Affiche la boîte de dialogue et attend que l'utilisateur la ferme
        Optional<ButtonType> result = alert.showAndWait();
    }
    
    /**
     * Obtient la configuration complète en tant que JsonNode
     * @return la configuration JSON
     */
    public JsonNode getConfiguration() {
        return configuration;
    }
    
    /**
     * Analyse les arguments de ligne de commande pour extraire le chemin de configuration
     * @param args les arguments de ligne de commande
     * @return le chemin du fichier de configuration ou null si non spécifié
     */
    public static String parseConfigArgument(String[] args) {
        for (int i = 0; i < args.length - 1; i++) {
            if ("--config".equals(args[i])) {
                return args[i + 1];
            }
        }
        return null;
    }
}
