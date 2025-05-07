import numpy as np
import matplotlib.pyplot as plt

def bezier(P0, P1, P2, P3, t):
    return ((1 - t)**3)[:, None] * P0 + (3 * (1 - t)**2 * t)[:, None] * P1 + (3 * (1 - t) * t**2)[:, None] * P2 + (t**3)[:, None] * P3

def hermite(P0, P1, T0, T1, t):
    h1, h2 = (2*t**3 - 3*t**2 + 1)[:, None], (t**3 - 2*t**2 + t)[:, None]
    h3, h4 = (-2*t**3 + 3*t**2)[:, None], (t**3 - t**2)[:, None]
    return h1 * P0 + h2 * T0 + h3 * P1 + h4 * T1

def get_points(n, prompt): return [np.array(list(map(float, input(f"{prompt} {i+1}: ").split()))) for i in range(n)]

def plot_curve(ctrl, curve, name):
    plt.plot(*ctrl.T, 'ro--', label='Control Points')
    plt.plot(*curve.T, 'b-', label=f'{name} Curve')
    plt.title(f'{name} Curve'); plt.xlabel('X'); plt.ylabel('Y')
    plt.legend(); plt.grid(True); plt.axis('equal'); plt.show()

def main():
    print("1. Bezier Curve\n2. Hermite Curve")
    choice = input("Choose (1 or 2): "); t = np.linspace(0, 1, 100)

    if choice == '1':
        P = get_points(4, "Bezier Point")
        curve = bezier(*P, t); plot_curve(np.vstack(P), curve, "Bezier")

    elif choice == '2':
        P0, P1 = get_points(2, "Endpoint")
        T0, T1 = get_points(2, "Tangent")
        curve = hermite(P0, P1, T0, T1, t)
        plot_curve(np.vstack([P0, P1]), curve, "Hermite")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()


# Example Input
# Choose (1 or 2): 1
# Bezier Point 1: 0 0
# Bezier Point 2: 1 3
# Bezier Point 3: 3 3
# Bezier Point 4: 4 0

# Choose (1 or 2): 2
# Endpoint 1: 0 0
# Endpoint 2: 4 0
# Tangent 1: 1 3
# Tangent 2: 1 -3
