# objetosDinamicos.py

from OpenGL.GL import *
from src import objetos as obj
import random

# Lista global con objetos cayendo
lista_objetos_cayendo = []
velocidad_caida = 0.05 # velocidad con la que bajan los objetos

def generar_objetos_dinamicos():
    """Genera dos objetos con posiciones aleatorias cerca del techo"""
    global lista_objetos_cayendo
    lista_objetos_cayendo = []

    tipos = ["tiempo", "errores"]
    for tipo in tipos:
        x = random.uniform(-8, 8)
        y = random.uniform(7, 9)  # Altura inicial
        z = random.uniform(-8, 8)
        objeto = {
            "tipo": tipo,
            "pos": [x, y, z],  # mutable para que caiga
            "radio": 1.5
        }
        lista_objetos_cayendo.append(objeto)

def obtener_objetos_dinamicos():
    """Devuelve la lista de objetos actuales"""
    return lista_objetos_cayendo

def actualizar_objetos_dinamicos():
    """Hace que los objetos caigan y elimina los que tocan el suelo"""
    global lista_objetos_cayendo
    nueva_lista = []

    for objeto in lista_objetos_cayendo:
        objeto['pos'][1] -= velocidad_caida  # bajar eje Y
        if objeto['pos'][1] > -3:  # aún no ha tocado suelo
            nueva_lista.append(objeto)

    lista_objetos_cayendo = nueva_lista

    # Si desaparecieron, crear nuevos
    if len(lista_objetos_cayendo) < 2:
        generar_objetos_dinamicos()

def dibujar_objetos_dinamicos():
    """Dibuja los objetos con forma y color según el tipo"""
    for obj_data in lista_objetos_cayendo:
        x, y, z = obj_data["pos"]
        glPushMatrix()
        glTranslatef(x, y, z)

        if obj_data["tipo"] == "tiempo":
            glColor3f(0.0, 0.7, 1.0)
            obj.draw_cube((0, 0, 0))
        elif obj_data["tipo"] == "errores":
            glColor3f(1.0, 0.5, 0.0)
            obj.draw_pyramid((0, 0, 0))

        glPopMatrix()
