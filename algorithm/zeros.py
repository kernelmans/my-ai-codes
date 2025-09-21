import mpmath
from mpmath import zetazero, zeta

# Configuration de la précision de mpmath
mpmath.mp.dps = 50  # Précision en nombre de décimales

def trouver_zeros_non_triviaux(n_zeros):
    """
    Trouve les premiers zéros non triviaux de la fonction zêta de Riemann.
    
    Arguments :
    n_zeros (int) : Nombre de zéros non triviaux à trouver.
    
    Retourne :
    List[complex] : Liste des zéros non triviaux trouvés.
    """
    zeros = []
    for k in range(1, n_zeros + 1):
        zero = zetazero(k)
        zeros.append(zero)
    return zeros

# Exemple : Trouver les 10 premiers zéros non triviaux
n = 1000
zeros_non_triviaux = trouver_zeros_non_triviaux(n)

# Afficher les résultats
print("Les {} premiers zéros non triviaux de la fonction zêta :".format(n))
for i, zero in enumerate(zeros_non_triviaux, start=1):
    print(f"Zero {i}: {zero}")