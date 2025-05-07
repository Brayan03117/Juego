import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # Agregar el directorio padre al sys.path

import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from pygame.locals import *
from time import time

from acciones.renderizarTexto import cargar_textura_desde_texto, renderizar_texto_textura
from Sonidos.sonidos import sonido

def stopsonido():
    pygame.mixer.music.stop()

def mostrar_titulo(display):
    glutInit()
    pygame.mixer.init()
    sonido("sonidos/Tetris.mp3")  # Cambia la ruta según tu archivo de audio

    inicio = time()
    duracion = 3.0
    parpadeo = True

    fuente_grande = pygame.font.Font("Fuentes/PressStart2P-Regular.ttf", 48)
    fuente_pequena = pygame.font.Font("Fuentes/PressStart2P-Regular.ttf", 18)

    # Título sin acentos y dividido en dos líneas
    titulo_linea1 = "LA GRAN AVENTURA"
    titulo_linea2 = "NUMERICA"
    tex_titulo1, w_titulo1, h_titulo1 = cargar_textura_desde_texto(titulo_linea1, fuente_grande, (250, 0, 0))  
    tex_titulo2, w_titulo2, h_titulo2 = cargar_textura_desde_texto(titulo_linea2, fuente_grande, (255, 165, 0))  


    # Créditos
    tex_dev, w_dev, h_dev = cargar_textura_desde_texto("Desarrollado por:", fuente_pequena, (255, 255, 255))
    tex_autor1, w1, h1 = cargar_textura_desde_texto("Jesus Alberto Arroyo Lugo", fuente_pequena, (200, 200, 200))
    tex_autor2, w2, h2 = cargar_textura_desde_texto("Brayan Alberto Lara Garcia", fuente_pequena, (200, 200, 200))
    tex_autor3, w3, h3 = cargar_textura_desde_texto("Milton Florencio Arzate", fuente_pequena, (200, 200, 200))

    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    gluOrtho2D(0, display[0], display[1], 0)
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()

    clock = pygame.time.Clock()
    salto = False

    while time() - inicio < duracion and not salto:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == KEYDOWN and evento.key == K_RETURN:
                salto = True

        glClearColor(0, 0, 0, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

       #glColor3f(1.0, 1.0, 0.0)  # Amarillo
        glColor3f(0.0, 1.0, 0.0)
        glBegin(GL_TRIANGLES)

        margen = 40  # Tamaño de los triángulos

        # Esquina superior izquierda
        glVertex2f(0, 0)
        glVertex2f(margen, 0)
        glVertex2f(0, margen)

        # Esquina superior derecha
        glVertex2f(display[0], 0)
        glVertex2f(display[0] - margen, 0)
        glVertex2f(display[0], margen)

        # Esquina inferior izquierda
        glVertex2f(0, display[1])
        glVertex2f(margen, display[1])
        glVertex2f(0, display[1] - margen)

        # Esquina inferior derecha
        glVertex2f(display[0], display[1])
        glVertex2f(display[0] - margen, display[1])
        glVertex2f(display[0], display[1] - margen)

        glEnd()


        if parpadeo:
            # Renderizar el título centrado y en amarillo en dos líneas (más arriba)
            centro_x = display[0] // 2
            centro_y = display[1] // 2

            # Ajustar las posiciones Y para que el título esté más arriba
            y_titulo_superior = centro_y - h_titulo1 - 50  # Aumentamos la resta para subirlo
            y_titulo_inferior = centro_y - 30           # Disminuimos la suma (o restamos) para subirlo

            renderizar_texto_textura(tex_titulo1, centro_x - w_titulo1 // 2, y_titulo_superior, w_titulo1, h_titulo1)
            renderizar_texto_textura(tex_titulo2, centro_x - w_titulo2 // 2, y_titulo_inferior, w_titulo2, h_titulo2)

        # Renderizar los créditos de forma constante
        centro_x_creditos = display[0] // 2
        base_y_creditos = display[1] // 2 + h_titulo2 + 80 # Ajustar posición de los créditos

        renderizar_texto_textura(tex_dev, centro_x_creditos - w_dev // 2, base_y_creditos, w_dev, h_dev)
        renderizar_texto_textura(tex_autor1, centro_x_creditos - w1 // 2, base_y_creditos + 30, w1, h1)
        renderizar_texto_textura(tex_autor2, centro_x_creditos - w2 // 2, base_y_creditos + 60, w2, h2)
        renderizar_texto_textura(tex_autor3, centro_x_creditos - w3 // 2, base_y_creditos + 90, w3, h3)

        parpadeo = not parpadeo
        pygame.display.flip()
        pygame.time.wait(200)  # Más rápido: 0.2 segundos

        clock.tick(60)

    # Limpiar matrices
    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)

def main():
    pygame.init()
    display = (800, 550)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    mostrar_titulo(display)
    stopsonido() # Apagar el sonido al terminar de mostrar el título

    import main
    main.main()

if __name__ == "__main__":
    main()