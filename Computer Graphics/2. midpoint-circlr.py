import matplotlib.pyplot as plt

def plot_circle_points(xc, yc, x, y, points):
    # 8-way symmetry
    points.extend([
        (xc + x, yc + y),
        (xc - x, yc + y),
        (xc + x, yc - y),
        (xc - x, yc - y),
        (xc + y, yc + x),
        (xc - y, yc + x),
        (xc + y, yc - x),
        (xc - y, yc - x)
    ])

def midpoint_circle(xc, yc, r):
    x = 0
    y = r
    d = 1 - r
    points = []

    while x <= y:
        plot_circle_points(xc, yc, x, y, points)

        if d < 0:
            d = d + 2 * x + 3
        else:
            d = d + 2 * (x - y) + 5
            y -= 1

        x += 1

    return points

def main():
    print("Midpoint Circle Drawing Algorithm")
    try:
        xc = int(input("Enter center x-coordinate: "))
        yc = int(input("Enter center y-coordinate: "))
        r = int(input("Enter radius: "))

        if r < 0:
            raise ValueError("Radius must be non-negative.")

        points = midpoint_circle(xc, yc, r)

        # Extract x and y coordinates
        x_coords, y_coords = zip(*points)

        # Plotting the circle
        plt.scatter(x_coords, y_coords, color='purple')
        plt.title("Midpoint Circle Drawing")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.grid(True)
        plt.gca().set_aspect('equal', adjustable='box')
        plt.show()

    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
