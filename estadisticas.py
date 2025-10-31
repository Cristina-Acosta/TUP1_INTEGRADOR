#Script de estadísticas
#from menu.API import paises_lista
from funciones_ordenamiento import ordenar_paises
# País con mayor y menor población
def mayor_menor_poblacion(paises):
    lista=ordenar_paises(paises,"poblacion","ascendente")
    print(f"País con mayor población en el mundo: {lista[-1]}")
    print(f"País con menor población en el mundo: {lista[0]}")

# Promedio de población o superficie
def funcion_promedio(paises,valor):
    suma=0
    for pais in paises:
        suma+=pais[valor]
    promedio=suma/(len(paises))
    print(f"Promedio {valor} mundial: {promedio}")

# Cantidad de países por continente
def cantidad_paises(paises):
    #Diccionario acumulador de paises
    cantidad = {"Asia": 0,"Europe": 0,"Africa": 0,"North America":0,"South America":0,"Antarctica":0,"Oceania": 0}
    for pais in paises:
        continente = pais["continente"]  
        # Sumamos uno al continente que corresponda
        if continente in cantidad:
            cantidad[continente] += 1
    print (*cantidad.items(), sep='\n')

if __name__=="__main__":
    paises=paises_lista()
    funcion_promedio(paises,"area")
    cantidad_paises(paises)
