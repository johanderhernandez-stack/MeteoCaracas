import json
import requests

from municipio import Municipio
from localidad import Localidad
from clima import Clima

class MeteoCaracas():
    """Clase principal del programa.

    Guarda la lista de los cinco municipios y la lista de los climas
    consultados en la sesion, y se encarga de conectarse a la API.
    """

    def __init__(self):
        """Crea el sistema con las dos listas vacias."""
        self.municipios = []
        self.consultas = []

    def carga_inicial(self):
        """Lee el archivo de zonas y muestra el reporte de la carga."""
        print("Cargando el archivo de zonas de Caracas, espere un momento...")
        if (self.cargar_zonas() == True):
            self.mostrar_reporte_de_carga()

    def cargar_zonas(self):
        """Lee zonas_caracas.json y lo pasa a listas de objetos.

        Los datos del archivo vienen en diccionarios, pero NO se guardan asi:
        de cada uno se crea una Localidad y se mete en su Municipio.
        """
        archivo_zonas = "zonas_caracas.json"

        try:
            archivo = open(archivo_zonas, "r", encoding="utf-8")
            datos = json.load(archivo)
            archivo.close()
        except:
            print(f"No se pudo leer el archivo {archivo_zonas}.")
            print("Tiene que estar en la misma carpeta que main.py y estar completo.")
            return False

        for nombre_municipio in datos:
            municipio = Municipio(nombre_municipio.replace("_", " "))

            for dato in datos[nombre_municipio]:
                localidad = Localidad(dato["localidad"], dato["latitud"],
                                      dato["longitud"], municipio.nombre)
                municipio.agregar_localidad(localidad)

            self.municipios.append(municipio)

        return True

    def hay_datos_cargados(self):
        """Devuelve True si se cargo al menos un municipio del archivo."""
        if (len(self.municipios) > 0):
            return True
        else:
            return False

    def mostrar_reporte_de_carga(self):
        """Muestra el reporte de carga de cada municipio (el punto 1 del
        enunciado) y al final los totales de toda la ciudad.
        """
        print("")
        print("=============================================")
        print("        REPORTE DE CARGA DE DATOS")
        print("=============================================")

        total = 0
        total_con = 0
        total_sin = 0
        for municipio in self.municipios:
            municipio.mostrar_reporte_de_carga()
            total = total + municipio.cantidad_localidades()
            total_con = total_con + len(municipio.localidades_con_coordenadas())
            total_sin = total_sin + len(municipio.localidades_sin_coordenadas())

        porcentaje = 0.0
        if (total > 0):
            porcentaje = total_con * 100 / total

        print("")
        print("---------------------------------------------")
        print(f"TOTAL de localidades cargadas: {total}")
        print(f"TOTAL con coordenadas geográficas: {total_con}")
        print(f"TOTAL sin coordenadas geográficas: {total_sin}")
        print(f"Porcentaje con coordenadas: {porcentaje} %")
        print("=============================================")

    def descargar_json(self, direccion):
        """Le hace la solicitud GET a la API y devuelve el json.

        El try-except es por si no hay internet. Si algo falla devuelve None.
        """
        try:
            respuesta = requests.get(direccion)
            datos = respuesta.json()
        except:
            print("No se pudo consultar la API de Open-Meteo. Revise su internet.")
            return None

        return datos

    def consultar_clima(self, localidad):
        """Consulta en la API el clima de ahorita de una localidad.

        Con lo que responde se crea un objeto Clima y se guarda en la
        localidad y en las consultas de la sesion. Devuelve None si fallo.
        """
        if (localidad.tiene_coordenadas() == False):
            print("Esa localidad no tiene coordenadas, no se le puede consultar el clima.")
            return None

        print(f"\nConsultando el clima de {localidad.nombre}, espere un momento...")
        direccion = (f"https://api.open-meteo.com/v1/forecast"
                     f"?latitude={localidad.latitud}"
                     f"&longitude={localidad.longitud}"
                     f"&current=temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code"
                     f"&timezone=auto")
        datos = self.descargar_json(direccion)
        if (datos == None):
            return None

        if ("current" not in datos):
            print("La API no mandó los datos del clima de esta localidad.")
            return None

        actual = datos["current"]
        clima = Clima(localidad,actual["time"],actual["temperature_2m"],actual["relative_humidity_2m"],actual["wind_speed_10m"],actual["weather_code"])
        localidad.climas.append(clima)
        self.consultas.append(clima)
        return clima

    def mostrar_municipios(self):
        """Muestra en pantalla la lista de municipios numerada."""
        print("")
        print("MUNICIPIOS DEL ÁREA METROPOLITANA DE CARACAS")
        print("---------------------------------------------")
        numero = 1
        for municipio in self.municipios:
            print(f"{numero}- {municipio.nombre} ({municipio.cantidad_localidades()} localidades)")
            numero = numero + 1

    def escoger_municipio(self):
        """Muestra los municipios y devuelve el que escoja el usuario.

        Devuelve None si el usuario escribe un numero que no esta en la lista.
        """
        self.mostrar_municipios()

        while True:
            try:
                numero = int(input("\nEscriba el número del municipio: "))
                break
            except:
                print("Por favor escriba un número entero válido.")

        if (numero < 1 or numero > len(self.municipios)):
            print("Ese número no está en la lista de municipios.")
            return None
        municipio = self.municipios[numero - 1]
        return municipio

    def mostrar_localidades(self, localidades):
        """Muestra una lista de localidades numerada."""
        print("")
        print("LOCALIDADES")
        print("---------------------------------------------")
        numero = 1
        for localidad in localidades:
            print(f"{numero}- {localidad.nombre}")
            numero = numero + 1

    def escoger_localidad(self, localidades):
        """Muestra las localidades y devuelve la que escoja el usuario.

        Devuelve None si la lista esta vacia o si el usuario escribe un numero
        que no esta en la lista.
        """
        if (len(localidades) == 0):
            print("No hay localidades con coordenadas para escoger.")
            return None

        self.mostrar_localidades(localidades)

        while True:
            try:
                numero = int(input("\nEscriba el número de la localidad: "))
                break
            except:
                print("Por favor escriba un número entero válido.")

        if (numero < 1 or numero > len(localidades)):
            print("Ese número no está en la lista de localidades.")
            return None
        localidad = localidades[numero - 1]
        return localidad

    def buscar_localidades_por_nombre(self, texto):
        """Busca en toda la ciudad las localidades que se llamen parecido.

        Solo las que tienen coordenadas, porque a las otras no se les puede
        consultar el clima.
        """
        encontradas = []
        for municipio in self.municipios:
            for localidad in municipio.buscar_localidad_por_nombre(texto):
                if (localidad.tiene_coordenadas() == True):
                    encontradas.append(localidad)
        return encontradas

    # REPORTES Y ESTADISTICAS
    def hubo_consultas(self):
        """Devuelve True si en esta sesion ya se consulto algun clima."""
        if (len(self.consultas) > 0):
            return True
        else:
            return False

    def clima_mas_calido(self):
        """Devuelve la consulta con la temperatura mas alta de la sesion."""
        ganador = None
        for clima in self.consultas:
            if (ganador == None or clima.temperatura > ganador.temperatura):
                ganador = clima
        return ganador

    def clima_mas_frio(self):
        """Devuelve la consulta con la temperatura mas baja de la sesion."""
        ganador = None
        for clima in self.consultas:
            if (ganador == None or clima.temperatura < ganador.temperatura):
                ganador = clima
        return ganador

    def promedio_de_temperatura(self):
        """Saca el promedio de temperatura de las consultas de la sesion.

        Si todavia no se ha consultado nada devuelve None, para no dividir
        entre cero.
        """
        if (self.hubo_consultas() == False):
            return None
        suma = 0.0
        for clima in self.consultas:
            suma = suma + clima.temperatura
        promedio = suma / len(self.consultas)
        return promedio

    def mostrar_ranking_de_temperatura(self):
        """Muestra el municipio con la localidad mas calida y la mas fria.

        Solo cuentan las localidades consultadas en esta sesion, como pide el
        enunciado.
        """
        print("")
        print("=============================================")
        print("        RANKING DE TEMPERATURA")
        print("=============================================")
        if (self.hubo_consultas() == False):
            print("Todavía no se ha consultado el clima de ninguna localidad.")
            print("Use las opciones 2 o 3 del menú y vuelva a entrar aquí.")
            return

        calido = self.clima_mas_calido()
        frio = self.clima_mas_frio()

        print(f"Consultas hechas en esta sesión: {len(self.consultas)}")
        print("---------------------------------------------")
        print("LA MÁS CÁLIDA")
        print(f"  Municipio: {calido.localidad.nombre_municipio}")
        print(f"  Localidad: {calido.localidad.nombre}")
        print(f"  Temperatura: {calido.temperatura} C")
        print("")
        print("LA MÁS FRÍA")
        print(f"  Municipio: {frio.localidad.nombre_municipio}")
        print(f"  Localidad: {frio.localidad.nombre}")
        print(f"  Temperatura: {frio.temperatura} C")
        print("---------------------------------------------")
        print("TODAS LAS CONSULTAS DE LA SESIÓN")
        for clima in self.consultas:
            clima.mostrar_resumen()
        print("=============================================")

    def mostrar_cobertura_geografica(self):
        """Muestra las localidades que no tienen coordenadas, por municipio.

        Son las que en el archivo vienen con la latitud y la longitud en null.
        """
        print("")
        print("=============================================")
        print("        COBERTURA GEOGRÁFICA")
        print("  Localidades SIN coordenadas registradas")
        print("=============================================")

        total = 0
        for municipio in self.municipios:
            faltantes = municipio.localidades_sin_coordenadas()
            print("")
            print(f"Municipio: {municipio.nombre} ({len(faltantes)} sin coordenadas)")
            print("---------------------------------------------")
            if (len(faltantes) == 0):
                print("  Todas sus localidades tienen coordenadas.")
            for localidad in faltantes:
                print(f"  - {localidad.nombre}")
            total = total + len(faltantes)

        print("")
        print("---------------------------------------------")
        print(f"TOTAL de localidades sin coordenadas: {total}")
        print("=============================================")

    def mostrar_promedio_general(self):
        """Muestra el promedio de temperatura de las consultas de la sesion."""
        print("")
        print("=============================================")
        print("        PROMEDIO GENERAL DE TEMPERATURA")
        print("=============================================")
        promedio = self.promedio_de_temperatura()
        if (promedio == None):
            print("Todavía no se ha consultado el clima de ninguna localidad.")
            print("Use las opciones 2 o 3 del menú y vuelva a entrar aquí.")
            return

        print(f"Localidades consultadas en la sesión: {len(self.consultas)}")
        for clima in self.consultas:
            clima.mostrar_resumen()
        print("---------------------------------------------")
        print(f"Temperatura promedio de la sesión: {promedio} C")
        print("=============================================")

