
#This is the file for the actual asteroids
import pygame
import random
from constants import *
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, 2)
        self.radius=radius

    def split(self):
        self.kill()
        if self.radius<=ASTEROID_MIN_RADIUS:
            return
        ast_angle=random.uniform(20,50)
        vector_a = self.velocity.rotate(ast_angle)
        vector_b = self.velocity.rotate(-ast_angle)
        new_radius=self.radius-ASTEROID_MIN_RADIUS
        asteroid=Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity=vector_a * 1.2
        asteroid=Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity=vector_b * 1.2
        
        

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        #forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += self.velocity * dt
        
