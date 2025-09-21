import matplotlib.pyplot as plt
import numpy as np

# Visualisation pour plusieurs points avec une plage plus large pour voir la spirale
def visualize_spiral_with_more_points(numbers):
    plt.figure(figsize=(10, 10))  # Taille du graphique
    ax = plt.subplot(111, polar=True)  # Configuration en coordonnées polaires

    for number in numbers:
        angle = np.sqrt(number)  # Calcul de l'angle en radians
        radius = number  # Rayon = valeur du nombre

        # Tracer chaque point
        ax.scatter(angle, radius, color='red', s=20)  # Points rouges avec taille 20

    # Esthétique du graphique
    ax.set_title("Visualisation de la spirale avec plus de points", va='bottom', fontsize=14, color='white')
    ax.set_facecolor("black")  # Fond noir pour un meilleur contraste
    plt.show()

# Étendre la plage pour voir la spirale
numbers = range(1, 101)  # Plage de valeurs : 1 à 100
visualize_spiral_with_more_points(numbers)