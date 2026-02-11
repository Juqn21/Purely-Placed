import pygame
from enfocate import GameBase, GameMetadata, COLORS 
from states.menu import MenuState
pygame.init()

class MiJuego(GameBase):
    def __init__(self) -> None:
        meta = GameMetadata(
            title="Purely Placed",
            description="Purely Placed es un juego para niños con TDAH",
            authors=["Juan Fernandez","Anelissa Espin","Erick Gomez","Katherin Martinez"],
            group_number=4 
        )
        self.escena_actual = MenuState()
        super().__init__(meta)

    def on_start(self):
        # Si esto se imprime en consola, el motor arrancó bien
        print("¡El motor ha iniciado correctamente!")

    def update(self, dt: float):
        self.escena_actual.update(dt)

    def draw(self):
    # Esto es vital: le pasas la "brocha" (surface) a tu estado de menú
        self.escena_actual.draw(self.surface)
        


if __name__ == "__main__":
    # Ejecuta el mini-motor integrado bajo los estándares del Core
    MiJuego().run_preview()

