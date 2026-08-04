from meteocaracas import MeteoCaracas


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


def escoger_localidad_de_un_municipio(sistema):
    """Deja escoger un municipio y despues una de sus localidades.

    Solo salen las que tienen coordenadas, que son las unicas que se pueden
    consultar. Devuelve None si el usuario se equivoca.
    """
    municipio = sistema.escoger_municipio()
    if (municipio == None):
        return None

    localidades = municipio.localidades_con_coordenadas()
    print(f"\nMunicipio: {municipio.nombre}")
    print(f"Tiene {len(localidades)} localidades con coordenadas validas.")
    localidad = sistema.escoger_localidad(localidades)
    return localidad


def opcion_reporte_carga(sistema):
    """Opcion 1: vuelve a mostrar el reporte de la carga de datos."""
    sistema.mostrar_reporte_de_carga()


def opcion_clima_por_municipio(sistema):
    """Opcion 2: consulta el clima escogiendo municipio y localidad."""
    localidad = escoger_localidad_de_un_municipio(sistema)
    if (localidad == None):
        return

    clima = sistema.consultar_clima(localidad)
    if (clima != None):
        clima.mostrar_detalles()


def opcion_clima_por_nombre(sistema):
    """Opcion 3: consulta el clima buscando la localidad por su nombre.

    Se escribe el nombre o una parte, salen todas las coincidencias de la
    ciudad y el usuario escoge.
    """
    texto = sistema.pedir_texto("\nEscriba el nombre de la localidad (o una parte): ")
    encontradas = sistema.buscar_localidades_por_nombre(texto)

    if (len(encontradas) == 0):
        print(f"No se encontro ninguna localidad con coordenadas que se llame '{texto}'.")
        print("Puede ser que exista pero que no tenga coordenadas en el archivo.")
        return

    print(f"\nSe encontraron {len(encontradas)} localidades:")
    numero = 1
    print("---------------------------------------------")
    for localidad in encontradas:
        print(f"{numero}- {localidad.nombre} ({localidad.nombre_municipio})")
        numero = numero + 1

    numero = sistema.pedir_numero_entero("\nEscriba el numero de la localidad: ")
    if (numero < 1 or numero > len(encontradas)):
        print("Ese numero no esta en la lista.")
        return

    localidad = encontradas[numero - 1]
    clima = sistema.consultar_clima(localidad)
    if (clima != None):
        clima.mostrar_detalles()


def opcion_estadisticas(sistema):
    """Opcion 4: submenu con los tres reportes que pide el enunciado.

    Se queda ahi hasta que el usuario decida volver, asi puede ver varios
    reportes seguidos.
    """
    while True:
        mostrar_menu_estadisticas()
        opcion = input("Seleccione una opcion: ")

        if (opcion == "1"):
            sistema.mostrar_ranking_de_temperatura()

        elif (opcion == "2"):
            sistema.mostrar_cobertura_geografica()

        elif (opcion == "3"):
            sistema.mostrar_promedio_general()

        elif (opcion == "4"):
            return

        else:
            print("Opcion no valida, escriba un numero del 1 al 4.")


def opcion_historicos(sistema):
    """Opcion 5: muestra el clima de una localidad en un periodo de tiempo.

    Se escoge la localidad, se piden las dos fechas y se muestran la tabla
    mes a mes, los promedios, los anios destacados y el grafico.
    """
    localidad = escoger_localidad_de_un_municipio(sistema)
    if (localidad == None):
        return

    print("")
    print(f"Localidad escogida: {localidad.nombre} ({localidad.nombre_municipio})")
    print("Ahora escriba el periodo que quiere analizar.")
    print("Las fechas van con el formato AAAA-MM-DD (ejemplo: 2020-01-01).")

    fecha_inicio = sistema.pedir_fecha("Fecha de inicio: ")
    fecha_fin = sistema.pedir_fecha("Fecha de fin: ")

    if (sistema.fecha_a_numero(fecha_inicio) > sistema.fecha_a_numero(fecha_fin)):
        print("La fecha de inicio no puede ser despues de la fecha de fin.")
        return

    historico = sistema.consultar_historico(localidad, fecha_inicio, fecha_fin)
    if (historico == None):
        return

    historico.mostrar_tabla_de_meses()
    historico.mostrar_promedios()
    historico.mostrar_anios_destacados()

    print("")
    respuesta = input("Desea ver el grafico comparativo? (1-Si / 2-No): ")
    if (respuesta == "1"):
        historico.mostrar_grafico()


def main():
    """Funcion principal: carga los datos y muestra el menu en un bucle."""
    sistema = MeteoCaracas()
    sistema.carga_inicial()

    if (sistema.hay_datos_cargados() == False):
        print("\nEl programa no puede seguir sin el archivo de zonas. Hasta luego.")
        return

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")

        if (opcion == "1"):
            opcion_reporte_carga(sistema)

        elif (opcion == "2"):
            opcion_clima_por_municipio(sistema)

        elif (opcion == "3"):
            opcion_clima_por_nombre(sistema)

        elif (opcion == "4"):
            opcion_estadisticas(sistema)

        elif (opcion == "5"):
            opcion_historicos(sistema)

        elif (opcion == "6"):
            print("Gracias por usar MeteoCaracas. Hasta luego.")
            break

        else:
            print("Opcion no valida, escriba un numero del 1 al 6.")


main()

