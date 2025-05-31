import numpy as np
import matplotlib.pyplot as plt

class Ship:
    def __init__(self, ax, start_pos=(0, 0), speed=0, color='r', trail_length=20):
        self.position = np.array(start_pos, dtype=float)
        self.speed = speed
        self.angle = 0

        self.trail_length = trail_length
        self.history = [self.position.copy()]  # list of past positions
        self.trail_dots = [ax.plot([], [], color + 'o', alpha=1.0)[0] for _ in range(trail_length)]

    def set_direction(self, angle_rad):
        self.angle = angle_rad

    def update(self, dt):
        dx = self.speed * np.cos(self.angle) * dt
        dy = self.speed * np.sin(self.angle) * dt
        self.position += np.array([dx, dy])

        # Update position history
        self.history.insert(0, self.position.copy())  # newest at the front
        if len(self.history) > self.trail_length:
            self.history.pop()

    def get_position(self):
        return self.position

    def draw(self):
        # Update each trailing dot with position and fading alpha
        for i, dot in enumerate(self.trail_dots):
            if i < len(self.history):
                x, y = self.history[i]
                dot.set_data(x, y)
                dot.set_alpha(1.0 - i / self.trail_length)  # fade with index
            else:
                dot.set_data([], [])

        return self.trail_dots  # return list of Line2D objects
