import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from pygame.locals import *
from acciones.jesusL import draw as draw_jesus 
from acciones.torchic import personaje as draw_torchic
from acciones.dyson import original5 as draw_dyson  
from Esenarios.escenario import draw_e  
from acciones.iluminacion import iluminacion  


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
        #iluminacion(0, 0, 0)  # Luz blanca
        glColor3f(1.0, 1.0, 1.0)

        # Dibujar JesusL
        glPushMatrix()
        glTranslatef(-3.0, 0.0, 0.0)
        glRotatef(90, 1, 0, 0)  
        glRotatef(180, 0, 1, 0)  
        glRotatef(90, 0, 0, 1)  
        draw_jesus(0, -3, -2.2, 0)          # x,y,z
        glPopMatrix()

        # Dibujar Torchic
        glPushMatrix()
        glTranslatef(3.0, 0.0, 0.0)
        glRotatef(180, 0, 1, 0)  # Girar 180 grados en el eje Y para que mire hacia la cámara
        draw_torchic()
        glPopMatrix()

        # Dibujar dyson
        glPushMatrix()
        glTranslatef(3.0, 1.5, -5.0)      # Posición en el mundo
        #glRotatef(180, 0, 1, 0) 
        glRotatef(375, 0, 1, 0)  
        draw_dyson((-10, 2, 7))             # Posición local en su propio sistema
        glPopMatrix()


        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()