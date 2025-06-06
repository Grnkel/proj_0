import numpy as np
import matplotlib.pyplot as plt

class Ship:
    def __init__(self, ax, start_pos=(0, 0), speed=0, angle=0, color='r', trail_length=100, world=None):
        self.position = np.array(start_pos, dtype=float)    
        self.speed = speed
        self.angle = angle
        
        self.position0 = self.position 
        self.speed0 = self.speed 
        self.angle0 = self.angle 

        self.world = world
        self.target = None # TODO

        self.trail_length = trail_length
        self.history = [self.position.copy()]
        self.trail_dots = [ax.plot([], [], color + 'o', alpha=1.0)[0] for _ in range(trail_length)]

    @property
    def angle(self):
        return self._angle

    @angle.setter
    def angle(self, value):
        self._angle = value % (2 * np.pi)

    def update(self, dt):
        # updating next position
        dx = self.speed * np.cos(self.angle) * dt
        dy = self.speed * np.sin(self.angle) * dt
        self.position += np.array([dx, dy])

        # past position history
        self.history.insert(0, self.position.copy())
        if len(self.history) > self.trail_length:
            self.history.pop()

    def draw(self):
        # trailing dots with fading opacity
        for i, dot in enumerate(self.trail_dots):
            if i < len(self.history):
                x, y = self.history[i]
                dot.set_data(x, y)
                dot.set_alpha(np.exp(-6 * (i / self.trail_length))) 
            else:
                dot.set_data([], [])

        return self.trail_dots
