import random

def is_prime(n, k=10):
    """
    Teste si un nombre est premier en utilisant le test probabiliste de Miller-Rabin.
    
    Paramètres:
    n (int): Le nombre à tester.
    k (int): Nombre d'itérations du test (plus grand = plus fiable).
    
    Retourne:
    bool: True si n est probablement premier, False sinon.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Écriture de n - 1 comme 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Test de Miller-Rabin
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)  # Calcul de (a^d) % n
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_large_prime(bit_length):
    """
    Génère un grand nombre premier d'une certaine longueur en bits.
    
    Paramètres:
    bit_length (int): La longueur en bits du nombre premier.
    
    Retourne:
    int: Un grand nombre premier.
    """
    while True:
        # Générer un nombre aléatoire de bit_length bits
        candidate = random.getrandbits(bit_length)
        # S'assurer que le nombre est impair
        candidate |= (1 << bit_length - 1) | 1
        # Tester la primalité
        if is_prime(candidate):
            return candidate

# Exemple d'utilisation
if __name__ == "__main__":
    bit_length = 512  # Taille du nombre en bits (par exemple, 512 pour un très grand nombre)
    prime = generate_large_prime(bit_length)
    print(f"Nombre premier de {bit_length} bits :\n{prime}")
