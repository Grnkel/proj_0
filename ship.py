import numpy as np
import matplotlib.pyplot as plt

class Ship:
    def __init__(self, ax, start_pos=(0, 0), speed=0, angle=0, color='r', trail_length=100, world=None):
        self.world = world  # Optional reference to the World instance
        self.position = np.array(start_pos, dtype=float)
        self.position0 = self.position 
        self.speed = speed
        self.speed0 = self.speed 
        self.angle = angle
        self.angle0 = self.angle 

        self.target = None

        self.trail_length = trail_length
        self.history = [self.position.copy()]
        self.trail_dots = [ax.plot([], [], color + 'o', alpha=1.0)[0] for _ in range(trail_length)]

    def update(self, dt):
        dx = self.speed * np.cos(self.angle) * dt
        dy = self.speed * np.sin(self.angle) * dt
        self.position += np.array([dx, dy])

        # Update position history
        self.history.insert(0, self.position.copy())  # newest at the front
        if len(self.history) > self.trail_length:
            self.history.pop()

    def draw(self):
        # Update each trailing dot with position and fading alpha
        for i, dot in enumerate(self.trail_dots):
            if i < len(self.history):
                x, y = self.history[i]
                dot.set_data(x, y)
                dot.set_alpha(np.exp(-6 * (i / self.trail_length)))  # fade with index
            else:
                dot.set_data([], [])

        return self.trail_dots  # return list of Line2D objects
