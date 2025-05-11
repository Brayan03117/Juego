import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from Esenarios import escenarioObjetos as es
from acciones.iluminacion import iluminacion
from src.textos import dibujar_label_texto
from acciones.jesusL import draw as draw_jesus
from acciones.torchic import personaje2 as draw_torchic
from acciones.dysonEm import dibujar_personaje as draw_dyson
def renderizar_escena(config, estado_juego, tablero):
    """Renderiza toda la escena del nivel"""
    # Limpiar la pantalla
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    # Aplicar iluminación solo si está encendida
    if config['luz_encendida']:
        iluminacion(1.0, 1.0, 1.0)  # Luz blanca
    
    # Aplicar transformaciones de cámara
    glPushMatrix()
    glTranslatef(config['cam_x'], config['cam_y'], config['cam_z'])  # Mueve la cámara

    # Mostrar el fondo del escenario
    es.mostrar_escenario(config['fondo_actual'])

    # Dibujar el personaje seleccionado en su posición
    glPushMatrix()
    # Aplicar la posición del jugador ANTES de las rotaciones específicas del modelo
    glTranslatef(config['player_x'], config['player_y'], config['player_z'])

    if config['personaje_id'] == 0:  # JesusL
        # Rotaciones específicas para este modelo
        glRotatef(90, 1, 0, 0)
        glRotatef(180, 0, 1, 0)
        glRotatef(90, 0, 0, 1)
        draw_jesus(0, -3, -2.2, config['jesus_posicion'])  # Usar la posición seleccionada
    elif config['personaje_id'] == 1:  # Torchic
        glRotatef(180, 0, 1, 0)
        draw_torchic(config['torchic_posicion'])  # Dibujar en el origen local
    elif config['personaje_id'] == 2:  # Dyson
        # Rotaciones/Traslaciones específicas para este modelo
        draw_dyson((0, 2, 8), emocion=config['dyson_emocion'])  # Ajusta la posición relativa si es necesario
   
    glPopMatrix()  # Fin del bloque del personaje
    glPopMatrix()  # Fin del bloque de la cámara

    # Dibujar el tablero de Sudoku
    from Niveles.nivel2_sudoku import dibujar_tablero_sudoku
    dibujar_tablero_sudoku(config, estado_juego, tablero)


    
    tiempo_str = f"{estado_juego.get('tiempo_restante', 0)}s"
    dibujar_label_texto(f"Tiempo restante: {tiempo_str}", pos_x=10, pos_y=370, tam=18)
    # Mostrar información del nivel
    dibujar_label_texto(f"Nivel 2 - Sudoku", pos_x=10, pos_y=580, tam=24)
    dibujar_label_texto(f"Usa las flechas para mover al personaje", pos_x=10, pos_y=550, tam=18)
    dibujar_label_texto(f"Usa W,A,S,D,Z,X para mover la camara", pos_x=10, pos_y=520, tam=18)
    dibujar_label_texto(f"Presiona ESC para salir", pos_x=10, pos_y=490, tam=18)
    dibujar_label_texto(f"Luz: {'Encendida' if config['luz_encendida'] else 'Apagada'}", pos_x=10, pos_y=460, tam=18)
    dibujar_label_texto(f"Errores: {estado_juego['error_count']}", pos_x=10, pos_y=430, tam=18)
    dibujar_label_texto(f"Aciertos: {estado_juego['correct_answers']}", pos_x=10, pos_y=400, tam=18)

def actualizar_personaje(config, estado_juego):
    """Actualiza la apariencia del personaje según el estado del juego"""
    # Esta función se puede expandir según sea necesario
    pass