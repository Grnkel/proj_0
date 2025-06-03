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

    def create_ship(self, start_pos=(0, 0), speed=0, color='b', trail_length=0):
        ship = Ship(self.ax, start_pos, speed, color, trail_length)
        self.entities.append(ship)
        return ship
    
    def add_function(self, func):
        self.functions.append(func) # adds new function to world

    def draw_entities(self):
        draw = []
        for ship in self.entities: # returns new points
            draw += ship.draw()
        return draw

    def update(self, frame):
        for function in self.functions: # activates all functions
            function()

        for ship in self.entities: # updates all ships
            ship.update(1 / self.framerate) 

        return self.draw_entities()
    
    def start(self):
        ani = animation.FuncAnimation( # you need to have a variable for this
            fig=self.fig, 
            func=self.update, 
            frames=self.frames, 
            init_func=self.draw_entities,
            blit=True, 
            interval=1000 / self.framerate
        )

        plt.show()

