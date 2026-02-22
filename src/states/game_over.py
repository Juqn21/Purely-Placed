import pygame
from .menu import Button

class GameOver:
    def __init__(self):
        self.btn_restart = Button(300, 400, 200, 60, "MENÚ", "MAIN_MENU")

    def handle_events(self, events):
        for e in events:
            if self.btn_restart.is_clicked(e): return "MAIN_MENU"
        return "GAME_OVER"

    def draw(self, screen):
        screen.fill((242, 177, 177))
        font = pygame.font.SysFont("Arial", 50)
        txt = font.render("¡NIVEL COMPLETADO!", True, (99, 66, 46))
        screen.blit(txt, (200, 200))
        self.btn_restart.draw(screen)