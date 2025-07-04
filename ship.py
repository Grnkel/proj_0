import numpy as np

class Ship:
    def __init__(self, ax, start_pos=(0, 0), speed=0, angle=0, color='r', tail_strength=15):
        self.position = np.array(start_pos, dtype=float)
        self.speed = speed
        self.angle = angle
        self.color = color
        self.ax = ax
        self.tail_strength = tail_strength
        self.history = []
        self.tail_dots = [] 

    @property
    def angle(self):
        return self._angle

    @angle.setter
    def angle(self, value):
        self._angle = value % (2 * np.pi)

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        self._speed = max(0, value)

    def update(self, dt):
        # updating next position
        dx = self.speed * np.cos(self.angle) * dt
        dy = self.speed * np.sin(self.angle) * dt
        self.position += np.array([dx, dy])
        # past position history
        self.history.insert(0, self.position.copy())
        dots_needed = max(int(self.tail_strength * (dt * (self.speed))), 1)
        # add or remove dots based on the number needed
        if len(self.tail_dots) <= dots_needed:
            new_dot = self.ax.plot([], [], self.color + 'o', alpha=1.0, markersize=10)[0]
            self.tail_dots.append(new_dot)
        elif len(self.tail_dots) > dots_needed:
            dot = self.tail_dots.pop()
            dot.remove()
        # trim history regularly
        if len(self.history) - len(self.tail_dots) > 10:
            self.history = self.history[:len(self.tail_dots)]

    def draw(self):
        # Update existing trail dots instead of creating new ones
        for i, tail_dot in enumerate(self.tail_dots):
            if i < len(self.history):
                x, y = self.history[i]
                tail_dot.set_data([x], [y])
                fraq = i / len(self.tail_dots)
                
                alpha = np.exp(-4 * fraq)
                tail_dot.set_markersize(10 * alpha)
                tail_dot.set_alpha(alpha)
            else:
                tail_dot.set_data([], [])
        
        return self.tail_dots
