import random

def main():
    while True:
        print("--BIENVENIDO-- ")
        print("Elija una opción")
        print("1. -- Jugar Pyngo.")
        print("2. -- Autores de el programa.")
        print("3. -- Salir del programa.")
        option = -1
        while option not in ["1", "2", "3"]:
           option = input("Opcion: ")
        if option == '1':
            pyngo()
        elif option == '2':
            autores()
        elif option == '3':
            break

def pyngo():
    p_bola = int(input("Define el rango de números: "))
    carton_placeholder = []
    carton = []
    carton_puntos = []
    pool_bolas = [*range(1, p_bola+1)]
    removed_bolas = [[], []]
    while True:
        print("--BIENVENIDO A PYNGO--")
        print("   BINGO EN PYTHON")
        print("1. -- Sacar bola.")
        print("2. -- Crear cartón.")
        print("3. -- Mostrar cartón.")
        print("4. -- Mostrar números.")
        print("5. -- Salir a menu.")
        option = -1
        while option not in ["1", "2", "3", "4", "5"]:
            option = input("Opcion: ")
        if option == "1":
            if len(pool_bolas) != 0:
                bola = random.choice(pool_bolas)
                removed_bolas[0].append(bola)
                pool_bolas.remove(bola)
                print("\nEl numero es... ", bola, "\n")
                for item01 in carton_placeholder:
                    for item in carton:
                        if bola in item:
                            index = item.index(bola)
                            item.remove(bola)
                            item.insert(index, "X")
                    if item01.count('X') == len(item01):
                        del carton_placeholder[carton_placeholder.index(item01)]
                        if not carton_placeholder:
                            print("¡BYNGO!")
                        else:
                            print("¡LINEA!")
            else:
                print("No hay mas bolas")
                break
        elif option == '2':
            print("-- Tamaño del carton --")
            height_carton = input("Ancho: ")
            length_carton = input("Largo: ")
            for i in range(int(length_carton)):
                carton.append([])
                carton_puntos.append([])
                for j in range(int(height_carton)):
                    carton[i].append(random.randint(1, p_bola))
                    carton_puntos[i].append(random.randint(1, 100))
            carton_placeholder = carton.copy()
            for item in carton:
                print(item)

        elif option == '3':
            print("CARTÓN")
            for item in carton:
                print(item)
            print("CARTÓN DE PUNTOS")
            for item in carton_puntos:
                print(item)
            print("PUNTUACIÓN TOTAL")
            print(sum_points(carton_puntos))
        elif option == '4':
            print("-- Números ya aparecidos -- ")
            print(*removed_bolas)
        elif option == '5':
            break

def autores():
    print("-- Autores del programa --\n")
    print("\t-JOEL CORNELLA RUIZ")
    print("\t-NICOLAS BONDIA PILGREN\n\n")

def sum_points(carton_puntos):
    points = []
    for item in carton_puntos:
        points.append(sum(item))
    return sum(points)

main()
