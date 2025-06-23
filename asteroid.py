import pygame
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
    

    def draw(self, screen):
        pygame.draw.circle(screen,"blue",self.position, self.radius,2)

    def update(self, dt):
        # Asteroids typically don't move or rotate in this simple implementation
        self.position += self.velocity * dt