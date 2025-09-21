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

# Générer les multiples d'un nombre jusqu'à une limite donnée
def generate_multiples(base, limit):
    return [x for x in range(base, limit + 1, base)]

# Tracer les nombres premiers et les multiples en spirale
def plot_prime_and_multiples_spiral(primes, multiples_dict, title):
    plt.figure(figsize=(10, 10))
    ax = plt.subplot(111, polar=True)

    # Tracer les nombres premiers
    theta_primes = np.sqrt(primes)  # L'angle suit une progression en spirale
    radius_primes = primes
    ax.scatter(theta_primes, radius_primes, s=1, color='yellow', alpha=0.75, label="Nombres premiers")

    # Tracer les multiples pour chaque base
    colors = ['red', 'green', 'blue', 'orange', 'purple']
    for i, (base, multiples) in enumerate(multiples_dict.items()):
        theta_multiples = np.sqrt(multiples)
        radius_multiples = multiples
        ax.scatter(theta_multiples, radius_multiples, s=1, color=colors[i % len(colors)], alpha=0.75, label=f"Multiples de {base}")

    # Esthétique
    ax.set_title(title, va='bottom', fontsize=14, color='white')
    ax.set_facecolor("black")  # Fond noir pour correspondre au style attendu
    ax.legend(loc="upper left", fontsize=10, bbox_to_anchor=(1.1, 1.05))  # Légende en dehors du graphique
    plt.show()

# Programme principal
def main():
    limit = 100000  # Limite pour les nombres premiers et les multiples
    primes = generate_primes(limit)

    # Générer les multiples pour des bases spécifiques
    bases = [3, 7, 11]  # Bases pour lesquelles on veut les multiples
    multiples_dict = {base: generate_multiples(base, limit) for base in bases}

    # Tracer les nombres premiers et les multiples
    plot_prime_and_multiples_spiral(primes, multiples_dict, title="Spirale des nombres premiers et multiples")

if __name__ == "__main__":
    main()