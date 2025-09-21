import random
import time

def fermat_test(n, k=5):
    if n <= 1:
        return False
    for _ in range(k):
        a = random.randint(2, n - 2)
        if pow(a, n - 1, n) != 1:
            return False
    return True

def miller_rabin_test(n, k=10):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

# Comparaison des deux algorithmes
def compare_algorithms(n):
    start_fermat = time.time()
    result_fermat = fermat_test(n)
    end_fermat = time.time()

    start_miller = time.time()
    result_miller = miller_rabin_test(n)
    end_miller = time.time()

    print(f"Fermat Test: {'Prime' if result_fermat else 'Composite'}, Time: {end_fermat - start_fermat:.5f}s")
    print(f"Miller-Rabin Test: {'Prime' if result_miller else 'Composite'}, Time: {end_miller - start_miller:.5f}s")

# Exemple
n = 10**9 + 7  # Grand nombre
compare_algorithms(n)
