class RegistroMes():
    """Los datos meteorologicos de un mes de un anio.

    Como la API manda los datos dia por dia, este objeto va sumando los dias
    de su mes y al final divide para sacar los promedios.
    """

    def __init__(self, anio, mes):
        """Crea el mes con todas las sumas y los contadores en cero."""
        self.anio = anio
        self.mes = mes

        self.suma_temperatura = 0.0
        self.dias_temperatura = 0

        self.suma_humedad = 0.0
        self.dias_humedad = 0

        self.total_precipitacion = 0.0
        self.dias_precipitacion = 0

        self.suma_viento = 0.0
        self.dias_viento = 0

    def agregar_dia(self, temperatura, humedad, precipitacion, viento):
        """Suma los datos de un dia al mes.

        Cada dato se revisa aparte porque la API a veces deja alguno en None,
        y ese no se puede sumar.
        """
        if (temperatura != None):
            self.suma_temperatura = self.suma_temperatura + temperatura
            self.dias_temperatura = self.dias_temperatura + 1

        if (humedad != None):
            self.suma_humedad = self.suma_humedad + humedad
            self.dias_humedad = self.dias_humedad + 1

        if (precipitacion != None):
            self.total_precipitacion = self.total_precipitacion + precipitacion
            self.dias_precipitacion = self.dias_precipitacion + 1

        if (viento != None):
            self.suma_viento = self.suma_viento + viento
            self.dias_viento = self.dias_viento + 1

    def temperatura_promedio(self):
        """Divide la suma entre los dias, o devuelve None si el mes no tiene."""
        if (self.dias_temperatura == 0):
            return None
        promedio = self.suma_temperatura / self.dias_temperatura
        return promedio

    def humedad_promedio(self):
        """Divide la suma entre los dias, o devuelve None si el mes no tiene."""
        if (self.dias_humedad == 0):
            return None
        promedio = self.suma_humedad / self.dias_humedad
        return promedio

    def precipitacion_acumulada(self):
        """Devuelve todo lo que llovio en el mes en milimetros.

        Esta no se promedia: el enunciado pide la lluvia acumulada, o sea la
        suma de todos los dias.
        """
        if (self.dias_precipitacion == 0):
            return None
        return self.total_precipitacion

    def viento_promedio(self):
        """Divide la suma entre los dias, o devuelve None si el mes no tiene."""
        if (self.dias_viento == 0):
            return None
        promedio = self.suma_viento / self.dias_viento
        return promedio

    def mostrar_fila(self):
        """Imprime la fila de la tabla con los cuatro datos del mes.

        Se le agregan espacios a cada columna para que la tabla salga alineada.
        """
        nombres_de_los_meses = ["", "Enero", "Febrero", "Marzo", "Abril","Mayo", "Junio", "Julio", "Agosto","Septiembre", "Octubre", "Noviembre","Diciembre"]

        linea = f"{nombres_de_los_meses[self.mes]} {self.anio}"
        while len(linea) < 16:
            linea = linea + " "

        valores = [self.temperatura_promedio(), self.humedad_promedio(),
                   self.precipitacion_acumulada(), self.viento_promedio()]

        for valor in valores:
            if (valor == None):
                columna = "sin dato"
            else:
                columna = f"{valor}"
            while len(columna) < 22:
                columna = columna + " "
            linea = linea + columna

        print(linea)
