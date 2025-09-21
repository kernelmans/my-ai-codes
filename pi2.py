import time
import math

def calculate_pi_with_error(n_terms):
    """
    Calcule une approximation de π avec la série de Leibniz et affiche l'erreur.
    
    Paramètres:
    n_terms (int): Nombre de termes à utiliser dans la série.
    
    Retourne:
    tuple: (Approximation de π, Erreur relative).
    """
    start_time = time.time()  # Démarrage du chronomètre
    pi_approx = 0.0
    
    for i in range(n_terms):
        term = (-1)**i / (2 * i + 1)  # Terme actuel de la série
        pi_approx += term  # Ajout du terme
    
    pi_approx *= 4  # Conversion de π/4 en π
    true_pi = math.pi  # Valeur réelle de π
    error = abs(pi_approx - true_pi)  # Erreur absolue
    
    end_time = time.time()  # Fin du chronomètre
    elapsed_time = end_time - start_time  # Temps écoulé
    
    # Afficher les résultats
    print(f"Approximation de π avec {n_terms} termes : {pi_approx}")
    print(f"Erreur absolue : {error}")
    print(f"Temps de calcul : {elapsed_time:.5f} secondes")
    
    return pi_approx, error

# Exemple d'utilisation
n_terms = 100000000  # Augmentez ce nombre pour plus de précision
calculate_pi_with_error(n_terms)
