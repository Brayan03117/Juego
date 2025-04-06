import pygame
from OpenGL.GLU import*
from OpenGL.GL import*
from OpenGL.GLUT import*
from pygame.locals import*
from PIL import Image

pygame.init()
pygame.mixer.init()


def load_texture(FileName):
    im = Image.open(FileName)
    ix, iy = im.size # ix e iy ahora obtienen el ancho y alto de la imagen
 
    image = im.tobytes("raw", "RGBX", 0, -1)
        
    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)

    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

    return texture_id

def draw_e(fileImage):
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, load_texture(fileImage))

    vertices = (
        # Pared trasera
        (0, 0, 15),
        (15, 0, 15),
        (15, 15, 15),
        (0, 15, 15),
        # Pared delantera
        (0, 0, 0),
        (15, 0, 0),
        (15, 15, 0),
        (0, 15, 0),
        # Pared izquierda
        (0, 0, 15),
        (0, 0, 0),
        (0, 15, 0),
        (0, 15, 15),
        # Pared derecha
        (15, 0, 15),
        (15, 0, 0),
        (15, 15, 0),
        (15, 15, 15),
        # Techo
        (0, 15, 15),
        (15, 15, 15),
        (15, 15, 0),
        (0, 15, 0),
        # Piso
        (0, 0, 15),
        (15, 0, 15),
        (15, 0, 0),
        (0, 0, 0)
    )

    texcoords = (
    # Pared trasera
    (0, 1), (1, 1), (1, 0), (0, 0),
    # Pared delantera
    (0, 1), (1, 1), (1, 0), (0, 0),
    # Pared izquierda
    (0, 1), (0, 0), (1, 0), (1, 1),
    # Pared derecha
    (0, 1), (0, 0), (1, 0), (1, 1),
    # Techo
    (0, 1), (1, 1), (1, 0), (0, 0),
    # Piso
    (0, 1), (1, 1), (1, 0), (0, 0)
)

    # Definición de índices para las caras
    faces = (
        (0, 1, 2, 3),  # Pared trasera
        (4, 5, 6, 7),  # Pared delantera
        (8, 9, 10, 11),  # Pared izquierda
        (12, 13, 14, 15),  # Pared derecha
        (16, 17, 18, 19),  # Techo
        (20, 21, 22, 23)  # Piso
    )

    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_QUADS)
    for face in faces:
        for i in range(4):
            glTexCoord2fv(texcoords[face[i]])
            glVertex3fv(vertices[face[i]])
    glEnd()

    glDisable(GL_TEXTURE_2D)