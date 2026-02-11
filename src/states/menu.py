import pygame
from enfocate import COLORS

class MenuState:
    def __init__(self):
        
        self.img_fondo = pygame.image.load("assest/images/menu/fondo.png")
        self.img_titulo = pygame.image.load("assest/images/menu/titulobg.png")
        self.img_cuadritos = pygame.image.load("assest/images/menu/cuadritosbg.png")
        
        self.done = False
        
    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            self.done = True

    def draw(self, surface):
        
        surface.blit(self.img_fondo, (0, 0))
        
        x_titulo = (surface.get_width() // 2) - (self.img_titulo.get_width() // 2)
        surface.blit(self.img_titulo, (x_titulo, 100))