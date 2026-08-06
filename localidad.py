class Localidad():
    """Una urbanizacion, barrio o sector de un municipio.
    Guarda el nombre, la latitud, la longitud, de que municipio es y los climas
    que se le han consultado. Ojo que las coordenadas pueden venir en None."""

    def __init__(self, nombre, latitud, longitud, nombre_municipio):
        """Guarda el nombre, las coordenadas y el nombre del municipio.
        La lista de climas arranca vacia y se va llenando con las consultas."""
        self.nombre = nombre
        self.latitud = latitud
        self.longitud = longitud
        self.nombre_municipio = nombre_municipio
        self.climas = []

    def tiene_coordenadas(self):
        """Dice si la localidad tiene latitud y longitud o si vino con null.
        Casi todo el programa pregunta esto antes de consultarle el clima."""
        if (self.latitud == None):
            return False
        if (self.longitud == None):
            return False
        return True

    def se_llama_parecido(self, texto):
        """Dice si el texto esta metido dentro del nombre, sin importar mayusculas.
        Asi con 'palos' se encuentra 'Los Palos Grandes' sin escribirlo completo."""
        if (texto.lower() in self.nombre.lower()):
            return True
        else:
            return False

    def mostrar_info(self):
        """Imprime el municipio, el nombre y las coordenadas de la localidad.
        Si no tiene coordenadas pone un aviso, en vez de dejar la linea en blanco."""
        print(f"Municipio: {self.nombre_municipio}")
        print(f"Localidad: {self.nombre}")

        if (self.tiene_coordenadas() == False):
            print("Coordenadas: sin coordenadas registradas")
        else:
            print(f"Coordenadas: Latitud {self.latitud} / Longitud {self.longitud}")
