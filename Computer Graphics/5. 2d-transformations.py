import numpy as np
import matplotlib.pyplot as plt

def get_polygon():
    n = int(input("Enter number of vertices: "))
    return np.array([[*map(float, input(f"x[{i+1}] y[{i+1}]: ").split()), 1] for i in range(n)])

def transform(p, mat): return p @ mat.T

def matrices():
    return {
        '1': lambda: np.array([[1, 0, float(input("tx: "))], [0, 1, float(input("ty: "))], [0, 0, 1]]),
        '2': lambda: np.array([[float(input("sx: ")), 0, 0], [0, float(input("sy: ")), 0], [0, 0, 1]]),
        '3': lambda: (lambda a: np.array([[np.cos(a), -np.sin(a), 0], [np.sin(a), np.cos(a), 0], [0, 0, 1]]))(np.radians(float(input("Angle (deg): ")))),
        '4': lambda: np.array([[1, float(input("shx: ")), 0], [float(input("shy: ")), 1, 0], [0, 0, 1]]),
        '5': lambda: {'x': [[1, 0, 0], [0, -1, 0], [0, 0, 1]], 'y': [[-1, 0, 0], [0, 1, 0], [0, 0, 1]], 'origin': [[-1, 0, 0], [0, -1, 0], [0, 0, 1]]}[input("Axis (x/y/origin): ").lower()]
    }

def plot(polygon, transformed):
    def close(p): return np.vstack([p[:, :2], p[0, :2]])
    plt.clf()
    plt.plot(*close(polygon).T, 'ro--', label="Original")
    plt.plot(*close(transformed).T, 'go-', label="Transformed")
    plt.title("2D Transformation"); plt.xlabel("X"); plt.ylabel("Y")
    plt.legend(); plt.axis('equal'); plt.grid(True)
    plt.pause(0.1)

def main():
    print("2D Transformations using Homogeneous Coordinates")
    polygon = get_polygon()
    transformed = polygon.copy()
    plt.ion(); plt.figure()

    while True:
        print("\n1: Translate \n2: Scale \n3: Rotate \n4: Shear \n5: Reflect \nq: Quit")
        choice = input("Choose transformation: ")
        if choice == 'q': break
        if choice in matrices():
            try:
                mat = np.array(matrices()[choice](), dtype=float)
                transformed = transform(transformed, mat)
                plot(polygon, transformed)
            except: print("Invalid input.")
        else:
            print("Invalid choice.")

    plt.ioff(); plt.show()

if __name__ == "__main__":
    main()
