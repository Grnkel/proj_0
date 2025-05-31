import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()
point, = plt.plot([], [], 'ro')

interpolants = range(1000000)
framerate = 60 # [hz]
v0 = 10 # [coord / s]

def rotate(x, y, rad):
    rot_matrix = np.array([
        [np.cos(rad), -np.sin(rad)],
        [np.sin(rad),  np.cos(rad)]
    ])
    vector = np.array([[x],
                       [y]])
    rotated = rot_matrix @ vector
    return rotated[0, 0], rotated[1, 0]

def init():
    ax.set_xlim(-100, 100)   # centered around 0
    ax.set_ylim(-100, 100)   # centered around 0
    return point,

def update_rotation(t):
    radius = 70
    x0,y0 = 0,radius
    
    x,y = rotate(x0,y0,np.deg2rad(t))    

    point.set_data(x, y)
    return point,

ani = animation.FuncAnimation(
    fig,
    update_rotation,
    frames=interpolants,
    init_func=init,
    blit=True,
    interval=1000 / framerate  # milliseconds per frame
)

plt.show()
