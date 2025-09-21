import numpy as np
import matplotlib.pyplot as plt
import mpmath

def oscillations_from_zeros(x_values, n_zeros=20):
    """
    Calcule les oscillations locales dues aux contributions des zéros non triviaux.
    
    Args:
        x_values (numpy.ndarray): Plage de valeurs pour x.
        n_zeros (int): Nombre de zéros non triviaux à inclure.
    
    Returns:
        oscillations (numpy.ndarray): Oscillations locales.
    """
    oscillations = np.zeros_like(x_values, dtype=float)
    for k in range(1, n_zeros + 1):
        zero = mpmath.zetazero(k)  # k-ième zéro
        gamma = float(mpmath.im(zero))  # Partie imaginaire
        oscillations += np.cos(gamma * np.log(x_values)) / np.sqrt(gamma)
    return oscillations

# Simulation des oscillations locales
x_values = np.linspace(10, 1000, 1000)  # Domaine pour x
n_zeros = 20  # Nombre de zéros à inclure
oscillations = oscillations_from_zeros(x_values, n_zeros)

# Visualisation des oscillations locales
plt.figure(figsize=(12, 6))
plt.plot(x_values, oscillations, label=f"Oscillations locales avec {n_zeros} zéros", color="blue")
plt.xlabel("x")
plt.ylabel("Amplitude des oscillations")
plt.title("Oscillations locales dues aux zéros de Riemann")
plt.legend()
plt.grid(True, linestyle="--", linewidth=0.5)
plt.show()
