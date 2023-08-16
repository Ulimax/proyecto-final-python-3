import sqlite3
import csv

# Conectarse a la base de datos SQLite
conn = sqlite3.connect('films.db')
cursor = conn.cursor()

# Nombre de la tabla
nombre_de_tabla = 'peliculas' 

# Ejecutar una consulta para obtener los datos de la tabla
cursor.execute(f'SELECT * FROM {nombre_de_tabla}')

# Obtener todos los resultados de la consulta
data = cursor.fetchall()

# Obtener los nombres de las columnas
columns = [description[0] for description in cursor.description]

# Cerrar la conexión a la base de datos
conn.close()

# Escribir los datos en un archivo CSV
with open('export.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    # Escribir encabezados de columna
    csv_writer.writerow(columns)
    # Escribir datos
    csv_writer.writerows(data)