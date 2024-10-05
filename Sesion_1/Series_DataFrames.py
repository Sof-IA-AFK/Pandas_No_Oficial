# Importamos la biblioteca pandas y la llamamos 'pd'
import pandas as pd

#Creamos una Serie de pandas que es co una lista con etiquetas
#Los valores son nombres de jugadores de PSG
# El índice especifica los números de camiseta de esos jugadores
psg_players = pd.Series(
    ['Navas', 'Mbappe', 'Neymar', 'Messi'],         #Lista de jugadores
    index =[1, 7, 10, 30]                           #Lista de indices (numeros de camisetas)    
)

#Imprimimos la Serie para ver su contenido
print(psg_players)

#Eliminamos el indice, por lo que pandas asigna un indice numerico automatico empezando desde 0
psg_players_2 = pd.Series(
    ['Navas', 'Mbappe', 'Neymar', 'Messi'],         #Lista de jugadores   
)

print(psg_players_2)

# Creamos un diccionario que asocia numeros de camiseta con nombres de jugadores
psg_dict = {1: 'Navas', 7: 'Mbappe', 10: 'Neymar', 30: 'Messi'}

#Creamos una Serie de pandas usando el diccionario
psg_players_2_dict = pd.Series(psg_dict)

#Imprimimos la serie creada a partir del diccionario
print(psg_players_2_dict)

#Imprimimos el valor en la posición (indice) 7 de la serie creada a partir del dict
print(psg_players_2_dict[7])
print(psg_players_2_dict[0:3])

#Diccionario con datos de jugadores
dict = {'Jugador': ['Navas', 'Mbappe', 'Neymar', 'Messi'],
        'Altura': [183.0, 170.0, 170.0, 165.0],
        'Goles': [2, 200, 150, 200]}

#crear un DataFrame con el diccionario y indices personalizados
df = pd.DataFrame(dict, index=[1, 7, 10, 30])

#Imprimir el DataFrame
print(df)

