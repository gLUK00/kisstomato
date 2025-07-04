# kisstomato-class-import-start-user-code-kisstomato
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
# kisstomato-class-import-stop-user-code-kisstomato

"""
Agent IA sur les MM
"""

class iaAgentMM:
    """
    Agent IA sur les MM
    """

    # kisstomato-class-properties-start-user-code-kisstomato
    # kisstomato-class-properties-stop-user-code-kisstomato

    def __init__(self, etat_taille, actions_taille):
        # kisstomato-class-init-start-user-code-kisstomato
        
        #self.etat = 'suivre'# suivre, achete, hold
        self.etat_taille = etat_taille
        self.actions_taille = actions_taille
        self.modele = self._construire_modele()
        self.gamma = 0.99  # Facteur d'escompte
        self.epsilon = 1.0  # Taux d'exploration initial
        self.epsilon_min = 0.01
        self.epsilon_decrement = 0.996

        # kisstomato-class-init-stop-user-code-kisstomato

    """
    Construction du modèle
    """
    def _construire_modele(self):
        oResult = None

        # kisstomato-class-methode-_construire_modele-start-user-code-kisstomato
        
        # Construction d'un modèle simple pour approximer Q(s, a)
        self.modele = Sequential([
            Dense(self.etat_taille, activation='relu', input_shape=(self.etat_taille,)),
            Dense(self.etat_taille, activation='relu'),
            Dense(self.actions_taille)
        ])
        self.modele.compile(loss='mse', optimizer='adam')
        oResult = self.modele

        # kisstomato-class-methode-_construire_modele-stop-user-code-kisstomato
        return oResult

    """
    Retourne l'action en fonction de la prédiction du modèle
    """
    # Argument :
    # - etat : object : (obligatoire) Etat du modèle
    def choisir_action(self, etat):
        oResult = None

        # kisstomato-class-methode-choisir_action-start-user-code-kisstomato
        
        if np.random.rand() <= self.epsilon:
            return np.random.choice(self.actions_taille)
        # Assurer que l'état a la forme correcte (1, etat_taille) pour le modèle
        etat_reshaped = np.expand_dims(etat, axis=0) if len(etat.shape) == 1 else etat
        q_valeurs = self.modele.predict(etat_reshaped, verbose=0)
        oResult = np.argmax(q_valeurs[0])

        # kisstomato-class-methode-choisir_action-stop-user-code-kisstomato
        return oResult

    """
    Méthode d'apprentissage
    """
    # Arguments :
    # - etat : array : (obligatoire) Etat du modèle
    # - action : number : (obligatoire) Action choisie
    # - reward : number : (obligatoire) Récompense ou pénalité
    # - etat_suivant : array : (obligatoire) Etat suivant du modèle
    # - done : boolean : (obligatoire) Détermine si l'apprentissage doit être stoppé
    def apprendre(self, etat, action, reward, etat_suivant, done):
        # kisstomato-class-methode-apprendre-start-user-code-kisstomato
        
        # Assurer que les états ont la forme correcte (1, etat_taille) pour le modèle
        etat_reshaped = np.expand_dims(etat, axis=0) if len(etat.shape) == 1 else etat
        etat_suivant_reshaped = np.expand_dims(etat_suivant, axis=0) if len(etat_suivant.shape) == 1 else etat_suivant
        
        q_valeurs = self.modele.predict(etat_reshaped, verbose=0)
        q_valeurs_suivantes = self.modele.predict(etat_suivant_reshaped, verbose=0)
        if done:
            q_valeurs[0][action] = reward
        else:
            q_valeurs[0][action] = reward + self.gamma * np.max(q_valeurs_suivantes[0])
        self.modele.fit(etat_reshaped, q_valeurs, verbose=0)
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decrement

        # kisstomato-class-methode-apprendre-stop-user-code-kisstomato
    """
    Enregistrement du modèle
    """
    # Argument :
    # - file : string : (obligatoire) Nom du modèle à sauvegarder
    def save(self, file):
        # kisstomato-class-methode-save-start-user-code-kisstomato
        self.modele.save(file)
        # kisstomato-class-methode-save-stop-user-code-kisstomato
    """
    Chargement du modèle
    """
    # Argument :
    # - file : string : (obligatoire) Nom du modèle à charger
    def load(self, file):
        # kisstomato-class-methode-load-start-user-code-kisstomato
        self.modele = tf.keras.models.load_model(file)
        # kisstomato-class-methode-load-stop-user-code-kisstomato
