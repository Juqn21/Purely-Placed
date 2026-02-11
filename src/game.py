import pygame
import sys
from enfocate import GameBase, GameMetadata, COLORS
##from src.settings import *

# Importamos los estados
from .states.menu import MenuState
from .states.juego import LevelSelector, Level
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
            "SELECTOR": LevelSelector(),
            "LEVEL 1": Level(1),
            "LEVEL 2": Level(2),
            "LEVEL 3": Level(3),
            "LEVEL 4": Level(4),
            "LEVEL 5": Level(5),
            "GAME_OVER": GameOver()
        }

    def update(self, dt: float):
        # 1. NO LLAMES A pygame.event.get() AQUÍ. 
        # Deja que el motor del SDK maneje los eventos internamente.

        # 2. Solo pide el cambio de estado
        # Le pasamos una lista vacía [] solo para que no de error la función
        new_state = self.states[self.current_state].handle_events([])
        
        if new_state == "EXIT":
            pygame.quit()
            sys.exit()
            
        if new_state in self.states:
            self.current_state = new_state

    def draw(self):
        """Renderizado en la superficie del motor"""
        # Limpiamos fondo
        self.surface.fill(COLORS.get("carbon_oscuro", (30, 30, 30)))
        
        # Dibujamos el estado activo
        self.states[self.current_state].draw(self.surface)
