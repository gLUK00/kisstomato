package com.kisstomato;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

public class App extends Application {
    
    private static Stage primaryStage;
    private static String[] applicationArgs;

    @Override
    public void start(Stage stage) throws Exception {
        primaryStage = stage;
        primaryStage.setTitle("KissTomato - Gestionnaire de Projets");
        
        // Initialise la configuration avec les paramètres de ligne de commande
        String configPath = ConfigurationManager.parseConfigArgument(applicationArgs);
        ConfigurationManager.getInstance().initialize(configPath);
        
        showMainPage();
        primaryStage.show();
    }

    public static void showMainPage() throws Exception {
        FXMLLoader loader = new FXMLLoader(App.class.getResource("/main.fxml"));
        Parent root = loader.load();
        Scene scene = new Scene(root, 800, 600);
        primaryStage.setScene(scene);
    }

    public static void showProjectPage(Project project) throws Exception {
        FXMLLoader loader = new FXMLLoader(App.class.getResource("/project.fxml"));
        Parent root = loader.load();
        ProjectController controller = loader.getController();
        controller.setProject(project);
        Scene scene = new Scene(root, 800, 600);
        primaryStage.setScene(scene);
    }

    public static void main(String[] args) {
        applicationArgs = args;
        launch(args);
    }
}
