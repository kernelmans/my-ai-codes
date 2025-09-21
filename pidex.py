import matplotlib.pyplot as plt
import numpy as np

# Étape 1 : Fonction pour vérifier si un nombre est premier
def est_premier(n):
    """Détermine si un nombre n est premier."""
    if n < 2:  # Les nombres < 2 ne sont pas premiers
        return False
    for i in range(2, int(n**0.5) + 1):  # Vérifie la divisibilité jusqu'à racine(n)
        if n % i == 0:
            return False
    return True

# Étape 2 : Fonction pour calculer π(x)
def pi_x(x):
    """Calcule la fonction de comptage des nombres premiers π(x)."""
    compteur = 0
    pi_values = []  # Liste pour stocker les valeurs de π(x)
    for i in range(1, x + 1):  # Parcourt les nombres de 1 à x
        if est_premier(i):  # Vérifie si le nombre est premier
            compteur += 1   # Incrémente le compteur si i est premier
        pi_values.append(compteur)  # Ajoute la valeur actuelle de π(x)
    return pi_values

# Étape 3 : Calcul et affichage graphique de π(x)
def tracer_pi_x(x_max):
    """Trace la fonction de comptage π(x) jusqu'à x_max."""
    x = np.arange(1, x_max + 1)  # Liste des valeurs de x
    pi_values = pi_x(x_max)      # Calcul de π(x)
    
    # Tracé de la courbe en escalier
    plt.figure(figsize=(10, 6))
    plt.step(x, pi_values, where='post', color='red', linewidth=2, label=r'$\pi(x)$ (nombre de nombres premiers)')
    plt.title(f"Fonction de comptage des nombres premiers $\pi(x)$ pour $x$ de 1 à {x_max}")
    plt.xlabel("x")
    plt.ylabel(r"$\pi(x)$")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()
    plt.show()

# Étape 4 : Exécution pour une valeur maximale donnée
x_max = 10 # Définir la valeur maximale de x
tracer_pi_x(x_max)