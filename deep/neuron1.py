import numpy as np

class NeuroneSimple:
    def __init__(self):
        # On commence avec des poids et un biais simples
        self.poids = np.array([0.5, 0.5])  # Poids identiques au départ
        self.biais = 0
        
    def predire(self, entrees):
        # Calcul simplifié
        somme = np.dot(entrees, self.poids) + self.biais
        return 1 / (1 + np.exp(-somme))  # Sigmoid
        
    def apprendre(self, entrees, sortie_attendue):
        # Prédiction actuelle
        sortie = self.predire(entrees)
        # Calcul de l'erreur
        erreur = sortie_attendue - sortie
        # Ajustement simple des poids et du biais
        self.poids += 0.1 * erreur * entrees
        self.biais += 0.1 * erreur
        return erreur

# Création du neurone
neurone = NeuroneSimple()

# Données pour la fonction ET logique
donnees = [
    ([0, 0], 0),  # 0 ET 0 = 0
    ([0, 1], 0),  # 0 ET 1 = 0
    ([1, 0], 0),  # 1 ET 0 = 0
    ([1, 1], 1)   # 1 ET 1 = 1
]

print("=== DÉBUT DE L'APPRENTISSAGE ===")
print("\nÉtat initial:")
for entrees, attendu in donnees:
    prediction = neurone.predire(np.array(entrees))
    print(f"Entrées {entrees}: prédit {prediction:.3f}, devrait être {attendu}")
print(f"Poids initiaux: {neurone.poids}, Biais: {neurone.biais:.3f}")

# Apprentissage sur 5 étapes clés
for etape in [1, 10, 50, 100, 500]:
    # Entraînement jusqu'à cette étape
    for _ in range(etape - 1):
        for entrees, attendu in donnees:
            neurone.apprendre(np.array(entrees), attendu)
    
    print(f"\nAprès {etape} cycles d'apprentissage:")
    erreur_totale = 0
    for entrees, attendu in donnees:
        prediction = neurone.predire(np.array(entrees))
        erreur = abs(attendu - prediction)
        erreur_totale += erreur
        print(f"Entrées {entrees}: prédit {prediction:.3f}, devrait être {attendu}")
    print(f"Erreur moyenne: {erreur_totale/4:.3f}")
    print(f"Poids: {neurone.poids}, Biais: {neurone.biais:.3f}")

print("\n=== APPRENTISSAGE TERMINÉ ===")