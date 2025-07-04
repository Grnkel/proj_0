import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import matplotlib

# my own classes
from ship import Ship  
from world import World

# backend
matplotlib.use('TkAgg')

# settings
FRAMERATE = 60
SIZE = 100

# init
world = World(FRAMERATE, SIZE)
ship0 = world.create_ship((0, 50), 100, 0, 'r')
ship1 = world.create_ship((-25, -25), 70, -np.pi/2, 'b')
ship2 = world.create_ship((0, 0), 100, -np.pi/4, 'g')
ship2 = world.create_ship((70, 70), 100, 5 * np.pi/4, 'y')

# functions
def border(ship: Ship):
    x1, y1 = ship.position
    world_angle = np.mod(np.arctan2(y1, x1), 2*np.pi)
    cartesian_distance = np.sqrt(np.square(x1) + np.square(y1))
    delta_angle = world_angle - ship.angle
    print(np.rad2deg(delta_angle)) 

def rotate_ship(ship: Ship):
    ship.angle -= ship.speed / (world.size/2) * (1 / FRAMERATE)

def robot(ship_0: Ship, ship_1: Ship):
    dx = ship_0.position[0] - ship_1.position[0]
    dy = ship_0.position[1] - ship_1.position[1]
    
    ship_1.angle = np.arctan2(dy, dx)
    proximity = np.sqrt(np.square(dy) + np.square(dx))
    if proximity < 3:
        print("BOOM")
        input()

def slowdown(ship: Ship, acceleration: float):
    ship.speed -= acceleration * world.physics_dt

# init functions
world.add_function(lambda: border(ship1))
world.add_function(lambda: rotate_ship(ship0))
world.add_function(lambda: robot(ship0, ship1))
world.add_function(lambda: slowdown(ship2, 10))




# start simulation
world.start()
