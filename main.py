
# Creación de un panel de administracion mediante FastAPI
# %%
import sqlite3 # Importacion de sqlite
from fastapi import FastAPI # importacion de fastapi
from pydantic import BaseModel # importacion de basemodel

# %%
# creamos un objeto 
class Item(BaseModel):
    posicion: str
    pelicula: str
    bruto: int
    release: str
    total: int           
    studio: str             

app = FastAPI()

# %%
@app.post("/agregar_elemento/") # definimos la url en la que se agrearan los nuevos elementos de la base
async def agregar_elemento(item: Item):
    conn = sqlite3.connect("films.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO peliculas (posicion, pelicula, bruto, release, total, studio) VALUES (?, ?, ?, ?, ?, ?)", (item.posicion, item.pelicula, item.bruto, item.release, item.total, item.studio))
    conn.commit()
    conn.close()
    return {"mensaje": "Datos agregados exitosamente"}

# %%
@app.get("/leer_elementos/")
async def leer_elementos():
    conn = sqlite3.connect("films.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM peliculas")
    resultados = cursor.fetchall()
    conn.close()
    if resultados:
        return [{"Posicion": resultado[0], "Pelicula": resultado[1], "Ingreso Bruto": resultado[2], "Fecha de estreno": f"{resultado[3]} / 2023"
                  , "Ingreso total": resultado[4], "Distribuidora": resultado[5]} for resultado in resultados]
    else:
        return {"mensaje": "No hay datos en la base de datos"}

# %%
@app.get("/leer_elemento/{id}/")
async def leer_elemento(id: int):
    conn = sqlite3.connect("films.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM peliculas WHERE id=?", (id,))
    resultado = cursor.fetchone()
    conn.close()
    if resultado is not None:
        return {"Posicion": resultado[0], "Pelicula": resultado[1], "Ingreso Bruto": resultado[2], "Fecha de estreno": f"{resultado[3]} / 2023"
                  , "Ingreso total": resultado[4], "Distribuidora": resultado[5]}
    else:
        return {"mensaje": "Datos no encontrados"}

# %%
@app.put("/actualizar_elemento/{id}/")
async def actualizar_elemento(id: int, item: Item):
    conn = sqlite3.connect("films.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE peliculas SET posicion=?, pelicula=?, bruto=? , total=? , studio=? , bruto=? WHERE id=?", (item.posicion, item.pelicula, item.bruto, item.release, item.total, item.studio, id))
    conn.commit()
    conn.close()
    return {"mensaje": "Datos actualizados exitosamente"}

# %%
@app.delete("/eliminar_elemento/{id}/")
async def eliminar_elemento(id: int):
    conn = sqlite3.connect("films.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM peliculas WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return {"mensaje": "Datos eliminados exitosamente"}

# %%
