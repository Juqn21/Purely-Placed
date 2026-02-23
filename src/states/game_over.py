import pygame
from .menu import Button

class GameOver:
    def __init__(self):
        self.btn_menu = Button(400, 400, 200, 60, "MENÚ", "MAIN_MENU")
        self.btn_next = Button(650, 400, 250, 60, "SIGUIENTE NIVEL", "NEXT_LEVEL")
        self.current_level = 1

    def handle_events(self, events):
        if self.btn_menu.is_clicked_no_event():
            return "MAIN_MENU"
        if self.btn_next.is_clicked_no_event():
            next_level = self.current_level + 1
            if next_level <= 3:
                return f"LEVEL_{next_level}"
            else:
                return "MAIN_MENU"
        return "GAME_OVER"

    def draw(self, screen):
        screen.fill((55, 55, 60))
        font = pygame.font.SysFont("Arial", 50)
        txt = font.render("¡NIVEL COMPLETADO!", True, (0, 0, 0))
        screen.blit(txt, (500, 200))
        self.btn_menu.draw(screen)
        self.btn_next.draw(screen)