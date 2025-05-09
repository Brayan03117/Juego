import pygame
from OpenGL.GL import *

def dibujar_label_texto(texto, pos_x=10, pos_y=580, tam=12, fuente_nombre="consolas", color=(255, 255, 255)):
    """
    Dibuja texto en la pantalla usando OpenGL y Pygame, con soporte para diferentes fuentes y tamaños.

    Parámetros:
    - texto: str. Texto a mostrar (puede tener múltiples líneas con '\n').
    - pos_x, pos_y: int. Posición inicial en pantalla.
    - tam: int. Tamaño de fuente. Se pueden usar tamaños grandes para títulos.
    - fuente_nombre: str. Nombre de la fuente del sistema o fuente instalada (como 'arial', 'timesnewroman', etc.).
    - color: tuple. Color del texto en formato RGB (r, g, b).
    """
    # Crear la fuente
    fuente = pygame.font.SysFont(fuente_nombre, tam)
    lineas = texto.strip().split('\n')

    total_altura = len(lineas) * (tam + 4)
    max_ancho = max([fuente.size(linea)[0] for linea in lineas])

    glPushAttrib(GL_ENABLE_BIT)
    glDisable(GL_TEXTURE_2D)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    glOrtho(0, 800, 0, 600, -1, 1)

    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()

    glColor4f(0, 0, 0, 0.5)
    glBegin(GL_QUADS)
    glVertex2f(pos_x - 10, pos_y + 10)
    glVertex2f(pos_x - 10 + max_ancho + 20, pos_y + 10)
    glVertex2f(pos_x - 10 + max_ancho + 20, pos_y - total_altura - 10)
    glVertex2f(pos_x - 10, pos_y - total_altura - 10)
    glEnd()

    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)
    glPopAttrib()

    for i, linea in enumerate(lineas):
        superficie = fuente.render(linea, True, color, (0, 0, 0))
        text_data = pygame.image.tostring(superficie, "RGBA", True)
        glWindowPos2d(pos_x, pos_y - i * (tam + 4))
        glDrawPixels(superficie.get_width(), superficie.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, text_data)
