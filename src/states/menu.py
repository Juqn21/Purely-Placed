import pygame
from settings import *

class Button:
    def __init__(self, x, y, width, height, text, target, color=(167, 215, 232)):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.target = target
        self.base_color = color
        # La fuente se carga aquí, por eso necesitamos inicializar en on_start
        self.font = pygame.font.SysFont("Arial", 30)

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        color = (184, 213, 179) if self.rect.collidepoint(mouse_pos) else self.base_color
        
        pygame.draw.rect(screen, color, self.rect, border_radius=12)
        pygame.draw.rect(screen, (99, 66, 46), self.rect, 3, border_radius=12)
        
        txt_surface = self.font.render(self.text, True, (99, 66, 46))
        txt_rect = txt_surface.get_rect(center=self.rect.center)
        screen.blit(txt_surface, txt_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return self.rect.collidepoint(event.pos)
        return False

class MainMenu:
    def __init__(self):
        # CORRECCIÓN: x, y, ancho, alto. 
        # Usamos valores fijos para ancho (200) y alto (60) para que se vean bien.
        self.btn_start = Button(300, 200, 200, 60, "START", "SELECTOR")
        self.btn_exit = Button(300, 300, 200, 60, "EXIT", "EXIT", color=(242, 177, 177))

    def handle_events(self, events):
        for e in events:
            if self.btn_start.is_clicked(e): return "SELECTOR"
            if self.btn_exit.is_clicked(e): return "EXIT"
        return "MAIN_MENU"

    def draw(self, screen):
        screen.fill((212, 241, 244))
        self.btn_start.draw(screen)
        self.btn_exit.draw(screen)