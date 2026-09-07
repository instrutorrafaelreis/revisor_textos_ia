import pygame
import math
from settings import *

class Enemy:
    def __init__(self, x, y, path):
        self.rect = pygame.Rect(x, y, ENEMY_SIZE, ENEMY_SIZE)
        self.color = RED
        self.path = path # List of tuples (x, y)
        self.current_target_index = 0
        self.speed = ENEMY_SPEED
        self.state = 'PATROL'
        self.angle = 0 # Radians
        self.chase_target = None

    def update(self, player_center, player_noise):
        if self.state == 'PATROL':
            self.patrol()
            self.check_vision_and_hearing(player_center, player_noise)
        elif self.state == 'CHASE':
            self.chase(player_center)

    def patrol(self):
        if not self.path:
            return
            
        target = self.path[self.current_target_index]
        dx = target[0] - self.rect.centerx
        dy = target[1] - self.rect.centery
        distance = math.hypot(dx, dy)
        
        if distance < self.speed:
            self.current_target_index = (self.current_target_index + 1) % len(self.path)
        else:
            self.rect.x += (dx / distance) * self.speed
            self.rect.y += (dy / distance) * self.speed
            self.angle = math.atan2(dy, dx)

    def chase(self, target_pos):
        dx = target_pos[0] - self.rect.centerx
        dy = target_pos[1] - self.rect.centery
        distance = math.hypot(dx, dy)
        
        if distance > 0:
            self.rect.x += (dx / distance) * (self.speed * 1.5)
            self.rect.y += (dy / distance) * (self.speed * 1.5)
            self.angle = math.atan2(dy, dx)
            
        # Give up if too far
        if distance > ENEMY_VISION_RANGE * 2:
            self.state = 'PATROL'

    def check_vision_and_hearing(self, p_center, p_noise):
        # Check Hearing
        dx = p_center[0] - self.rect.centerx
        dy = p_center[1] - self.rect.centery
        distance = math.hypot(dx, dy)
        
        if distance < p_noise: # Heard the player!
            self.state = 'CHASE'
            return
            
        # Check Vision
        if distance < ENEMY_VISION_RANGE:
            angle_to_player = math.atan2(dy, dx)
            # Normalize angles
            diff = (angle_to_player - self.angle + math.pi) % (2 * math.pi) - math.pi
            if abs(math.degrees(diff)) < ENEMY_VISION_ANGLE / 2:
                # In cone! (Ignoring walls for simplicity in prototype)
                self.state = 'CHASE'

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        
        # Draw Vision Cone
        end_x1 = self.rect.centerx + ENEMY_VISION_RANGE * math.cos(self.angle - math.radians(ENEMY_VISION_ANGLE/2))
        end_y1 = self.rect.centery + ENEMY_VISION_RANGE * math.sin(self.angle - math.radians(ENEMY_VISION_ANGLE/2))
        
        end_x2 = self.rect.centerx + ENEMY_VISION_RANGE * math.cos(self.angle + math.radians(ENEMY_VISION_ANGLE/2))
        end_y2 = self.rect.centery + ENEMY_VISION_RANGE * math.sin(self.angle + math.radians(ENEMY_VISION_ANGLE/2))
        
        points = [self.rect.center, (end_x1, end_y1), (end_x2, end_y2)]
        pygame.draw.polygon(surface, (255, 100, 100, 50), points, 1) # Just an outline
