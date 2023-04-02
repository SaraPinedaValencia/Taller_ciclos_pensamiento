import random

from typing import List


def main():
    nombre: str = input("Ingrese su nombre para participar: ")
    acum: int = 0
    cont: int = 0
    multiplos: List[int] = []

    while nombre == "" or any(map(str.isdigit, nombre)):
        nombre = input("Nombre no válido; ingrese su nombre para participar: ")

    while nombre != "":

        while any(map(str.isdigit, nombre)):
            nombre = input("Nombre no válido; ingrese su nombre para participar: ")
            print()

        numero = random.randint(0, 25)
        cont += 1
        acum += numero

        print(f"El estudiante {nombre} imprimió el valor de: {numero}")
        print()

        if acum % 5 == 0:
            print("---------------------------------------------------------")
            print(f"*El acumulado {acum} es múltiplo de 5")
            multiplos.append(acum)
            print(f"*Las ocurrencias de los múltiplos de 5 son: {len(multiplos)}")
            print("---------------------------------------------------------")
            print()

        nombre = input("Ingrese su nombre para participar o presione enter para salir: ")

    print("Resultados:")
    print("---------------------------------------------------------")
    print("| Descripción                                                | Resultado        |")
    print("---------------------------------------------------------")
    print(f"| El promedio de los números sacados por los estudiantes    | {round(acum / cont, 2)}          |")

    if multiplos:
        print(
            f"| El porcentaje acumulado de los acumulados múltiplos de 5  | {round(sum(multiplos) / acum * 100, 2)}%        |")
        print(f"| El máximo entre los acumulados múltiplos de 5             | {max(multiplos)}            |")
        print(f"| El mínimo entre los acumulados múltiplos de 5             | {min(multiplos)}            |")
    else:
        print(f"| El porcentaje acumulado de los acumulados múltiplos de 5  | 0%        |")
        print(f"| El máximo entre los acumulados múltiplos de 5             | No hay múltiplos de 5      |")
        print(f"| El mínimo entre los acumulados múltiplos de 5             | No hay múltiplos de 5      |")

    print("---------------------------------------------------------")


main()