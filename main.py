import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()

point1, = plt.plot([], [], 'ro')  # red point
point2, = plt.plot([], [], 'bo')  # blue point

interpolants = range(1000000)
framerate = 60

def rotate(x, y, rad):
    rot_matrix = np.array([
        [np.cos(rad), -np.sin(rad)],
        [np.sin(rad),  np.cos(rad)]
    ])
    vector = np.array([[x], [y]])
    rotated = rot_matrix @ vector
    return rotated[0, 0], rotated[1, 0]

def init():
    ax.set_xlim(-100, 100)
    ax.set_ylim(-100, 100)
    return point1, point2

def update_rotation(t):
    angle = np.deg2rad(t)

    # First point rotates at radius 50
    x1, y1 = rotate(0, 50, angle)
    point1.set_data(x1, y1)

    # Second point rotates at radius 30
    x2, y2 = rotate(0, 30, -angle)  # rotating in opposite direction
    point2.set_data(x2, y2)

    return point1, point2

ani = animation.FuncAnimation(
    fig,
    update_rotation,
    frames=interpolants,
    init_func=init,
    blit=True,
    interval=1000 / framerate
)

plt.show()
