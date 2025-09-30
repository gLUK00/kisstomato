package org.kisstomato.plugins.models.python_flask;

import java.util.Arrays;

/**
 * Classe principale pour le générateur de projets Python Flask
 */
public class Main {
    
    private static final int SUCCESS = 0;
    private static final int PARSING_ERROR = 1;
    
    public static void main(String[] args) {
        try {
            if (args.length == 0) {
                showUsage();
                System.exit(PARSING_ERROR);
            }
            
            String action = null;
            String data = null;
            String file = null;
            
            // Parse arguments
            for (String arg : args) {
                if (arg.startsWith("--action=")) {
                    action = arg.substring("--action=".length());
                } else if (arg.startsWith("--data=")) {
                    data = arg.substring("--data=".length());
                } else if (arg.startsWith("--file=")) {
                    file = arg.substring("--file=".length());
                }
            }
            
            if (action == null) {
                System.err.println("Erreur: L'argument --action est requis");
                showUsage();
                System.exit(PARSING_ERROR);
            }
            
            switch (action) {
                case "create":
                    if (data == null) {
                        System.err.println("Erreur: L'argument --data est requis pour l'action 'create'");
                        showUsage();
                        System.exit(PARSING_ERROR);
                    }
                    CreateNewProject.execute(data);
                    break;
                    
                case "open":
                    if (file == null) {
                        System.err.println("Erreur: L'argument --file est requis pour l'action 'open'");
                        showUsage();
                        System.exit(PARSING_ERROR);
                    }
                    OpenProject.execute(file);
                    break;
                    
                default:
                    System.err.println("Erreur: Action inconnue '" + action + "'");
                    showUsage();
                    System.exit(PARSING_ERROR);
            }
            
            System.exit(SUCCESS);
            
        } catch (Exception e) {
            System.err.println("Erreur: " + e.getMessage());
            e.printStackTrace();
            System.exit(PARSING_ERROR);
        }
    }
    
    private static void showUsage() {
        System.out.println("Usage:");
        System.out.println("  java -jar python-flask-generator-cli.jar --action=create --data='{\"projectName\":\"MyFlaskApp\", \"author\":\"John Doe\"}'");
        System.out.println("  java -jar python-flask-generator-cli.jar --action=open --file='/path/to/project.xml'");
        System.out.println();
        System.out.println("Actions disponibles:");
        System.out.println("  create : Créer un nouveau projet Flask");
        System.out.println("  open   : Ouvrir un projet existant");
        System.out.println();
        System.out.println("Codes de retour:");
        System.out.println("  0 : Succès");
        System.out.println("  1 : Erreur de parsing des arguments");
    }
}
