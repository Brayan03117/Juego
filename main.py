from src.pantalla1 import pantalla_inicial
from seleccion import main as seleccion_personaje

def main():
    while True:
        opcion = pantalla_inicial()
        if opcion == "iniciar":
            print("Aquí puedes poner la lógica del juego principal.")
            break  # Aquí iría la pantalla principal del juego
        elif opcion == "seleccionar_personaje":
            personaje_id = seleccion_personaje()
            print(f"Seleccionaste el personaje {personaje_id}")
        elif opcion == "salir":
            break

if __name__ == "__main__":
    main()