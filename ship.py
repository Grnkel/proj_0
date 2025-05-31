import numpy as np
import matplotlib.pyplot as plt

class Ship:
    def __init__(self, ax, start_pos=(0, 0), speed=0, color='r'):
        self.position = np.array(start_pos, dtype=float)
        self.speed = speed
        self.angle = 0 

        self.plot, = ax.plot([], [], color + 'o') 

    def set_direction(self, angle_rad):
        self.angle = angle_rad

    def update(self, dt):
        dx = self.speed * np.cos(self.angle) * dt
        dy = self.speed * np.sin(self.angle) * dt
        self.position += np.array([dx, dy])

    def get_position(self):
        return self.position

    def draw(self):
        x, y = self.get_position()
        self.plot.set_data(x, y)
        return self.plot
