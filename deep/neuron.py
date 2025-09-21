import numpy as np

class Neurone:
    def __init__(self, nombre_entrees):
        # Initialisation aléatoire des poids entre -1 et 1
        self.poids = np.random.uniform(-1, 1, nombre_entrees)
        # Initialisation du biais à 0
        self.biais = 0
        
    def fonction_activation(self, x):
        # Fonction d'activation sigmoid : transforme toute entrée en valeur entre 0 et 1
        return 1 / (1 + np.exp(-x))
    
    def forward(self, entrees):
        # Vérifie que le nombre d'entrées correspond au nombre de poids
        if len(entrees) != len(self.poids):
            raise ValueError(f"Attendu {len(self.poids)} entrées, reçu {len(entrees)}")
        
        # Calcul de la somme pondérée : Σ(entrées * poids) + biais
        somme_ponderee = np.dot(entrees, self.poids) + self.biais
        
        # Application de la fonction d'activation
        sortie = self.fonction_activation(somme_ponderee)
        return sortie

# Exemple d'utilisation
if __name__ == "__main__":
    # Créons un neurone avec 2 entrées
    neurone = Neurone(nombre_entrees=2)
    
    # Testons-le avec quelques entrées
    entree_test = np.array([0.5, 0.8])
    resultat = neurone.forward(entree_test)
    print(f"Poids du neurone : {neurone.poids}")
    print(f"Biais du neurone : {neurone.biais}")
    print(f"Pour les entrées {entree_test}, la sortie est : {resultat}")