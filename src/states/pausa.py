import pygame 
from pathlib import Path
from src.states.menu import Button 

class Pause():
    def __init__(self):
        self.continuar = False
        self.salir = False
        self.previous_state = None
        self.previous_state_obj = None

        ROOT_DIR = Path(__file__).resolve().parent.parent.parent
        path_fuente = ROOT_DIR / "assets" / "fonts" / "flatory-slab-condensed.ttf"
        
        self.font = pygame.font.Font(str(path_fuente), 100)
    

        self.boton_continuar = Button(550, 300, 200, 50, "CONTINUAR", "CONTINUE")
        self.boton_salir = Button(550, 400, 200, 50, "SALIR", "MAIN_MENU")

    def handle_events(self, events):

        if self.boton_continuar.is_clicked_no_event():
            return self.previous_state if self.previous_state else "SELECTOR"
        
        if self.boton_salir.is_clicked_no_event():
            return "MAIN_MENU"
        return "PAUSE"

    def draw(self, surface):

        if self.previous_state_obj:
            self.previous_state_obj.draw(surface)
        
        overlay = pygame.Surface(surface.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))  
        surface.blit(overlay, (0, 0))

        title = self.font.render("PAUSA", True, (255, 255, 255))
        surface.blit(title, (525, 50))
        self.boton_continuar.draw(surface)
        self.boton_salir.draw(surface)
