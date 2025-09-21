import random

def is_prime_fermat(n, k=5):
    """
    Teste si un nombre est premier en utilisant le test probabiliste de Fermat.
    
    Paramètres:
    n (int): Le nombre à tester.
    k (int): Nombre d'itérations du test.
    
    Retourne:
    bool: True si n est probablement premier, False sinon.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    for _ in range(k):
        a = random.randint(2, n - 2)
        if pow(a, n - 1, n) != 1:
            return False
    return True

def is_prime_miller_rabin(n, k=10):
    """
    Teste si un nombre est premier en utilisant le test probabiliste de Miller-Rabin.
    
    Paramètres:
    n (int): Le nombre à tester.
    k (int): Nombre d'itérations du test.
    
    Retourne:
    bool: True si n est probablement premier, False sinon.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Écriture de n-1 comme 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Test de Miller-Rabin
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)  # a^d % n
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
    Teste le nombre avec deux méthodes : Fermat et Miller-Rabin.
    
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
        # Tester la primalité avec Fermat et Miller-Rabin
        if is_prime_fermat(candidate) and is_prime_miller_rabin(candidate):
            return candidate

def interactive_prime_generator():
    """
    Programme interactif pour générer des grands nombres premiers à la demande.
    """
    print("=== Générateur de grands nombres premiers ===")
    bit_length = int(input("Entrez la taille en bits des nombres premiers (ex : 512) : "))
    
    while True:
        try:
            count = int(input("Combien de nombres premiers voulez-vous générer ? (Entrez 0 pour quitter) : "))
            if count == 0:
                print("Programme terminé. Merci d'avoir utilisé le générateur !")
                break

            print(f"Génération de {count} nombres premiers de {bit_length} bits...\n")
            for i in range(count):
                prime = generate_large_prime(bit_length)
                print(f"N°{i + 1} : {prime}\n")
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")

# Lancer le programme interactif
interactive_prime_generator()
