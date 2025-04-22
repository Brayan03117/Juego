import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from pygame.locals import *


def cargar_textura_desde_texto(texto, fuente, color=(255, 255, 0)):
    text_surface = fuente.render(texto, True, color)
    text_data = pygame.image.tostring(text_surface, "RGBA", True)
    ancho, alto = text_surface.get_size()

    tex_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, tex_id)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, ancho, alto, 0, GL_RGBA, GL_UNSIGNED_BYTE, text_data)

    return tex_id, ancho, alto

def renderizar_texto_textura(tex_id, x, y, ancho, alto):
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, tex_id)
    glColor3f(1.0, 1.0, 1.0)

    glBegin(GL_QUADS)
    glTexCoord2f(0, 1); glVertex2f(x, y)
    glTexCoord2f(1, 1); glVertex2f(x + ancho, y)
    glTexCoord2f(1, 0); glVertex2f(x + ancho, y + alto)
    glTexCoord2f(0, 0); glVertex2f(x, y + alto)
    glEnd()

    glDisable(GL_TEXTURE_2D)
