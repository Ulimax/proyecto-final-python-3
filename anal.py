import sqlite3

# Conectarse a la base de datos SQLite
conn = sqlite3.connect('films.db')
cursor = conn.cursor()

# Nombre de la tabla
nombre_de_tabla = 'peliculas' 

# Ejecutar una consulta para obtener los datos de la tabla
cursor.execute(f'SELECT * FROM {nombre_de_tabla} WHERE posicion = 3')

# Obtener todos los resultados de la consulta
data = cursor.fetchall()

# Cerrar la conexión a la base de datos
conn.close()

peliculas3 = []
total3 = []
# Imprimir la columna "posicion" de cada fila
for row in data:
    peliculas3.append(row[2]) 
    total3.append(row[5]) 
print(peliculas3)
print(total3)

