import numpy as np
import matplotlib.pyplot as plt

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

# Tracer les nombres premiers en spirale
def plot_prime_spiral(primes, title):
    plt.figure(figsize=(10, 10))
    ax = plt.subplot(111, polar=True)

    # Calcul des coordonnées polaires
    theta = np.sqrt(primes)  # L'angle suit une croissance progressive (racine carrée pour une spirale)
    radius = primes  # Le rayon est égal au nombre premier

    # Tracer les points
    ax.scatter(theta, radius, s=1, color='yellow', alpha=0.75)

    # Esthétique
    ax.set_title(title, va='bottom', fontsize=14, color='white')
    ax.set_facecolor("black")  # Fond noir pour correspondre au style attendu
    plt.show()

# Programme principal
def main():
    limit = 100000  # Limite pour les nombres premiers
    primes = generate_primes(limit)
    plot_prime_spiral(primes, title="Spirale des nombres premiers corrigée")

if __name__ == "__main__":
    main()