import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
import os
import random
from pygame.locals import DOUBLEBUF, OPENGL  # Añadir esta línea
from Esenarios import escenarioObjetos1 as es

def inicializar_nivel(personaje_id):
    """Inicializa todas las configuraciones del nivel"""
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
    
    # Reproducir la música inicial
    sonido_actual = 2  # Comenzamos con el segundo sonido
    sonidos_escenarios[sonido_actual].play(-1)  # Reproducir en bucle

    # Inicializar fondos
    es.inicializar_fondos()
    
    # Configuración inicial
    config = {
        'personaje_id': personaje_id,
        'display': display,
        'sonidos_escenarios': sonidos_escenarios,
        'sonido_actual': sonido_actual,
        'fondo_actual': 2,
        'jesus_posicion': 0,
        'torchic_posicion': 0,
        'dyson_emocion': "original",
        'dyson_posicion': 0,
        'luz_encendida': True,
        'cam_x': -4, 
        'cam_y': 0, 
        'cam_z': 15,
        'rot_x': 0, 
        'rot_y': 0,
        'player_x': 0.0, 
        'player_y': 0.0, 
        'player_z': 0.0,
        'player_speed': 0.5,
        'clock': pygame.time.Clock(),
        'font': pygame.font.SysFont('Arial', 30),
        'pista_activa': False,
        'pista': [{"tipo": "pista", "pos": (8, 0, 0.0), "radio": 2.5}],
        'pistas_disponibles': 1
    }
    
    # Configurar la perspectiva
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, -2.0, -30)  # Aleja la cámara para que el fondo se vea mejor

    # Habilitar prueba de profundidad e iluminación
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_COLOR_MATERIAL)
    
    return config

def cambiar_escenario_y_musica(config):
    """Cambia el escenario y la música de forma aleatoria"""
    # Detener la música actual
    config['sonidos_escenarios'][config['sonido_actual']].stop()
    
    # Cambiar a un nuevo escenario y música (diferentes al actual)
    nuevos_indices = list(range(1, 6))
    nuevos_indices.remove(config['fondo_actual'])  # Remover el escenario actual
    
    # Seleccionar un nuevo escenario aleatorio
    config['fondo_actual'] = random.choice(nuevos_indices)
    
    # Seleccionar una nueva música aleatoria
    config['sonido_actual'] = random.choice(list(config['sonidos_escenarios'].keys()))
    
    # Reproducir la nueva música
    config['sonidos_escenarios'][config['sonido_actual']].play(-1)  # Reproducir en bucle