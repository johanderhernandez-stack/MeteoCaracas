class Localidad():
    """Representa una localidad de un municipio.

    Guarda el nombre de la localidad, latitud, longitud y el nombre del
    municipio al que pertenece. La latitud y la longitud pueden ser None. Tambien guarda 
    la lista de los climas que se le han consultado durante la sesion (objetos Clima).
    """

    def __init__(self, nombre, latitud, longitud, nombre_municipio):
        """Guarda los datos de la localidad y deja vacia la lista de climas."""
        self.nombre = nombre
        self.latitud = latitud
        self.longitud = longitud
        self.nombre_municipio = nombre_municipio
        self.climas = []

    def tiene_coordenadas(self):
        """Devuelve True si la localidad tiene latitud y longitud (no son null)."""
        if self.latitud == None:
            return False
        if self.longitud == None:
            return False
        return True

    def se_llama_parecido(self, texto):
        """Devuelve True si el texto aparece dentro del nombre de la localidad.

        Se usa en la busqueda por nombre, para que el usuario no tenga que escribir el
        nombre completo, lo pone en minusculas.
        """
        if texto.lower() in self.nombre.lower():
            return True
        else:
            return False

    def guardar_clima(self, clima):
        """Agrega a la lista el clima que se acaba de consultar."""
        self.climas.append(clima)

    def texto_coordenadas(self):
        """Devuelve la latitud y la longitud escritas para mostrarlas."""
        if self.tiene_coordenadas() == False:
            texto = "sin coordenadas registradas"
        else:
            texto = f"Latitud {self.latitud} / Longitud {self.longitud}"
        return texto

    def mostrar_en_lista(self, numero):
        """Imprime una linea de la lista de localidades, con su numero.
        """
        print(f"{numero}- {self.nombre}")

    def mostrar_info(self):
        """Imprime el municipio, el nombre y las coordenadas de la localidad."""
        print(f"Municipio: {self.nombre_municipio}")
        print(f"Localidad: {self.nombre}")
        print(f"Coordenadas: {self.texto_coordenadas()}")
