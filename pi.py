import math

def archimede_pi(n_sides):
    """
    Approxime π en utilisant la méthode d'Archimède.
    
    Paramètres:
    n_sides (int): Nombre initial de côtés (doit être une puissance de 2, comme 6, 12, 24...).
    
    Retourne:
    tuple: (Périmètre inscrit, Périmètre circonscrit, Approximation de π).
    """
    radius = 1  # Rayon du cercle
    side_length = 2 * radius * math.sin(math.pi / n_sides)  # Longueur d'un côté inscrit
    circumscribed_side_length = 2 * radius * math.tan(math.pi / n_sides)  # Longueur côté circonscrit
    
    # Périmètres
    perimeter_inscribed = n_sides * side_length
    perimeter_circumscribed = n_sides * circumscribed_side_length
    
    # Approximation de π
    pi_lower_bound = perimeter_inscribed / (2 * radius)
    pi_upper_bound = perimeter_circumscribed / (2 * radius)
    
    return pi_lower_bound, pi_upper_bound, (pi_lower_bound + pi_upper_bound) / 2

# Exemple d'utilisation
n_sides = 96  # Nombre de côtés
pi_lower, pi_upper, pi_approx = archimede_pi(n_sides)
print(f"Encadrement de π avec {n_sides} côtés : {pi_lower} < π < {pi_upper}")
print(f"Approximation de π : {pi_approx}")
