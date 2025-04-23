from acciones.dyson import set_naranja, set_verde, set_amarillo, set_negro, set_robot_purple, set_gray, set_azul, set_azul_grisaceo, set_purple, set_rojo
#from acciones.dyson import animar_brazos_rechazo, animar_brazos_alegria
from acciones.dyson import dibujar_cuerpo, dibujar_cabeza, dibujar_brazo_izquierdo, dibujar_brazo_derecho, dibujar_pierna_izquierda, dibujar_pierna_derecha

from acciones.dyson import *

colores_emocion = {
    "original": {
        "cuerpo": set_naranja,
        "brazo_izquierdo": set_verde,
        "brazo_derecho": set_verde,
        "pierna_izquierda": set_verde,
        "pierna_derecha": set_verde,
        "cabeza": set_amarillo,
        "ojos": set_negro,
        "casco": set_robot_purple,
        "pico": set_verde
    },
    "happy": {
        "cuerpo": set_robot_purple,
        "brazo_izquierdo": set_robot_purple,
        "brazo_derecho": set_robot_purple,
        "pierna_izquierda": set_blue,
        "pierna_derecha": set_blue,
        "cabeza": set_blue_light,
        "ojos": set_purple,
        "casco": set_rojo,
        "pico": set_amarillo
    },
    "sad": {
        "cuerpo": set_gray,
        "brazo_izquierdo": set_blue,
        "brazo_derecho": set_blue,
        "pierna_izquierda": set_blue,
        "pierna_derecha": set_blue,
        "cabeza": set_blue_light,
        "ojos": set_purple,
        "casco": set_rojo,
        "pico": set_amarillo
    },
    "gesto": {
        "cuerpo": set_gray,
        "brazo_izquierdo": set_naranja,
        "brazo_derecho": set_naranja,
        "pierna_izquierda": set_naranja,
        "pierna_derecha": set_naranja,
        "cabeza": set_amarillo,
        "ojos": set_negro,
        "casco": set_naranja,
        "pico": set_marron_opaco
    },
    "asco": {
        "cuerpo": set_verde,
        "brazo_izquierdo": set_amarillo,
        "brazo_derecho": set_amarillo,
        "pierna_izquierda": set_naranja,
        "pierna_derecha": set_naranja,
        "cabeza": set_verde,
        "ojos": set_black,
        "casco": set_naranja,
        "pico": set_amarillo
    },
    "duda": {
        "cuerpo": set_purpura,
        "brazo_izquierdo": set_azul_grisaceo,
        "brazo_derecho": set_azul_grisaceo,
        "pierna_izquierda": set_naranja,
        "pierna_derecha": set_naranja,
        "cabeza": set_blue_light,
        "ojos": set_negro,
        "casco": set_negro,
        "pico": set_amarillo
    },
    "enojar": {
        "cuerpo": set_rojo,
        "brazo_izquierdo": set_rojo,
        "brazo_derecho": set_rojo,
        "pierna_izquierda": set_rojo,
        "pierna_derecha": set_rojo,
        "cabeza": set_rojo,
        "ojos": set_negro,
        "casco": set_negro,
        "pico": set_naranja
    },
    "admirar": {
        "cuerpo": set_purpura,
        "brazo_izquierdo": set_naranja,
        "brazo_derecho": set_naranja,
        "pierna_izquierda": set_naranja,
        "pierna_derecha": set_naranja,
        "cabeza": set_amarillo,
        "ojos": set_naranja,
        "casco": set_naranja,
        "pico": set_amarillo
    }
}

def color_por_parte(parte, paleta):
    correspondencias = {
        "cuerpo": "cuerpo",
        "brazo_izquierdo": "brazo_izquierdo",
        "brazo_derecho": "brazo_derecho",
        "pierna_izquierda": "pierna_izquierda",
        "pierna_derecha": "pierna_derecha",
        "cabeza": "cabeza",
        "ojos": "ojos",
        "casco": "casco",
        "pico": "pico"
    }
    clave = correspondencias.get(parte, "cuerpo")
    return paleta.get(clave, set_azul)

acciones_emocion = {
    "asco": {
        "brazo_derecho": animar_brazo_asco,
        "cabeza": animar_cabeza_asco
    }
}


def dibujar_personaje(position, emocion):
    paleta = colores_emocion[emocion]
    
    partes_animadas = set()
    if emocion in acciones_emocion:
        partes_animadas = set(acciones_emocion[emocion].keys())
        for parte, funcion in acciones_emocion[emocion].items():
            if parte == "cabeza":
                funcion(
                    position,
                    paleta["cabeza"],
                    paleta["ojos"],
                    paleta["casco"],
                    paleta["pico"]
                )
            else:
                color = color_por_parte(parte, paleta)
                funcion(position, color)


    # Dibujo de partes estáticas si no están animadas
    if "cuerpo" not in partes_animadas:
        dibujar_cuerpo(position, paleta["cuerpo"])

    if "brazo_izquierdo" not in partes_animadas:
        dibujar_brazo_izquierdo(position, paleta["brazo_izquierdo"])
    if "brazo_derecho" not in partes_animadas:
        dibujar_brazo_derecho(position, paleta["brazo_derecho"])

    if "pierna_izquierda" not in partes_animadas:
        dibujar_pierna_izquierda(position, paleta["pierna_izquierda"])
    if "pierna_derecha" not in partes_animadas:
        dibujar_pierna_derecha(position, paleta["pierna_derecha"])

    if "cabeza" not in partes_animadas:
        dibujar_cabeza(position, paleta["cabeza"], paleta["ojos"], paleta["casco"], paleta["pico"])



