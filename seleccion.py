import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from pygame.locals import *
from OpenGL.GLUT import GLUT_BITMAP_TIMES_ROMAN_24
from acciones.jesusL import draw as draw_jesus 
from acciones.torchic import personaje as draw_torchic
#from acciones.dyson import original5 as draw_dyson  
from acciones.dysonEm import dibujar_personaje as draw_dyson
# from Esenarios.escenario import draw_e  
from acciones import iluminacion  
from src.textos import dibujar_label_texto


personaje_posiciones = [(-0.5, 6.0, 0.0), (5.0, 6.0, 0.0), (-6, 6.0, 0.0)]  # Coordenadas para la flecha
personaje_nombres = ["JESUSL", "TORCHIC", "DYSON"]  # Nombres de los personajes
seleccion_actual = 0

# Definir una función básica para renderizar texto
def renderizar_texto(texto, x, y, escala=1.0, color=(1.0, 1.0, 1.0)):
    """Función básica para renderizar texto en OpenGL"""
    glDisable(GL_LIGHTING)
    glColor3f(*color)
    glRasterPos2f(x, y)
    for caracter in texto:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(caracter))
    glEnable(GL_LIGHTING)


def main():
    global seleccion_actual
    global personaje_posiciones
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("Sonidos/Jumper.mp3")
    pygame.mixer.music.play(-1)
    display = (800, 600)
    pygame.display.quit()
    pygame.display.init()
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, -2.0, -15)    

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_COLOR_MATERIAL)

    # Inicializar GLUT para renderizar texto
    glutInit()

    #iluminacion.activar_iluminacion('phong')  # Cambia el modelo de iluminación aquí

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    seleccion_actual = (seleccion_actual + 1) % len(personaje_posiciones)
                elif event.key == pygame.K_LEFT:
                    seleccion_actual = (seleccion_actual - 1) % len(personaje_posiciones)
                elif event.key in (pygame.K_KP_ENTER, pygame.K_RETURN):
                    pygame.display.quit()
                    return seleccion_actual

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        iluminacion.iluminacion(0, 0, 0)  # Luz blanca
        glColor3f(1.0, 1.0, 1.0)

        # Dibujar JesusL
        glPushMatrix()
        glTranslatef(-1.5, 0.0, 0.0)
        glRotatef(90, 1, 0, 0)  
        glRotatef(180, 0, 1, 0)  
        glRotatef(90, 0, 0, 1)  
        #glDisable(GL_LIGHTING)

        if seleccion_actual == 2 or seleccion_actual == 1:
            glEnable(GL_LIGHTING)
            glColor3f(1.0, 1.0, 1.0)  # Iluminado normal
        else:
            glDisable(GL_LIGHTING)
            glColor3f(0, 0, 0)  # Oscuro

        draw_jesus(0, -3, -2.2, 0)   
        glPopMatrix()


        # Dibujar Torchic
        glPushMatrix()
        glTranslatef(5.0, 0.0, 0.0)
        glRotatef(180, 0, 1, 0)  # Girar 180 grados en el eje Y para que mire hacia la cámara
        if seleccion_actual == 0 or seleccion_actual == 2:
            glEnable(GL_LIGHTING)
            glColor3f(1.0, 1.0, 1.0)
        else:
            glDisable(GL_LIGHTING)
            glColor3f(0.2, 0.2, 0.2)
        draw_torchic()
        glPopMatrix()


        # Dibujar Dyson
        glPushMatrix()
        glTranslatef(3.0, 1.5, -4.0)      # Posición en el mundo
        glRotatef(0, 0, 1, 0) 
        if seleccion_actual == 1 or seleccion_actual == 0:
            glEnable(GL_LIGHTING)
            glColor3f(1.0, 1.0, 1.0)
        else:
            glDisable(GL_LIGHTING)
            glColor3f(0.2, 0.2, 0.2) 
        draw_dyson((-9, 2, 8),emocion="dormir")             # Posición local en su propio sistema
        glPopMatrix()


        # Dibujar flecha sobre personaje seleccionado
        glPushMatrix()
        glTranslatef(*personaje_posiciones[seleccion_actual])
        glDisable(GL_LIGHTING)
        glColor3f(1.0, 0.0, 0.0)
        glBegin(GL_TRIANGLES)
        glVertex3f(0.0, 0.0, 0.0)   # Punto inferior (punta de la flecha)
        glVertex3f(-0.5, 1.0, 0.0)  # Izquierda
        glVertex3f(0.5, 1.0, 0.0)   # Derecha
        glEnd()
        glEnable(GL_LIGHTING)
        glPopMatrix()

        # Dibujar el nombre del personaje seleccionado en la parte inferior
        glMatrixMode(GL_PROJECTION)
        glPushMatrix()
        glLoadIdentity()
        gluOrtho2D(0, display[0], 0, display[1])
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glLoadIdentity()
        glDisable(GL_LIGHTING)
        glDisable(GL_DEPTH_TEST)
        
        # Dibujar un fondo para el texto
        glColor4f(0.0, 0.0, 0.0, 0.7)  # Negro semi-transparente
        glBegin(GL_QUADS)
        glVertex2f(0, 0)
        glVertex2f(display[0], 0)
        glVertex2f(display[0], 50)
        glVertex2f(0, 50)
        glEnd()
        
        # Dibujar el texto del nombre con colores más llamativos
        nombre_personaje = personaje_nombres[seleccion_actual]
        
        # Usar colores diferentes según el personaje seleccionado
        if seleccion_actual == 0:  # JESUSL
            color_texto = (1.0, 0.8, 0.0)  # Dorado
        elif seleccion_actual == 1:  # TORCHICH
            color_texto = (1.0, 0.5, 0.0)  # Naranja
        else:  # DYSON
            color_texto = (0.0, 0.8, 1.0)  # Azul claro
            
        # Usar una escala mayor para hacer el texto más grande
        renderizar_texto(f"PERSONAJE: {nombre_personaje}", display[0]/2 - 120, 20, escala=2.0, color=color_texto)
        
        # Restaurar matrices
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glPopMatrix()
        glMatrixMode(GL_PROJECTION)
        glPopMatrix()
        glMatrixMode(GL_MODELVIEW)


        dibujar_label_texto("Selecciona tu personaje", pos_x=220, pos_y=550, tam=24)
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
