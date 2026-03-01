import pygame
import sys
from enfocate import GameBase, GameMetadata, COLORS
from .states.menu import MenuState, Button
from .states.selector import LevelSelectorState
from .states.juego import Level
from .states.game_over import GameOver
from .states.pausa import Pause
from pathlib import Path

class MiJuego(GameBase):
    def __init__(self) -> None:
        self.ROOT_DIR = Path(__file__).resolve().parent.parent 
        self.ASSETS_DIR = self.ROOT_DIR / "assets"
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
        self.states = {
             # Ahora sí creamos los estados con seguridad
            "MAIN_MENU": MenuState(),
            "SELECTOR": LevelSelectorState(),
            "LEVEL_1": Level(1),
            "LEVEL_2": Level(2),
            "LEVEL_3": Level(3),
            "GAME_OVER": GameOver(),
            "PAUSE": Pause()
        }
        
        
        self.is_muted = False
        
        self.path_sound_on = self.ASSETS_DIR / "images" / "menu" / "sound_on.png"
        self.path_sound_off = self.ASSETS_DIR / "images" / "menu" / "sound_off.png"

        try:
            self.img_sound_on = pygame.image.load(str(self.path_sound_on)).convert_alpha()
            self.img_sound_off = pygame.image.load(str(self.path_sound_off)).convert_alpha()
        except Exception as e:
            print("Error cargando imagenes de sonido:", e)
            self.img_sound_on = None
            self.img_sound_off = None

        self.btn_sound = Button(0, 0, 50, 50, "", "TOGGLE_SOUND")
        
        if self.img_sound_on:
            self.btn_sound.image = self.img_sound_on
            self.btn_sound.rect = self.img_sound_on.get_rect()
            self.btn_sound.mask = None 
        # -----------------------------------------

        self.cambiar_musica("menusong.mp3")

    def toggle_sound(self):
        self.is_muted = not self.is_muted
        vol_music = 0.0 if self.is_muted else 0.5
        vol_sfx = 0.0 if self.is_muted else 0.6

        pygame.mixer.music.set_volume(vol_music)

        for level_name in ["LEVEL_1", "LEVEL_2", "LEVEL_3"]:
            if level_name in self.states:
                estado = self.states[level_name]
                if hasattr(estado, 'mapa_logica') and estado.mapa_logica.snd_encaje:
                    estado.mapa_logica.snd_encaje.set_volume(vol_sfx)

        if self.img_sound_on and self.img_sound_off:
            self.btn_sound.image = self.img_sound_off if self.is_muted else self.img_sound_on
            self.btn_sound.mask = None 

    def handle_events(self, events):
        self.current_events = events

    def update(self, dt: float):
        # SOLO detectamos clic en el botón si NO estamos dentro de un nivel
        if not self.current_state.startswith("LEVEL_"):
            if self.btn_sound.is_clicked_no_event():
                self.toggle_sound()

        new_state = self.states[self.current_state].handle_events(self.current_events)
        
        if new_state == "EXIT":
            self._stop_context()

        if new_state in self.states:
            if new_state != self.current_state:
                
                if new_state == "LEVEL_1":
                    self.cambiar_musica("nivel1song.mp3")
                elif new_state == "LEVEL_2":
                    self.cambiar_musica("nivel2song.mp3")
                elif new_state == "LEVEL_3":
                    self.cambiar_musica("nivel3song.mp3")
                elif new_state == "MAIN_MENU":
                    self.cambiar_musica("menusong.mp3")

                if new_state == "PAUSE":
                    self.states["PAUSE"].previous_state = self.current_state
                    self.states["PAUSE"].previous_state_obj = self.states[self.current_state]
                elif new_state == "GAME_OVER":
                    if self.current_state.startswith("LEVEL_"):
                        level_num = int(self.current_state.split("_")[1])
                        self.states["GAME_OVER"].current_level = level_num
                self.current_state = new_state
    
    def cambiar_musica(self, nombre_archivo):
        try:
            ruta = self.ASSETS_DIR / "music" / nombre_archivo
            pygame.mixer.music.stop()
            pygame.mixer.music.load(str(ruta))
            
            vol_music = 0.0 if self.is_muted else 0.5
            pygame.mixer.music.set_volume(vol_music)
            
            pygame.mixer.music.play(-1)
        except Exception as e:
            print(f"Error al cambiar música: {e}")

    def draw(self):
        self.surface.fill(COLORS.get("carbon_oscuro", (30, 30, 30)))
        
        # 1. Dibujamos la pantalla en la que estemos
        self.states[self.current_state].draw(self.surface)

        # 2. LÓGICA DE DIBUJO Y POSICIÓN DEL BOTÓN
        
        if not self.current_state.startswith("LEVEL_"):
            
            if self.current_state == "SELECTOR":
               
                self.btn_sound.rect.topright = (1260, 20)
            else:
                
                self.btn_sound.rect.bottomright = (1260, 700)
                
            # Finalmente lo dibujamos
            self.btn_sound.draw(self.surface)