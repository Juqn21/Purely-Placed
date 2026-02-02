import pygame

pygame.init()
pantalla = pygame.display.set_mode((800, 600))

fondo = pygame.image.load("fondo.png").convert()
fondo = pygame.transform.scale(fondo, (800, 600))

imagen = pygame.image.load("zapato-removebg-preview.png").convert_alpha()
imagen_caja= pygame.image.load("caja (2).png").convert_alpha()

imagen = pygame.transform.scale(imagen, (150, 100))
imagen_caja = pygame.transform.scale(imagen_caja, (150, 100))
rect_objeto = imagen.get_rect(topleft=(100, 150))
rect_caja=imagen_caja.get_rect(topleft=(300, 200))

mascara_zapato = pygame.mask.from_surface(imagen)
mascara_caja = pygame.mask.from_surface(imagen_caja)

arrastrando = False
offset_x, offset_y = 0, 0

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                # Paso 1: ¿Está el mouse dentro del cuadro?
                if rect_objeto.collidepoint(evento.pos):
                    # Paso 2: ¿Qué pixel de la IMAGEN tocamos?
                    x_rel = evento.pos[0] - rect_objeto.x
                    y_rel = evento.pos[1] - rect_objeto.y
                    
                    # Paso 3: ¿Ese pixel específico pertenece al zapato?
                    # get_at devuelve 1 si hay zapato, 0 si hay vacío
                    if mascara_zapato.get_at((x_rel, y_rel)):
                        arrastrando = True
                        offset_x = rect_objeto.x - evento.pos[0]
                        offset_y = rect_objeto.y - evento.pos[1]

        if evento.type == pygame.MOUSEBUTTONUP:
            if arrastrando:
                arrastrando = False
                # Snap al objetivo si está cerca
            offset = (rect_objeto.x - rect_caja.x, rect_objeto.y - rect_caja.y)
            pixeles_coincidentes = mascara_caja.overlap_area(mascara_zapato, offset)

            if pixeles_coincidentes > (mascara_zapato.count() * 0.1):

                rect_objeto.center = rect_caja.center
                

        if evento.type == pygame.MOUSEMOTION and arrastrando:
            rect_objeto.x = evento.pos[0] + offset_x
            rect_objeto.y = evento.pos[1] + offset_y

    # DIBUJO
    pantalla.blit(fondo, (0, 0))
    pantalla.blit(imagen_caja, rect_caja)
    pantalla.blit(imagen, rect_objeto)
    pygame.display.flip()