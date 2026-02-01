import pygame
from enfocate import GameBase, GameMetadata, COLORS 

class MiJuego(GameBase):
    def __init__(self) -> None:
        meta = GameMetadata(
            title="Purely Placed",
            description="Purely Placed es un juego para niños con tdh",
            authors=["Juan Fernandez","Anelissa Espin","Erick Gomez","Katherin Apellido"],
            group_number=4 
        )
        super().__init__(meta)

    def on_start(self):
        # Si esto se imprime en consola, el motor arrancó bien
        print("¡El motor ha iniciado correctamente!")

    def update(self, dt: float):
        pass

    def draw(self):
        # Pintamos el fondo para verificar que el render funciona
        self.surface.fill(COLORS["carbon_oscuro"])

