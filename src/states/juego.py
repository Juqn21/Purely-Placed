import pygame
from src.states.menu import Button
from src.states.mapa import mapas
# Importamos las listas de objetos y las rutas de imágenes desde constants
from src.utils.constants import *

class Level:
    def __init__(self, num):
        self.num = num
        self.font = pygame.font.SysFont("Arial", 40)
        
     
        if self.num == 1:
            self.mapa_logica = mapas(lista_nivel1, NIVEL1)
            
            try:
                self.fondo = pygame.image.load("fondo.png").convert()
            except:
                self.fondo = pygame.Surface((1280, 720))
                self.fondo.fill((200, 200, 200))

    def handle_events(self, events):
       
        for e in events:
           
            if hasattr(self, 'mapa_logica'):
                self.mapa_logica.handle_event(e)
            
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_m: return "SELECTOR"
                if e.key == pygame.K_p: return "GAME_OVER" 
        
        
        return f"LEVEL_{self.num}"

    def draw(self, screen):
       
        if hasattr(self, 'mapa_logica'):
            self.mapa_logica.draw(screen, self.fondo)
        else:
            screen.fill((200, 200, 200))
            txt = self.font.render(f"CARGANDO NIVEL {self.num}...", True, (50, 50, 50))
            screen.blit(txt, (250, 200))