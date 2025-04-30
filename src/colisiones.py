from Esenarios.escenarioObjetos import obtener_obstaculos

def hay_colision(pos):
    px, py, pz = pos
    for obj in obtener_obstaculos():
        ox, oy, oz = obj["pos"]
        r = obj["radio"]
        if (ox - r <= px <= ox + r) and (oy - r <= py <= oy + r) and (oz - r <= pz <= oz + r):
            print("Colisión tipo AABB detectada")
            return True
    return False
