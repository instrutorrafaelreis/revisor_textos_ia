import pygame

# Configurações da Janela
WIDTH = 800
HEIGHT = 600
FPS = 60
TITLE = "Peter Panela: O Robin Hood Digital"

# Cores (Paleta Temporária / Placeholders)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_GRAY = (40, 40, 40)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
COPPER = (184, 115, 51) # Cor da armadura de panela

# Configurações do Jogador
PLAYER_SPEED = 4
PLAYER_SPEED_STEALTH = 2
PLAYER_SPEED_RUN = 7
PLAYER_SIZE = 32

# Raio de Ruído (Visual/Detecção)
NOISE_RADIUS_STEALTH = 10
NOISE_RADIUS_WALK = 40
NOISE_RADIUS_RUN = 120

# Configurações dos Inimigos
ENEMY_SIZE = 32
ENEMY_SPEED = 2
ENEMY_VISION_RANGE = 150
ENEMY_VISION_ANGLE = 60 # Graus

# Estados do Jogo
STATE_MENU = 0
STATE_PLAYING = 1
STATE_HACKING = 2
STATE_GAME_OVER = 3
STATE_VICTORY = 4
