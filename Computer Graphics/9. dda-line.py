import matplotlib.pyplot as plt

def dda_line(x1, y1, x2, y2):
    points = []

    dx = x2 - x1
    dy = y2 - y1

    steps = int(max(abs(dx), abs(dy)))

    x_inc = dx / steps
    y_inc = dy / steps

    x = x1
    y = y1

    for _ in range(steps + 1):
        points.append((round(x), round(y)))
        x += x_inc
        y += y_inc

    return points

def main():
    print("DDA Line Drawing Algorithm")
    try:
        x1 = float(input("Enter x1: "))
        y1 = float(input("Enter y1: "))
        x2 = float(input("Enter x2: "))
        y2 = float(input("Enter y2: "))

        points = dda_line(x1, y1, x2, y2)

        # Extract x and y coordinates
        x_coords, y_coords = zip(*points)

        # Plotting the line
        plt.plot(x_coords, y_coords, marker='o', color='green')
        plt.title("DDA Line Drawing")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.grid(True)
        plt.gca().set_aspect('equal', adjustable='box')
        plt.show()

    except ValueError:
        print("Please enter valid numeric values.")

if __name__ == "__main__":
    main()
