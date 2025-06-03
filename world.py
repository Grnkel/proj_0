import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from ship import Ship  

class World():
    def __init__(self, framerate, frames, size, max_turn=1, max_speed=1):
        self.framerate = framerate
        self.frames = frames
        self.size = size
        self.entities = []
        self.functions = []

        self.max_turn = max_turn
        self.max_speed = max_speed

        self.fig, self.ax = plt.subplots()
        self.ax.set_xlim(-size, size)
        self.ax.set_ylim(-size, size)

    def create_ship(self, *args, **kwargs):
        kwargs['world'] = self
        ship = Ship(self.ax, *args, **kwargs)
        return self.add_ship(ship)

    def add_ship(self, ship):
        self.entities.append(ship)
        return ship
    
    def add_function(self, func):
        # adds new function to world
        self.functions.append(func) 

    def draw_entities(self):
        draw = []
        for ship in self.entities: 
            draw += ship.draw()
        return draw

    def update(self, frame):
        for function in self.functions:
            function()

        for ship in self.entities:
            ship.update(1 / self.framerate)
        
        # giving world torus shape
        shift = ((ship.position + self.size) % (2 * self.size))
        ship.position = shift - self.size 

        return self.draw_entities()
    
    def start(self):
        ani = animation.FuncAnimation( 
            fig=self.fig, 
            func=self.update, 
            frames=self.frames, 
            init_func=self.draw_entities,
            blit=True, 
            interval=1000 / self.framerate
        )
        plt.show()

