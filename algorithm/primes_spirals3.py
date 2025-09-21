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
    plt.figure(figsize=(12, 12))  # Taille du graphique
    ax = plt.subplot(111, polar=True)

    # Tracer les nombres premiers
    theta_primes = np.sqrt(primes)  # L'angle suit une progression en spirale
    radius_primes = primes
    ax.scatter(
        theta_primes,
        radius_primes,
        s=5,  # Taille des points (plus grand pour la lisibilité)
        color='gold',
        alpha=0.9,
        label="Nombres premiers"
    )

    # Tracer les multiples pour chaque base
    colors = ['red', 'lime', 'cyan', 'orange', 'magenta']
    for i, (base, multiples) in enumerate(multiples_dict.items()):
        theta_multiples = np.sqrt(multiples)
        radius_multiples = multiples
        ax.scatter(
            theta_multiples,
            radius_multiples,
            s=3,  # Taille des points (plus petits pour les multiples)
            color=colors[i % len(colors)],
            alpha=0.7,
            label=f"Multiples de {base}"
        )

    # Esthétique du graphique
    ax.set_facecolor("black")  # Fond noir
    ax.grid(color="gray", linestyle="--", alpha=0.4)  # Grille discrète
    ax.spines['polar'].set_visible(False)  # Supprimer le contour par défaut
    ax.tick_params(colors='white')  # Couleur blanche pour les angles
    ax.set_title(title, va='bottom', fontsize=16, color='white', pad=20)  # Titre stylisé

    # Ajouter une légende
    ax.legend(
        loc="upper right",
        fontsize=10,
        bbox_to_anchor=(1.3, 1.1),
        frameon=True,
        facecolor="black",
        edgecolor="white",
        labelcolor="white"
    )
    plt.show()

# Programme principal
def main():
    limit = 100000  # Limite pour les nombres premiers et les multiples
    primes = generate_primes(limit)

    # Générer les multiples pour des bases spécifiques
    bases = [3, 7, 11]  # Bases pour lesquelles on veut les multiples
    multiples_dict = {base: generate_multiples(base, limit) for base in bases}

    # Tracer les nombres premiers et les multiples
    plot_prime_and_multiples_spiral(
        primes,
        multiples_dict,
        title="Spirale des nombres premiers et multiples (améliorée)"
    )

if __name__ == "__main__":
    main()