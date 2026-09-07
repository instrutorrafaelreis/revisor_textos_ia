import pygame
from settings import *
from database import get_all_alunos, update_nota

class HackingMinigame:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("courier", 24)
        self.input_text = ""
        self.logs = [
            "Conectado ao DB da Escola.",
            "Comandos: listar, update <nome> <nota>, sair",
            "> "
        ]
        self.active = False
        self.done = False
        
        # Otimização: Criar superfície translúcida apenas uma vez
        self.overlay = pygame.Surface((WIDTH, HEIGHT))
        self.overlay.set_alpha(200)
        self.overlay.fill(BLACK)

    def handle_event(self, event):
        if not self.active:
            return
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.process_command(self.input_text.strip())
                self.input_text = ""
            elif event.key == pygame.K_BACKSPACE:
                self.input_text = self.input_text[:-1]
            elif event.key == pygame.K_ESCAPE:
                self.active = False
            else:
                self.input_text += event.unicode

    def process_command(self, cmd):
        self.logs[-1] = "> " + cmd
        if cmd == "listar":
            alunos = get_all_alunos()
            for a in alunos:
                self.logs.append(f"{a[0]}: {a[1]}")
        elif cmd.startswith("update"):
            parts = cmd.split()
            if len(parts) == 3:
                nome = parts[1]
                nota = parts[2]
                if update_nota(nome, nota):
                    self.logs.append(f"Nota de {nome} alterada para {nota}")
                    self.check_win()
                else:
                    self.logs.append(f"Aluno {nome} não encontrado.")
            else:
                self.logs.append("Uso: update <nome> <nota>")
        elif cmd == "sair":
            self.active = False
        else:
            self.logs.append("Comando inválido.")
            
        self.logs.append("> ")
        # Keep only last 15 lines
        if len(self.logs) > 15:
            self.logs = self.logs[-15:]

    def check_win(self):
        alunos = get_all_alunos()
        all_a = all(a[1] == 'A' for a in alunos)
        if all_a:
            self.logs.append("SISTEMA COMPROMETIDO. MISSÃO CUMPRIDA!")
            self.done = True

    def draw(self):
        if not self.active:
            return
            
        # Draw transparent background (cached)
        self.screen.blit(self.overlay, (0,0))
        
        y = 50
        for line in self.logs[:-1]:
            text_surface = self.font.render(line, True, GREEN)
            self.screen.blit(text_surface, (50, y))
            y += 30
            
        # Draw current input
        current_line = self.logs[-1] + self.input_text
        text_surface = self.font.render(current_line, True, GREEN)
        self.screen.blit(text_surface, (50, y))
