import pygame
from OpenGL.GL import *
from src.colisiones import hay_colision
from Niveles.nivel2_config import cambiar_escenario_y_musica
from Transiciones.GameOver import mostrar_game_over # <--- AÑADIR ESTA LÍNEA
from Esenarios.escenarioObjetos2 import obtener_obstaculos
from src.objetosDinamicos import obtener_objetos_dinamicos, generar_objetos_dinamicos
from sonidos import sonidos as so
# Se eliminaron las importaciones de tkinter ya que no se usan ventanas emergentes

def manejar_eventos(config, estado_juego, tablero, solucion):
    """Maneja todos los eventos del nivel"""
    # Verificar si es la primera vez que se ejecuta esta función
    if not hasattr(manejar_eventos, "inicializado"):
        # Reiniciar posiciones de personajes
        config['torchic_posicion'] = 0
        config['dyson_posicion'] = 0
        config['dyson_emocion'] = "original"
        manejar_eventos.inicializado = True
        print("[INIT] Posiciones de personajes reiniciadas a 0")
    
    # Depuración: Imprimir posiciones actuales
    if config['personaje_id'] == 1:  # Torchic
        print(f"[DEBUG] Torchic posición actual: {config['torchic_posicion']}, Errores: {estado_juego['error_count']}")
    elif config['personaje_id'] == 2:  # Dyson
        print(f"[DEBUG] Dyson posición actual: {config['dyson_posicion']}, Errores: {estado_juego['error_count']}")

    # Actualizar el tiempo de visualización del mensaje de tecla no válida
    if estado_juego.get('mostrar_mensaje_tecla', False):
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - estado_juego.get('tiempo_mensaje_tecla', 0) > 2000:  # 2 segundos
            estado_juego['mostrar_mensaje_tecla'] = False
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Detener todos los sonidos antes de salir
            for sonido in config['sonidos_escenarios'].values():
                sonido.stop()
            pygame.quit()
            return "salir"
        
        # Control de teclado para salir (ESC) y mover la cámara
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                # Detener todos los sonidos antes de salir
                for sonido in config['sonidos_escenarios'].values():
                    sonido.stop()
                return "back"
            # Movimiento de cámara (desactivado)
            #elif event.key == pygame.K_w:
            #    if config['cam_z'] < 20:
            #        config['cam_z'] += 0.5
            #elif event.key == pygame.K_s:
            #    if config['cam_z'] > 10:
            #        config['cam_z'] -= 0.5
            #elif event.key == pygame.K_a:
            #    if config['cam_x'] < 20:
            #        config['cam_x'] += 0.5
            #elif event.key == pygame.K_d:
            #    if config['cam_x'] > -20:  
            #        config['cam_x'] -= 0.5
            #elif event.key == pygame.K_z:
            #    if config['cam_y'] < 10:
            #        config['cam_y'] += 0.5
            #elif event.key == pygame.K_x:
            #    if config['cam_y'] > -10: 
            #        config['cam_y'] -= 0.5
            # Control de iluminación (desactivado)
            #elif event.key == pygame.K_l:  # Tecla L para apagar la luz
            #    config['luz_encendida'] = False
            #    glDisable(GL_LIGHTING)
            #elif event.key == pygame.K_k:  # Tecla K para encender la luz
            #    config['luz_encendida'] = True
            #    glEnable(GL_LIGHTING)
            elif event.key == pygame.K_t:  # Tecla T para mostrar/ocultar texto
                config['mostrar_texto'] = not config.get('mostrar_texto', True)
            elif event.key == pygame.K_y:
                config['mostrar_tablero'] = not config.get('mostrar_tablero', True)
            
            # Manejo de entrada para el Sudoku
            elif event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4,pygame.K_5,pygame.K_6]:
                # Obtener el valor numérico de la tecla
                input_value = event.key - pygame.K_0
                # Si hay una celda seleccionada y está vacía en el tablero original
                if estado_juego['selected_cell'] is not None:
                    row, col = estado_juego['selected_cell']
                    # Verificar si la celda está vacía (0) en el tablero actual
                    if tablero[row][col] == 0:
                        # Verificar si el valor es correcto
                        if input_value == solucion[row][col]:
                            # Valor correcto
                            tablero[row][col] = input_value
                            # JesusL muestra pose feliz (0-4) cuando la respuesta es correcta
                            if config['personaje_id'] == 0:  # JesusL
                                config['jesus_posicion'] = estado_juego['correct_answers'] % 5  # Poses 0,1,2,3,4
                            # Guardar información sobre la última inserción
                            estado_juego['last_insertion'] = (row, col, input_value)
                            # Incrementar contador de respuestas correctas
                            estado_juego['correct_answers'] += 1
                            so.sonido("sonidos/feli.mp3")
                            # Cambiar escenario y música
                            cambiar_escenario_y_musica(config)
                            # Cambiar la emoción del personaje según el personaje seleccionado
                            #if config['personaje_id'] == 1:  # Torchic
                            #    config['torchic_posicion'] = 2  # Feliz
                            #elif config['personaje_id'] == 2:  # Dyson
                            #    config['dyson_emocion'] = "happy"
                        else:
                            # Valor incorrecto
                            estado_juego['error_count'] += 1
                            # JesusL cambia de posición cuando hay un error (poses 0-4)
                            if config['personaje_id'] == 0:  # JesusL
                                config['jesus_posicion'] = pygame.time.get_ticks() % 5  # Poses 0,1,2,3,4
                            # Guardar información sobre el intento fallido
                            estado_juego['last_insertion'] = (row, col, input_value)
                            # Cambiar la emoción del personaje según el personaje seleccionado
                            if config['personaje_id'] == 1:  # Torchic
                                # Solo cambiar posición si no ha alcanzado 4 errores
                                if estado_juego['error_count'] <= 3:  # Cambiado de < 4 a <= 3 para mayor claridad
                                    # Limitar la posición a un máximo de 4
                                    if config['torchic_posicion'] < 4:
                                        config['torchic_posicion'] += 1
                                        print(f"Torchic posición incrementada a: {config['torchic_posicion']}, Errores: {estado_juego['error_count']}")
                                    else:
                                        print(f"Torchic ya alcanzó la posición máxima: {config['torchic_posicion']}")
                                else:
                                    print(f"No se incrementa posición de Torchic. Posición actual: {config['torchic_posicion']}, Errores: {estado_juego['error_count']}")
                            elif config['personaje_id'] == 2:  # Dyson
                                config['dyson_emocion'] = "sad"  # Siempre cambia a triste
                                # Solo cambiar posición si no ha alcanzado 4 errores
                                if estado_juego['error_count'] <= 3:  # Cambiado de < 4 a <= 3 para mayor claridad
                                    # Limitar la posición a un máximo de 4
                                    if config['dyson_posicion'] < 4:
                                        config['dyson_posicion'] += 1
                                        print(f"Dyson posición incrementada a: {config['dyson_posicion']}, Errores: {estado_juego['error_count']}")
                                    else:
                                        print(f"Dyson ya alcanzó la posición máxima: {config['dyson_posicion']}")
                                else:
                                    print(f"No se incrementa posición de Dyson. Posición actual: {config['dyson_posicion']}, Errores: {estado_juego['error_count']}")

                            # Comprobar si se alcanzó el límite de errores
                            if estado_juego['error_count'] >= 5:
                                # Detener todos los sonidos del nivel antes de mostrar Game Over
                                for sonido_escenario in config['sonidos_escenarios'].values():
                                    sonido_escenario.stop()
                                decision_game_over = mostrar_game_over(config['display'])
                                if decision_game_over == 'menu':
                                    return "menu" # O la señal que uses para volver al menú
                                elif decision_game_over == 'salir':
                                    pygame.quit()
                                    return "salir"
            elif event.key in [pygame.K_7, pygame.K_8, pygame.K_9, pygame.K_0]:
                if estado_juego['selected_cell'] is not None:
                    row, col = estado_juego['selected_cell']
                    if tablero[row][col] == 0 and event.key not in [pygame.K_LEFT,pygame.K_RIGHT,pygame.K_UP,pygame.K_DOWN]: # Corregido K_RIGTH a K_RIGHT
                        # JesusL muestra pose (0-4) cuando se usa una tecla no válida
                        if config['personaje_id'] == 0:  # JesusL
                            config['jesus_posicion'] = pygame.time.get_ticks() % 5  # Poses 0,1,2,3,4 aleatorias
                        # Mostrar mensaje en pantalla
                        estado_juego['mostrar_mensaje_tecla'] = True
                        estado_juego['mensaje_tecla'] = "¡TECLA NO VÁLIDA!"
                        estado_juego['tiempo_mensaje_tecla'] = pygame.time.get_ticks()
                        # Solo mostrar mensaje en pantalla (sin ventana emergente)
            elif event.key in [pygame.K_LEFT, pygame.K_RIGHT ,pygame.K_UP , pygame.K_DOWN]:
                print("Movimiento con flechas")
            else:
                if estado_juego['selected_cell'] is not None:
                    row, col = estado_juego['selected_cell']
                    if tablero[row][col] == 0:
                        # JesusL muestra pose (0-4) cuando se usa una tecla no válida
                        if config['personaje_id'] == 0:  # JesusL
                            config['jesus_posicion'] = pygame.time.get_ticks() % 5  # Poses 0,1,2,3,4 aleatorias
                        # Mostrar mensaje en pantalla
                        estado_juego['mostrar_mensaje_tecla'] = True
                        estado_juego['mensaje_tecla'] = "¡TECLA NO VÁLIDA!"
                        estado_juego['tiempo_mensaje_tecla'] = pygame.time.get_ticks()
                        # Solo mostrar mensaje en pantalla (sin ventana emergente)
        # Manejo de clics del ratón para seleccionar celdas del Sudoku
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Clic izquierdo
                # Convertir coordenadas de pantalla a coordenadas de OpenGL
                x, y = event.pos
                y = config['display'][1] - y  # Invertir Y para OpenGL
                
                # Calcular posición del tablero
                cell_size = 50
                board_width = 6 * cell_size
                board_height = 6 * cell_size
                board_x = config['display'][0] - board_width - 20
                board_y = config['display'][1] - board_height -20
                
                # Verificar si el clic está dentro del tablero
                if (board_x <= x <= board_x + board_width and
                    board_y <= y <= board_y + board_height):
                    # Calcular la celda seleccionada
                    col = int((x - board_x) / cell_size)
                    row = 5 - int((y - board_y) / cell_size)  # Invertir filas
                    
                    # Actualizar celda seleccionada
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
    cam_x, cam_y, cam_z = config['cam_x'], config['cam_y'], config['cam_z']
    
    # Verificar colisiones y cambiar pose de JesusL si hay colisión
    obstaculos_dinamicos = obtener_obstaculos()
    if hay_colision(nueva_pos, obstaculos_dinamicos) and config['personaje_id'] == 0:
        # JesusL muestra pose feliz (0-4) cuando colisiona con un objeto
        config['jesus_posicion'] = pygame.time.get_ticks() % 5  # Poses 0,1,2,3,4
        
    # Ajusta esta posición para que coincida con donde *visualmente* está el tablero
    sudoku_virtual = {
        "tipo": "sudoku_virtual",
        "pos": (cam_x + (10.5), cam_y + (4.5), 0),
        "radio":4   # Puedes afinar el radio según el tamaño visible
    }

    obstaculos_dinamicos = obtener_obstaculos()

    if not hay_colision(nueva_pos, obstaculos_dinamicos):
        config['player_x'], config['player_y'] = nueva_x, nueva_y
        objetos = obtener_objetos_dinamicos()
        for obj_d in objetos:
            ox, oy, oz = obj_d["pos"]
            r = obj_d["radio"]
            if (ox - r <= nueva_x <= ox + r) and (oy - r <= nueva_y <= oy + r) and (oz - r <= config['player_z'] <= oz + r):
                if obj_d["tipo"] == "tiempo":
                    estado_juego['tiempo_maximo'] += 10
                    print("¡Colisión con objeto de TIEMPO! +10s")
                    if config['personaje_id'] == 0:  # JesusL
                        config['jesus_posicion'] = pygame.time.get_ticks() % 5  # Poses 0,1,2,3,4
                elif obj_d["tipo"] == "errores":
                    # Guardar el valor anterior de error_count
                    error_anterior = estado_juego['error_count']
                    estado_juego['error_count'] = max(0, estado_juego['error_count'] - 1)
                    print(f"¡Colisión con objeto de ERRORES! -1 error. Errores: {estado_juego['error_count']}")
                    
                    # Actualizar posición de personajes según el nuevo contador de errores
                    if config['personaje_id'] == 0:  # JesusL
                        config['jesus_posicion'] = pygame.time.get_ticks() % 5  # Poses 0,1,2,3,4
                    elif config['personaje_id'] == 1 and error_anterior > 4 and estado_juego['error_count'] <= 4:  # Torchic
                        # Si bajamos de 5 a 4 errores o menos, ajustar la posición
                        config['torchic_posicion'] = min(4, estado_juego['error_count'])
                        print(f"Ajustando posición de Torchic a: {config['torchic_posicion']}")
                    elif config['personaje_id'] == 2 and error_anterior > 4 and estado_juego['error_count'] <= 4:  # Dyson
                        # Si bajamos de 5 a 4 errores o menos, ajustar la posición
                        config['dyson_posicion'] = min(4, estado_juego['error_count'])
                        print(f"Ajustando posición de Dyson a: {config['dyson_posicion']}")
                    
        
        # Regenerar objetos para que se reubiquen
                generar_objetos_dinamicos()
                break
    if config['pista_activa']==False:
        if hay_colision(nueva_pos, config['pista']):
            config['pista_activa'] = True
            if config['personaje_id'] == 0:  # JesusL
                config['jesus_posicion'] = pygame.time.get_ticks() % 5  # Poses 0,1,2,3,4