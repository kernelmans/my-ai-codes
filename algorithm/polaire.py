import numpy as np
import matplotlib.pyplot as plt

def complex_to_polar(z):
    """
    Convertit un nombre complexe en forme polaire.
    Retourne la magnitude et l'angle en radians.
    """
    magnitude = np.abs(z)
    angle = np.angle(z)  # Angle en radians
    return magnitude, angle

def polar_to_complex(magnitude, angle):
    """
    Convertit la forme polaire en nombre complexe.
    """
    real = magnitude * np.cos(angle)
    imaginary = magnitude * np.sin(angle)
    return complex(real, imaginary)

def plot_polar_form(z, magnitude, angle):
    """
    Affiche le graphique de la représentation polaire d'un nombre complexe.
    """
    plt.figure(figsize=(6, 6))
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    
    # Tracé de la ligne représentant le nombre complexe
    plt.quiver(0, 0, magnitude * np.cos(angle), magnitude * np.sin(angle), 
               angles='xy', scale_units='xy', scale=1, color='blue', label=f"{z} (polaire)")
    
    # Cercle pour la magnitude
    circle = plt.Circle((0, 0), magnitude, color='gray', fill=False, linestyle='dotted', label="Magnitude")
    plt.gca().add_artist(circle)
    
    # Annotation de l'angle
    plt.text(magnitude * np.cos(angle) / 2, magnitude * np.sin(angle) / 2, 
             f"θ = {np.degrees(angle):.2f}°", fontsize=10, color='red')
    
    # Paramètres du graphique
    plt.xlim(-magnitude - 1, magnitude + 1)
    plt.ylim(-magnitude - 1, magnitude + 1)
    plt.grid()
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title("Représentation polaire du nombre complexe")
    plt.xlabel("Re (Partie réelle)")
    plt.ylabel("Im (Partie imaginaire)")
    plt.legend()
    plt.show()

# Entrée de l'utilisateur
print("Entrer un nombre complexe (par exemple : 3+4j) :")
z = complex(input())

# Calcul de la forme polaire
magnitude, angle = complex_to_polar(z)

# Conversion en degrés pour affichage
angle_degrees = np.degrees(angle)

# Affichage des résultats
print(f"\nForme polaire de {z} :")
print(f"  Magnitude : {magnitude:.2f}")
print(f"  Angle (radians) : {angle:.2f}")
print(f"  Angle (degrés) : {angle_degrees:.2f}°")

# Vérification : Retour à la forme cartésienne
cartesian = polar_to_complex(magnitude, angle)
print(f"\nConversion inverse en forme cartésienne : {cartesian}")

# Affichage graphique
plot_polar_form(z, magnitude, angle)