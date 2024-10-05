# Importa la libreria pandas, que es fundamental para el analisis de datos
import pandas as pd

#Define la ruta del archivo CSV que contiene los datos
# Si el archivo está en el mismo directorio que el script, basta con poner el nombre del archivo
path = 'Harry_Potter.csv'

# Lee el archivo CSV usando la funcion 'read_csv? de Pandas
# Se especifica la codificacion 'latin1' (tambien conocida como ISO-8859-1) para manejar caracteres especiales.
harry_potter = pd.read_csv(path, encoding='latin1') 

#Muestra el tipo de la variable 'harry_potter' para confirmar que es un Dataframe 
# Un DataFrame es una estructura de datos bidimensional (filas y columnas) similar a una tabla
print(type(harry_potter))

#Imprime todo el contenido del DataFrame 'harry_potter' para visualizar los datos que fueron leídos del archivo csv.
print(harry_potter) 
