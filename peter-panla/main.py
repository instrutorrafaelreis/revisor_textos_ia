import pygame
import sys
import asyncio
from settings import *
from player import Player
from enemy import Enemy
from level import Level
from hacking_minigame import HackingMinigame
from database import init_db

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.state = STATE_MENU
        self.running = True
        self.font = pygame.font.SysFont(None, 48)
        
        # Init DB
        init_db()
        
        self.reset_level()

    def reset_level(self):
        self.level = Level()
        self.player = Player(50, 50)
        # Add an enemy with a patrol path
        self.enemies = [
            Enemy(100, 400, [(100, 400), (500, 400), (500, 100), (100, 100)])
        ]
        self.hacking = HackingMinigame(self.screen)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if self.state == STATE_MENU:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.state = STATE_PLAYING
            
            elif self.state == STATE_PLAYING:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.state = STATE_MENU
                    elif event.key == pygame.K_e:
                        # Check interaction
                        if self.player.rect.colliderect(self.level.terminal_rect):
                            self.state = STATE_HACKING
                            self.hacking.active = True
                            
            elif self.state == STATE_HACKING:
                self.hacking.handle_event(event)
                if not self.hacking.active:
                    self.state = STATE_PLAYING
                if self.hacking.done:
                    self.state = STATE_VICTORY
                    
            elif self.state == STATE_GAME_OVER or self.state == STATE_VICTORY:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.reset_level()
                        self.state = STATE_PLAYING
                    elif event.key == pygame.K_ESCAPE:
                        self.state = STATE_MENU

    def update(self):
        if self.state == STATE_PLAYING:
            self.player.update(self.level.walls)
            
            for enemy in self.enemies:
                enemy.update(self.player.get_center(), self.player.noise_radius)
                if enemy.state == 'CHASE' and enemy.rect.colliderect(self.player.rect):
                    self.state = STATE_GAME_OVER

    def draw(self):
        if self.state == STATE_MENU:
            self.screen.fill(BLACK)
            text = self.font.render("Peter Panela - Pressione ENTER", True, COPPER)
            self.screen.blit(text, text.get_rect(center=(WIDTH/2, HEIGHT/2)))
            
        elif self.state == STATE_PLAYING or self.state == STATE_HACKING:
            self.screen.fill(DARK_GRAY)
            self.level.draw(self.screen)
            self.player.draw(self.screen)
            for enemy in self.enemies:
                enemy.draw(self.screen)
                
            # UI text
            ui_text = self.font.render("E para Hackear Terminal (Verde)", True, WHITE)
            self.screen.blit(ui_text, (10, 10))
            
            if self.state == STATE_HACKING:
                self.hacking.draw()
                
        elif self.state == STATE_GAME_OVER:
            self.screen.fill(BLACK)
            text = self.font.render("FOGO NA PANELA! VOCE FOI PEGO!", True, RED)
            self.screen.blit(text, text.get_rect(center=(WIDTH/2, HEIGHT/2)))
            sub = self.font.render("Pressione R para reiniciar", True, WHITE)
            self.screen.blit(sub, sub.get_rect(center=(WIDTH/2, HEIGHT/2 + 50)))
            
        elif self.state == STATE_VICTORY:
            self.screen.fill(BLACK)
            text = self.font.render("NOTAS ALTERADAS! VITORIA!", True, GREEN)
            self.screen.blit(text, text.get_rect(center=(WIDTH/2, HEIGHT/2)))
            sub = self.font.render("Pressione R para reiniciar", True, WHITE)
            self.screen.blit(sub, sub.get_rect(center=(WIDTH/2, HEIGHT/2 + 50)))

        pygame.display.flip()

    async def run(self):
        while self.running:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
            await asyncio.sleep(0)  # Requerido pelo Pygbag no navegador
            
        pygame.quit()
        sys.exit()

async def main():
    game = Game()
    await game.run()

if __name__ == "__main__":
    asyncio.run(main())
