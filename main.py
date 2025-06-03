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
ship1 = world.create_ship(start_pos=(0, 50), speed=20, color='r', trail_length=20)
ship2 = world.create_ship(start_pos=(0, -50), speed=5, color='b', trail_length=20)

ship1.set_direction(0)  
ship2.set_direction(-np.pi)  

# world function
def function():
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

world.add_function(function)

# start simulation

world.start()
