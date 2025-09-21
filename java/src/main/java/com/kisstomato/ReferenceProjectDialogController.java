package com.kisstomato;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.stage.FileChooser;
import javafx.stage.Stage;

import java.io.File;
import java.io.IOException;

public class ReferenceProjectDialogController {
    
    @FXML
    private TextField txtFilePath;
    
    @FXML
    private Button btnBrowse;
    
    @FXML
    private Button btnValidate;
    
    @FXML
    private Button btnCancel;
    
    @FXML
    private Label lblError;
    
    private Stage dialogStage;
    private boolean confirmed = false;
    private String selectedProjectPath = null;
    
    public void setDialogStage(Stage dialogStage) {
        this.dialogStage = dialogStage;
    }
    
    public boolean isConfirmed() {
        return confirmed;
    }
    
    public String getSelectedProjectPath() {
        return selectedProjectPath;
    }
    
    @FXML
    private void browseForFile() {
        FileChooser fileChooser = new FileChooser();
        fileChooser.setTitle("Sélectionner le fichier de configuration du projet");
        
        // Configurer les filtres de fichiers
        FileChooser.ExtensionFilter jsonFilter = new FileChooser.ExtensionFilter("Fichiers JSON (*.json)", "*.json");
        fileChooser.getExtensionFilters().add(jsonFilter);
        
        // Définir le répertoire initial si possible
        String currentPath = txtFilePath.getText().trim();
        if (!currentPath.isEmpty()) {
            File currentFile = new File(currentPath);
            if (currentFile.getParent() != null) {
                File parentDir = new File(currentFile.getParent());
                if (parentDir.exists() && parentDir.isDirectory()) {
                    fileChooser.setInitialDirectory(parentDir);
                }
            }
        }
        
        File selectedFile = fileChooser.showOpenDialog(dialogStage);
        if (selectedFile != null) {
            txtFilePath.setText(selectedFile.getAbsolutePath());
        }
        
        // Masquer le message d'erreur lors de la sélection d'un nouveau fichier
        hideError();
    }
    
    @FXML
    private void validateProject() {
        String filePath = txtFilePath.getText().trim();
        
        if (filePath.isEmpty()) {
            showError("Veuillez sélectionner un fichier de configuration.");
            return;
        }
        
        File file = new File(filePath);
        if (!file.exists()) {
            showError("Le fichier spécifié n'existe pas.");
            return;
        }
        
        if (!file.isFile()) {
            showError("Le chemin spécifié ne pointe pas vers un fichier.");
            return;
        }
        
        if (!file.getName().toLowerCase().endsWith(".json")) {
            showError("Le fichier doit être au format JSON (.json).");
            return;
        }
        
        // Valider le contenu JSON
        if (!validateJsonContent(file)) {
            return; // Le message d'erreur est déjà affiché par validateJsonContent
        }
        
        // Si tout est valide
        selectedProjectPath = filePath;
        confirmed = true;
        dialogStage.close();
    }
    
    @FXML
    private void cancelDialog() {
        confirmed = false;
        dialogStage.close();
    }
    
    private boolean validateJsonContent(File file) {
        try {
            ObjectMapper objectMapper = new ObjectMapper();
            JsonNode jsonNode = objectMapper.readTree(file);
            
            // Vérifier que c'est un objet JSON valide
            if (!jsonNode.isObject()) {
                showError("Le fichier JSON doit contenir un objet.");
                return false;
            }
            
            // Liste des champs requis avec leurs alternatives possibles
            String[] nameFields = {"name", "nom", "project_name"};
            String[] descriptionFields = {"description", "desc"};
            String[] modelFields = {"model", "type", "plugin_type", "typePlugin"};
            String[] versionFields = {"version"};
            String[] authorFields = {"author", "auteur"};
            
            // Vérifier la présence des champs requis
            if (!hasAnyField(jsonNode, nameFields)) {
                showError("Le fichier JSON doit contenir un champ 'name' (ou équivalent).");
                return false;
            }
            
            if (!hasAnyField(jsonNode, descriptionFields)) {
                showError("Le fichier JSON doit contenir un champ 'description' (ou équivalent).");
                return false;
            }
            
            if (!hasAnyField(jsonNode, modelFields)) {
                showError("Le fichier JSON doit contenir un champ 'model' (ou équivalent).");
                return false;
            }
            
            if (!hasAnyField(jsonNode, versionFields)) {
                showError("Le fichier JSON doit contenir un champ 'version'.");
                return false;
            }
            
            if (!hasAnyField(jsonNode, authorFields)) {
                showError("Le fichier JSON doit contenir un champ 'author' (ou équivalent).");
                return false;
            }
            
            return true;
            
        } catch (IOException e) {
            showError("Erreur lors de la lecture du fichier JSON : " + e.getMessage());
            return false;
        } catch (Exception e) {
            showError("Format JSON invalide : " + e.getMessage());
            return false;
        }
    }
    
    private boolean hasAnyField(JsonNode jsonNode, String[] fieldNames) {
        for (String fieldName : fieldNames) {
            if (jsonNode.has(fieldName) && !jsonNode.get(fieldName).isNull()) {
                String value = jsonNode.get(fieldName).asText().trim();
                if (!value.isEmpty()) {
                    return true;
                }
            }
        }
        return false;
    }
    
    private void showError(String message) {
        lblError.setText(message);
        lblError.setVisible(true);
    }
    
    private void hideError() {
        lblError.setVisible(false);
        lblError.setText("");
    }
}
