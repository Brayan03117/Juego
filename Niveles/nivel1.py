import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from pygame.locals import *
import sys
import random

# Importar funciones para dibujar escenarios
from Esenarios import escenarioObjetos as es

# Importar personajes
from acciones.jesusL import draw as draw_jesus
from acciones.torchic import personaje as draw_torchic
from acciones.dysonEm import dibujar_personaje as draw_dyson
from acciones.expresiones import draw_cejas_chad,draw_feliz,draw_triste,draw_enojado,draw_nervioso

# Importar otras utilidades
from acciones.iluminacion import iluminacion
from src.textos import dibujar_label_texto
from src.colisiones import hay_colision

# Importar módulo para sonidos
import os

def iniciar_nivel1(personaje_id):
    """
    Inicia el Nivel 1 con el personaje seleccionado.
    
    Args:
        personaje_id: ID del personaje seleccionado (0=JesusL, 1=Torchic, 2=Dyson)
    """
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Sudoku - Nivel 1")
    
    # Inicializar el módulo de sonido
    pygame.mixer.init()
    
    # Cargar los sonidos para cada escenario
    sonidos_escenarios = {
        1: pygame.mixer.Sound(os.path.join("Sonidos", "BackOnTrack.mp3")),
        2: pygame.mixer.Sound(os.path.join("Sonidos", "Cycles.mp3")),
        3: pygame.mixer.Sound(os.path.join("Sonidos", "Electroman.mp3")),
        4: pygame.mixer.Sound(os.path.join("Sonidos", "GeometricalDominator.mp3")),
        5: pygame.mixer.Sound(os.path.join("Sonidos", "Jumper.mp3"))
    }

    # Inicializar fondos
    es.inicializar_fondos()
    # Puedes cambiar el índice del fondo si quieres otro diferente
    fondo_actual = 2
    
    # Variable para controlar la posición de JesusL
    jesus_posicion = 0

    torchic_posicion = 0

    dyson_emocion="original"
    
    # Variable para controlar la iluminación
    luz_encendida = True

    # Configurar la perspectiva
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, -2.0, -30) # Aleja la cámara para que el fondo se vea mejor

    # Habilitar prueba de profundidad e iluminación
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_COLOR_MATERIAL)
    
    # Variables para controlar la cámara
    cam_x, cam_y, cam_z = -4, 0, 15  # Iniciar con la cámara más cerca
    rot_x, rot_y = 0, 0

    # Variables para la posición y velocidad del jugador
    player_x, player_y, player_z = 0.0, 0.0, 0.0
    player_speed = 0.1 # Ajusta la velocidad según sea necesario

    # Crear tablero de Sudoku 2x2 (4x4)
    # Tablero inicial con algunas casillas llenas
    sudoku_board = [
        [4, 0, 2, 0],
        [2, 0, 0, 0],
        [0, 2, 0, 0],
        [0, 0, 3, 0]
    ]
    
    # Solución del Sudoku 2x2 (4x4)
    sudoku_solution = [
        [4, 3, 2, 1],
        [2, 1, 4, 3],
        [3, 2, 1, 4],
        [1, 4, 3, 2]
    ]
    
    # Variables para el juego de Sudoku
    selected_cell = None
    input_value = 0
    error_count = 0
    showing_options = False
    cell_options = []
    options_cell_coords = None
    last_insertion = None  # Para almacenar la última inserción (fila, columna, valor)

    # Fuente para el Sudoku
    pygame.font.init()
    font = pygame.font.SysFont('Arial', 30)
    
    # Crear un reloj para controlar el framerate
    clock = pygame.time.Clock()
    
    # Bucle principal del juego
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            # Control de teclado para salir (ESC) y mover la cámara (opcional)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return
                # Movimiento de cámara (si aún lo quieres)
                elif event.key == pygame.K_w:
                    cam_z += 0.5
                elif event.key == pygame.K_s:
                    cam_z -= 0.5
                elif event.key == pygame.K_a:
                    cam_x += 0.5
                elif event.key == pygame.K_d:
                    cam_x -= 0.5
                elif event.key == pygame.K_z:
                    cam_y += 0.5
                elif event.key == pygame.K_x:
                    cam_y -= 0.5
                # Control de iluminación
                elif event.key == pygame.K_l:  # Tecla L para apagar la luz
                    luz_encendida = False
                    glDisable(GL_LIGHTING)
                elif event.key == pygame.K_k:  # Tecla K para encender la luz
                    luz_encendida = True
                    glEnable(GL_LIGHTING)
                
                # Manejo de entrada para el Sudoku
                elif event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]:
                    # Obtener el valor numérico de la tecla
                    input_value = event.key - pygame.K_0
                    
                    # Si hay una celda seleccionada y está vacía en el tablero original
                    if selected_cell:
                        row, col = selected_cell
                        # Verificar si la celda está vacía (0) en el tablero actual
                        if sudoku_board[row][col] == 0:
                            # Verificar si el valor es correcto
                            if input_value == sudoku_solution[row][col]:
                                # Valor correcto
                                sudoku_board[row][col] = input_value
                                # JesusL mantiene su posición original
                                jesus_posicion = 0
                                # Guardar información sobre la última inserción
                                last_insertion = (row, col, input_value)
                            else:
                                # Valor incorrecto
                                error_count += 1
                                # JesusL cambia de posición cuando hay un error
                                jesus_posicion = error_count % 5 + 1
                                # Guardar información sobre el intento fallido
                                last_insertion = (row, col, input_value)
                        else:
                            # Celda ya ocupada
                            last_insertion = None
                    else:
                        # No hay celda seleccionada
                        last_insertion = None
                
                # Selección de celda con las flechas
                elif event.key == pygame.K_UP and selected_cell and selected_cell[0] > 0:
                    selected_cell = (selected_cell[0] - 1, selected_cell[1])
                    print(f"Seleccionada celda: Fila {selected_cell[0]+1}, Columna {selected_cell[1]+1}")
                elif event.key == pygame.K_DOWN and selected_cell and selected_cell[0] < 3:
                    selected_cell = (selected_cell[0] + 1, selected_cell[1])
                    print(f"Seleccionada celda: Fila {selected_cell[0]+1}, Columna {selected_cell[1]+1}")
                elif event.key == pygame.K_LEFT and selected_cell and selected_cell[1] > 0:
                    selected_cell = (selected_cell[0], selected_cell[1] - 1)
                    print(f"Seleccionada celda: Fila {selected_cell[0]+1}, Columna {selected_cell[1]+1}")
                elif event.key == pygame.K_RIGHT and selected_cell and selected_cell[1] < 3:
                    selected_cell = (selected_cell[0], selected_cell[1] + 1)
                    print(f"Seleccionada celda: Fila {selected_cell[0]+1}, Columna {selected_cell[1]+1}")
                
                # Inicializar la selección de celda si no hay ninguna seleccionada
                elif event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT] and not selected_cell:
                    selected_cell = (0, 0)
                    print(f"Inicializada selección en: Fila 1, Columna 1")
                    
                # Sistema de opciones múltiples (3 opciones)
                elif event.key == pygame.K_SPACE and selected_cell:
                    row, col = selected_cell
                    # Solo mostrar opciones si la celda está vacía en el tablero original
                    if sudoku_board[row][col] == 0:
                        # Generar 3 opciones (una correcta y dos incorrectas)
                        correct_option = sudoku_solution[row][col]
                        
                        # Generar opciones incorrectas (diferentes a la correcta)
                        incorrect_options = []
                        while len(incorrect_options) < 2:
                            option = random.randint(1, 4)  # Cambiado a 4 para un tablero 4x4
                            if option != correct_option and option not in incorrect_options:
                                incorrect_options.append(option)
                        
                        # Mezclar las opciones
                        options = [correct_option] + incorrect_options
                        random.shuffle(options)
                        
                        # Guardar las opciones y las coordenadas de la celda
                        cell_options = options
                        showing_options = True
                        options_cell_coords = (row, col)
                        selected_option = None
                        
                # Seleccionar una opción (1, 2 o 3)
                elif event.key in [pygame.K_1, pygame.K_2, pygame.K_3] and showing_options and options_cell_coords:
                    option_index = event.key - pygame.K_1  # 0 para tecla 1, 1 para tecla 2, 2 para tecla 3

                    # Asegurarse de que el índice esté dentro del rango
                    if option_index < len(cell_options):
                        selected_option = cell_options[option_index]

                        # Obtener las coordenadas de la celda donde se pidieron las opciones
                        row, col = options_cell_coords

                        # Verificar si la opción seleccionada es correcta
                        if selected_option == sudoku_solution[row][col]:
                            # Opción correcta - actualizar ESTA celda específica
                            sudoku_board[row][col] = selected_option
                            # JesusL mantiene su posición original
                            jesus_posicion = 0
                        else:
                            # Opción incorrecta
                            error_count += 1
                            # JesusL cambia de posición cuando hay un error
                            jesus_posicion = error_count % 5 + 1

                        # Ocultar las opciones y resetear estado después de seleccionar
                        showing_options = False
                        options_cell_coords = None
                        cell_options = []
        
        # Limpiar la pantalla
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        # Aplicar iluminación solo si está encendida
        if luz_encendida:
            iluminacion(1.0, 1.0, 1.0)  # Luz blanca
        
        # Aplicar transformaciones de cámara (si las usas)
        glPushMatrix()
        glTranslatef(cam_x, cam_y, cam_z) # Mueve la cámara

        # Mostrar el fondo del escenario
        es.mostrar_escenario(fondo_actual)

        # Dibujar el personaje seleccionado en su posición
        glPushMatrix()
        # Aplicar la posición del jugador ANTES de las rotaciones específicas del modelo
        glTranslatef(player_x, player_y, player_z)

        if personaje_id == 0:  # JesusL
            # Rotaciones específicas para este modelo
            glRotatef(90, 1, 0, 0)
            glRotatef(180, 0, 1, 0)
            glRotatef(90, 0, 0, 1)
            draw_jesus(0, -3, -2.2, jesus_posicion) # Usar la posición seleccionada
        elif personaje_id == 1:  # Torchic
            glRotatef(180, 0, 1, 0)
            if torchic_posicion == 0:
                draw_torchic()
            elif torchic_posicion == 1:
                draw_triste()
            elif torchic_posicion == 2:
                draw_feliz()
            elif torchic_posicion == 3:
                draw_enojado()
            elif torchic_posicion == 5:
                draw_cejas_chad()
            draw_torchic() # Dibujar en el origen local
        elif personaje_id == 2:  # Dyson
            # Rotaciones/Traslaciones específicas para este modelo
            draw_dyson((0, 2, 8),emocion=dyson_emocion) # Ajusta la posición relativa si es necesario
       
        glPopMatrix() # Fin del bloque del personaje

        glPopMatrix() # Fin del bloque de la cámara

        # Renderizar el tablero de Sudoku en 2D
        # Cambiar a modo 2D para dibujar el tablero
        glMatrixMode(GL_PROJECTION)
        glPushMatrix()
        glLoadIdentity()
        gluOrtho2D(0, display[0], 0, display[1])
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glLoadIdentity()
        glDisable(GL_DEPTH_TEST)
        
        # Dibujar el tablero de Sudoku
        cell_size = 60  # Aumentado para mejor visibilidad
        board_width = 4 * cell_size  # 4 columnas
        board_height = 4 * cell_size  # 4 filas
        board_x = (display[0] - board_width) // 2
        board_y = (display[1] - board_height) // 2
        
        # Dibujar el fondo del tablero
        glColor3f(1.0, 1.0, 1.0)  # Color blanco
        glBegin(GL_QUADS)
        glVertex2f(board_x, board_y)
        glVertex2f(board_x + board_width, board_y)
        glVertex2f(board_x + board_width, board_y + board_height)
        glVertex2f(board_x, board_y + board_height)
        glEnd()
        
        # Dibujar las líneas del tablero
        glColor3f(0.0, 0.0, 0.0)  # Color negro
        glLineWidth(2.0)
        glBegin(GL_LINES)
        # Líneas horizontales
        for i in range(5):  # 5 líneas para 4 filas
            y = board_y + i * cell_size
            glVertex2f(board_x, y)
            glVertex2f(board_x + board_width, y)
        # Líneas verticales
        for i in range(5):  # 5 líneas para 4 columnas
            x = board_x + i * cell_size
            glVertex2f(x, board_y)
            glVertex2f(x, board_y + board_height)
        glEnd()
        
        # Dibujar líneas más gruesas para separar los bloques 2x2
        glLineWidth(4.0)
        glBegin(GL_LINES)
        # Línea horizontal central
        y = board_y + 2 * cell_size
        glVertex2f(board_x, y)
        glVertex2f(board_x + board_width, y)
        # Línea vertical central
        x = board_x + 2 * cell_size
        glVertex2f(x, board_y)
        glVertex2f(x, board_y + board_height)
        glEnd()
        
        # Dibujar los números del tablero
        for row in range(4):  # 4 filas
            for col in range(4):  # 4 columnas
                if sudoku_board[row][col] != 0:
                    # Renderizar el número
                    num_surface = font.render(str(sudoku_board[row][col]), True, (0, 0, 0))
                    num_texture = pygame.image.tostring(num_surface, 'RGBA', True)
                    
                    # Crear textura OpenGL
                    texture_id = glGenTextures(1)
                    glBindTexture(GL_TEXTURE_2D, texture_id)
                    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
                    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
                    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, num_surface.get_width(), num_surface.get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, num_texture)
                    
                    # Dibujar la textura
                    # Dibujar la textura
                    glEnable(GL_TEXTURE_2D)
                    glEnable(GL_BLEND)
                    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
                    
                    # Corregir la posición de dibujo para que coincida con la matriz interna
                    # La fila 0 debe ser la superior, no la inferior
                    x = board_x + col * cell_size + cell_size // 2 - num_surface.get_width() // 2
                    y = board_y + (3 - row) * cell_size + cell_size // 2 - num_surface.get_height() // 2
                    
                    glBegin(GL_QUADS)
                    glTexCoord2f(0, 0); glVertex2f(x, y)
                    glTexCoord2f(1, 0); glVertex2f(x + num_surface.get_width(), y)
                    glTexCoord2f(1, 1); glVertex2f(x + num_surface.get_width(), y + num_surface.get_height())
                    glTexCoord2f(0, 1); glVertex2f(x, y + num_surface.get_height())
                    glEnd()
                    
                    glDisable(GL_TEXTURE_2D)
                    glDisable(GL_BLEND)
                    
                    # Liberar la textura
                    glDeleteTextures(1, [texture_id])
        
        # Resaltar la celda seleccionada
        if selected_cell:
            row, col = selected_cell
            # Corregir la posición de la selección
            x = board_x + col * cell_size
            y = board_y + (3 - row) * cell_size
            
            glColor3f(1.0, 0.0, 0.0)  # Color rojo para la selección
            glLineWidth(3.0)
            glBegin(GL_LINE_LOOP)
            glVertex2f(x, y)
            glVertex2f(x + cell_size, y)
            glVertex2f(x + cell_size, y + cell_size)
            glVertex2f(x, y + cell_size)
            glEnd()

        # Volver al modo 3D
        glEnable(GL_DEPTH_TEST)
        glMatrixMode(GL_PROJECTION)
        glPopMatrix()
        glMatrixMode(GL_MODELVIEW)
        glPopMatrix()

        # Mostrar información del juego
        dibujar_label_texto(f"Sudoku 2x2 - Nivel 1", pos_x=10, pos_y=580, tam=24)
        dibujar_label_texto(f"Usa las flechas para seleccionar una celda", pos_x=10, pos_y=550, tam=18)
        dibujar_label_texto(f"Presiona ESPACIO para ver opciones", pos_x=10, pos_y=520, tam=18)
        dibujar_label_texto(f"Selecciona 1, 2 o 3 para elegir una opción", pos_x=10, pos_y=490, tam=18)
        dibujar_label_texto(f"Presiona ESC para salir", pos_x=10, pos_y=460, tam=18)
        dibujar_label_texto(f"Errores: {error_count}", pos_x=10, pos_y=430, tam=18)
        dibujar_label_texto(f"Luz: {'Encendida' if luz_encendida else 'Apagada'}", pos_x=10, pos_y=400, tam=18)
        
        # Mostrar la casilla seleccionada actualmente
        if selected_cell:
            row, col = selected_cell
            # Mostrar directamente la fila y columna +1 para que sean del 1 al 4
            visual_row = row + 1
            visual_col = col + 1
            dibujar_label_texto(f"Casilla seleccionada: Fila {visual_row}, Columna {visual_col}", pos_x=10, pos_y=370, tam=18)
        
        # Mostrar información sobre la última inserción
        if last_insertion:
            row, col, value = last_insertion
            visual_row = row + 1
            visual_col = col + 1
            if value == sudoku_solution[row][col]:
                dibujar_label_texto(f"¡Correcto! Insertado {value} en Fila {visual_row}, Columna {visual_col}", pos_x=10, pos_y=340, tam=18)
            else:
                dibujar_label_texto(f"¡Incorrecto! Intentaste insertar {value} en Fila {visual_row}, Columna {visual_col}", pos_x=10, pos_y=340, tam=18)

        # Mostrar las opciones si están activas
        if showing_options and selected_cell:
            option_y = 350
            for i, option in enumerate(cell_options):
                dibujar_label_texto(f"Opción {i+1}: {option}", pos_x=10, pos_y=option_y, tam=18)
                option_y -= 30
                
        pygame.display.flip()
        clock.tick(60)  # Mantener 60 FPS