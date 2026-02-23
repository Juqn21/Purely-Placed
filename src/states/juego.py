import pygame
from src.states.menu import Button
from src.states.mapa import mapas
# Importamos las listas de objetos y las rutas de imágenes desde constants
from src.utils.constants import *

class Level:
    def __init__(self, num):
        self.num = num
        self.font = pygame.font.SysFont("Arial", 40)
        self.nivel_completo_tiempo = 0
        
    
        if self.num == 1:

            self.mapa_logica = mapas(lista_nivel1, NIVEL1)

            self.fondo = pygame.Surface((1280, 720))
            self.fondo.fill((155, 246, 255))

        if self.num == 2:

            self.mapa_logica = mapas(lista_nivel2, NIVEL2)

            self.fondo = pygame.Surface((1280, 720))
            self.fondo.fill((155, 246, 255))

        if self.num == 3:

            self.mapa_logica = mapas(lista_nivel3, NIVEL3)
            
            self.fondo = pygame.Surface((1280, 720))
            self.fondo.fill((155, 246, 255))

    def handle_events(self, events):

        for e in events:

            if hasattr(self, 'mapa_logica'):
                self.mapa_logica.handle_event(e)
                
                if self.mapa_logica.nivel_completado():
                    if self.nivel_completo_tiempo == 0:
                        self.nivel_completo_tiempo = pygame.time.get_ticks()
                    elif pygame.time.get_ticks() - self.nivel_completo_tiempo > 300:
                        return "GAME_OVER"
            
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_m: return "SELECTOR"
                if e.key == pygame.K_p: return "GAME_OVER"
                if e.key == pygame.K_ESCAPE: return "PAUSE"
        
        
        return f"LEVEL_{self.num}"

    def draw(self, screen):

        if hasattr(self, 'mapa_logica'):
            self.mapa_logica.draw(screen, self.fondo)
        else:
            screen.fill((200, 200, 200))
            txt = self.font.render(f"CARGANDO NIVEL {self.num}...", True, (50, 50, 50))
            screen.blit(txt, (250, 200))