import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from pygame.locals import *
import sys

# Importar funciones para dibujar escenarios
from Esenarios import escenario as es

# Importar personajes
from acciones.jesusL import draw as draw_jesus
from acciones.torchic import personaje as draw_torchic
from acciones.dysonEm import dibujar_personaje as draw_dyson
from acciones.expresiones import draw_cejas_chad,draw_feliz,draw_triste,draw_enojado,draw_nervioso

# Importar otras utilidades
from acciones.iluminacion import iluminacion
from src.textos import dibujar_label_texto

def iniciar_nivel2(personaje_id):
    """
    Inicia el nivel 2 con el personaje seleccionado.
    
    Args:
        personaje_id: ID del personaje seleccionado (0=JesusL, 1=Torchic, 2=Dyson)
    """
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Nivel 2")

    # Inicializar fondos
    es.inicializar_fondos()
    # Puedes cambiar el índice del fondo si quieres otro diferente
    fondo_actual = 1
    
    # Variable para controlar la posición de JesusL
    jesus_posicion = 0

    torchic_posicion = 0

    dyson_posicion = 0

    # Configurar la perspectiva
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, -2.0, -30) # Aleja la cámara para que el fondo se vea mejor

    # Habilitar prueba de profundidad e iluminación
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_COLOR_MATERIAL)
    
    # Variables para controlar la cámara
    cam_x, cam_y, cam_z = -4, 0, 15  # Iniciar con la cámara más cerca
    rot_x, rot_y = 0, 0

    # Variables para la posición y velocidad del jugador
    player_x, player_y, player_z = 0.0, 0.0, 0.0
    player_speed = 0.1 # Ajusta la velocidad según sea necesario
    
    # Bucle principal del juego
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            # Control de teclado para salir (ESC) y mover la cámara (opcional)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return
                # Movimiento de cámara (si aún lo quieres)
                elif event.key == pygame.K_w:
                    cam_z += 0.5
                elif event.key == pygame.K_s:
                    cam_z -= 0.5
                elif event.key == pygame.K_a:
                    cam_x += 0.5
                elif event.key == pygame.K_d:
                    cam_x -= 0.5
                elif event.key == pygame.K_z:
                    cam_y += 0.5
                elif event.key == pygame.K_x:
                    cam_y -= 0.5
                # Cambio de escenarios y posiciones de JesusL
                elif event.key == pygame.K_1:
                    fondo_actual = 1
                    if personaje_id == 0:  # Solo si es JesusL
                        jesus_posicion = 1
                    if personaje_id == 1:  # Solo si es Torchic
                        torchic_posicion = 1
                elif event.key == pygame.K_2:
                    fondo_actual = 2
                    if personaje_id == 0:  # Solo si es JesusL
                        jesus_posicion = 2
                    if personaje_id == 1:
                        torchic_posicion = 2
                elif event.key == pygame.K_3:
                    fondo_actual = 3
                    if personaje_id == 0:  # Solo si es JesusL
                        jesus_posicion = 3
                    if personaje_id == 1:
                        torchic_posicion = 3
                elif event.key == pygame.K_4:
                    fondo_actual = 4
                    if personaje_id == 0:  # Solo si es JesusL
                        jesus_posicion = 4
                    if personaje_id == 1:
                        torchic_posicion = 4
                elif event.key == pygame.K_5:
                    fondo_actual = 5
                    if personaje_id == 0:  # Solo si es JesusL
                        jesus_posicion = 5
                    if personaje_id == 1:
                        torchic_posicion = 5

        # --- Control de movimiento del personaje (fuera del bucle de eventos) ---
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed
        if keys[pygame.K_UP]:
            # Mover hacia arriba en el eje Y
            player_y += player_speed
        if keys[pygame.K_DOWN]:
            # Mover hacia abajo en el eje Y
            player_y -= player_speed
        
        # Limpiar la pantalla
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        # Aplicar iluminación
        iluminacion(1.0, 1.0, 1.0)  # Luz blanca
        
        # Aplicar transformaciones de cámara (si las usas)
        glPushMatrix()
        glTranslatef(cam_x, cam_y, cam_z) # Mueve la cámara

        # Mostrar el fondo del escenario
        es.mostrar_escenario(fondo_actual)

        # Dibujar el personaje seleccionado en su posición
        glPushMatrix()
        # Aplicar la posición del jugador ANTES de las rotaciones específicas del modelo
        glTranslatef(player_x, player_y, player_z)

        if personaje_id == 0:  # JesusL
            # Rotaciones específicas para este modelo
            glRotatef(90, 1, 0, 0)
            glRotatef(180, 0, 1, 0)
            glRotatef(90, 0, 0, 1)
            draw_jesus(0, -3, -2.2, jesus_posicion) # Usar la posición seleccionada
        elif personaje_id == 1:  # Torchic
            glRotatef(180, 0, 1, 0)
            if torchic_posicion == 0:
                draw_torchic()
            elif torchic_posicion == 1:
                draw_triste()
            elif torchic_posicion == 2:
                draw_feliz()
            elif torchic_posicion == 3:
                draw_enojado()
            elif torchic_posicion == 4:
                draw_nervioso()
            elif torchic_posicion == 5:
                draw_cejas_chad()
            draw_torchic() # Dibujar en el origen local
        elif personaje_id == 2:  # Dyson
            # Rotaciones/Traslaciones específicas para este modelo
            draw_dyson((0, 2, 8),emocion="asco") # Ajusta la posición relativa si es necesario
       
        glPopMatrix() # Fin del bloque del personaje

        glPopMatrix() # Fin del bloque de la cámara

        # Mostrar información del nivel (actualizada)
        dibujar_label_texto(f"Nivel 2", pos_x=10, pos_y=580, tam=24)
        dibujar_label_texto(f"Usa las flechas para mover al personaje", pos_x=10, pos_y=550, tam=18)
        dibujar_label_texto(f"Usa W,A,S,D,Z,X para mover la camara (opcional)", pos_x=10, pos_y=520, tam=18)
        dibujar_label_texto(f"Presiona ESC para salir", pos_x=10, pos_y=490, tam=18)
        dibujar_label_texto(f"Presiona 1-5 para cambiar el escenario", pos_x=10, pos_y=460, tam=18)
        
        # Información adicional para JesusL
        if personaje_id == 0:
            dibujar_label_texto(f"Presiona 1-5 para cambiar expresiones de JesusL", pos_x=10, pos_y=430, tam=18)

        pygame.display.flip()
        pygame.time.wait(10) # Considera usar pygame.time.Clock().tick(60) para framerate estable