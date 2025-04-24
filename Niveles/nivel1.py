import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from pygame.locals import *
import sys

# Importar funciones para dibujar escenarios
#from Esenarios.escenario import draw_e

# Importar personajes
from acciones.jesusL import draw as draw_jesus
from acciones.torchic import personaje as draw_torchic
from acciones.dysonEm import dibujar_personaje as draw_dyson

# Importar otras utilidades
from acciones.iluminacion import iluminacion
from src.textos import dibujar_label_texto

def iniciar_nivel1(personaje_id):
    """
    Inicia el nivel 1 con el personaje seleccionado.
    
    Args:
        personaje_id: ID del personaje seleccionado (0=JesusL, 1=Torchic, 2=Dyson)
    """
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Nivel 1")
    
    # Configurar la perspectiva
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    # Ajustamos la cámara inicial para ver mejor al personaje en el origen
    glTranslatef(0.0, -2.0, -10) # Un poco más cerca
    
    # Habilitar prueba de profundidad e iluminación
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_COLOR_MATERIAL)
    
    # Variables para controlar la cámara (opcional, puedes mantenerlas o quitarlas)
    cam_x, cam_y, cam_z = 0, 0, 0
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
        # Puedes añadir K_PAGEUP / K_PAGEDOWN para mover en Z si lo necesitas
        # if keys[pygame.K_PAGEUP]:
        #     player_z -= player_speed # Hacia adelante
        # if keys[pygame.K_PAGEDOWN]:
        #     player_z += player_speed # Hacia atrás
        
        # Limpiar la pantalla
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        # Aplicar iluminación
        iluminacion(1.0, 1.0, 1.0)  # Luz blanca
        
        # Aplicar transformaciones de cámara (si las usas)
        glPushMatrix()
        glTranslatef(cam_x, cam_y, cam_z) # Mueve la cámara
        # Puedes añadir rotación de cámara aquí si quieres
        # glRotatef(rot_x, 1, 0, 0)
        # glRotatef(rot_y, 0, 1, 0)
        
        # Dibujar el escenario (si tienes uno)
        # draw_e() 
        
        # Dibujar el personaje seleccionado en su posición
        glPushMatrix()
        # Aplicar la posición del jugador ANTES de las rotaciones específicas del modelo
        glTranslatef(player_x, player_y, player_z)

        if personaje_id == 0:  # JesusL
            # Rotaciones específicas para este modelo
            glRotatef(90, 1, 0, 0)
            glRotatef(180, 0, 1, 0)
            glRotatef(90, 0, 0, 1)
            # Ajusta las coordenadas relativas si es necesario (probablemente a 0,0,0)
            draw_jesus(0, 0, 0, 0) # Dibujar en el origen local después de translate/rotate
        elif personaje_id == 1:  # Torchic
            # Rotaciones específicas para este modelo
            glRotatef(180, 0, 1, 0)
            draw_torchic() # Dibujar en el origen local
        elif personaje_id == 2:  # Dyson
            # Rotaciones/Traslaciones específicas para este modelo
            # glTranslatef(0, 1.5, 0) # Esta traslación ahora es relativa a player_pos
            draw_dyson((0, 1.5, 0), emocion="asco") # Ajusta la posición relativa si es necesario
        glPopMatrix() # Fin del bloque del personaje
        
        glPopMatrix() # Fin del bloque de la cámara
        
        # Mostrar información del nivel (actualizada)
        dibujar_label_texto(f"Nivel 1", pos_x=10, pos_y=580, tam=24)
        dibujar_label_texto(f"Usa las flechas para mover al personaje", pos_x=10, pos_y=550, tam=18)
        dibujar_label_texto(f"Usa W,A,S,D,Z,X para mover la camara (opcional)", pos_x=10, pos_y=520, tam=18)
        dibujar_label_texto(f"Presiona ESC para salir", pos_x=10, pos_y=490, tam=18)
        
        pygame.display.flip()
        pygame.time.wait(10) # Considera usar pygame.time.Clock().tick(60) para framerate estable