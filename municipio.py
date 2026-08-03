class Municipio():
    """Representa los municipios de Caracas

    Los municipios son Chacao, Baruta, El Hatillo, Sucre y Libertador y cada municipio
    tiene sus localidades.
    """

    def __init__(self, nombre):
        """Guarda el nombre del municipio y deja vacia la lista de localidades."""
        self.nombre = nombre
        self.localidades = []

    def agregar_localidad(self, localidad):
        """Agrega una localidad a la lista del municipio."""
        self.localidades.append(localidad)

    def cantidad_localidades(self):
        """Devuelve cuantas localidades tiene el municipio."""
        cantidad = len(self.localidades)
        return cantidad

    def localidades_con_coordenadas(self):
        """Devuelve la lista de las localidades que si tienen coordenadas."""
        encontradas = []
        for localidad in self.localidades:
            if localidad.tiene_coordenadas() == True:
                encontradas.append(localidad)
        return encontradas

    def localidades_sin_coordenadas(self):
        """Devuelve la lista de las localidades que vienen null."""
        encontradas = []
        for localidad in self.localidades:
            if localidad.tiene_coordenadas() == False:
                encontradas.append(localidad)
        return encontradas

    def porcentaje_con_coordenadas(self):
        """Devuelve que porcentaje de las localidades tiene coordenadas.

        Se revisa que la cantidad no sea cero antes de dividir, porque no se
        puede dividir entre cero y el programa se caeria.
        """
        if self.cantidad_localidades() == 0:
            porcentaje = 0.0
            return porcentaje
        cuantas = len(self.localidades_con_coordenadas())
        porcentaje = cuantas * 100 / self.cantidad_localidades()
        return porcentaje

    def buscar_localidad_por_nombre(self, texto):
        """Devuelve la lista de localidades cuyo nombre se parece al texto."""
        encontradas = []
        for localidad in self.localidades:
            if localidad.se_llama_parecido(texto) == True:
                encontradas.append(localidad)
        return encontradas

    def mostrar_reporte_de_carga(self):
        """Imprime el reporte de carga de este municipio.

        Muestra lo que pide el enunciado: cuantas localidades se cargaron,
        cuantas tienen coordenadas, cuantas no, y el porcentaje.
        """
        con = len(self.localidades_con_coordenadas())
        sin = len(self.localidades_sin_coordenadas())
        print("")
        print(f"Municipio: {self.nombre}")
        print(f"  Localidades cargadas...................: {self.cantidad_localidades()}")
        print(f"  Con coordenadas geograficas............: {con}")
        print(f"  Sin coordenadas geograficas conocidas..: {sin}")
        print(f"  Porcentaje con coordenadas.............: {self.porcentaje_con_coordenadas():.2f} %")
