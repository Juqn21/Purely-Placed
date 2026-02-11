import pygame
import sys
from enfocate import GameBase, GameMetadata, COLORS
from settings import *

# Importamos los estados
from .states.menu import MainMenu
from .states.juego import LevelSelector, Level
from .states.game_over import GameOver

class MiJuego(GameBase):
    def __init__(self) -> None:
        # 1. Metadatos del juego
        meta = GameMetadata(
            title="Purely Placed",
            description="Juego de estrategia modular.",
            authors=["Tu Nombre"],
            group_number=3
        )
        # 2. Inyección al motor
        super().__init__(meta)
        
        # 3. Preparar variables (sin instanciar clases que usen fuentes aún)
        self.states = {}
        self.current_state = "MAIN_MENU"

    def on_start(self):
        """Este método lo llama el motor cuando Pygame ya está listo"""
        # Ahora sí creamos los estados con seguridad
        self.states = {
            "MAIN_MENU": MainMenu(),
            "SELECTOR": LevelSelector(),
            "LEVEL 1": Level(1),
            "LEVEL 2": Level(2),
            "LEVEL 3": Level(3),
            "LEVEL 4": Level(4),
            "LEVEL 5": Level(5),
            "GAME_OVER": GameOver()
        }

    def update(self, dt: float):
        """Lógica de transiciones"""
        events = pygame.event.get()
        
        # El estado actual nos dice a qué estado ir
        new_state = self.states[self.current_state].handle_events(events)
        
        if new_state == "EXIT":
            pygame.quit()
            sys.exit()
            
        self.current_state = new_state

    def draw(self):
        """Renderizado en la superficie del motor"""
        # Limpiamos fondo
        self.surface.fill(COLORS.get("carbon_oscuro", (30, 30, 30)))
        
        # Dibujamos el estado activo
        self.states[self.current_state].draw(self.surface)