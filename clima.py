class Clima():
    """El clima de una localidad en un momento, ya convertido en objeto.
    Guarda la hora, la temperatura, la humedad, el viento, el codigo del tiempo y
    la localidad completa, asi desde el clima se llega hasta el municipio."""

    def __init__(self, localidad, hora, temperatura, humedad, viento, codigo_tiempo):
        """Guarda los seis datos de la consulta.
        La localidad entra como objeto y no como texto, para no perder de donde es."""
        self.localidad = localidad
        self.hora = hora
        self.temperatura = temperatura
        self.humedad = humedad
        self.viento = viento
        self.codigo_tiempo = codigo_tiempo

    def descripcion_del_tiempo(self):
        """Agarra el codigo que manda la API y lo pasa a palabras.
        La tabla es una lista de listas y no un diccionario, como pide el enunciado.
        Si el codigo no esta en ella, pone que no se sabe en vez de quedar vacio."""
        codigos_del_tiempo = [[0, "Despejado"],[1, "Mayormente despejado"],[2, "Parcialmente nublado"],[3, "Nublado"],[45, "Neblina"],[48, "Neblina con escarcha"],[51, "Llovizna ligera"],[53, "Llovizna moderada"],[55, "Llovizna intensa"],[56, "Llovizna helada ligera"],[57, "Llovizna helada intensa"],[61, "Lluvia ligera"],[63, "Lluvia moderada"],[65, "Lluvia fuerte"],[66, "Lluvia helada ligera"],[67, "Lluvia helada fuerte"],[71, "Nevada ligera"],[73, "Nevada moderada"],[75, "Nevada fuerte"],[77, "Granos de nieve"],[80, "Chubascos ligeros"],[81, "Chubascos moderados"],[82, "Chubascos violentos"],[85, "Chubascos de nieve ligeros"],[86, "Chubascos de nieve fuertes"],[95, "Tormenta eléctrica"],[96, "Tormenta con granizo ligero"],[99, "Tormenta con granizo fuerte"]]

        descripcion = "Estado del tiempo desconocido"
        for fila in codigos_del_tiempo:
            if (fila[0] == self.codigo_tiempo):
                descripcion = fila[1]
                break
        return descripcion

    def mostrar_detalles(self):
        """Saca en pantalla todo lo que pide el punto 2 del enunciado: municipio,
        localidad, coordenadas, temperatura, humedad, viento y estado del tiempo."""
        print("")
        print("=============================================")
        print("        CLIMA EN TIEMPO REAL")
        print("=============================================")
        self.localidad.mostrar_info()
        print(f"Hora de la medición: {self.hora}")
        print("---------------------------------------------")
        print(f"Temperatura actual: {self.temperatura} C")
        print(f"Humedad relativa: {self.humedad} %")
        print(f"Velocidad del viento: {self.viento} km/h")
        print(f"Estado del tiempo: {self.codigo_tiempo} - {self.descripcion_del_tiempo()}")
        print("=============================================")

    def mostrar_resumen(self):
        """Lo mismo pero apretado en una sola linea.
        Se usa en el ranking y en el promedio, donde hay que listar varias seguidas."""
        print(f"{self.localidad.nombre_municipio} / {self.localidad.nombre}: {self.temperatura} C ({self.descripcion_del_tiempo()})")
    