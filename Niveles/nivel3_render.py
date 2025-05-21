import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from Esenarios import escenarioObjetos2 as es
from acciones.iluminacion import iluminacion
from src.textos import dibujar_label_texto
from acciones.jesusL import draw as draw_jesus
from acciones.torchic import personaje2 as draw_torchic
from acciones.dysonEm import dibujarPersonaje as draw_dyson
from src.objetosDinamicosNiv3 import dibujar_objetos_dinamicos

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
    es.mostrar_escenario(config['fondo_actual'],-5,0,config['pista_activa'])
    dibujar_objetos_dinamicos()

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
        draw_dyson(config['dyson_posicion'],(0, 2, 0), emocion=config['dyson_emocion'])  # Ajusta la posición relativa si es necesario
   
    glPopMatrix()  # Fin del bloque del personaje
    glPopMatrix()  # Fin del bloque de la cámara

    # Dibujar el tablero de Sudoku
    from Niveles.nivel3_sudoku import dibujar_tablero_sudoku
    if config.get('mostrar_tablero', True):
        dibujar_tablero_sudoku(config, estado_juego, tablero)

    tiempo_str = f"{estado_juego.get('tiempo_restante', 0)}s"
    
    # Mostrar información del nivel SOLO si mostrar_texto está activo
    if config.get('mostrar_texto', True):
        dibujar_label_texto(f"Nivel 3 - Sudoku Presiona la Tecla T quitar/mostrar instrucciones", pos_x=10, pos_y=580, tam=20)
        dibujar_label_texto("Sudoku se oculta si tiempo < 20s o si presionas Y", pos_x=10, pos_y=520, tam=15)
        dibujar_label_texto("Sudoku aparece cuando tiempo ≥ 60s", pos_x=10, pos_y=490, tam=15)
        dibujar_label_texto(f"Usa las flechas para mover al personaje", pos_x=10, pos_y=550, tam=15)
        dibujar_label_texto(f"Usa el mouse para seleccionar las celdas", pos_x=10, pos_y=520, tam=15)
        dibujar_label_texto(f"Presiona 1-9 para insertar un número en la celda seleccionada", pos_x=10, pos_y=490, tam=15)
        dibujar_label_texto(f"Presiona ESC para salir", pos_x=10, pos_y=460, tam=15)
        dibujar_label_texto(f"Luz: {'Encendida' if config['luz_encendida'] else 'Apagada'}", pos_x=10, pos_y=430, tam=15)
        dibujar_label_texto(f"Errores: {estado_juego['error_count']}", pos_x=10, pos_y=400, tam=15)
        dibujar_label_texto(f"Aciertos: {estado_juego['correct_answers']}", pos_x=10, pos_y=370, tam=15)
        dibujar_label_texto(f"Objeto azul: +10 segundos", pos_x=10, pos_y=340, tam=15)
        dibujar_label_texto(f"Objeto Naranja: -1 error", pos_x=10, pos_y=310, tam=15)
        dibujar_label_texto(f"Objeto Verde: +1 acierto", pos_x=10, pos_y=280, tam=15)
        dibujar_label_texto(f"No puede haber 2 numeros iguales en una fila o columna", pos_x=10, pos_y=250, tam=15)
        dibujar_label_texto(f"Objetivo: Completa el Sudoku antes de que termina el tiempo", pos_x=10, pos_y=230, tam=15)

    # Mostrar el cronómetro en rojo y abajo
    tiempo_str = f"Tiempo restante: {estado_juego.get('tiempo_restante', 0)}s"
    dibujar_label_texto(tiempo_str, pos_x=config['display'][0] // 2 - 50, pos_y=30, tam=20, color=(255, 0, 0))

    # Mostrar "PAUSA" si el juego está en pausa
    if config['pausa']:
        dibujar_label_texto("Reanudar", pos_x=config['display'][0] // 2 - 50, pos_y=config['display'][1] // 2, tam=48, color=(255, 0, 0))
        
    # Mostrar mensaje de tecla no válida si está activo
    if estado_juego.get('mostrar_mensaje_tecla', False):
        dibujar_label_texto(estado_juego['mensaje_tecla'], pos_x=config['display'][0]//2 - 100, pos_y=config['display'][1]//2, tam=36, color=(255, 0, 0))

def actualizar_personaje(config, estado_juego):
    """Actualiza la apariencia del personaje según el estado del juego"""
    # Esta función se puede expandir según sea necesario
    pass