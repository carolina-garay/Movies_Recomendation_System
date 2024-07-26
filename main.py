# Importación de librerías necesarias
from fastapi import FastAPI, HTTPException
import pandas as pd
from typing import Optional

# Punto de partida para construir una aplicación web API
app = FastAPI(title="API de Películas", description="API para consultas sobre películas by Carolina Garay")

# Leer los archivos .parquet para el consumo de la API
df = pd.read_parquet("api_consult.parquet")

# Convertir la columna release_date a tipo datetime
df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')

# Ruta de inicio
@app.get("/")
async def index():
    return {"message": "¡Bienvenid@ a la API de Películas by Carolina Garay!"}

# Ruta de información
@app.get("/about")
async def about():
    return {"message": "Esta aplicación ha sido creada por Carolina Garay."}

# Ruta de cantidad de filmaciones para un determinado mes 
@app.get("/cantidad_peliculas_mes/{mes}", name="Cantidad de películas  (mes)")
async def cantidad_peliculas_mes(mes: str):
    '''Se ingresa el mes y la función retorna la cantidad de películas que se estrenaron ese mes históricamente.'''
    mes = mes.lower()
    meses = {
        'enero': 1, 'febrero': 2, 'marzo': 3, 'abril': 4,
        'mayo': 5, 'junio': 6, 'julio': 7, 'agosto': 8,
        'septiembre': 9, 'octubre': 10, 'noviembre': 11, 'diciembre': 12
    }
    if mes not in meses:
        raise HTTPException(status_code=400, detail=f"El mes {mes} no es válido")
    num_mes = meses[mes]
    cantidad = df[df['release_date'].dt.month == num_mes].shape[0]
    return f"En el mes de {mes} se estrenaron {cantidad} películas"

# Ruta de cantidad de filmaciones para un determinado día 
@app.get("/cantidad_peliculas_dia/{dia}", name="Cantidad de películas (día)")
async def cantidad_peliculas_dia(dia: str):
    '''Se ingresa el día y la función retorna la cantidad de películas que se estrenaron ese día históricamente.'''
    dia = dia.lower()
    dias = {
        'lunes': 0, 'martes': 1, 'miércoles': 2, 'jueves': 3,
        'viernes': 4, 'sábado': 5, 'domingo': 6
    }
    if dia not in dias:
        raise HTTPException(status_code=400, detail=f"El día {dia} no es válido")
    num_dia = dias[dia]
    cantidad = df[df['release_date'].dt.weekday == num_dia].shape[0]
    return f"En el día {dia} se estrenaron {cantidad} películas"

# Ruta de score por título
@app.get("/score_titulo/{titulo}", name="Score por título de película")
async def score_titulo(titulo: str):
    '''Se ingresa el título de una película y se retorna el título, el año de estreno y el score.'''
    pelicula = df[df['title'].str.contains(titulo, case=False, na=False)]
    if pelicula.empty:
        raise HTTPException(status_code=404, detail="Título no encontrado.")
    resultado = pelicula[['title', 'release_year', 'vote_average']].to_dict(orient='records')[0]
    return {"title": resultado['title'], "release_year": resultado['release_year'], "score": resultado['vote_average']}

# Ruta de votos por título
@app.get("/votos_titulo/{titulo}", name="Votos por título de película")
async def votos_titulo(titulo: str):
    '''Se ingresa el título de una película y se retorna el título, la cantidad de votos y el promedio de votaciones.'''
    pelicula = df[df['title'].str.contains(titulo, case=False, na=False)]
    if pelicula.empty:
        raise HTTPException(status_code=404, detail="Título no encontrado.")
    pelicula = pelicula.iloc[0]
    if pelicula['vote_count'] < 2000:
        return {"message": "La película no cumple con la condición de tener al menos 2000 valoraciones."}
    return {
        "title": pelicula['title'],
        "release_year": pelicula['release_year'],
        "vote_count": pelicula['vote_count'],
        "vote_average": pelicula['vote_average']
    }

# Ruta para obtener información de un actor
@app.get("/get_actor/{nombre_actor}", name="Información de actor")
async def get_actor(nombre_actor: str):
    '''Se ingresa el nombre de un actor y se retorna su éxito medido a través del retorno, cantidad de películas y promedio de retorno.'''
    actor_data = df[df['actors'].str.contains(nombre_actor, case=False, na=False)]
    if actor_data.empty:
        raise HTTPException(status_code=404, detail="Actor no encontrado.")
    total_retorno = actor_data['return'].sum()
    cantidad_peliculas = actor_data.shape[0]
    promedio_retorno = total_retorno / cantidad_peliculas if cantidad_peliculas > 0 else 0
    return {
        "actor": nombre_actor,
        "cantidad_peliculas": cantidad_peliculas,
        "total_retorno": total_retorno,
        "promedio_retorno": promedio_retorno
    }

# Ruta para obtener información de un director
@app.get("/get_director/{nombre_director}", name="Información de director")
async def get_director(nombre_director: str):
    '''Se ingresa el nombre de un director y se retorna su éxito medido a través del retorno, nombre de cada película, fecha de lanzamiento, retorno individual, costo y ganancia.'''
    director_data = df[df['director'].str.contains(nombre_director, case=False, na=False)]
    if director_data.empty:
        raise HTTPException(status_code=404, detail="Director no encontrado.")
    resultado = []
    for index, row in director_data.iterrows():
        resultado.append({
            "title": row['title'],
            "release_date": row['release_date'],
            "return": row['return'],
            "budget": row['budget'],
            "revenue": row['revenue']
        })
    total_retorno = director_data['return'].sum()
    return {
        "director": nombre_director,
        "total_retorno": total_retorno,
        "peliculas": resultado
    }
