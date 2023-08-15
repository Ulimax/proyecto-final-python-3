# %%
import sqlite3
import csv

def create_film_table():   # definimos una funcion que nos crea la base de datos y el esqueleto de esta
    conn = sqlite3.connect("films.db") # Creamos la base de daros films y nos conectamos a ella
    cursor = conn.cursor()            # instanciamos un cursor

    cursor.execute("""CREATE TABLE IF NOT EXISTS peliculas(
                   id INTEGER PRIMARY KEY,
                   posicion TEXT NOT NULL,
                   pelicula TEXT NOT NULL,
                   bruto INTEGER NOT NULL,
                   release TEXT NOT NULL,
                   total INTEGER NOT NULL,
                   studio  TEXT NOT NULL
                   )
                   """) # Creamos la tabla que contendra las peliculas
    
    conn.commit()
    conn.close()


# %%
def read_csv_file(csv_file):     # Funcion para la lectura de archivos csv
    with open(csv_file, newline='') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data

def insert_data_to_ranking_table(data): # Funcion para la insercion de datos en la base de datos
    conn = sqlite3.connect("films.db")
    cursor = conn.cursor()

    for row in data:
        cursor.execute("""
            INSERT INTO peliculas (posicion, pelicula, bruto, release, total, studio )
            VALUES (?, ?, ?, ?, ?, ?)
        """, (row["Posicion"], row["Pelicula"], int(row["Ingreso Bruto"]), row["Fecha de estreno"], int(row["Ingreso Total"]), row["Distribuidora"]))

    conn.commit()
    conn.close()


# %%
if __name__ == "__main__":  # Creamos la base de datos
    create_film_table()
# %%
# %%

if __name__ == "__main__":
    año="2023"
    meses = ["january", "february", "march", "april", "may", "june", "july", "august"]
    for mes in meses:
        csv_file = f"data/Taquilleras-{mes}-{año}.csv" # Nombre del archivo csv que contiene los datos
        data_to_insert = read_csv_file(csv_file)
        insert_data_to_ranking_table(data_to_insert)



# %%
