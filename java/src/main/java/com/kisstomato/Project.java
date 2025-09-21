package com.kisstomato;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import java.io.File;
import java.io.IOException;

public class Project {
    private String nom;
    private String description;
    private String model;
    private String filePath;
    
    // Constructeur par défaut pour Jackson
    public Project() {
    }

    public Project(String nom, String description, String model) {
        this.nom = nom;
        this.description = description;
        this.model = model;
    }

    /**
     * Charge un projet depuis un fichier JSON
     * @param filePath le chemin vers le fichier de projet
     * @return le projet chargé ou null en cas d'erreur
     */
    public static Project loadFromFile(String filePath) {
        try {
            ObjectMapper objectMapper = new ObjectMapper();
            File file = new File(filePath);
            
            if (!file.exists()) {
                System.err.println("Le fichier de projet n'existe pas : " + filePath);
                return null;
            }
            
            JsonNode jsonNode = objectMapper.readTree(file);
            
            // Extrait les informations du projet selon le format JSON
            String nom = extractStringValue(jsonNode, "name", "nom", "project_name");
            String description = extractStringValue(jsonNode, "description", "desc");
            String model = extractStringValue(jsonNode, "model", "plugin_type", "typePlugin");
            
            // Utilise le nom du fichier si le nom n'est pas défini
            if (nom == null || nom.trim().isEmpty()) {
                nom = file.getName().replaceAll("\\.json$", "");
            }
            
            Project project = new Project(nom, description, model);
            project.setFilePath(filePath);
            
            return project;
            
        } catch (IOException e) {
            System.err.println("Erreur lors du chargement du projet depuis " + filePath + " : " + e.getMessage());
            return null;
        }
    }
    
    /**
     * Méthode utilitaire pour extraire une valeur string du JSON avec plusieurs clés possibles
     */
    private static String extractStringValue(JsonNode jsonNode, String... possibleKeys) {
        for (String key : possibleKeys) {
            if (jsonNode.has(key)) {
                JsonNode valueNode = jsonNode.get(key);
                if (!valueNode.isNull()) {
                    return valueNode.asText();
                }
            }
        }
        return "";
    }

    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public String getModel() {
        return model;
    }

    public void setModel(String model) {
        this.model = model;
    }

    public String getFilePath() {
        return filePath;
    }

    public void setFilePath(String filePath) {
        this.filePath = filePath;
    }

    @Override
    public String toString() {
        return nom;
    }
}
