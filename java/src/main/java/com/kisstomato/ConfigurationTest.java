package com.kisstomato;

/**
 * Classe utilitaire pour tester la configuration
 */
public class ConfigurationTest {
    
    public static void main(String[] args) {
        System.out.println("=== Test de la Configuration KissTomato ===");
        
        // Test 1: Configuration par défaut
        System.out.println("\n1. Test configuration par défaut:");
        ConfigurationManager configManager = ConfigurationManager.getInstance();
        configManager.initialize(null);
        
        System.out.println("Chemin de base: " + configManager.getBasePath());
        System.out.println("Fichier config: " + configManager.getConfigFilePath());
        System.out.println("Configuration chargée: " + configManager.isConfigurationLoaded());
        
        // Debug : vérifier le contenu de la configuration
        if (configManager.isConfigurationLoaded()) {
            System.out.println("Configuration JSON chargée avec succès");
            System.out.println("Contenu de la configuration:");
            System.out.println(configManager.getConfigurationContent());
        } else {
            System.out.println("ATTENTION: Configuration non chargée !");
        }
        
        // Test 2: Lecture des projets
        System.out.println("\n2. Projets configurés:");
        var projectPaths = configManager.getProjectPaths();
        for (int i = 0; i < projectPaths.size(); i++) {
            System.out.println("  " + (i + 1) + ". " + projectPaths.get(i));
        }
        
        // Test 3: Test avec fichier de configuration spécifique
        System.out.println("\n3. Test avec fichier de configuration personnalisé:");
        if (args.length >= 2 && "--config".equals(args[0])) {
            configManager.initialize(args[1]);
            System.out.println("Fichier config personnalisé: " + configManager.getConfigFilePath());
        } else {
            System.out.println("Aucun fichier de configuration personnalisé spécifié");
            System.out.println("Usage: java ConfigurationTest --config <chemin_vers_config.json>");
        }
        
        // Test 4: Ajout/suppression de projets
        System.out.println("\n4. Test ajout/suppression de projets:");
        String testProject = configManager.getBasePath() + "/test_nouveau_projet.json";
        System.out.println("Ajout du projet test: " + testProject);
        configManager.addProject(testProject);
        
        System.out.println("Projets après ajout:");
        projectPaths = configManager.getProjectPaths();
        for (int i = 0; i < projectPaths.size(); i++) {
            System.out.println("  " + (i + 1) + ". " + projectPaths.get(i));
        }
        
        System.out.println("\nSuppression du projet test");
        configManager.removeProject(testProject);
        
        System.out.println("Projets après suppression:");
        projectPaths = configManager.getProjectPaths();
        for (int i = 0; i < projectPaths.size(); i++) {
            System.out.println("  " + (i + 1) + ". " + projectPaths.get(i));
        }
        
        System.out.println("\n=== Fin du test ===");
    }
}
