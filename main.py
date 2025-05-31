import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from ship import Ship  

fig, ax = plt.subplots()
ax.set_xlim(-100, 100)
ax.set_ylim(-100, 100)

# Create two ships
ship1 = Ship(ax, start_pos=(0, 50), speed=20, color='r')
ship2 = Ship(ax, start_pos=(0, -50), speed=10, color='b')
ship1.set_direction(np.pi / 2)  
ship2.set_direction(-np.pi / 2)

# Settings
framerate = 60
interpolants = range(100000)

def init():
    return ship1.draw(), ship2.draw()

def update(frame):
    dt = 1 / framerate
    ship1.angle += 1/100
    ship2.angle -= 1/100

    ship1.update(dt)
    ship2.update(dt)
    return ship1.draw(), ship2.draw()

ani = animation.FuncAnimation(
    fig, update, frames=interpolants, init_func=init,
    blit=True, interval=1000 / framerate
)

plt.show()
