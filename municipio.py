class Municipio():
    """Uno de los 5 municipios: Chacao, Baruta, El Hatillo, Sucre o Libertador.
    Guarda su nombre y la lista de sus localidades, que es como viene armado el
    archivo zonas_caracas.json."""

    def __init__(self, nombre):
        """Guarda el nombre y deja la lista de localidades vacia.
        Se va llenando con agregar_localidad() mientras se lee el archivo."""
        self.nombre = nombre
        self.localidades = []

    def agregar_localidad(self, localidad):
        """Le mete una localidad a la lista del municipio.
        Se llama una vez por cada localidad que trae el json."""
        self.localidades.append(localidad)

    def cantidad_localidades(self):
        """Cuenta cuantas localidades tiene el municipio.
        No se guarda en ningun atributo, se cuenta cada vez que se pide, asi nunca
        queda desactualizado."""
        cantidad = len(self.localidades)
        return cantidad

    def localidades_con_coordenadas(self):
        """Devuelve una lista nueva solo con las que tienen latitud y longitud.
        Son las unicas a las que se les puede pedir el clima a la API."""
        encontradas = []
        for localidad in self.localidades:
            if (localidad.tiene_coordenadas() == True):
                encontradas.append(localidad)
        return encontradas

    def localidades_sin_coordenadas(self):
        """Devuelve una lista nueva solo con las que vienen en null.
        Son las que salen en el reporte de cobertura geografica del punto 3b."""
        encontradas = []
        for localidad in self.localidades:
            if (localidad.tiene_coordenadas() == False):
                encontradas.append(localidad)
        return encontradas

    def porcentaje_con_coordenadas(self):
        """Saca que porcentaje de las localidades si tiene coordenadas.
        Revisa primero que la cantidad no sea cero, porque no se puede dividir entre
        cero y el programa se caeria."""
        if (self.cantidad_localidades() == 0):
            return 0.0
        cuantas = len(self.localidades_con_coordenadas())
        porcentaje = cuantas * 100 / self.cantidad_localidades()
        return porcentaje

    def buscar_localidad_por_nombre(self, texto):
        """Busca dentro de este municipio las que se llamen parecido al texto.
        Devuelve una lista porque puede haber varias que coincidan."""
        encontradas = []
        for localidad in self.localidades:
            if (localidad.se_llama_parecido(texto) == True):
                encontradas.append(localidad)
        return encontradas

    def mostrar_reporte_de_carga(self):
        """Imprime las 4 lineas del punto 1 para este municipio: cargadas, con
        coordenadas, sin coordenadas y el porcentaje."""
        con = len(self.localidades_con_coordenadas())
        sin = len(self.localidades_sin_coordenadas())
        print("")
        print(f"Municipio: {self.nombre}")
        print(f"  Localidades cargadas: {self.cantidad_localidades()}")
        print(f"  Con coordenadas geográficas: {con}")
        print(f"  Sin coordenadas geográficas conocidas: {sin}")
        print(f"  Porcentaje con coordenadas: {self.porcentaje_con_coordenadas()} %")
