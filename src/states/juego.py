import pygame
from src.states.menu import Button

class Level:
    def __init__(self, num):
        self.num = num
        self.font = pygame.font.SysFont("Arial", 40)

    def handle_events(self, events):
        for e in events:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_m: return "SELECTOR"
                if e.key == pygame.K_p: return "GAME_OVER" 
        return f"LEVEL {self.num}"

    def draw(self, screen):
        screen.fill((255, 255, 255))
        txt = self.font.render(f"JUGANDO NIVEL {self.num}", True, (50, 50, 50))
        hint = self.font.render("'P' para Ganar | 'M' para Menú", True, (150, 150, 150))
        screen.blit(txt, (250, 200))
        screen.blit(hint, (180, 300))