package com.kisstomato;

import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TabPane;
import javafx.scene.control.TreeView;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import java.io.File;
import java.io.IOException;

public class ProjectController {

    // Éléments du bandeau en haut
    @FXML
    private Button btnProjectProperties;

    @FXML
    private Label lblPluginType;

    @FXML
    private Label lblProjectName;

    @FXML
    private Button btnGenerateCode;

    @FXML
    private Button btnCloseProject;

    // Éléments de la section gauche
    @FXML
    private Button btnMoveDown;

    @FXML
    private Button btnMoveUp;

    @FXML
    private TreeView<String> treeViewProject;

    // Éléments de la section droite
    @FXML
    private TabPane tabPaneInfo;

    private Project project;
    private JsonNode pluginConfiguration;
    private JsonNode projectXml;

    public void setProject(Project project) {
        this.project = project;
        if (project != null) {
            lblProjectName.setText(project.getNom());
            // TODO: Récupérer le type de plugin depuis le projet
            lblPluginType.setText("Type Plugin");
        } else {
            lblProjectName.setText("Nom du Projet");
            lblPluginType.setText("Plugin Type");
        }

        // chargement du XML du plugin
        loadPluginConfiguration();

        // chargement du XML du projet
        loadProjectXml();    }

    /**
     * Charge le fichier configuration.json du plugin correspondant au modèle du projet
     */
    private void loadPluginConfiguration() {
        if (project == null || project.getModel() == null || project.getModel().trim().isEmpty()) {
            System.out.println("Aucun modèle de plugin défini pour ce projet");
            pluginConfiguration = null;
            return;
        }

        try {
            // Construction du chemin vers le fichier configuration.json du plugin
            String pluginPath = ConfigurationManager.getInstance().getBasePath() + "/plugins/models/" + project.getModel() + "/configuration.json";
            File configFile = new File(pluginPath);
            
            if (!configFile.exists()) {
                System.err.println("Fichier de configuration du plugin introuvable : " + pluginPath);
                pluginConfiguration = null;
                return;
            }

            // Chargement et parsing du fichier JSON
            ObjectMapper objectMapper = new ObjectMapper();
            pluginConfiguration = objectMapper.readTree(configFile);
            
            System.out.println("Configuration du plugin '" + project.getModel() + "' chargée avec succès");
            
        } catch (IOException e) {
            System.err.println("Erreur lors du chargement de la configuration du plugin : " + e.getMessage());
            pluginConfiguration = null;
        }
    }

    /**
     * Charge le fichier XML du projet à partir de la propriété filePath
     */
    private void loadProjectXml() {
        if (project == null || project.getFilePath() == null || project.getFilePath().trim().isEmpty()) {
            System.out.println("Aucun chemin de fichier défini pour ce projet");
            projectXml = null;
            return;
        }

        try {
            File projectFile = new File(project.getFilePath());
            
            if (!projectFile.exists()) {
                System.err.println("Fichier de projet introuvable : " + project.getFilePath());
                projectXml = null;
                return;
            }

            // Chargement et parsing du fichier XML/JSON
            ObjectMapper objectMapper = new ObjectMapper();
            projectXml = objectMapper.readTree(projectFile);
            
            System.out.println("Données du projet '" + project.getNom() + "' chargées avec succès depuis " + project.getFilePath());
            
        } catch (IOException e) {
            System.err.println("Erreur lors du chargement du fichier de projet : " + e.getMessage());
            projectXml = null;
        }
    }

    /**
     * Retourne la configuration du plugin chargée
     * @return la configuration du plugin ou null si non chargée
     */
    public JsonNode getPluginConfiguration() {
        return pluginConfiguration;
    }

    /**
     * Retourne les données XML/JSON du projet chargées
     * @return les données du projet ou null si non chargées
     */
    public JsonNode getProjectXml() {
        return projectXml;
    }

    @FXML
    private void handleRetour() {
        try {
            App.showMainPage();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    // Méthodes pour les futurs développements (boutons actuellement sans action)
    
    @FXML
    private void handleProjectProperties() {
        // À implémenter plus tard
        System.out.println("Propriétés du projet - À implémenter");
    }

    @FXML
    private void handleGenerateCode() {
        // À implémenter plus tard
        System.out.println("Générer le code - À implémenter");
    }

    @FXML
    private void handleMoveDown() {
        // À implémenter plus tard
        System.out.println("Déplacer vers le bas - À implémenter");
    }

    @FXML
    private void handleMoveUp() {
        // À implémenter plus tard
        System.out.println("Déplacer vers le haut - À implémenter");
    }
}