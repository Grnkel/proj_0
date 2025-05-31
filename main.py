import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

from ship import Ship  

# Settings
framerate = 60
interpolants = range(100000)
world_size = 100

fig, ax = plt.subplots()
ax.set_xlim(-world_size, world_size)
ax.set_ylim(-world_size, world_size)

# Create two ships
ship1 = Ship(ax, start_pos=(0, 50), speed=20, color='r')
ship2 = Ship(ax, start_pos=(0, -50), speed=10, color='b')

ship1.set_direction(0)  
ship2.set_direction(-np.pi)


def init():
    return ship1.draw() + ship2.draw()

def update(frame):
    dt = 1 / framerate

    dx = ship1.position[0] - ship2.position[0]
    dy = ship1.position[1] - ship2.position[1]

    if dx > 0:
        new_angle = np.arctan(dy/dx)
    else:
        new_angle = np.arctan(dy/dx) + np.pi

    ship1.angle -= 1/100
    ship2.angle = new_angle
    print(round(np.rad2deg(new_angle),3), "\t ", (round(dx,1),round(dy,1)))

    proximity = np.sqrt(np.square(dx) + np.square(dy))
    if proximity < 3:
        print("BOOM")
        input()

    ship1.update(dt)
    ship2.update(dt)
    return ship1.draw() + ship2.draw()

ani = animation.FuncAnimation(
    fig, update, frames=interpolants, init_func=init,
    blit=True, interval=1000 / framerate
)

plt.show()
