import matplotlib.pyplot as plt

INSIDE, LEFT, RIGHT, BOTTOM, TOP = 0, 1, 2, 4, 8

def compute_code(x, y, rect):
    xmin, xmax, ymin, ymax = rect
    return (LEFT if x < xmin else RIGHT if x > xmax else 0) | \
           (BOTTOM if y < ymin else TOP if y > ymax else 0)

def clip_line(x1, y1, x2, y2, rect):
    code1, code2 = compute_code(x1, y1, rect), compute_code(x2, y2, rect)
    while True:
        if not (code1 | code2):
            return x1, y1, x2, y2
        elif code1 & code2:
            return None
        out = code1 or code2
        xmin, xmax, ymin, ymax = rect
        if out & TOP:     x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1); y = ymax
        elif out & BOTTOM:x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1); y = ymin
        elif out & RIGHT: y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1); x = xmax
        elif out & LEFT:  y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1); x = xmin
        if out == code1: x1, y1, code1 = x, y, compute_code(x, y, rect)
        else:            x2, y2, code2 = x, y, compute_code(x, y, rect)

def main():
    print("Cohen–Sutherland Line Clipping")
    x1, y1 = map(float, input("Enter x1 y1: ").split())
    x2, y2 = map(float, input("Enter x2 y2: ").split())
    rect = tuple(map(float, input("Enter xmin xmax ymin ymax: ").split()))
    clipped = clip_line(x1, y1, x2, y2, rect)

    fig, ax = plt.subplots()
    ax.add_patch(plt.Rectangle((rect[0], rect[2]), rect[1]-rect[0], rect[3]-rect[2], edgecolor='black', fill=False, linestyle='--'))
    ax.plot([x1, x2], [y1, y2], 'r--', label="Original Line")
    if clipped:
        ax.plot([clipped[0], clipped[2]], [clipped[1], clipped[3]], 'g-', label="Clipped Line")
    else:
        print("Line is completely outside the clipping window.")

    plt.title("Cohen–Sutherland Line Clipping")
    plt.xlabel("X"); plt.ylabel("Y"); plt.grid(True); plt.axis('equal'); plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
