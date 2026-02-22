import pygame
import sys
from enfocate import GameBase, GameMetadata, COLORS
##from src.settings import *

# Importamos los estados
from .states.menu import MenuState
from .states.selector import LevelSelectorState
from .states.juego import Level
from .states.game_over import GameOver

class MiJuego(GameBase):
    def __init__(self) -> None:
        # 1. Metadatos del juego
        meta = GameMetadata(
            title="Purely Placed",
            description="Purely Placed es un juego para niños con TDAH",
            authors=["Juan Fernandez","Anelissa Espin","Erick Gomez","Katherin Martinez"],
            group_number=4 
        )
        self.escena_actual = MenuState()
        super().__init__(meta)
        
        # 3. Preparar variables (sin instanciar clases que usen fuentes aún)
        self.states = {}
        self.current_state = "MAIN_MENU"

    def on_start(self):
        """Este método lo llama el motor cuando Pygame ya está listo"""
        # Ahora sí creamos los estados con seguridad
        self.states = {
            "MAIN_MENU": MenuState(),
            "SELECTOR": LevelSelectorState(),
            "LEVEL_1": Level(1),
            "LEVEL_2": Level(2),
            "LEVEL_3": Level(3),
            "GAME_OVER": GameOver()
        }

    def update(self, dt: float):
        # 1. CORRECCIÓN DEL ATRIBUTO:
        # En el SDK enfocate, la lista de eventos se guarda en self._events
        eventos_actuales = pygame.event.get() 

        # 2. Pasamos los eventos reales al estado actual
        new_state = self.states[self.current_state].handle_events(eventos_actuales)
        
        if new_state == "EXIT":
            pygame.quit()
            sys.exit()
            
        # 3. Gestión de cambio de estado
        if new_state in self.states:
            if new_state != self.current_state:
                self.current_state = new_state

    def draw(self):
        self.surface.fill(COLORS.get("carbon_oscuro", (30, 30, 30)))
    
        self.states[self.current_state].draw(self.surface)
