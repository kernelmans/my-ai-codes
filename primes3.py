import numpy as np
import matplotlib.pyplot as plt
from mpmath import zetazero, li
import sympy

# Configuration de précision
import mpmath
mpmath.mp.dps = 50  # Précision pour mpmath

def pi_exact(x):
    """
    Calcule le nombre exact de nombres premiers inférieurs ou égaux à x.
    """
    return sympy.primepi(x)

def pi_approximation(x, n_zeros):
    """
    Approximation de la fonction pi(x) en utilisant les zéros non triviaux de la fonction zêta.
    
    Args:
        x (float): La borne supérieure pour le comptage des nombres premiers.
        n_zeros (int): Nombre de zéros non triviaux utilisés pour l'approximation.
    
    Returns:
        float: Valeur approximative de pi(x).
    """
    # Étape 1 : Approximation principale avec le logarithme intégral
    approximation = li(x)  # Logarithme intégral

    # Étape 2 : Ajouter les corrections dues aux zéros non triviaux
    for k in range(1, n_zeros + 1):
        zero = zetazero(k)  # Obtenir le k-ième zéro non trivial
        rho = zero.real + 1j * zero.imag  # Forme complexe du zéro
        correction = li(x ** rho).real  # Contribution réelle de x^rho
        approximation -= correction  # Ajouter la correction

    return approximation

# Plage des valeurs de x
x_values = np.logspace(1, 4, 10)  # Valeurs de x de 10^1 à 10^4 (échelle logarithmique)

# Calculer les valeurs exactes et approximatives
n_zeros_list = [5, 10, 20]  # Différents nombres de zéros à considérer
exact_values = [pi_exact(int(x)) for x in x_values]

# Calculer les approximations pour chaque valeur de n_zeros
approximations = {}
for n_zeros in n_zeros_list:
    approximations[n_zeros] = [pi_approximation(x, n_zeros) for x in x_values]

# Visualisation des résultats
plt.figure(figsize=(10, 6))
plt.plot(x_values, exact_values, 'o-', color='black', label="Pi(x) exact")
for n_zeros, approx_values in approximations.items():
    plt.plot(x_values, approx_values, '--', label=f"Approximation ({n_zeros} zéros)")

# Mise en forme du graphique
plt.xscale('log')  # Échelle logarithmique pour l'axe x
plt.xlabel("x (échelle logarithmique)")
plt.ylabel("Valeurs de Pi(x)")
plt.title("Pi(x) exact vs approximations utilisant les zéros non triviaux")
plt.legend()
plt.grid(True, linestyle="--", linewidth=0.5)
plt.show()