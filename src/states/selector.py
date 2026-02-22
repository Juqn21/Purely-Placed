import pygame
from pathlib import Path
from src.states.menu import Button 
from src.states.juego import Level

ROOT_DIR = Path(__file__).resolve().parent.parent.parent

class LevelSelectorState:
    def __init__(self):
        # 1. Definir la ruta de la carpeta de imágenes
        path_images = ROOT_DIR / "assets" / "images" / "selector"
        
        # 2. Carga del fondo específico para el selector
        # (Asegúrate de que el nombre del archivo coincida con el tuyo, ej: fondo_niveles.png)
        path_fondo = path_images / "FondoSelector.png" 
        
        try:
            self.img_fondo = pygame.image.load(str(path_fondo)).convert_alpha()
        except FileNotFoundError:
            print("Error: No se encontró el fondo del selector. Usando fondo gris.")
            self.img_fondo = pygame.Surface((1280, 720))
            self.img_fondo.fill((50, 50, 50)) # Fondo oscuro de emergencia

        # 3. Botones con imagen para los niveles
        # Formato: Button(x, y, ancho, alto, texto_vacio, destino, ruta_imagen)
        self.btn_lvl1 = Button(0, 0, 200, 200, "", "LEVEL_1", path_images / "SelecN1.png")
        self.btn_lvl2 = Button(0, 0, 200, 200, "", "LEVEL_2", path_images / "SelecN2.png")
        self.btn_lvl3 = Button(0, 0, 200, 200, "", "LEVEL_3", path_images / "SelecN3.png")
        
        # Botón para volver (este puede ser solo texto para mantener el estilo)
        self.btn_back = Button(50, 40, 150, 50, "Volver", "MAIN_MENU")

    def handle_events(self, events):
        if self.btn_lvl1.is_clicked_no_event(): return "LEVEL_1"
        if self.btn_lvl2.is_clicked_no_event(): return "LEVEL_2"
        if self.btn_lvl3.is_clicked_no_event(): return "LEVEL_3"
        if self.btn_back.is_clicked_no_event(): return "MAIN_MENU"
        return "SELECTOR"

    def update(self, dt):
        pass

    def draw(self, surface):
        surface.blit(self.img_fondo, (0, 0))
        self.btn_lvl1.draw(surface)
        self.btn_lvl2.draw(surface)
        self.btn_lvl3.draw(surface)
        self.btn_back.draw(surface)