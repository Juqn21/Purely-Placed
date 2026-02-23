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
            img_original = self.imagenes[obj["tipo"]]
            
            if "size" in obj:
                img_original = pygame.transform.scale(img_original, obj["size"])
            else:
                img_original = pygame.transform.scale(img_original, (150, 100))  # Tamaño por defecto
            
            img = img_original
            if "rotation" in obj:
                img = pygame.transform.rotate(img_original, obj["rotation"])
            
            rect = img.get_rect(topleft=obj["pos"])
            mask = pygame.mask.from_surface(img)
            mask_original = pygame.mask.from_surface(img_original)
            
            silueta_img = mask_original.to_surface(setcolor=(50, 50, 50, 150), unsetcolor=(0, 0, 0, 0))
            rect_meta = img_original.get_rect(topleft=obj["pos_meta"])
            
            self.objetos_activos.append({
                'tipo': obj["tipo"],
                'img': img,
                'img_original': img_original,
                'img_rotated': img if "rotation" in obj else None,
                'rect': rect,
                'mask': mask,
                'silueta': silueta_img,
                'rect_meta': rect_meta,
                'encajado': False,
                'rotated': "rotation" in obj,
                'has_rotation': "rotation" in obj
            })
        
    
    def obtener_objeto(self, NIVEL):
        # Ajustado para usar la ruta dinámica
        imagenes_listas = {}
        for clave, ruta in NIVEL.items():
        # Cargamos la imagen sin escalar
            IMAGE_PATH = self.BASE_DIR / ruta
            img = pygame.image.load(str(IMAGE_PATH)).convert_alpha()
            imagenes_listas[clave] = img
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
                        
                        try:
                            if 0 <= x_rel < obj['mask'].get_size()[0] and 0 <= y_rel < obj['mask'].get_size()[1]:
                                if obj['mask'].get_at((x_rel, y_rel)):
                                    print(f"¡Agarraste el objeto: {obj['tipo']}!")
                                    self.objeto_seleccionado = obj
                                    self.offset_x = obj['rect'].x - event.pos[0]
                                    self.offset_y = obj['rect'].y - event.pos[1]
                                    
                                    if obj['rotated']:
                                        centro = obj['rect'].center
                                        obj['img'] = obj['img_original']
                                        obj['rect'] = obj['img'].get_rect(center=centro)
                                        obj['mask'] = pygame.mask.from_surface(obj['img'])
                                        obj['rotated'] = False
                                    
                                    self.objetos_activos.remove(obj)
                                    self.objetos_activos.append(obj)
                        except IndexError:
                            pass
                        print(f"¡Objeto seleccionado: {obj['tipo']}!")
                        break

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and self.objeto_seleccionado:
                obj = self.objeto_seleccionado
                
                distancia = pygame.math.Vector2(obj['rect'].topleft).distance_to(obj['rect_meta'].topleft)
                
                if distancia < 40:
                    obj['rect'].topleft = obj['rect_meta'].topleft
                    obj['encajado'] = True
                    print(f"¡{obj['tipo']} colocado correctamente!")

                else:
                    if obj['has_rotation'] and not obj['rotated']:
                        centro = obj['rect'].center
                        obj['img'] = obj['img_rotated']
                        obj['rect'] = obj['img'].get_rect(center=centro)
                        obj['mask'] = pygame.mask.from_surface(obj['img'])
                        obj['rotated'] = True
                
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
    