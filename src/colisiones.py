from Esenarios.escenarioObjetos import obtener_obstaculos

def hay_colision(pos, obstaculos=None):
    px, py, pz = pos
    lista = obstaculos if obstaculos else obtener_obstaculos()
    for obj in lista:
        ox, oy, oz = obj["pos"]
        r = obj["radio"]
        if (ox - r <= px <= ox + r) and (oy - r <= py <= oy + r) and (oz - r <= pz <= oz + r):
            print("Colisión tipo AABB detectada")
            return True
    return False
