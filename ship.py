import matplotlib.lines
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

class Ship:
    def __init__(self, ax, start_pos=(0, 0), speed=0, angle=0, color='r', tail_length=10): # TODO typdeklarera
        self.position = np.array(start_pos, dtype=float)
        self.speed = speed
        self.angle = angle
        self.color = color
        self.ax = ax
        self.tail_length = tail_length
        self.history = []
        self.tail_dots = [] 

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
        dots_needed = int(self.tail_length / (dt * self.speed)) if self.speed > 0 else 1
        # Add more trail dots if we need them TODO TODO
        if len(self.tail_dots) < dots_needed:
            new_dot = self.ax.plot([], [], self.color + 'o', alpha=1.0)[0]
            self.tail_dots.append(new_dot)
        elif len(self.tail_dots) > dots_needed:
            dot = self.tail_dots.pop()
            dot.remove() 
        # Trim history to match available dots
        self.history = self.history[:len(self.tail_dots)]

    def draw(self):
        # Update existing trail dots instead of creating new ones
        for i, tail_dot in enumerate(self.tail_dots):
            assert(type(tail_dot) == matplotlib.lines.Line2D)
            x, y = self.history[i]
            tail_dot.set_data([x], [y])
            fraq = i / len(self.tail_dots)
            tail_dot.set_markersize(10 * (1-fraq))
            alpha = np.exp(-6 * fraq) # TODO
            tail_dot.set_alpha(alpha)
        
        return self.tail_dots
