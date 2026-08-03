class Clima():
    """Representa el clima de una localidad en un momento dado.

    Guarda la localidad que se consulto,hora de la medicion,temperatura en grados centigrados,
    humedad relativa en porcentaje, velocidad del viento y el codigo del tiempo de la API.
    Esto se usa para armar estadisticas.
    """

    def __init__(self, localidad, hora, temperatura, humedad, viento, codigo_tiempo):
        """Guarda los datos meteorologicos de la consulta."""
        self.localidad = localidad
        self.hora = hora
        self.temperatura = temperatura
        self.humedad = humedad
        self.viento = viento
        self.codigo_tiempo = codigo_tiempo

    def descripcion_del_tiempo(self):
        """Devuelve en palabras lo que significa el codigo del tiempo de 
        acuerdo a la documentacion de la API de Open-Meteo.
        """
        codigos_del_tiempo = [
            [0, "Despejado"],
            [1, "Mayormente despejado"],
            [2, "Parcialmente nublado"],
            [3, "Nublado"],
            [45, "Neblina"],
            [48, "Neblina con escarcha"],
            [51, "Llovizna ligera"],
            [53, "Llovizna moderada"],
            [55, "Llovizna intensa"],
            [56, "Llovizna helada ligera"],
            [57, "Llovizna helada intensa"],
            [61, "Lluvia ligera"],
            [63, "Lluvia moderada"],
            [65, "Lluvia fuerte"],
            [66, "Lluvia helada ligera"],
            [67, "Lluvia helada fuerte"],
            [71, "Nevada ligera"],
            [73, "Nevada moderada"],
            [75, "Nevada fuerte"],
            [77, "Granos de nieve"],
            [80, "Chubascos ligeros"],
            [81, "Chubascos moderados"],
            [82, "Chubascos violentos"],
            [85, "Chubascos de nieve ligeros"],
            [86, "Chubascos de nieve fuertes"],
            [95, "Tormenta electrica"],
            [96, "Tormenta con granizo ligero"],
            [99, "Tormenta con granizo fuerte"],
        ]

        descripcion = "Estado del tiempo desconocido"
        for fila in codigos_del_tiempo:
            if fila[0] == self.codigo_tiempo:
                descripcion = fila[1]
                break
        return descripcion

    def mostrar_detalles(self):
        """Imprime en pantalla todos los detalles meteorologicos del clima.
        """
        print("")
        print("=============================================")
        print("        CLIMA EN TIEMPO REAL")
        print("=============================================")
        self.localidad.mostrar_info()
        print(f"Hora de la medicion: {self.hora}")
        print("---------------------------------------------")
        print(f"Temperatura actual...: {self.temperatura} C")
        print(f"Humedad relativa.....: {self.humedad} %")
        print(f"Velocidad del viento.: {self.viento} km/h")
        print(f"Estado del tiempo....: {self.codigo_tiempo} - {self.descripcion_del_tiempo()}")
        print("=============================================")

    def mostrar_resumen(self):
        """Imprime en una sola linea el municipio, la localidad y la temperatura.

        Se usa en el ranking y en la lista de las consultas de la sesion.
        """
        print(f"{self.localidad.nombre_municipio} / {self.localidad.nombre}: {self.temperatura} C ({self.descripcion_del_tiempo()})")
