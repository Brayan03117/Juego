import pygame
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *

def iluminacion(R, G, B):
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    # Posición de la luz más cercana al objeto
    posicion_luz = (2.0, 2.0, 2.0, 1.0)

    # Luz ambiental menos intensa
    luz_ambiental = (1.0, 0.0, 0.0, 1.0)

    # Luz difusa con el color especificado
    difusion = (R, G, B, 0.1)

    # Luz especular (opcional, para añadir brillo)
    especular = (0.5, 0.5, 0.5, 1.0)

    glLightfv(GL_LIGHT0, GL_POSITION, posicion_luz)
    glLightfv(GL_LIGHT0, GL_AMBIENT, luz_ambiental)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, difusion)
    glLightfv(GL_LIGHT0, GL_SPECULAR, especular)

    # Configurar el material del objeto
    glMaterialfv(GL_FRONT, GL_DIFFUSE, (R, G, B, 1.0))
    glMaterialfv(GL_FRONT, GL_SPECULAR, (1.0, 1.0, 1.0, 1.0))
    glMaterialf(GL_FRONT, GL_SHININESS, 50.0)