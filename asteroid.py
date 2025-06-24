import pygame
from constants import *
from circleshape import CircleShape
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
    

    def draw(self, screen):
        pygame.draw.circle(screen,"blue",self.position, self.radius,2)

    def update(self, dt):
        # Asteroids typically don't move or rotate in this simple implementation
        self.position += self.velocity * dt
    def split(self):
        self.kill()

        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20,50)

        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)
        # Create two new asteroids with reduced radius and new velocities
        new_radius = self.radius  - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = a * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = b * 1.2
            