import pygame
from .menu import Button

class LevelSelector:
    def __init__(self):
        self.buttons = []
        for i in range(5):
            x = 100 + (i * 125)
            self.buttons.append(Button(x, 250, 100, 100, f"{i+1}", f"LEVEL {i+1}"))
        self.btn_back = Button(20, 20, 100, 40, "Back", "MAIN_MENU")

    def handle_events(self, events):
        for e in events:
            if self.btn_back.is_clicked(e): return "MAIN_MENU"
            for b in self.buttons:
                if b.is_clicked(e): return b.target
        return "SELECTOR"

    def draw(self, screen):
        screen.fill((225, 238, 221))
        self.btn_back.draw(screen)
        for b in self.buttons:
            b.draw(screen)

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