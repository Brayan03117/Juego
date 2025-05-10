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
# from Sonidos.sonidos import sonido # Puedes agregar un sonido de Game Over si lo tienes

# def stop_game_over_sound(): # Si agregas sonido, necesitarás una función para detenerlo
#     pygame.mixer.music.stop()

def mostrar_game_over(display):
    glutInit()
    if not pygame.mixer.get_init(): # Inicializar pygame.mixer si no lo está
        pygame.mixer.init()
    
    try:
        pygame.mixer.music.load("Sonidos/xStep.mp3") # Cargar la música
        pygame.mixer.music.play(-1)  # Reproducir en bucle (-1)
    except pygame.error as e:
        print(f"No se pudo cargar o reproducir la música: Sonidos/xSep.mp3 - {e}")


    parpadeo_activo = True
    tiempo_ultimo_parpadeo = time()
    intervalo_parpadeo = 0.5  # Segundos

    fuente_grande = pygame.font.Font("Fuentes/PressStart2P-Regular.ttf", 60) # Un poco más grande para "GAME OVER"
    fuente_pequena = pygame.font.Font("Fuentes/PressStart2P-Regular.ttf", 18)

    # Título "GAME OVER"
    titulo_game_over = "GAME OVER"
    tex_game_over, w_go, h_go = cargar_textura_desde_texto(titulo_game_over, fuente_grande, (255, 0, 0))  # Rojo

    # Opciones
    opcion_menu_texto = "Presiona ENTER para ir al Menú Principal" # <--- TEXTO CORREGIDO
    tex_op_menu, w_op_menu, h_op_menu = cargar_textura_desde_texto(opcion_menu_texto, fuente_pequena, (255, 255, 255))
    
    # Eliminamos la opción de reiniciar
    # opcion_reiniciar_texto = "Presiona ESPACIO para Reiniciar Nivel"
    # tex_op_reiniciar, w_op_reiniciar, h_op_reiniciar = cargar_textura_desde_texto(opcion_reiniciar_texto, fuente_pequena, (255, 255, 255))

    opcion_salir_texto = "Presiona ESC para Salir del Juego" # <--- CAMBIO DE TEXTO
    tex_op_salir, w_op_salir, h_op_salir = cargar_textura_desde_texto(opcion_salir_texto, fuente_pequena, (255, 255, 255))

    # Configuración de OpenGL para renderizado 2D con texturas
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    gluOrtho2D(0, display[0], display[1], 0)
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()

    glEnable(GL_TEXTURE_2D)  # <--- AÑADIR ESTO
    glEnable(GL_BLEND)       # <--- AÑADIR ESTO (o asegurarse de que esté activo)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA) # <--- AÑADIR ESTO (o asegurarse)


    clock = pygame.time.Clock()
    corriendo = True
    decision = None # Para almacenar la decisión del usuario ('menu', 'salir')

    while corriendo:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == KEYDOWN:
                if evento.key == K_RETURN:
                    decision = 'menu' # <--- VALOR CORREGIDO
                    corriendo = False
                if evento.key == K_ESCAPE:
                    decision = 'salir'
                    corriendo = False
                # Eliminamos la opción de reiniciar
                # if evento.key == K_SPACE:
                #     decision = 'reiniciar'
                #     corriendo = False

        glClearColor(0.1, 0.1, 0.1, 1)  # Fondo gris oscuro
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Triángulos decorativos (opcional, puedes cambiar colores o quitarlos)
        glColor3f(0.5, 0.0, 0.0) # Rojo oscuro
        glBegin(GL_TRIANGLES)
        margen = 40
        glVertex2f(0, 0); glVertex2f(margen, 0); glVertex2f(0, margen)
        glVertex2f(display[0], 0); glVertex2f(display[0] - margen, 0); glVertex2f(display[0], margen)
        glVertex2f(0, display[1]); glVertex2f(margen, display[1]); glVertex2f(0, display[1] - margen)
        glVertex2f(display[0], display[1]); glVertex2f(display[0] - margen, display[1]); glVertex2f(display[0], display[1] - margen)
        glEnd()

        # Parpadeo del texto "GAME OVER"
        if time() - tiempo_ultimo_parpadeo > intervalo_parpadeo:
            parpadeo_activo = not parpadeo_activo
            tiempo_ultimo_parpadeo = time()

        if parpadeo_activo:
            centro_x = display[0] // 2
            y_game_over = display[1] // 2 - h_go // 2 - 50 # Un poco más arriba
            renderizar_texto_textura(tex_game_over, centro_x - w_go // 2, y_game_over, w_go, h_go)

        # Renderizar opciones
        centro_x_opciones = display[0] // 2
        y_opciones_base = display[1] // 2 + h_go // 2 + 30

        renderizar_texto_textura(tex_op_menu, centro_x_opciones - w_op_menu // 2, y_opciones_base, w_op_menu, h_op_menu)
        # Eliminamos la renderización de la opción reiniciar
        # renderizar_texto_textura(tex_op_reiniciar, centro_x_opciones - w_op_reiniciar // 2, y_opciones_base + h_op_menu + 20, w_op_reiniciar, h_op_reiniciar)
        
        # Ajustamos la posición de la opción salir
        renderizar_texto_textura(tex_op_salir, centro_x_opciones - w_op_salir // 2, y_opciones_base + h_op_menu + 20, w_op_salir, h_op_salir)
        
        pygame.display.flip()
        clock.tick(30) # Controlar FPS

    # Limpiar matrices
    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)

    glDisable(GL_TEXTURE_2D) # <--- AÑADIR ESTO para limpiar el estado
    # glDisable(GL_BLEND) # Opcional, dependiendo de si el siguiente estado lo necesita deshabilitado

    if pygame.mixer.get_init(): # Detener sonido si se usó
        pygame.mixer.music.stop() # Detener la música al salir de la pantalla de Game Over
        
    return decision

def main_test_game_over(): # Función de prueba para esta pantalla
    pygame.init()
    display = (800, 550)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    decision_usuario = mostrar_game_over(display)
    print(f"El usuario decidió: {decision_usuario}")

    if decision_usuario == 'pantalla1': # <--- CAMBIO DE VALOR
        print("Yendo a Pantalla 1...")
        # Aquí llamarías a la función que muestra pantalla1.py
        # from Transiciones.pantalla1 import mostrar_pantalla1 # Ejemplo
        # mostrar_pantalla1(display)
        pass
    # Eliminamos la condición de reiniciar
    # elif decision_usuario == 'reiniciar':
    #     print("Reiniciando el nivel...")
    #     # Aquí llamarías a la función que reinicia el nivel actual
    #     # from Niveles.nivel1_main import iniciar_nivel1 # Ejemplo
    #     # iniciar_nivel1() # O como se llame tu función para iniciar/reiniciar el nivel
    #     pass
    elif decision_usuario == 'salir':
        print("Saliendo del juego...")
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main_test_game_over()