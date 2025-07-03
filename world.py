import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from ship import Ship  
import time

class World():
    def __init__(self, framerate, size):
        self.framerate = framerate
        self.size = size

        self.entities = []
        self.functions = []

        self.timer = FrameTimer(self, 10)
        self.frametime_ms = 0

        self.fig, self.ax = plt.subplots()
        self.ax.set_xlim(-size, size)
        self.ax.set_ylim(-size, size)

    def create_ship(self, *args, **kwargs):
        # constructor for ships
        kwargs['world'] = self
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
        #update timer
        self.timer.check()
        
        # updating functions and ships
        for function in self.functions:
            function()
        for ship in self.entities:
            assert(type(ship) == Ship)
            ship.update(1 / self.framerate)
            # giving world torus shape
            shift = ((ship.position + self.size) % (2 * self.size))
            ship.position = shift - self.size 

        # update timer
        self.timer.check()
        return self.draw_entities()
    
    def start(self):
        # starts animation
        ani = animation.FuncAnimation( 
            fig=self.fig, 
            func=self.update, 
            interval=1000 / self.framerate - self.frametime_ms,
            blit=True,
            cache_frame_data=False
        )
        plt.show()

class FrameTimer():
    # class for checking frametimes
    def __init__(self, world: World, width):
        # init necessary class variables
        self.world = world
        self.width = width
        self.history = np.zeros(width)
        self.time = time.perf_counter()
        self.index = 0

    def check(self):
        # updates world with time since last check
        result = time.perf_counter() - self.time
        self.time = time.perf_counter()
        self.history[self.index] = result
        self.index = (self.index + 1) % self.width
        self.world.frametime_ms = np.mean(self.history)
        
