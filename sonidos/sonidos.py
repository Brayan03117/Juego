import pygame
import os

pygame.init()
pygame.mixer.init()

def get_absolute_path(relative_path):
    # Obtiene la ruta absoluta a partir de una ruta relativa
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, relative_path)

def sonido(FileName):
    audio_file = FileName
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()

def reproducir_musica(FileName, loops=-1):
    """
    Reproduce música de fondo con opción de repetición
    loops: -1 para repetir indefinidamente, 0 para reproducir una vez
    """
    # Si la ruta es relativa, convertirla a absoluta
    if not os.path.isabs(FileName):
        audio_file = get_absolute_path(FileName)
    else:
        audio_file = FileName
    
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play(loops)

def stopsonido():
    pygame.mixer.music.stop()
