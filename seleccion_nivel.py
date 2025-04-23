import pygame
import sys
from pygame.locals import *

def seleccion_nivel(personaje_id):
    """
    Muestra una pantalla para seleccionar el nivel del juego usando flechas.
    
    Args:
        personaje_id: El ID del personaje seleccionado
        
    Returns:
        str: El nivel seleccionado ("nivel1", "nivel2", "nivel3")
    """
    # Inicializar pygame
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("Sonidos/Cycles.mp3")
    pygame.mixer.music.play(-1)
    
    # Configuración de la pantalla
    ancho, alto = 800, 600
    pantalla = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("Selección de Nivel")
    
    # Colores
    NEGRO = (0, 0, 0)
    BLANCO = (255, 255, 255)
    AMARILLO = (255, 255, 0)
    
    # Fuentes
    fuente_titulo = pygame.font.Font(None, 60)
    fuente_opciones = pygame.font.Font(None, 40)
    
    # Opciones de nivel
    opciones = ["Nivel 1", "Nivel 2", "Nivel 3"]
    coordenadas_opciones = [(ancho // 2, 250), (ancho // 2, 300), (ancho // 2, 350)]
    seleccion_actual = 0
    
    # Reloj para controlar la velocidad de fotogramas
    reloj = pygame.time.Clock()
    
    # Bucle principal
    while True:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            
            if evento.type == KEYDOWN:
                if evento.key == K_UP:
                    seleccion_actual = (seleccion_actual - 1) % len(opciones)
                elif evento.key == K_DOWN:
                    seleccion_actual = (seleccion_actual + 1) % len(opciones)
                elif evento.key == K_RETURN:
                    pygame.quit()
                    return f"nivel{seleccion_actual + 1}"
        
        # Dibujar fondo
        pantalla.fill(NEGRO)
        
        # Dibujar título
        texto_titulo = fuente_titulo.render("Seleccione su nivel", True, BLANCO)
        pantalla.blit(texto_titulo, (ancho // 2 - texto_titulo.get_width() // 2, 100))
        
        # Dibujar información del personaje
        texto_personaje = fuente_opciones.render(f"Personaje seleccionado: {personaje_id}", True, BLANCO)
        pantalla.blit(texto_personaje, (ancho // 2 - texto_personaje.get_width() // 2, 170))
        
        # Dibujar opciones
        for i, opcion in enumerate(opciones):
            color = AMARILLO if i == seleccion_actual else BLANCO
            texto_opcion = fuente_opciones.render(opcion, True, color)
            x, y = coordenadas_opciones[i]
            
            # Dibujar flecha si es la opción seleccionada
            if i == seleccion_actual:
                flecha = "> "
            else:
                flecha = "  "
                
            texto_flecha = fuente_opciones.render(flecha, True, color)
            
            # Centrar texto horizontalmente
            ancho_total = texto_flecha.get_width() + texto_opcion.get_width()
            x_flecha = x - ancho_total // 2
            x_opcion = x_flecha + texto_flecha.get_width()
            
            pantalla.blit(texto_flecha, (x_flecha, y))
            pantalla.blit(texto_opcion, (x_opcion, y))
        
        # Instrucciones
        instrucciones = fuente_opciones.render("Use las flechas ↑↓ para navegar y Enter para seleccionar", True, BLANCO)
        pantalla.blit(instrucciones, (ancho // 2 - instrucciones.get_width() // 2, 450))
        
        # Actualizar pantalla
        pygame.display.flip()
        
        # Controlar velocidad
        reloj.tick(30)