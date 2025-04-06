import pygame

pygame.init()
pygame.mixer.init()

def sonido(FileName):
    audio_file = FileName
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()

def stopsonido():
    pygame.mixer.music.stop()
