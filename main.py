import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from pygame.locals import *
from Acciones.jesusL import draw as draw_jesus  # Cambiado
from Acciones.torchic import personaje as draw_torchic  # Cambiado
from Esenarios.escenario import draw_e  # Cambiado
from Acciones.iluminacion import iluminacion  # Cambiado

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, -2.0, -15)

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_COLOR_MATERIAL)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        iluminacion(1.0, 1.0, 1.0)  # Luz blanca

        # Dibujar JesusL
        glPushMatrix()
        glTranslatef(-3.0, 0.0, 0.0)
        draw_jesus(2, 2, 1.5, 0)  
        glPopMatrix()

        # Dibujar Torchic
        glPushMatrix()
        glTranslatef(3.0, 0.0, 0.0)
        draw_torchic()
        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()