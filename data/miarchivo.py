import codecs
import sys

class MiArchivo:
    # Constructor
    def __init__(self, nombre):
        """
        """
        self.nombre_archivo = nombre
        self.archivo = codecs.open(self.nombre_archivo, "r")
    # Método para obtener información
    def obtener_informacion(self):
        return self.archivo.readlines()
    # Método para cerrrar archivo
    def cerrar_archivo(self):
        self.archivo.close()
