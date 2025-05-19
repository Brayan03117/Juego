import pygame
from OpenGL.GL import *
from src.colisiones import hay_colision
# Cambiar a nivel3_config si es necesario ajustar algo específico para el nivel 3
from Niveles.nivel3_config import cambiar_escenario_y_musica 
from Transiciones.GameOver import mostrar_game_over 
from Esenarios.escenarioObjetos2 import obtener_obstaculos # Podría ser escenarioObjetos3
from src.objetosDinamicos import obtener_objetos_dinamicos, generar_objetos_dinamicos
from sonidos import sonidos as so

def manejar_eventos(config, estado_juego, tablero, solucion):
    """Maneja todos los eventos del nivel"""
    if estado_juego.get('mostrar_mensaje_tecla', False):
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - estado_juego.get('tiempo_mensaje_tecla', 0) > 2000:  # 2 segundos
            estado_juego['mostrar_mensaje_tecla'] = False
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            for sonido in config['sonidos_escenarios'].values():
                sonido.stop()
            pygame.quit()
            return "salir"
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                for sonido in config['sonidos_escenarios'].values():
                    sonido.stop()
                return "back"
            elif event.key == pygame.K_w:
                if config['cam_z'] < 20:
                    config['cam_z'] += 0.5
            elif event.key == pygame.K_s:
                if config['cam_z'] > 10:
                    config['cam_z'] -= 0.5
            # La lógica de L y K para encender/apagar luz manualmente se puede quitar
            # ya que ahora es automático, o dejarla para debug.
            # Por ahora la comentaré para evitar conflictos con la luz intermitente.
            # elif event.key == pygame.K_l:  # Tecla L para apagar la luz
            #     config['luz_encendida'] = False
            #     glDisable(GL_LIGHTING)
            #     estado_juego['luz_intermitente_activa'] = False # Desactivar parpadeo si se controla manualmente
            # elif event.key == pygame.K_k:  # Tecla K para encender la luz
            #     config['luz_encendida'] = True
            #     glEnable(GL_LIGHTING)
            #     estado_juego['luz_intermitente_activa'] = False # Desactivar parpadeo
            elif event.key == pygame.K_p: # Tecla P para reactivar/desactivar parpadeo de luz (opcional)
                estado_juego['luz_intermitente_activa'] = not estado_juego.get('luz_intermitente_activa', True)
                if not estado_juego['luz_intermitente_activa'] and not config['luz_encendida']:
                     glEnable(GL_LIGHTING) # Si se desactiva el parpadeo y estaba apagada, encenderla
                     config['luz_encendida'] = True

            elif event.key == pygame.K_t:  # Tecla T para mostrar/ocultar texto
                config['mostrar_texto'] = not config.get('mostrar_texto', True)
            elif event.key == pygame.K_y:
                config['mostrar_tablero'] = not config.get('mostrar_tablero', True)
            
            elif event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4,pygame.K_5,pygame.K_6]:
                input_value = event.key - pygame.K_0
                if estado_juego['selected_cell'] is not None:
                    row, col = estado_juego['selected_cell']
                    if tablero[row][col] == 0:
                        if input_value == solucion[row][col]:
                            tablero[row][col] = input_value
                            if config['personaje_id'] == 0:  
                                config['jesus_posicion'] = estado_juego['correct_answers'] % 5  
                            estado_juego['last_insertion'] = (row, col, input_value)
                            estado_juego['correct_answers'] += 1
                            so.sonido("sonidos/feli.mp3")
                            cambiar_escenario_y_musica(config)
                        else:
                            estado_juego['error_count'] += 1
                            if config['personaje_id'] == 0: 
                                config['jesus_posicion'] = pygame.time.get_ticks() % 5  
                            estado_juego['last_insertion'] = (row, col, input_value)
                            if config['personaje_id'] == 1:  
                                config['torchic_posicion'] = config['torchic_posicion']+1
                            elif config['personaje_id'] == 2:  
                                config['dyson_emocion'] = "sad"
                                config['dyson_posicion'] = config['dyson_posicion']+1
                            if estado_juego['error_count'] >= 5:
                                for sonido_escenario in config['sonidos_escenarios'].values():
                                    sonido_escenario.stop()
                                decision_game_over = mostrar_game_over(config['display'])
                                if decision_game_over == 'menu':
                                    return "menu" 
                                elif decision_game_over == 'salir':
                                    pygame.quit()
                                    return "salir"
            elif event.key in [pygame.K_7, pygame.K_8, pygame.K_9, pygame.K_0]:
                if estado_juego['selected_cell'] is not None:
                    row, col = estado_juego['selected_cell']
                    if tablero[row][col] == 0 and event.key not in [pygame.K_LEFT,pygame.K_RIGHT,pygame.K_UP,pygame.K_DOWN]: 
                        if config['personaje_id'] == 0:  
                            config['jesus_posicion'] = pygame.time.get_ticks() % 5  
                        estado_juego['mostrar_mensaje_tecla'] = True
                        estado_juego['mensaje_tecla'] = "¡TECLA NO VÁLIDA!"
                        estado_juego['tiempo_mensaje_tecla'] = pygame.time.get_ticks()
            elif event.key in [pygame.K_LEFT, pygame.K_RIGHT ,pygame.K_UP , pygame.K_DOWN]:
                pass # El movimiento se maneja en manejar_movimiento
            else:
                if estado_juego['selected_cell'] is not None:
                    row, col = estado_juego['selected_cell']
                    if tablero[row][col] == 0:
                        if config['personaje_id'] == 0:  
                            config['jesus_posicion'] = pygame.time.get_ticks() % 5  
                        estado_juego['mostrar_mensaje_tecla'] = True
                        estado_juego['mensaje_tecla'] = "¡TECLA NO VÁLIDA!"
                        estado_juego['tiempo_mensaje_tecla'] = pygame.time.get_ticks()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  
                x, y = event.pos
                y = config['display'][1] - y  
                
                cell_size = 50
                board_width = 6 * cell_size
                board_height = 6 * cell_size
                board_x = config['display'][0] - board_width - 20
                board_y = config['display'][1] - board_height -20
                
                if (board_x <= x <= board_x + board_width and
                    board_y <= y <= board_y + board_height):
                    col = int((x - board_x) / cell_size)
                    row = 5 - int((y - board_y) / cell_size)  
                    estado_juego['selected_cell'] = (row, col)
    
    return "continuar"

def manejar_movimiento(config,estado_juego):
    """Maneja el movimiento del personaje"""
    keys = pygame.key.get_pressed()
    nueva_x, nueva_y = config['player_x'], config['player_y']
    
    if keys[pygame.K_LEFT]:
        if config['cam_x'] < 20:
            config['cam_x'] += 0.5
            nueva_x -= config['player_speed']
    if keys[pygame.K_RIGHT]:
        if config['cam_x'] > -20:  
            config['cam_x'] -= 0.5
            nueva_x += config['player_speed']
    if keys[pygame.K_UP]:
        if config['cam_y'] > -10: 
            config['cam_y'] -= 0.5
            nueva_y += config['player_speed']
    if keys[pygame.K_DOWN]:
        if config['cam_y'] < 10:
            config['cam_y'] += 0.5
            nueva_y -= config['player_speed']
    
    nueva_pos = [nueva_x, nueva_y, config['player_z']]
    
    obstaculos_dinamicos = obtener_obstaculos() # O obtener_obstaculos_nivel3()
    if hay_colision(nueva_pos, obstaculos_dinamicos) and config['personaje_id'] == 0:
        config['jesus_posicion'] = pygame.time.get_ticks() % 5  
    
    # Colisión con objetos dinámicos (power-ups)
    objetos_actuales = obtener_objetos_dinamicos()
    objetos_a_eliminar = []

    for i, obj in enumerate(objetos_actuales):
        if hay_colision(nueva_pos, [obj]): # hay_colision espera una lista de obstáculos
            if obj["tipo"] == "tiempo":
                estado_juego['tiempo_maximo'] += 10
                estado_juego['tiempo_restante'] +=10
                so.sonido("sonidos/TFR.mp3")
            elif obj["tipo"] == "error":
                if estado_juego['error_count'] > 0:
                    estado_juego['error_count'] -= 1
                so.sonido("sonidos/error.mp3")
            elif obj["tipo"] == "pista":
                if config['pistas_disponibles'] < 3: # Limite de pistas
                     config['pistas_disponibles'] += 1
                so.sonido("sonidos/pista.mp3")
            
            objetos_a_eliminar.append(i)
            # Cambiar pose de JesusL al recoger un objeto
            if config['personaje_id'] == 0:
                config['jesus_posicion'] = pygame.time.get_ticks() % 5 

    # Eliminar objetos recogidos (iterando en reversa para no afectar índices)
    for i in sorted(objetos_a_eliminar, reverse=True):
        objetos_actuales.pop(i)
    
    # Si no hay colisión, actualizar posición
    if not hay_colision(nueva_pos, obstaculos_dinamicos):
        config['player_x'], config['player_y'] = nueva_x, nueva_y
    else:
        # Si hay colisión con obstáculos fijos, el personaje no se mueve
        # y puede cambiar de pose si es JesusL (ya manejado arriba)
        pass
    
    # Lógica para generar nuevos objetos dinámicos si es necesario
    if not obtener_objetos_dinamicos(): # Si la lista está vacía
        generar_objetos_dinamicos() # Genera nuevos objetos