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

def iniciar_nivel3(personaje_id):
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
    glTranslatef(0.0, -2.0, -15)
    
    # Habilitar prueba de profundidad e iluminación
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_COLOR_MATERIAL)
    
    # Variables para controlar la cámara
    cam_x, cam_y, cam_z = 0, 0, 0
    rot_x, rot_y = 0, 0
    
    # Bucle principal del juego
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            # Control de teclado para mover la cámara
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return
                # Movimiento de cámara
                elif event.key == pygame.K_w:
                    cam_z += 1
                elif event.key == pygame.K_s:
                    cam_z -= 1
                elif event.key == pygame.K_a:
                    cam_x += 1
                elif event.key == pygame.K_d:
                    cam_x -= 1
                elif event.key == pygame.K_z:
                    cam_y += 1
                elif event.key == pygame.K_x:
                    cam_y -= 1
        
        # Limpiar la pantalla
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        # Aplicar iluminación
        iluminacion(1.0, 1.0, 1.0)  # Luz blanca
        
        # Aplicar transformaciones de cámara
        glPushMatrix()
        glTranslatef(cam_x, cam_y, cam_z)
        glRotatef(rot_x, 1, 0, 0)
        glRotatef(rot_y, 0, 1, 0)
        
        # Dibujar el escenario
        
        # Dibujar el personaje seleccionado
        glPushMatrix()
        if personaje_id == 0:  # JesusL
            glTranslatef(0, 0, 0)
            glRotatef(90, 1, 0, 0)
            glRotatef(180, 0, 1, 0)
            glRotatef(90, 0, 0, 1)
            draw_jesus(0, -3, -2.2, 0)
        elif personaje_id == 1:  # Torchic
            glTranslatef(0, 0, 0)
            glRotatef(180, 0, 1, 0)
            draw_torchic()
        elif personaje_id == 2:  # Dyson
            glTranslatef(0, 1.5, 0)
            draw_dyson((0, 0, 0), emocion="asco")
        glPopMatrix()
        
        glPopMatrix()
        
        # Mostrar información del nivel
        dibujar_label_texto(f"Nivel 1", pos_x=10, pos_y=580, tam=24)
        dibujar_label_texto(f"Usa W,A,S,D,Z,X para moverte", pos_x=10, pos_y=550, tam=18)
        dibujar_label_texto(f"Presiona ESC para salir", pos_x=10, pos_y=520, tam=18)
        
        pygame.display.flip()
        pygame.time.wait(10)