import pygame
from pathlib import Path

class mapas():
    def __init__(self,lista_nivel,imagenes_libreria):
        self.BASE_DIR = Path(__file__).resolve().parent.parent.parent
        self.ASSETS_DIR = self.BASE_DIR / "assets"
        self.arrastrando = False
        self.offset_x, self.offset_y = 0, 0
        self.objetos_activos = [] # Aquí guardaremos diccionarios con {imagen, rect}
        self.objeto_seleccionado = None
        self.imagenes = self.obtener_objeto(imagenes_libreria)
        # Inicializamos los objetos del nivel UNA SOLA VEZ
        for obj in lista_nivel:
            img = self.imagenes[obj["tipo"]]
            rect = img.get_rect(topleft=obj["pos"])
            mask = pygame.mask.from_surface(img)
            silueta_img = mask.to_surface(setcolor=(50, 50, 50, 150), unsetcolor=(0, 0, 0, 0))
            # Creamos la sombra (meta) para este objeto
            rect_meta = img.get_rect(topleft=obj["pos_meta"])
            
            self.objetos_activos.append({
                'tipo': obj["tipo"],
                'img': img,
                'rect': rect,
                'mask': mask,
                'silueta': silueta_img,
                'rect_meta': rect_meta,
                'encajado': False
            })
        
    
    def obtener_objeto(self, NIVEL):
        # Ajustado para usar la ruta dinámica
        imagenes_listas = {}
        for clave, ruta in NIVEL.items():
        # Cargamos y optimizamos la imagen para Pygame
           IMAGE_PATH = self.BASE_DIR / ruta
           img = pygame.image.load(str(IMAGE_PATH)).convert_alpha()
           image = pygame.transform.scale(img, (150, 100)) 
           imagenes_listas[clave] = image
        return imagenes_listas
    
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print(f"Clic en: {event.pos}")
                # Revisamos de arriba hacia abajo (reversed) para agarrar el que esté encima
                for obj in reversed(self.objetos_activos):
                    print(f"Revisando objeto {obj['tipo']} en {obj['rect']}")
                    if not obj['encajado'] and obj['rect'].collidepoint(event.pos):
                        print("¡Colisión detectada!")
                        # Verificación Pixel-Perfect antes de agarrar
                        x_rel = event.pos[0] - obj['rect'].x
                        y_rel = event.pos[1] - obj['rect'].y
                        
                        if obj['mask'].get_at((x_rel, y_rel)):
                            print(f"¡Agarraste el objeto: {obj['tipo']}!")
                            self.objeto_seleccionado = obj
                            self.offset_x = obj['rect'].x - event.pos[0]
                            self.offset_y = obj['rect'].y - event.pos[1]
                        print(f"¡Objeto seleccionado: {obj['tipo']}!")
                        break

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and self.objeto_seleccionado:
                # LÓGICA DE ENCAJE (SNAP)
                obj = self.objeto_seleccionado
                
                # Calculamos distancia entre el objeto y su meta
                distancia = pygame.math.Vector2(obj['rect'].topleft).distance_to(obj['rect_meta'].topleft)
                
                # Si está a menos de 40 píxeles, lo succionamos a la meta
                if distancia < 40:
                    obj['rect'].topleft = obj['rect_meta'].topleft
                    obj['encajado'] = True
                    print(f"¡{obj['tipo']} colocado correctamente!")
                
                self.objeto_seleccionado = None

        elif event.type == pygame.MOUSEMOTION:
            if self.objeto_seleccionado:
                self.objeto_seleccionado['rect'].x = event.pos[0] + self.offset_x
                self.objeto_seleccionado['rect'].y = event.pos[1] + self.offset_y

    def draw(self, surface, pantalla):     
        
        surface.blit(pantalla, (0, 0))
    # 1. Dibujamos todas las siluetas PRIMERO (para que queden al fondo)
        for obj in self.objetos_activos:
            if not obj['encajado']:
            # Dibujamos la silueta en la posición de destino
                surface.blit(obj['silueta'], obj['rect_meta'])

    # 2. Dibujamos los objetos reales ENCIMA
        for obj in self.objetos_activos:
            surface.blit(obj['img'], obj['rect'])
    