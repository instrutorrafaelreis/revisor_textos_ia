import pygame
import math
from settings import *

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PLAYER_SIZE, PLAYER_SIZE)
        self.color = COPPER
        self.speed = PLAYER_SPEED
        self.noise_radius = NOISE_RADIUS_WALK
        
        # Stats
        self.esfirras = 0
        self.has_admin_pass = False

    def handle_keys(self):
        keys = pygame.key.get_pressed()
        
        # Determine speed and noise
        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            self.speed = PLAYER_SPEED_RUN
            self.noise_radius = NOISE_RADIUS_RUN
        elif keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]:
            self.speed = PLAYER_SPEED_STEALTH
            self.noise_radius = NOISE_RADIUS_STEALTH
        else:
            self.speed = PLAYER_SPEED
            self.noise_radius = NOISE_RADIUS_WALK

        # Calculate movement
        dx, dy = 0, 0
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            dy -= self.speed
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            dy += self.speed
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            dx -= self.speed
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            dx += self.speed
            
        # Normalize diagonal movement
        if dx != 0 and dy != 0:
            length = math.hypot(dx, dy)
            dx = (dx / length) * self.speed
            dy = (dy / length) * self.speed

        return dx, dy

    def move(self, dx, dy, walls):
        # Move on X
        self.rect.x += dx
        self.collide_with_walls(dx, 0, walls)
        
        # Move on Y
        self.rect.y += dy
        self.collide_with_walls(0, dy, walls)

    def collide_with_walls(self, dx, dy, walls):
        for wall in walls:
            if self.rect.colliderect(wall):
                if dx > 0:
                    self.rect.right = wall.left
                if dx < 0:
                    self.rect.left = wall.right
                if dy > 0:
                    self.rect.bottom = wall.top
                if dy < 0:
                    self.rect.top = wall.bottom

    def update(self, walls):
        dx, dy = self.handle_keys()
        self.move(dx, dy, walls)
        
        # Only make noise if moving
        if dx == 0 and dy == 0:
            self.noise_radius = 0

    def draw(self, surface):
        # Draw Noise Circle (Visual Feedback)
        if self.noise_radius > 0:
            pygame.draw.circle(surface, (100, 100, 100), self.rect.center, self.noise_radius, 1)
        # Draw Player
        pygame.draw.rect(surface, self.color, self.rect)

    def get_center(self):
        return self.rect.center
