import pygame
from enfocate import COLORS
import os
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent.parent

class Button:
    def __init__(self, x, y, width, height, text, target, image_path=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.target = target
        self.font = None
        self.pressed = False
        self.image = None
        self.mask = None
        
        if image_path:
            try:
                self.image = pygame.image.load(str(image_path)).convert_alpha()
                self.rect = self.image.get_rect(topleft=(x, y))
                
                self.mask = pygame.mask.from_surface(self.image)
            except:
                print(f"Error cargando: {image_path}")

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        is_hover = False
        if self.image and self.mask:
            pos_in_mask = (mouse_pos[0] - self.rect.x, mouse_pos[1] - self.rect.y)
            if self.rect.collidepoint(mouse_pos) and self.mask.get_at(pos_in_mask):
                is_hover = True
        else:
            is_hover = self.rect.collidepoint(mouse_pos)

        if self.image:
            if is_hover:
                temp_img = self.image.copy()
                temp_img.fill((40, 40, 40), special_flags=pygame.BLEND_RGB_ADD)
                screen.blit(temp_img, self.rect)
            else:
                screen.blit(self.image, self.rect)
        else:
            if self.font is None:
                path_fuente = ROOT_DIR / "assets" / "fonts" / "flatory-slab-condensed.ttf" 
                try:
                    self.font = pygame.font.Font(str(path_fuente), 45)
                except:
                    self.font = pygame.font.SysFont("Arial", 45)

            color_texto = (255, 255, 255)
            if is_hover:
                color_texto = (180, 180, 180)

            text_surf = self.font.render(self.text, True, color_texto)
            text_rect = text_surf.get_rect(center=self.rect.center)
            screen.blit(text_surf, text_rect)
            screen.blit(text_surf, (text_rect.x + 1, text_rect.y))

    def is_clicked_no_event(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_state = pygame.mouse.get_pressed()
        
        click_valido = False
        if self.image and self.mask:
            pos_in_mask = (mouse_pos[0] - self.rect.x, mouse_pos[1] - self.rect.y)
            if self.rect.collidepoint(mouse_pos) and self.mask.get_at(pos_in_mask):
                click_valido = True
        else:
            click_valido = self.rect.collidepoint(mouse_pos)

        if click_valido:
            if mouse_state[0]:
                self.pressed = True
            else:
                if self.pressed:
                    self.pressed = False
                    return True
        else:
            self.pressed = False
        return False
    
class MenuState:
    def __init__(self):
        folder = "assets" 
        path_fondo = ROOT_DIR / folder / "images" / "menu" / "fondo.png"
        path_titulo = ROOT_DIR / folder / "images" / "menu" / "titulobg.png"
        path_cuadritos = ROOT_DIR / folder / "images" / "menu" / "cuadritosbg.png"

        try:
            self.img_fondo = pygame.image.load(str(path_fondo))
            self.img_titulo = pygame.image.load(str(path_titulo))
            self.img_cuadritos = pygame.image.load(str(path_cuadritos))
        except FileNotFoundError:
            self.img_fondo = pygame.Surface((1280, 720))
            self.img_titulo = pygame.Surface((200, 50))
            self.img_cuadritos = pygame.Surface((200, 50))
        
        # BOTONES "SOLITOS" (Solo texto con borde)
        # Ajusta las posiciones X e Y para que caigan justo donde quieres
        self.btn_start = Button(950, 230, 200, 60, "Jugar", "SELECTOR")
        self.btn_config = Button(990, 310, 250, 60, "Configuración", "CONFIG")
        self.btn_exit = Button(950, 390, 200, 60, "Salir", "EXIT")
        
    def handle_events(self, events):
        if self.btn_start.is_clicked_no_event(): return "SELECTOR"
        if self.btn_exit.is_clicked_no_event(): return "EXIT"
        return "MAIN_MENU"

    def draw(self, surface):
        surface.blit(self.img_fondo, (0, 0))
        surface.blit(self.img_cuadritos, (0, 0))
        surface.blit(self.img_titulo, (0, 0))
        
        self.btn_start.draw(surface)
        self.btn_config.draw(surface)
        self.btn_exit.draw(surface)