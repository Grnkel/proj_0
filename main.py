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

red = world.create_ship((0, 50), 100, 0, 'r')
blue = world.create_ship((-25, -25), 70, -np.pi/2, 'b')
green = world.create_ship((0, 0), 50, -np.pi/4, 'g')
yellow = world.create_ship((70, 70), 100, 5 * np.pi/4, 'y')

def control_force(ship: Ship, radius):
    dist = np.linalg.norm(ship.position)
    if dist > radius:
        direction = ship.position / dist
        print(direction)
        # Apply a spring-like restoring force
        force = -direction * (dist - radius) * 10
        ship.speed += force * (1 / FRAMERATE)

# functions
def border(ship: Ship):
    x1, y1 = ship.position
    world_angle = np.arctan2(y1, x1)
    delta_angle = world_angle - ship.angle - np.pi
    #ship.angle -= delta_angle
    
    print(round(np.rad2deg(world_angle)), "\t", round(np.rad2deg(ship.angle)), "\t", round(np.rad2deg(delta_angle)))

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
world.add_function(lambda: border(red))
world.add_function(lambda: rotate_ship(red))
world.add_function(lambda: robot(red, blue))
world.add_function(lambda: slowdown(yellow, 10))

world.add_function(lambda: control_force(green, SIZE))




# start simulation
world.start()
