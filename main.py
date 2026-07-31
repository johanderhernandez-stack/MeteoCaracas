def mostrar_menu():
    """Imprime en pantalla las opciones del menu principal."""

    print("")
    print("===========================================")
    print("            MetroArt - Catalogo")
    print("   Museo Metropolitano de Arte (The Met)")
    print("===========================================")
    print("1- Ver lista de obras por Departamento")
    print("2- Ver lista de obras por Nacionalidad del autor")
    print("3- Ver lista de obras por nombre del autor")
    print("4- Salir del programa")


def opcion_departamento():
    """Opcion 1: muestra los departamentos y lista las obras del elegido."""


def opcion_nacionalidad():
    """Opcion 2: muestra las nacionalidades y lista las obras de la elegida."""


def opcion_autor():
    """Opcion 3: pide el nombre del autor y lista sus obras."""


def main():
    """Funcion de inicio que inicia el programa."""

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            opcion_departamento()

        elif opcion == "2":
            opcion_nacionalidad()

        elif opcion == "3":
            opcion_autor()

        elif opcion == "4":
            print("Gracias por usar MetroArt. Hasta luego.")
            break

        else:
            print("Opcion no valida, escriba un numero del 1 al 4.")


main()