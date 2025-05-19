import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from Esenarios import escenarioObjetos2 as es # Podría ser escenarioObjetos3
from acciones.iluminacion import iluminacion
from src.textos import dibujar_label_texto
from acciones.jesusL import draw as draw_jesus
from acciones.torchic import personaje2 as draw_torchic
from acciones.dysonEm import dibujarPersonaje as draw_dyson
from src.objetosDinamicos import dibujar_objetos_dinamicos

def renderizar_escena(config, estado_juego, tablero):
    """Renderiza toda la escena del nivel"""
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    if config['luz_encendida']:
        iluminacion(1.0, 1.0, 1.0)  
    # Si la luz está apagada, la función iluminacion no se llama o se llama con parámetros oscuros
    # La lógica de encender/apagar la luz (glEnable/glDisable(GL_LIGHTING)) 
    # se maneja en el bucle principal de nivel3.py
    
    glPushMatrix()
    glTranslatef(config['cam_x'], config['cam_y'], config['cam_z'])  

    es.mostrar_escenario(config['fondo_actual'],-5,5,config['pista_activa']) # Podría ser es_nivel3
    dibujar_objetos_dinamicos()

    glPushMatrix()
    glTranslatef(config['player_x'], config['player_y'], config['player_z'])

    if config['personaje_id'] == 0:  
        glRotatef(90, 1, 0, 0)
        glRotatef(180, 0, 1, 0)
        glRotatef(90, 0, 0, 1)
        draw_jesus(0, -3, -2.2, config['jesus_posicion'])  
    elif config['personaje_id'] == 1:  
        glRotatef(180, 0, 1, 0)
        draw_torchic(config['torchic_posicion'])  
    elif config['personaje_id'] == 2:  
        draw_dyson(config['dyson_posicion'],(0, 2, 0), emocion=config['dyson_emocion'])
   
    glPopMatrix()  
    glPopMatrix()  

    # Cambiar a nivel3_sudoku si es necesario
    from Niveles.nivel3_sudoku import dibujar_tablero_sudoku 
    if config.get('mostrar_tablero', True):
        dibujar_tablero_sudoku(config, estado_juego, tablero)

    tiempo_str = f"{estado_juego.get('tiempo_restante', 0)}s"
    
    if config.get('mostrar_texto', True):
        dibujar_label_texto(f"Nivel 3 - Sudoku Oscuro", pos_x=10, pos_y=580, tam=24) # Cambiado a Nivel 3
        dibujar_label_texto(f"Usa las flechas para mover al personaje", pos_x=10, pos_y=550, tam=18)
        dibujar_label_texto(f"Presiona ESC para salir", pos_x=10, pos_y=490, tam=18)
        dibujar_label_texto(f"Luz: {'Encendida' if config['luz_encendida'] else 'Apagada'}", pos_x=10, pos_y=460, tam=18)
        dibujar_label_texto(f"Errores: {estado_juego['error_count']}", pos_x=10, pos_y=430, tam=18)
        dibujar_label_texto(f"Aciertos: {estado_juego['correct_answers']}", pos_x=10, pos_y=400, tam=18)
        dibujar_label_texto(f"Tiempo restante: {tiempo_str}", pos_x=10, pos_y=370, tam=18)
        dibujar_label_texto(f"Objeto azul: +10 segundos", pos_x=10, pos_y=340, tam=18)
        dibujar_label_texto(f"Objeto Naranja: -1 error", pos_x=10, pos_y=310, tam=18)
        dibujar_label_texto(f"Tecla P: Act/Desact Parpadeo Luz", pos_x=10, pos_y=280, tam=18)
        
    if estado_juego.get('mostrar_mensaje_tecla', False):
        dibujar_label_texto(estado_juego['mensaje_tecla'], pos_x=config['display'][0]//2 - 100, pos_y=config['display'][1]//2, tam=36, color=(255, 0, 0))

def actualizar_personaje(config, estado_juego):
    """Actualiza la apariencia del personaje según el estado del juego"""
    pass