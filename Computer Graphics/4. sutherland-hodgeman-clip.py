import matplotlib.pyplot as plt

def inside(p, edge, rect):
    x, y = p; xmin, xmax, ymin, ymax = rect
    return (x >= xmin if edge == 'LEFT' else
            x <= xmax if edge == 'RIGHT' else
            y >= ymin if edge == 'BOTTOM' else
            y <= ymax)

def intersect(p1, p2, edge, rect):
    x1, y1 = p1; x2, y2 = p2; xmin, xmax, ymin, ymax = rect
    dx, dy = x2 - x1, y2 - y1
    if dx == 0: m = float('inf')
    else: m = dy / dx

    if edge == 'LEFT': return (xmin, y1 + m * (xmin - x1))
    if edge == 'RIGHT': return (xmax, y1 + m * (xmax - x1))
    if edge == 'BOTTOM': return (x1 if m == float('inf') else x1 + (ymin - y1) / m, ymin)
    if edge == 'TOP': return (x1 if m == float('inf') else x1 + (ymax - y1) / m, ymax)

def sutherland_hodgman(polygon, rect):
    for edge in ['LEFT', 'RIGHT', 'BOTTOM', 'TOP']:
        output = []
        s = polygon[-1]
        for e in polygon:
            if inside(e, edge, rect):
                if not inside(s, edge, rect): output.append(intersect(s, e, edge, rect))
                output.append(e)
            elif inside(s, edge, rect):
                output.append(intersect(s, e, edge, rect))
            s = e
        polygon = output
    return polygon

def main():
    print("Sutherland–Hodgman Polygon Clipping")
    n = int(input("Enter number of vertices: "))
    polygon = [tuple(map(float, input(f"Enter x[{i+1}], y[{i+1}]: ").split())) for i in range(n)]
    rect = tuple(map(float, input("Enter xmin, xmax, ymin, ymax: ").split()))
    clipped = sutherland_hodgman(polygon, rect)

    fig, ax = plt.subplots()
    ax.plot(*zip(*(polygon + [polygon[0]])), 'r--', label='Original')
    if clipped:
        ax.plot(*zip(*(clipped + [clipped[0]])), 'g-', label='Clipped')
    ax.add_patch(plt.Rectangle((rect[0], rect[2]), rect[1]-rect[0], rect[3]-rect[2], edgecolor='black', fill=False, linestyle='--', label='Clip Window'))
    plt.title("Sutherland–Hodgman Polygon Clipping")
    plt.xlabel("X"); plt.ylabel("Y"); plt.legend(); plt.grid(True)
    ax.set_aspect('equal', adjustable='box'); plt.show()

if __name__ == "__main__":
    main()


# Example Input
# Enter number of vertices: 4
# Enter x[1], y[1]: 30 30
# Enter x[2], y[2]: 180 50
# Enter x[3], y[3]: 220 180
# Enter x[4], y[4]: 50 220
# Enter xmin, xmax, ymin, ymax: 50 200 50 200
