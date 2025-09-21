import mpmath
from mpmath import zetazero, li
import sympy

# Configuration de la précision
mpmath.mp.dps = 50  # Précision en décimales

def pi_approximation(x, n_zeros=10):
    """
    Approximations de la fonction pi(x) en utilisant les zéros non triviaux de la fonction zêta.
    
    Arguments :
    x (float) : La borne supérieure pour le comptage des nombres premiers.
    n_zeros (int) : Nombre de zéros non triviaux à utiliser pour affiner l'approximation.
    
    Retourne :
    float : Approximations de pi(x).
    """
    # Étape 1 : Approximation principale avec la fonction logarithme intégrale
    approximation = li(x)  # La fonction logarithme intégrale

    # Étape 2 : Ajout des corrections avec les zéros non triviaux
    for k in range(1, n_zeros + 1):
        zero = zetazero(k)  # Récupère le k-ième zéro non trivial
        rho = zero.real + 1j * zero.imag  # Forme complexe du zéro
        correction = li(x ** rho).real  # Contribution réelle de x^rho
        approximation -= correction  # Soustraire la contribution

    return approximation

def pi_exact(x):
    """
    Calcule le nombre exact de nombres premiers inférieurs ou égaux à x.
    """
    return sympy.primepi(x)

# Paramètres
x_values = [10, 100, 1000, 10000]  # Valeurs de x pour le test
n_zeros = 10  # Nombre de zéros non triviaux à utiliser

# Comparaison entre les valeurs exactes et les approximations
print(f"{'x':>10} {'Pi(x) exact':>15} {'Pi(x) approx':>20} {'Erreur':>15}")
for x in x_values:
    exact = int(pi_exact(x))  # Conversion explicite en entier
    approx = float(pi_approximation(x, n_zeros))  # Conversion explicite en flottant
    error = abs(exact - approx)
    print(f"{x:>10} {exact:>15} {approx:>20.5f} {error:>15.5f}")