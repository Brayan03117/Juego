import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
from src.textos import dibujar_label_texto

opciones = ["Iniciar", "Seleccionar Personaje", "Salir"]
coordenadas_opciones = [(150, 280), (150, 230), (150, 180)]
seleccion_actual = 0

def pantalla_inicial():
    global seleccion_actual
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluOrtho2D(0, 800, 0, 600)
    glClearColor(0, 0, 0, 1)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return "salir"
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    seleccion_actual = (seleccion_actual - 1) % len(opciones)
                elif event.key == K_DOWN:
                    seleccion_actual = (seleccion_actual + 1) % len(opciones)
                elif event.key in (K_RETURN, K_KP_ENTER):
                    return opciones[seleccion_actual].lower().replace(" ", "_")
                elif event.key == K_ESCAPE:
                    return "salir"

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Título del juego
        dibujar_label_texto("La Gran Aventura Numérica", pos_x=180, pos_y=500, tam=36)

        # Dibuja las opciones
        for i, texto in enumerate(opciones):
            x, y = coordenadas_opciones[i]
            dibujar_label_texto(texto, pos_x=x, pos_y=y, tam=28)

        # Dibuja el triangulito de selección (ajustado)
        glColor3f(1, 0, 0)
        x, y = coordenadas_opciones[seleccion_actual]
        glBegin(GL_TRIANGLES)
        glVertex2f(x - 40, y - 8)
        glVertex2f(x - 20, y)
        glVertex2f(x - 40, y + 8)
        glEnd()

        pygame.display.flip()
        pygame.time.wait(10)
