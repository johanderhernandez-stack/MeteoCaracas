def mostrar_menu():
    """Imprime en pantalla las opciones del menu principal."""
    print("")
    print("=============================================")
    print("               MeteoCaracas")
    print("   Clima del area Metropolitana de Caracas")
    print("=============================================")
    print("1- Ver el reporte de la carga de datos")
    print("2- Consultar el clima por municipio y localidad")
    print("3- Consultar el clima buscando por nombre")
    print("4- Reportes y estadisticas")
    print("5- Historicos (clima de un periodo de tiempo)")
    print("6- Salir del programa")



def mostrar_menu_estadisticas():
    """Imprime en pantalla las opciones del modulo de estadisticas."""
    print("")
    print("---------------------------------------------")
    print("        REPORTES Y ESTADISTICAS")
    print("---------------------------------------------")
    print("1- Ranking de temperatura (la mas calida y la mas fria)")
    print("2- Cobertura geografica (localidades sin coordenadas)")
    print("3- Promedio general de temperatura de la sesion")
    print("4- Volver al menu principal")


def opcion_reporte_carga():
    """Opcion 1: vuelve a mostrar el reporte de la carga de datos."""

def opcion_clima_por_municipio():
        """Opcion 2: consulta el clima escogiendo municipio y localidad."""

def opcion_clima_por_nombre():
    """Opcion 3: consulta el clima buscando la localidad por su nombre.

    El usuario escribe el nombre o una parte del nombre y muestra todas las
    coincidencias de toda la ciudad y el usuario escoge cual quiere.
    """

def opcion_estadisticas():
    """Opcion 4: menu de reportes que pide el enunciado acerca de las estadisticas
    """


def opcion_historicos():
    """Opcion 5: muestra el clima de una localidad en un periodo de tiempo.

    Se escoge la localidad y se piden las dos fechas y se muestra la tabla de cada mes, 
    los promedios del periodo y los años destacados con su gráfico.
    """



def main():
    """Funcion principal: carga los datos y muestra el menu en un bucle."""

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            opcion_reporte_carga()

        elif opcion == "2":
            opcion_clima_por_municipio()

        elif opcion == "3":
            opcion_clima_por_nombre()

        elif opcion == "4":
            opcion_estadisticas()

        elif opcion == "5":
            opcion_historicos()

        elif opcion == "6":
            print("Gracias por usar MeteoCaracas. Hasta luego.")
            break

        else:
            print("Opcion no valida, escriba un numero del 1 al 6.")


main()
