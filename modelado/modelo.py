class arregloBinario:
    # Constructor
    def __init__(self, datos):
        self.datos = datos
    # Metodo apra agregar datos
    def agregar_datos(self, dat):
        self.datos = dat
    # Método para buscar de forma binaria en una lista
    def busquedaBinaria(self, busqueda):
        # Declaración de variables
        inferior = 0
        superior = len(self.datos) - 1
        medio = int((inferior + superior + 1) / 2)
        ubicacion = int(-1)
        b = busqueda
        # Ciclo while para comprobar la poscicion del numero en el arreglo
        while((inferior <= superior) & (ubicacion == -1)):
            if(b == self.datos[medio]):
                ubicacion = medio
            elif(b < self.datos[medio]):
                superior = medio - 1
            else:
                inferior = medio + 1
            medio = int((inferior + superior + 1) / 2)
        return ubicacion
