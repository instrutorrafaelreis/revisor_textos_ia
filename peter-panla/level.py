import pygame
from settings import *

class Level:
    def __init__(self):
        self.walls = []
        self.terminal_rect = pygame.Rect(700, 50, 60, 60)
        self.build_level()

    def build_level(self):
        # Create some basic walls (x, y, w, h)
        wall_data = [
            (0, 0, WIDTH, 20),
            (0, HEIGHT-20, WIDTH, 20),
            (0, 0, 20, HEIGHT),
            (WIDTH-20, 0, 20, HEIGHT),
            (300, 200, 200, 20),
            (300, 350, 20, 150),
            (600, 100, 20, 300)
        ]
        for w in wall_data:
            self.walls.append(pygame.Rect(*w))

    def draw(self, surface):
        for wall in self.walls:
            pygame.draw.rect(surface, BLUE, wall)
            
        # Draw Terminal
        pygame.draw.rect(surface, GREEN, self.terminal_rect)
