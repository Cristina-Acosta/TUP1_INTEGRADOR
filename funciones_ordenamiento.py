#Script ordenamiento
from operator import itemgetter
#itemgetter nos permite seleccionar de la lista de diccionarios por la key y sorted la ordena 

# Ordenar países por nombre
def ordenar_paises(lista_paises,key, orden):
    try:
        return sorted(lista_paises, key=itemgetter(key), reverse=orden)
    except KeyError:
        print("Error: clave 'nombre' no encontrada en los datos.")
        return []
