import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def get_cube():
    # Define the 8 vertices of a unit cube
    cube = np.array([
        [1, 1, 1, 1],
        [1, 1, -1, 1],
        [1, -1, 1, 1],
        [1, -1, -1, 1],
        [-1, 1, 1, 1],
        [-1, 1, -1, 1],
        [-1, -1, 1, 1],
        [-1, -1, -1, 1]
    ])
    return cube

def translate(cube, tx, ty, tz):
    T = np.array([[1, 0, 0, tx],
                  [0, 1, 0, ty],
                  [0, 0, 1, tz],
                  [0, 0, 0, 1]])
    return np.dot(cube, T.T)

def scale(cube, sx, sy, sz):
    S = np.array([[sx, 0, 0, 0],
                  [0, sy, 0, 0],
                  [0, 0, sz, 0],
                  [0, 0, 0, 1]])
    return np.dot(cube, S.T)

def rotate_x(cube, angle_deg):
    angle_rad = np.radians(angle_deg)
    R_x = np.array([[1, 0, 0, 0],
                    [0, np.cos(angle_rad), -np.sin(angle_rad), 0],
                    [0, np.sin(angle_rad), np.cos(angle_rad), 0],
                    [0, 0, 0, 1]])
    return np.dot(cube, R_x.T)

def rotate_y(cube, angle_deg):
    angle_rad = np.radians(angle_deg)
    R_y = np.array([[np.cos(angle_rad), 0, np.sin(angle_rad), 0],
                    [0, 1, 0, 0],
                    [-np.sin(angle_rad), 0, np.cos(angle_rad), 0],
                    [0, 0, 0, 1]])
    return np.dot(cube, R_y.T)

def rotate_z(cube, angle_deg):
    angle_rad = np.radians(angle_deg)
    R_z = np.array([[np.cos(angle_rad), -np.sin(angle_rad), 0, 0],
                    [np.sin(angle_rad), np.cos(angle_rad), 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]])
    return np.dot(cube, R_z.T)

def parallel_projection(cube):
    # Parallel (orthogonal) projection
    P = np.array([[1, 0, 0, 0],
                  [0, 1, 0, 0],
                  [0, 0, 0, 0],
                  [0, 0, 0, 1]])
    return np.dot(cube, P.T)

def perspective_projection(cube, d=3):
    # Perspective projection matrix
    P = np.array([[1, 0, 0, 0],
                  [0, 1, 0, 0],
                  [0, 0, 0, d],
                  [0, 0, 1/d, 0]])
    return np.dot(cube, P.T)

def plot_3d_object(cube, ax):
    # Plot the cube edges
    ax.clear()
    
    edges = [
        (0, 1), (1, 3), (3, 2), (2, 0), # Front face
        (4, 5), (5, 7), (7, 6), (6, 4), # Back face
        (0, 4), (1, 5), (2, 6), (3, 7)  # Connecting edges
    ]
    
    for edge in edges:
        ax.plot([cube[edge[0], 0], cube[edge[1], 0]],
                [cube[edge[0], 1], cube[edge[1], 1]],
                [cube[edge[0], 2], cube[edge[1], 2]], 'b')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title("3D Object Transformation")

def main():
    cube = get_cube()
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    print("Welcome to 3D Transformations and Projections!")
    
    while True:
        print("\nChoose a transformation to apply:")
        print("1. Translation")
        print("2. Scaling")
        print("3. Rotation")
        print("4. Parallel Projection")
        print("5. Perspective Projection")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            tx = float(input("Enter translation along X (tx): "))
            ty = float(input("Enter translation along Y (ty): "))
            tz = float(input("Enter translation along Z (tz): "))
            print("\nApplying Translation:")
            cube = translate(cube, tx, ty, tz)
            plot_3d_object(cube, ax)
            plt.draw()

        elif choice == '2':
            sx = float(input("Enter scaling factor along X (sx): "))
            sy = float(input("Enter scaling factor along Y (sy): "))
            sz = float(input("Enter scaling factor along Z (sz): "))
            print("\nApplying Scaling:")
            cube = scale(cube, sx, sy, sz)
            plot_3d_object(cube, ax)
            plt.draw()

        elif choice == '3':
            rotation_axis = input("Enter axis of rotation (x, y, z): ").lower()
            angle = float(input("Enter rotation angle (in degrees): "))
            print("\nApplying Rotation:")
            if rotation_axis == 'x':
                cube = rotate_x(cube, angle)
                axis = 'X'
            elif rotation_axis == 'y':
                cube = rotate_y(cube, angle)
                axis = 'Y'
            elif rotation_axis == 'z':
                cube = rotate_z(cube, angle)
                axis = 'Z'
            else:
                print("Invalid axis. Please choose x, y, or z.")
                continue
            plot_3d_object(cube, ax)
            plt.draw()

        elif choice == '4':
            print("\nApplying Parallel Projection:")
            cube = parallel_projection(cube)
            plot_3d_object(cube, ax)
            plt.draw()

        elif choice == '5':
            d = float(input("Enter depth factor for perspective projection (default 3): ") or 3)
            print("\nApplying Perspective Projection:")
            cube = perspective_projection(cube, d)
            plot_3d_object(cube, ax)
            plt.draw()

        elif choice == '6':
            print("Exiting program.")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 6.")

if __name__ == "__main__":
    plt.ion()  # Turn on interactive mode
    main()
    plt.show(block=True)  # Keep the plot open after the loop ends
