import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

from ship import Ship  
from world import World

# settings
framerate = 60
frames = range(100000)
size = 100

# world
world = World(framerate, frames, size)

# ships
ship1 = Ship(world.ax, (0, 50), 100, 0, 'r', 20)
ship2 = Ship(world.ax, (-25, -25), 50, -np.pi, 'b', 20)

world.add_ship(ship1)
world.add_ship(ship2)

def torus():
    ship2.position = ((ship2.position + world.size) % (2 * world.size)) - world.size

# functions
def border():
    radius = 75

    pass

def rotate_ship():
    ship1.angle -= ship1.speed / (world.size/2) * (1 / framerate)

def robot():
    dx = ship1.position[0] - ship2.position[0]
    dy = ship1.position[1] - ship2.position[1]

    if dx > 0:
        new_angle = np.arctan(dy/dx)
    else:
        new_angle = np.arctan(dy/dx) + np.pi

    ship2.angle = new_angle
    #print(round(np.rad2deg(new_angle),3), "\t ", (round(dx,1),round(dy,1)))

    proximity = np.sqrt(np.square(dx) + np.square(dy))
    if proximity < 3:
        print("BOOM")
        input()

#world.add_function(robot)
world.add_function(rotate_ship)
world.add_function(torus)

# start simulation
world.start()
