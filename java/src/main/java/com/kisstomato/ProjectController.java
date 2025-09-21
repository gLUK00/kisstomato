package com.kisstomato;

import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.Label;

public class ProjectController {

    @FXML
    private Label lblMessage;

    @FXML
    private Button btnRetour;

    private Project project;

    public void setProject(Project project) {
        this.project = project;
        if (project != null) {
            lblMessage.setText("Bienvenue sur le projet : " + project.getNom());
        } else {
            lblMessage.setText("Bienvenue sur le projet");
        }
    }

    @FXML
    private void handleRetour() {
        try {
            App.showMainPage();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
