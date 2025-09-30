package com.kisstomato;

import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.input.MouseEvent;
import javafx.stage.Modality;
import javafx.stage.Stage;

import java.io.File;
import java.io.IOException;
import java.net.URL;
import java.util.List;
import java.util.ResourceBundle;

public class MainController implements Initializable {

    @FXML
    private TableView<Project> tableProjects;

    @FXML
    private TableColumn<Project, String> colNom;

    @FXML
    private TableColumn<Project, String> colDescription;

    @FXML
    private TableColumn<Project, String> colTypePlugin;

    @FXML
    private Button btnReferenceProject;

    @FXML
    private Button btnCreateProject;

    private ObservableList<Project> projects;

    @Override
    public void initialize(URL location, ResourceBundle resources) {
        // Initialiser les colonnes du tableau
        colNom.setCellValueFactory(new PropertyValueFactory<>("nom"));
        colDescription.setCellValueFactory(new PropertyValueFactory<>("description"));
        colTypePlugin.setCellValueFactory(new PropertyValueFactory<>("model"));

        // Charger les projets depuis la configuration
        loadProjectsFromConfiguration();

        tableProjects.setItems(projects);

        // Gérer les clics sur le tableau
        tableProjects.setOnMouseClicked(this::handleTableClick);
    }

    /**
     * Charge les projets depuis la configuration
     */
    private void loadProjectsFromConfiguration() {
        projects = FXCollections.observableArrayList();
        
        try {
            ConfigurationManager configManager = ConfigurationManager.getInstance();
            List<String> projectPaths = configManager.getProjectPaths();
            
            for (String projectPath : projectPaths) {
                try {
                    File projectFile = new File(projectPath);
                    if (projectFile.exists()) {
                        Project project = Project.loadFromFile(projectPath);
                        if (project != null) {
                            projects.add(project);
                        }
                    }
                } catch (Exception e) {
                    System.err.println("Erreur lors du chargement du projet : " + projectPath + " - " + e.getMessage());
                }
            }
            
            // Si aucun projet n'est trouvé, ajoute des projets d'exemple
            if (projects.isEmpty()) {
                createSampleProjects();
            }
            
        } catch (Exception e) {
            System.err.println("Erreur lors du chargement des projets : " + e.getMessage());
            createSampleProjects();
        }
    }
    
    /**
     * Crée des projets d'exemple si aucun projet n'est trouvé
     */
    private void createSampleProjects() {
        projects.addAll(
            new Project("Projet Flask", "Application web avec Flask", "python_flask"),
            new Project("Projet HTML", "Site web statique", "html_maker"),
            new Project("Script Python", "Script d'automatisation", "python_script"),
            new Project("App Flask Exp", "Application Flask expérimentale", "exp_flask"),
            new Project("Modèle KissTomato", "Modèle de base KissTomato", "kisstomato_model")
        );
    }

    /**
     * Gère les clics sur le tableau des projets
     * @param event l'événement de clic
     */
    @FXML
    private void handleTableClick(MouseEvent event) {
        if (event.getClickCount() == 2) { // Double-clic
            Project selectedProject = tableProjects.getSelectionModel().getSelectedItem();
            if (selectedProject != null) {
                try {
                    App.showProjectPage(selectedProject);
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        }
    }
    
    /**
     * Recharge les projets depuis la configuration
     */
    @FXML
    private void reloadProjects() {
        ConfigurationManager.getInstance().reloadConfiguration();
        loadProjectsFromConfiguration();
        tableProjects.setItems(projects);
    }
    
    /**
     * Ouvre un dialogue pour référencer un projet existant
     */
    @FXML
    private void referenceExistingProject() {
        try {
            // Charger le fichier FXML pour la fenêtre modale
            FXMLLoader loader = new FXMLLoader(getClass().getResource("/reference_project_dialog.fxml"));
            Parent root = loader.load();
            
            // Obtenir le contrôleur de la fenêtre modale
            ReferenceProjectDialogController controller = loader.getController();
            
            // Créer la fenêtre modale
            Stage dialogStage = new Stage();
            dialogStage.setTitle("Référencer un projet existant");
            dialogStage.initModality(Modality.WINDOW_MODAL);
            dialogStage.initOwner(btnReferenceProject.getScene().getWindow());
            dialogStage.setScene(new Scene(root));
            dialogStage.setResizable(false);
            
            // Passer la référence du stage au contrôleur
            controller.setDialogStage(dialogStage);
            
            // Afficher la fenêtre modale et attendre la fermeture
            dialogStage.showAndWait();
            
            // Vérifier si l'utilisateur a validé la sélection
            if (controller.isConfirmed()) {
                String projectPath = controller.getSelectedProjectPath();
                addProjectToList(projectPath);
            }
            
        } catch (IOException e) {
            System.err.println("Erreur lors de l'ouverture de la fenêtre de référencement : " + e.getMessage());
            e.printStackTrace();
        }
    }
    
    /**
     * Ajoute un projet à la liste et à la configuration
     * @param projectPath le chemin vers le fichier de projet
     */
    private void addProjectToList(String projectPath) {
        try {
            // Charger le projet depuis le fichier
            Project project = Project.loadFromFile(projectPath);
            if (project != null) {
                // Vérifier si le projet n'est pas déjà dans la liste
                boolean projectExists = projects.stream()
                    .anyMatch(p -> projectPath.equals(p.getFilePath()));
                
                if (!projectExists) {
                    // Ajouter le projet à la liste observable
                    projects.add(project);
                    
                    // Ajouter le chemin du projet à la configuration
                    ConfigurationManager configManager = ConfigurationManager.getInstance();
                    configManager.addProject(projectPath);
                    
                    // Rafraîchir l'affichage du tableau
                    tableProjects.refresh();
                    
                    System.out.println("Projet ajouté avec succès : " + project.getNom());
                } else {
                    System.out.println("Le projet est déjà référencé dans la liste.");
                }
            } else {
                System.err.println("Impossible de charger le projet depuis : " + projectPath);
            }
        } catch (Exception e) {
            System.err.println("Erreur lors de l'ajout du projet : " + e.getMessage());
            e.printStackTrace();
        }
    }
    
    /**
     * Ouvre un dialogue pour créer un nouveau projet
     */
    @FXML
    private void createNewProject() {
        // TODO: Implémenter la logique pour créer un nouveau projet
        System.out.println("Créer un nouveau projet - À implémenter");
    }
}
