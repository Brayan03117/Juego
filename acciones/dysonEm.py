from acciones.dyson import set_naranja, set_verde, set_amarillo, set_negro, set_robot_purple, set_gray, set_azul, set_azul_grisaceo, set_purple, set_rojo
#from acciones.dyson import animar_brazos_rechazo, animar_brazos_alegria
from acciones.dyson import dibujar_cuerpo, dibujar_brazos, dibujar_piernas, dibujar_cabeza

from dyson import *

colores_emocion = {
    "original": {
        "cuerpo": set_naranja,
        "brazos": set_verde,
        "piernas": set_verde,
        "cabeza": set_amarillo,
        "ojos": set_negro,
        "casco": set_robot_purple,
        "pico": set_verde
    },
    "happy": {
        "cuerpo": set_robot_purple,
        "brazos": set_robot_purple,
        "piernas": set_blue,
        "cabeza": set_blue_light,
        "ojos": set_purple,
        "casco": set_rojo,
        "pico": set_amarillo
    },
    "sad": {
        "cuerpo": set_gray,
        "brazos": set_blue,
        "piernas": set_blue,
        "cabeza": set_blue_light,
        "ojos": set_purple,
        "casco": set_rojo,
        "pico": set_amarillo
    },
    "gesto": {
        "cuerpo": set_gray,
        "brazos": set_naranja,
        "piernas": set_naranja,
        "cabeza": set_amarillo,
        "ojos": set_negro,
        "casco": set_naranja,
        "pico": set_marron_opaco
    },
    "asco": {
        "cuerpo": set_naranja,
        "brazos": set_amarillo,
        "piernas": set_naranja,
        "cabeza": set_verde,
        "ojos": set_naranja,
        "casco": set_naranja,
        "pico": set_negro
    },
    "duda": {
        "cuerpo": set_purpura,
        "brazos": set_azul_grisaceo,
        "piernas": set_naranja,
        "cabeza": set_blue_light,
        "ojos": set_negro,
        "casco": set_negro,
        "pico": set_amarillo
    },
    "enojar": {
        "cuerpo": set_rojo,
        "brazos": set_rojo,
        "piernas": set_rojo,
        "cabeza": set_rojo,
        "ojos": set_negro,
        "casco": set_negro,
        "pico": set_naranja
    },
    "admirar": {
        "cuerpo": set_purpura,
        "brazos": set_naranja,
        "piernas": set_naranja,
        "cabeza": set_amarillo,
        "ojos": set_naranja,
        "casco": set_naranja,
        "pico": set_amarillo
    }
}


colores_emocion = {

    "sad": {
        "cuerpo": set_gray,
        "brazos": set_azul,
        "piernas": set_azul,
        "cabeza": set_azul_grisaceo,
        "ojos": set_purple,
        "casco": set_rojo,
        "pico": set_amarillo
    }
    
}


"""animaciones_por_emocion = {
    "asco": animar_brazos_rechazo,
    "happy": animar_brazos_alegria,
    "duda": None,
}
"""

def dibujar_personaje(position, emocion):
    paleta = colores_emocion[emocion]
    dibujar_cuerpo(position, paleta["cuerpo"])
    dibujar_brazos(position, paleta["brazos"])
    dibujar_piernas(position, paleta["piernas"])
    dibujar_cabeza(position, paleta["cabeza"], paleta["ojos"], paleta["casco"], paleta["pico"])

""" if emocion in animaciones_por_emocion and animaciones_por_emocion[emocion]:
    animaciones_por_emocion[emocion](position)"""
