import pygame
import sys
from enfocate import GameBase, GameMetadata, COLORS

# Importamos los estados
from .states.menu import MenuState
from .states.selector import LevelSelectorState
from .states.juego import Level
from .states.game_over import GameOver
from .states.pausa import Pause

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
        self.current_events = []

    def on_start(self):
        """Este método lo llama el motor cuando Pygame ya está listo"""
        # Ahora sí creamos los estados con seguridad
        self.states = {
            "MAIN_MENU": MenuState(),
            "SELECTOR": LevelSelectorState(),
            "LEVEL_1": Level(1),
            "LEVEL_2": Level(2),
            "LEVEL_3": Level(3),
            "GAME_OVER": GameOver(),
            "PAUSE": Pause()
        }

    def handle_events(self, events):
        self.current_events = events

    def update(self, dt: float):
        
        new_state = self.states[self.current_state].handle_events(self.current_events)
        
        if new_state == "EXIT":
            pygame.quit()
            sys.exit()
            

        if new_state in self.states:
            if new_state != self.current_state:

                if new_state == "PAUSE":
                    self.states["PAUSE"].previous_state = self.current_state
                    self.states["PAUSE"].previous_state_obj = self.states[self.current_state]
                elif new_state == "GAME_OVER":
                    # Guardar el nivel actual en game_over
                    if self.current_state.startswith("LEVEL_"):
                        level_num = int(self.current_state.split("_")[1])
                        self.states["GAME_OVER"].current_level = level_num
                self.current_state = new_state

    def draw(self):
        self.surface.fill(COLORS.get("carbon_oscuro", (30, 30, 30)))
    
        self.states[self.current_state].draw(self.surface)
