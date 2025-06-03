import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

from ship import Ship  
from world import World

# settings
framerate = 60
frames = range(100000)
size = 100

# init
world = World(framerate, frames, size)

ship1 = world.create_ship((0, 50), 150, 0, 'r', 20)
ship2 = world.create_ship((-25, -25), 70, -np.pi/2, 'b', 20)
ship3 = world.create_ship((0, 0), 200, -np.pi/4 + 0.2, 'g', 20)

# functions
def border():
    x1,y1 = ship3.position
    world_angle = (np.arctan(y1/x1) + np.pi * min(x1, 0) / x1) % (2*np.pi)
    pos_angle = (world_angle + np.pi/2) % (2*np.pi)
    neg_angle = (world_angle - np.pi/2) % (2*np.pi)
    cartesian_dist = np.sqrt(np.square(x1) + np.square(y1))

    if (ship3.angle - world_angle < np.pi/2) and (ship3.angle - world_angle > 0):
        closest = pos_angle
    elif (ship3.angle - world_angle < 0) and (ship3.angle - world_angle > -np.pi/2):
        closest = neg_angle
    else:
        closest = None
    if closest != None:
        
        print(round(np.rad2deg(closest),2), "\t", round(np.rad2deg(ship3.angle),2))


    #ship3.speed = ship3.speed0 * (1 - dist / (world.size*0.5))
    #print((1 - dist / (world.size)))
    #ship3.angle += 
    #print(np.rad2deg(world_angle))

def rotate_ship():
    ship1.angle -= ship1.speed / (world.size/2) * (1 / framerate)

def robot():
    dx = ship1.position[0] - ship2.position[0]
    dy = ship1.position[1] - ship2.position[1]
    ship2.angle = np.arctan(dy/dx) + np.pi * min(dx, 0) / dx 
    proximity = np.sqrt(np.square(dx) + np.square(dy))
    if proximity < 3:
        print("BOOM")
        input()

world.add_function(border)
world.add_function(robot)
world.add_function(rotate_ship)

# start simulation
world.start()
