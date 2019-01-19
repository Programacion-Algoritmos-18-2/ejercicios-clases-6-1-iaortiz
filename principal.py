# Importación de clases
from modelado.modelo import arregloBinario
from data.miarchivo import MiArchivo
# Variable para leer el archivo
ma = MiArchivo("data/datos.txt")
# creamos una lista y almacenamos el archivo leido
lista1 = ma.obtener_informacion()
lista1 = [l.split(",") for l in lista1]
# CReamos otra lista para almcaenar la lista ordenada
lista_ordenada = []
# Recorremos lista1 con 2 ciclos for para recorrer cada elemento de la lista
for i in lista1:
    for n in i:
        # Agregamos en la lista ordenada cada cariable
        lista_ordenada.append(int(n))
# Ordenamos la lista
lista_ordenada.sort()
# Pedimos el número que desea buscar el usuario
pedir = int(input("- Ingrese el valor a buscar\n"))
# creamos un objeto de tipo arreglo binario, el cual recibe como parametro la lista rodenada
tra = arregloBinario(lista_ordenada)
# Buscamos el número deseado en  la lista
buscar = tra.busquedaBinaria(pedir)
# Presentación
print("TRABAJO EN CLASE")
print("- La posición del nunero en la lista es: %d\n"%(buscar))
print("Lista ordenada")
print(lista_ordenada)

ma.cerrar_archivo




