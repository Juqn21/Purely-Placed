import pygame
from enfocate import COLORS
# Mantengo el import por si lo usas, si da error puedes comentarlo con #
try:
    from settings import *
except ImportError:
    pass

class Button:
    def __init__(self, x, y, width, height, text, target, color=(167, 215, 232)):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.target = target
        self.base_color = color
        self.font = None
        self.pressed = False  # Para evitar que el clic se repita infinitamente

    def draw(self, screen):
        # Carga perezosa de la fuente para evitar errores de inicialización
        if self.font is None:
            self.font = pygame.font.SysFont("Arial", 30)
            
        mouse_pos = pygame.mouse.get_pos()
        # Cambia de color si el mouse está encima
        color = (184, 213, 179) if self.rect.collidepoint(mouse_pos) else self.base_color
        
        # Dibujo del botón
        pygame.draw.rect(screen, color, self.rect, border_radius=12)
        pygame.draw.rect(screen, (99, 66, 46), self.rect, 3, border_radius=12)
        
        # Texto centrado
        txt_surface = self.font.render(self.text, True, (99, 66, 46))
        txt_rect = txt_surface.get_rect(center=self.rect.center)
        screen.blit(txt_surface, txt_rect)

    def is_clicked_no_event(self):
        """
        Detecta el clic usando el estado del hardware.
        Es la forma más segura cuando el motor del juego 'roba' los eventos.
        """
        mouse_pos = pygame.mouse.get_pos()
        mouse_state = pygame.mouse.get_pressed() # [izq, centro, der]
        
        # Si el mouse está sobre el botón
        if self.rect.collidepoint(mouse_pos):
            # Si se está presionando el botón izquierdo
            if mouse_state[0]:
                self.pressed = True
            else:
                # Si se presionó y se soltó, ¡es un clic válido!
                if self.pressed:
                    self.pressed = False
                    return True
        else:
            self.pressed = False
            
        return False

class MenuState:
    def __init__(self):
        # Mantenemos 'assest' como pediste
        self.img_fondo = pygame.image.load("assest/images/menu/fondo.png")
        self.img_titulo = pygame.image.load("assest/images/menu/titulobg.png")
        self.img_cuadritos = pygame.image.load("assest/images/menu/cuadritosbg.png")
        
        # Inicializamos los botones dentro del estado del menú
        # Ajusté las posiciones Y (350 y 450) para que no tapen el título
        self.btn_start = Button(1030, 211, 200, 60, "START", "SELECTOR")
        self.btn_exit = Button(1030, 418, 200, 60, "EXIT", "EXIT", color=(242, 177, 177))
        
        self.done = False
        
    def handle_events(self, events):
        # Usamos la nueva función "guerrera"
        if self.btn_start.is_clicked_no_event():
            print("Cambiando a SELECTOR...")
            return "SELECTOR"
        
        if self.btn_exit.is_clicked_no_event():
            return "EXIT"
            
        return "MAIN_MENU"
        
    def update(self, dt):
        # Lógica para avanzar si presionas Enter
        #keys = pygame.key.get_pressed()
        # if keys[pygame.K_RETURN]:
          ##  self.done = True
            
        # Aquí podrías agregar la lógica de detección de clics si pasas los eventos
        pass

    def draw(self, surface):
        surface.blit(self.img_fondo, (0, 0))
        surface.blit(self.img_cuadritos, (0, 0))
        surface.blit(self.img_titulo, (0, 0))
        
        # Solo dibujarlos, ya tienen su posición desde el init
        self.btn_start.draw(surface)
        self.btn_exit.draw(surface)