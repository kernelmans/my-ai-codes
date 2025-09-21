import matplotlib.pyplot as plt
import numpy as np

# Générer les nombres premiers jusqu'à une limite donnée
def generate_primes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False  # 0 et 1 ne sont pas premiers
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    primes = [x for x, is_prime in enumerate(sieve) if is_prime]
    return primes

# Visualisation des nombres premiers en spirale
def visualize_prime_spiral(primes):
    plt.figure(figsize=(10, 10))  # Taille du graphique
    ax = plt.subplot(111, polar=True)  # Configuration en coordonnées polaires

    for prime in primes:
        angle = np.sqrt(prime)  # Calcul de l'angle en radians
        radius = prime  # Rayon = valeur du nombre premier

        # Tracer chaque point
        ax.scatter(angle, radius, color='gold', s=20)  # Points dorés avec taille 20

    # Esthétique du graphique
    ax.set_title("Spirale des nombres premiers", va='bottom', fontsize=14, color='white')
    ax.set_facecolor("black")  # Fond noir pour un meilleur contraste
    plt.show()

# Générer les nombres premiers et visualiser leur spirale
primes = generate_primes(100)  # Limite pour les nombres premiers (1 à 100)
visualize_prime_spiral(primes)