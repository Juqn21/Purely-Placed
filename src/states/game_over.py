import pygame
from .menu import Button
from pathlib import Path

class GameOver:
    def __init__(self):
        # 1. Rutas y carga inicial (UNA SOLA VEZ)
        self.BASE_DIR = Path(__file__).resolve().parent.parent.parent
        self.ASSETS_DIR = self.BASE_DIR / "assets"
        self.path_nivelcompletado = self.ASSETS_DIR / "images" / "menu" / "nivelcompletado.png"
        
        # 2. Intentamos cargar la imagen de victoria
        try:
            self.img_nc = pygame.image.load(str(self.path_nivelcompletado)).convert_alpha()
            # Si quieres que ocupe un tamaño específico (ej. 800x400):
            # self.img_nc = pygame.transform.scale(self.img_nc, (800, 400))
        except FileNotFoundError:
            print("Error: No se encontró la imagen de nivel completado")
            self.img_nc = None

        # 3. Botones centrados
        # Calculamos posiciones para que se vean bien (Pantalla 1280x720)
        self.btn_menu = Button(400, 500, 200, 60, "MENÚ", "MAIN_MENU")
        self.btn_next = Button(650, 500, 280, 60, "SIGUIENTE NIVEL", "NEXT_LEVEL")
        
        self.current_level = 1

    def handle_events(self, events):
        # Lógica de botones
        if self.btn_menu.is_clicked_no_event():
            return "MAIN_MENU"
        
        if self.btn_next.is_clicked_no_event():
            next_level = self.current_level + 1
            if next_level <= 3:
                return f"LEVEL_{next_level}"
            else:
                return "MAIN_MENU" # Si ya no hay más niveles, vuelve al menú
        
        return "GAME_OVER"

    def draw(self, screen):
        # 1. Limpiar pantalla con un color sólido (Fondo oscuro)
        screen.fill((22, 30, 84)) # El azul oscuro de tu juego (#161e54)

        # 2. Dibujar la imagen de victoria centrada
        if self.img_nc:
            # Esto centra la imagen automáticamente
            rect_img = self.img_nc.get_rect(center=(640, 360))
            screen.blit(self.img_nc, rect_img)
        else:
            # Respaldo si no hay imagen
            font = pygame.font.SysFont("Arial", 60)
            txt = font.render("¡NIVEL COMPLETADO!", True, (255, 255, 255))
            screen.blit(txt, (400, 250))

        # 3. Dibujar botones
        self.btn_menu.draw(screen)
        self.btn_next.draw(screen)