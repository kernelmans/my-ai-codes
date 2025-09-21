import numpy as np
import matplotlib.pyplot as plt

# Fonction pour générer les nombres premiers jusqu'à une limite donnée
def generate_primes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False  # 0 et 1 ne sont pas premiers
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    primes = [x for x, is_prime in enumerate(sieve) if is_prime]
    return primes

# Étape 1 : Représenter les nombres en coordonnées polaires
def plot_primes_polar(primes, limit, title, modulo=None):
    plt.figure(figsize=(8, 8))
    ax = plt.subplot(111, polar=True)

    # Calculer les coordonnées polaires pour les nombres
    theta = []
    radius = []
    for p in primes:
        if modulo and p % modulo != 0:
            continue
        theta.append(2 * np.pi * (p / limit))
        radius.append(p)

    # Tracer les points (spirales)
    ax.scatter(theta, radius, s=1, color='yellow', alpha=0.75)
    ax.set_title(title, va='bottom')
    plt.show()

# Étape 2 : Tracer les progressions arithmétiques
def plot_arithmetic_progressions(limit, modulo, title):
    plt.figure(figsize=(8, 8))
    ax = plt.subplot(111, polar=True)

    theta = []
    radius = []
    for n in range(1, limit + 1):
        theta.append(2 * np.pi * (n / modulo))
        radius.append(n)

    # Tracer les points
    ax.scatter(theta, radius, s=1, color='green', alpha=0.75)
    ax.set_title(title, va='bottom')
    plt.show()

# Étape 3 : Comparaison avec un modulo spécifique
def plot_primes_with_modulo(primes, limit, modulo, title):
    plt.figure(figsize=(8, 8))
    ax = plt.subplot(111, polar=True)

    theta = []
    radius = []
    for p in primes:
        theta.append(2 * np.pi * (p % modulo) / modulo)
        radius.append(p)

    # Tracer les points
    ax.scatter(theta, radius, s=1, color='blue', alpha=0.75)
    ax.set_title(title, va='bottom')
    plt.show()

# Étape 4 : Générer les graphiques
def main():
    limit = 100000  # Limite supérieure pour les nombres
    modulo = 44  # Exemple : modulo pour les progressions

    # Générer les nombres premiers
    primes = generate_primes(limit)

    # Graphique 1 : Nombres premiers en spirale
    plot_primes_polar(primes, limit, title="Spirale des nombres premiers (n, n)")

    # Graphique 2 : Progressions arithmétiques
    plot_arithmetic_progressions(limit, modulo, title=f"Progressions arithmétiques modulo {modulo}")

    # Graphique 3 : Progressions arithmétiques modulo avec nombres premiers
    plot_primes_with_modulo(primes, limit, modulo, title=f"Nombres premiers modulo {modulo}")

# Exécuter le programme
if __name__ == "__main__":
    main()