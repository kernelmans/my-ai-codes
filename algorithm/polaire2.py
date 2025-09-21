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

def plot_polar_form(z, magnitude, angle, label):
    """
    Affiche le graphique de la représentation polaire d'un nombre complexe.
    """
    plt.quiver(0, 0, magnitude * np.cos(angle), magnitude * np.sin(angle), 
               angles='xy', scale_units='xy', scale=1, label=label)

# Entrée des deux nombres complexes
print("Entrer le premier nombre complexe (par exemple : 3+4j) :")
z1 = complex(input())
print("Entrer le deuxième nombre complexe (par exemple : 2+3j) :")
z2 = complex(input())

# Conversion en forme polaire
magnitude1, angle1 = complex_to_polar(z1)
magnitude2, angle2 = complex_to_polar(z2)

# Affichage des formes polaires
print(f"\nForme polaire de {z1} :")
print(f"  Magnitude : {magnitude1:.2f}")
print(f"  Angle (radians) : {angle1:.2f}, Angle (degrés) : {np.degrees(angle1):.2f}°")

print(f"\nForme polaire de {z2} :")
print(f"  Magnitude : {magnitude2:.2f}")
print(f"  Angle (radians) : {angle2:.2f}, Angle (degrés) : {np.degrees(angle2):.2f}°")

# Produit des deux nombres complexes en forme polaire
magnitude_product = magnitude1 * magnitude2
angle_product = angle1 + angle2
z_product = polar_to_complex(magnitude_product, angle_product)

print(f"\nProduit des deux nombres complexes ({z1} * {z2}) :")
print(f"  Magnitude : {magnitude_product:.2f}")
print(f"  Angle (radians) : {angle_product:.2f}, Angle (degrés) : {np.degrees(angle_product):.2f}°")
print(f"  Forme cartésienne : {z_product}")

# Affichage graphique
plt.figure(figsize=(6, 6))
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# Tracé des deux nombres complexes et du produit
plot_polar_form(z1, magnitude1, angle1, label=f"{z1} (z1)")
plot_polar_form(z2, magnitude2, angle2, label=f"{z2} (z2)")
plot_polar_form(z_product, magnitude_product, angle_product, label="Produit (z1 * z2)")

# Configuration du graphique
plt.xlim(-magnitude_product - 1, magnitude_product + 1)
plt.ylim(-magnitude_product - 1, magnitude_product + 1)
plt.grid()
plt.gca().set_aspect('equal', adjustable='box')
plt.title("Représentation polaire des nombres complexes et du produit")
plt.xlabel("Re (Partie réelle)")
plt.ylabel("Im (Partie imaginaire)")
plt.legend()
plt.show()