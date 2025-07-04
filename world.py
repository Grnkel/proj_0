import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import time

# own classes
from ship import Ship  

class World():
    def __init__(self, framerate, size):
        # initializing world
        self.size = size
        self.entities = []
        self.functions = []
        # fixed physics time step
        self.framerate = framerate
        self.physics_dt = 1.0 / framerate
        self.accumulated_time = 0.0
        self.last_time = time.perf_counter()
        # creating figure and axes
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlim(-size, size)
        self.ax.set_ylim(-size, size)

    def create_ship(self, *args, **kwargs):
        # constructor for ships
        ship = Ship(self.ax, *args, **kwargs)
        return self.add_entity(ship)

    def add_entity(self, ship):
        self.entities.append(ship)
        return ship
    
    def add_function(self, func):
        # adds new function to world
        self.functions.append(func) 

    def draw_entities(self):
        # drawing all entities
        draw = []
        for ship in self.entities: 
            draw += ship.draw()
        return draw

    def update(self, frame):
        # calculate real elapsed time
        current_time = time.perf_counter()
        frame_time = current_time - self.last_time
        self.last_time = current_time
        # accumulate time and run physics in fixed time steps
        self.accumulated_time += frame_time
        # run deterministic simulation with fixed time steps
        while np.greater_equal(self.accumulated_time, self.physics_dt):
            # updating functions and ships with fixed dt
            for function in self.functions:
                function()
            for ship in self.entities:
                ship.update(self.physics_dt)
                # giving world torus shape
                shift = np.mod((ship.position + self.size), (2 * self.size))
                ship.position = shift - self.size 
            self.accumulated_time -= self.physics_dt
        return self.draw_entities()
    
    def start(self):
        # starts animation
        ani = animation.FuncAnimation( 
            fig=self.fig, 
            func=self.update, 
            interval=0,
            blit=False, # put to True if slow
            cache_frame_data=False
        )
        plt.show()
        
