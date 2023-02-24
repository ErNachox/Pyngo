"""
TODO GUIDELINES

Bingo con sistema de menús

PROGRAMA BÁSICO (6 PUNTOS DE 10)
Menú:
    ·Crear cartón
        Pedir numero de filas/columnas para tamaño cartón
        Asignar numero 1-99 a cada casilla
    ·Mostrar cartón
        Mostrar estado cartón e indicar si algún numero ha salido
        Anterior^ ha de ser mostrado en formato tabla legible
    ·Mostrar número
        Muestra lista con numeros que ya han salido. Formato legible usando \t
    ·Sacar bola
        Sacar bola al azar 1-99
        Actualizar cartones
        Informar cambios

EXTRA CONFIGURACIÓN (1 PUNTO)
    ·Rango numeros
        Opción inicial antes de primer Menú para elegir rango números en lugar del 1-99.
EXTRA MULTICARTÓN (2 PUNTOS)
    Menú:
        ·Varios cartones
            Varios cartones jugando a la vez
            Guardar lista con los cartones
            Cada cartón debe ser un diccionario
            Se ha de indicar en que cartón especificamente hay cambios
EXTRA PUNTUACIÓN (2 PUNTOS)
    Definir por casilla una puntuación aleatoria
    En cada línea/bingo mostrar también la puntuación correspondiente a las casillas
    En MOSTRAR CARTÓN se debe mostrar puntuación por casilla tambien
    En MOSTRAR CARTÓN se debe mostrar puntuación total cartón tambien

    IDEAS:
        Que haga clear después de cada opción/cambio de menú
"""
import random

num = list(range(1, 99))
"""
-- random num coger --
newnum = (random.choice(num))
            carton.append(newnum)
            print(carton)
            print(newnum)
"""
#Funcion principal en bucle
def main():
    while True:
        carton = list()
        print("--BIENVENIDO-- ")
        print("Elija una opción")
        print("1. -- Jugar Pyngo.")
        print("2. -- Autores de el programa.")
        print("3. -- Salir del programa.")
        option = -1
        while option not in ["1", "2", "3"]:
           option = input(print("Opcion: "))
        if option == '1':
            pyngo()
        elif option == '2':
            autores()
        elif option == '3':
            break

#Juego uwu
def pyngo():
    while True:
        #lista de cartones
        list_carton = [
            []
        ]
        print("--BIENVENIDO A PYNGO--")
        print("   BINGO EN PYTHON")
        print("1. -- Sacar bola")
        print("2. -- Crear cartón.")
        print("3. -- Mostar número")
        print("4. -- Salir a menu")
        option = -1
        while option not in ["1", "2", "3", "4"]:
            option = input("Opcion: ")
        if option == "1":
            bola = (random.choice(num))
            print("El numero es... ", bola)
        elif option == '2':
            print("-- Tamaño del carton --")
            height_carton = input("Ancho: ")
            length_carton = input("Largo: ")
            temp_carton = 1
        elif option == '3':
            print("")
        elif option == '4':
            break



#Funcion enseñar autores del programa
def autores():
    print("-- Autores del programa --\n")
    print("\t-JOEL CORNELLA RUIZ")
    print("\t-NICOLAS BONDIA PILGREN\n\n")


main()

