import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from pygame.locals import *
import sys

# Importar funciones para dibujar escenarios
from Esenarios import escenarioObjetos as es

# Importar personajes
from acciones.jesusL import draw as draw_jesus
from acciones.torchic import personaje as draw_torchic
from acciones.dysonEm import dibujar_personaje as draw_dyson
from acciones.expresiones import draw_cejas_chad,draw_feliz,draw_triste,draw_enojado,draw_nervioso

# Importar otras utilidades
from acciones.iluminacion import iluminacion
from src.textos import dibujar_label_texto
from src.colisiones import hay_colision

# Importar módulo para sonidos
import os

def iniciar_nivel3(personaje_id):
    """
    Inicia el nivel 3 con el personaje seleccionado.
    
    Args:
        personaje_id: ID del personaje seleccionado (0=JesusL, 1=Torchic, 2=Dyson)
    """
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Nivel 3")
    
    # Inicializar el módulo de sonido
    pygame.mixer.init()
    
    # Cargar los sonidos para cada escenario
    sonidos_escenarios = {
        1: pygame.mixer.Sound(os.path.join("Sonidos", "BackOnTrack.mp3")),
        2: pygame.mixer.Sound(os.path.join("Sonidos", "Cycles.mp3")),
        3: pygame.mixer.Sound(os.path.join("Sonidos", "Electroman.mp3")),
        4: pygame.mixer.Sound(os.path.join("Sonidos", "GeometricalDominator.mp3")),
        5: pygame.mixer.Sound(os.path.join("Sonidos", "Jumper.mp3"))
    }

    # Inicializar fondos
    es.inicializar_fondos()
    # Puedes cambiar el índice del fondo si quieres otro diferente
    fondo_actual = 2
    
    # Variable para controlar la posición de JesusL
    jesus_posicion = 0

    torchic_posicion = 0

    dyson_emocion="original"
    
    # Variable para controlar la iluminación
    luz_encendida = True

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
                # Control de iluminación
                elif event.key == pygame.K_6:  # Tecla 6 para apagar la luz
                    luz_encendida = False
                    glDisable(GL_LIGHTING)
                elif event.key == pygame.K_7:  # Tecla 7 para encender la luz
                    luz_encendida = True
                    glEnable(GL_LIGHTING)
                # En la sección donde manejas los eventos de teclado:
                # Cambio de escenarios y posiciones
                elif event.key == pygame.K_1:
                    # Detener sonido actual y reproducir el nuevo
                    for sonido in sonidos_escenarios.values():
                        sonido.stop()
                    sonidos_escenarios[1].play()
                    
                    fondo_actual = 1
                    if personaje_id == 0:  # Solo si es JesusL
                        jesus_posicion = 1
                    if personaje_id == 2: 
                        dyson_emocion="happy"
                    if personaje_id == 1:  # Solo si es Torchic
                        torchic_posicion = 1
                elif event.key == pygame.K_2:
                    # Detener sonido actual y reproducir el nuevo
                    for sonido in sonidos_escenarios.values():
                        sonido.stop()
                    sonidos_escenarios[2].play()
                    
                    fondo_actual = 2
                    if personaje_id == 0:  # Solo si es JesusL
                        jesus_posicion = 2
                    if personaje_id == 2: 
                        dyson_emocion="sad"
                    if personaje_id == 1:
                        torchic_posicion = 2
                elif event.key == pygame.K_3:
                    # Detener sonido actual y reproducir el nuevo
                    for sonido in sonidos_escenarios.values():
                        sonido.stop()
                    sonidos_escenarios[3].play()
                    
                    fondo_actual = 3
                    if personaje_id == 0:  # Solo si es JesusL
                        jesus_posicion = 3
                    if personaje_id == 2: 
                        dyson_emocion="asco"
                    if personaje_id == 1:
                        torchic_posicion = 3
                elif event.key == pygame.K_4:
                    # Detener sonido actual y reproducir el nuevo
                    for sonido in sonidos_escenarios.values():
                        sonido.stop()
                    sonidos_escenarios[4].play()
                    
                    fondo_actual = 4
                    if personaje_id == 0:  # Solo si es JesusL
                        jesus_posicion = 4
                    if personaje_id == 2: 
                        dyson_emocion="admirar"
                    if personaje_id == 1:
                        torchic_posicion = 4
                elif event.key == pygame.K_5:
                    # Detener sonido actual y reproducir el nuevo
                    for sonido in sonidos_escenarios.values():
                        sonido.stop()
                    sonidos_escenarios[5].play()
                    
                    fondo_actual = 5
                    if personaje_id == 0:  # Solo si es JesusL
                        jesus_posicion = 5
                    if personaje_id == 2: 
                        dyson_emocion="dormir"
                    if personaje_id == 1:
                        torchic_posicion = 5


        # --- Control de movimiento del personaje (fuera del bucle de eventos) ---
        keys = pygame.key.get_pressed()
        nueva_x, nueva_y = player_x, player_y
        if keys[pygame.K_LEFT]:
            nueva_x -= player_speed
        if keys[pygame.K_RIGHT]:
            nueva_x += player_speed
        if keys[pygame.K_UP]:
            # Mover hacia arriba en el eje Y
            nueva_y += player_speed
        if keys[pygame.K_DOWN]:
            # Mover hacia abajo en el eje Y
            nueva_y -= player_speed
        
        nueva_pos = [nueva_x, nueva_y, player_z]

        if not hay_colision(nueva_pos):
            player_x, player_y = nueva_x, nueva_y
        
        
        # Limpiar la pantalla
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        # Aplicar iluminación solo si está encendida
        if luz_encendida:
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
            draw_dyson((0, 2, 8),emocion=dyson_emocion) # Ajusta la posición relativa si es necesario
       
        glPopMatrix() # Fin del bloque del personaje

        glPopMatrix() # Fin del bloque de la cámara

        # Mostrar información del nivel (actualizada)
        dibujar_label_texto(f"Nivel 3", pos_x=10, pos_y=580, tam=24)
        dibujar_label_texto(f"Usa las flechas para mover al personaje", pos_x=10, pos_y=550, tam=18)
        dibujar_label_texto(f"Usa W,A,S,D,Z,X para mover la camara (opcional)", pos_x=10, pos_y=520, tam=18)
        dibujar_label_texto(f"Presiona ESC para salir", pos_x=10, pos_y=490, tam=18)
        dibujar_label_texto(f"Presiona 1-5 para cambiar el escenario y expresiones", pos_x=10, pos_y=460, tam=18)
        dibujar_label_texto(f"Presiona 6 para apagar la luz, 7 para encenderla", pos_x=10, pos_y=430, tam=18)
        dibujar_label_texto(f"Luz: {'Encendida' if luz_encendida else 'Apagada'}", pos_x=10, pos_y=400, tam=18)

        pygame.display.flip()
        pygame.time.wait(10) # Considera usar pygame.time.Clock().tick(60) para framerate estable