import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from pygame.locals import *
from acciones.jesusL import draw as draw_jesus 
from acciones.torchic import personaje as draw_torchic
from acciones.dyson import original5 as draw_dyson  
from Esenarios.escenario import draw_e  
from acciones import iluminacion  

personaje_posiciones = [(-0.5, 6.0, 0.0), (5.0, 6.0, 0.0), (-6, 6.0, 0.0)]  # Coordenadas para la flecha
seleccion_actual = 0


def main():
    global seleccion_actual
    global personaje_posiciones
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, -2.0, -15)    

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_COLOR_MATERIAL)

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
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_KP_ENTER:
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
        glDisable(GL_LIGHTING)

        if seleccion_actual == 2 or seleccion_actual == 1:
            glEnable(GL_LIGHTING)
            glColor3f(1.0, 1.0, 1.0)  # Iluminado normal
        else:
            glDisable(GL_LIGHTING)
            glColor3f(0.2, 0.2, 0.2)  # Oscuro

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
        draw_dyson((-9, 2, 8))             # Posición local en su propio sistema
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

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()