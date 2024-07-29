# Importación de librerías necesarias
from fastapi import FastAPI, HTTPException
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from typing import Optional

# Punto de partida para construir una aplicación web API
app = FastAPI(title="Películas...hacé tu consulta!", description="API para consultas sobre películas by Carolina Garay",
               docs_url="/docs")

# Leer los archivos .parquet para el consumo de la API
df = pd.read_parquet("api_consult.parquet")
model1 = pd.read_parquet("movies_model.parquet")


# Ruta de inicio
@app.get("/")
async def index():
    return "¡Bienvenid@ a la API de Películas by Carolina Garay!"

# Ruta de información
@app.get("/about")
async def about():
    return "Esta aplicación ha sido creada por Carolina Garay"

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
    return {"Título de la película": resultado['title'], "Año": resultado['release_year'], "Puntaje": resultado['vote_average']}

# Ruta de votos por título
@app.get("/votos_titulo/{titulo}", name="Votos por título de película")
async def votos_titulo(titulo: str):
    '''Se ingresa el título de una película y se retorna el título, la cantidad de votos y el promedio de votaciones.'''
    pelicula = df[df['title'].str.contains(titulo, case=False, na=False)]
    if pelicula.empty:
        raise HTTPException(status_code=404, detail="Título no encontrado.")
    else:
        year_es = int(pelicula["release_year"].iloc[0])
        voto_tot = int(pelicula["vote_count"].iloc[0])
        voto_prom = pelicula["vote_average"].iloc[0]
        # Retornar el nombre del titulo ubicado en la columna title
        titulo = pelicula["title"].iloc[0]
        if voto_tot >= 2000:
            # muestra los datos
            return {
                'Título de la película': titulo, 
                 'Año': year_es, 
                 'Voto total': voto_tot, 
                 'Voto promedio': voto_prom
            }
        else:
            # En caso de que la cantidad de votos sea menor a 2000
            return f"La película {titulo} no cumple con la condición de tener al menos 2000 valoraciones "
        

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
        "Actor/Actriz": nombre_actor,
        "Cantidad de películas": cantidad_peliculas,
        "Retorno Total": total_retorno,
        "Retorno Promedio": promedio_retorno
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
            "Título de la película": row['title'],
            "Fecha de lanzamiento": row['release_date'],
            "Retorno": row['return'],
            "Presupuesto": row['budget'],
            "Ganancia": row['revenue']
        })
    total_retorno = director_data['return'].sum()
    return {
        "Director": nombre_director,
        "Retorno Total": total_retorno,
        "Películas": resultado
    }


#Machine Learning
# Crear una instancia de TfidfVectorizer con los parámetros deseados
tfidf_1 = TfidfVectorizer(stop_words="english", ngram_range=(1, 2))
# Se manejan los valores nan
model1['overview'] = model1['overview'].fillna('') # Replace None with empty strings
# Aplicar la transformación TF-IDF al atributo 'overview'
tfidf_matriz_1 = tfidf_1.fit_transform(model1['overview'])


# Ruta de recomendación de peliculas
# Función para obtener recomendaciones
@app.get('/recomendacion_m1/{titulo}', name = "Sistema de recomendación")
def recomendacion_m1(titulo):
    # Crear un objeto 'indices' que mapea los títulos de las películas a sus índices correspondientes en el DataFrame 'model1'
    indices = pd.Series(model1.index, index=model1['title']).drop_duplicates()
    if titulo not in indices:
        return 'La pelicula ingresada no se encuentra en la base de datos'
    else:
        # Obtener el índice de la película que coincide con el título
        idx = pd.Series(indices[titulo]) if titulo in indices else None
        # Si el título de la película está duplicado, devolver el índice de la primera aparición del título en el DataFrame
        if model1.duplicated(['title']).any():
            primer_idx = model1[model1['title'] == titulo].index[0]
            if not idx.equals(pd.Series(primer_idx)):
                idx = pd.Series(primer_idx)
        # Calcular la similitud coseno entre la película de entrada y todas las demás películas en la matriz de características
        cosine_sim = cosine_similarity(tfidf_matriz_1[idx], tfidf_matriz_1).flatten()
        simil = sorted(enumerate(cosine_sim), key=lambda x: x[1], reverse=True)[1:6]
        # Verificar que los índices obtenidos son válidos
        valid_indices = [i[0] for i in simil if i[0] < len(model1)]
         # Obtener los títulos de las películas más similares utilizando el índice de cada película
        recomendaciones = model1.iloc[valid_indices]['title'].tolist()
        # Devolver la lista de títulos de las películas recomendadas
        return recomendaciones
