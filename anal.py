import sqlite3
import pandas as pd
# Conectarse a la base de datos SQLite
conn = sqlite3.connect('films.db')
cursor = conn.cursor()

# Nombre de la tabla
nombre_de_tabla = 'peliculas' 

# Ejecutar una consulta para obtener los datos de la tabla
cursor.execute(f'SELECT * FROM {nombre_de_tabla} WHERE posicion = 3')

# Obtener todos los resultados de la consulta
data = cursor.fetchall()



peliculas3 = []
total3 = []
# Imprimir la columna "posicion" de cada fila
for row in data:
    peliculas3.append(row[2]) 
    total3.append(row[5]) 


dataset1 = {
    'Pelicula top3': peliculas3,
    'Ingreso total': total3
    }

dfTop3 = pd.DataFrame(dataset1)

import matplotlib.pyplot as plt
import numpy as np

x=dfTop3['Pelicula top3'].values
y=dfTop3['Ingreso total'].values

plt.title("Peliculas en el top 3")
plt.xlabel("Nombre de pelicula")
plt.ylabel("Ingreso obtenido en taquilla")

plt.scatter(x,y)

plt.grid()
plt.show()

# Explorando datos para encontrar las peliculas con minimo y maximo ingreso historico

# Nombre de la tabla
nombre_de_tabla = 'peliculas' 

# Ejecutar una consulta para conocer la maxima ganancia obtenida por las peliculas
cursor.execute(f'SELECT  pelicula, max(total) AS mayor FROM {nombre_de_tabla} GROUP BY pelicula;')

# Obtener todos los resultados de la consulta
data2 = cursor.fetchall()

peli= []
totalmax = []

# Imprimir la columna "posicion" de cada fila
for row in data2:
    peli.append(row[0]) 
    totalmax.append(row[1]) 
dataset2 = {
    'Pelicula': peli,
    'Ingreso total': totalmax
    }
df_max = pd.DataFrame(dataset2)
min_ingreso= df_max['Ingreso total'].max()
max_ingreso= df_max['Ingreso total'].min()

#Encontramos las peliculas con menor y mayor ingreso
pelicula_menor = df_max[df_max['Ingreso total']== min_ingreso]
pelicula_mayor = df_max[df_max['Ingreso total']== max_ingreso]

print(pelicula_menor)
print(pelicula_mayor)

#Vamos a conocer la productora de estas peliculas
# Nombre de la tabla
nombre_de_tabla = 'peliculas' 

# Ejecutar una consulta para conocer la productora de la pelicula con mayor ingreso
cursor.execute(f'SELECT * FROM {nombre_de_tabla} WHERE pelicula ="The Super Mario Bros. Movie";')
# Obtener todos los resultados de la consulta
dataMayor = cursor.fetchone()

studioMayor = dataMayor[6]

# PAra el menor
cursor.execute(f'SELECT * FROM {nombre_de_tabla} WHERE pelicula ="The Story of Film: A New Generation";')
# Obtener todos los resultados de la consulta
dataMenor = cursor.fetchone()

studioMenor = dataMenor[6]

print(studioMayor)
print(studioMenor)

# Identificamos que Universal pictures es la distribuidora que obtuvo el mayor ingreso con la pelicula The Super Mario Bros. Movie
# Identificamos que Universal pictures es la distribuidora que obtuvo el menor ingreso con la pelicula The Story of Film: A New Generation 