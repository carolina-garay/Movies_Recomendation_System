

# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>
# <h1 align=center> **Carolina del Valle Garay** </h1>

# <h1 align=center>**`Machine Learning Operations (MLOps)`**</h1>

![MLops](assets/MLops.webp)

## ```Introducción```

¡Hola a tod@s! Estoy emocionada de presentarles mi primer proyecto individual de [Henry](https://www.soyhenry.com/), un sistema de recomendación de películas. Este proyecto combina mi pasión por la Matemática, la Programación y el Cine, utilizando técnicas de Ciencia de Datos y Machine Learning para ofrecer recomendaciones personalizadas.

Mi proyecto simula un ambiente de trabajo real en una _start-up_ que provee servicios de agregación de plataformas de streaming. Aquí he desarrollado una API que permite consultar información detallada sobre películas, actores y directores, así como obtener recomendaciones de películas basadas en diversos criterios como géneros, slogans, actores principales y directores. El objetivo principal es ayudar a los usuarios a descubrir nuevas películas que se alineen con sus gustos e intereses.

El sistema utiliza un enfoque de filtrado basado en contenido, donde se analiza el texto descriptivo de las películas y se calcula la similitud entre ellas. Para ello, he aplicado técnicas de procesamiento de lenguaje natural, como la vectorización TF-IDF, que transforma el texto en datos numéricos que pueden ser procesados por algoritmos de machine learning.

Además, el proyecto incluye una interfaz de usuario simple y amigable, donde se pueden hacer consultas específicas, como la cantidad de películas estrenadas en un mes determinado o el puntaje promedio de una película. También he incluido una sección para explorar el éxito de actores y directores, midiendo su impacto en términos de retorno financiero.

Este proyecto no sólo ha sido una excelente oportunidad para aplicar mis habilidades en programación y análisis de datos, sino que también me ha permitido explorar la intersección entre el entretenimiento y la tecnología. Espero que lo encuentren interesante y útil, y estoy ansiosa por recibir sus comentarios y sugerencias para seguir mejorando. ¡Gracias Henry por acompañarme en este viaje!



## :white_check_mark: ```Objetivo General```

- :pushpin: Implementar una API para acceso a datos y recomendaciones.

## :white_check_mark: ```Objetivos Específicos ```

- :pushpin: Realizar un preprocesamiento de datos (ETL)
- :pushpin: Realizar un análisis exploratorio de datos (EDA) 
- :pushpin: Crear endpoints de API que permitan consultas específicas y recomendaciones de películas


## :white_check_mark: ```Metodología de trabajo```

Para llevar a cabo los objetivos, se ejecutaron los siguientes procedimientos utilizando diversas herramientas:

-  :one: ${\color{red} \textbf{Google Drive}}$: se utilizó la cuenta de quien les escribe para almacenar el conjunto de datos de los datasets, ambos conjuntos se descargaron en el notebook ETL_Garay.ipynb

- :two: ${\color{red} \textbf{Visual Studio Code}}$: se utilizó este editor de código para crear un directorio con el nombre del proyecto y se implementó un entorno virtual de forma local. En este entorno se procedió a crear la API junto a los endpoints. Para la construcción de la Api se utilizó el framework de Python FastAPI.

Los endpoints desarrollados fueron: 

- ```def cantidad_peliculas_mes(mes)```: Se ingresa el mes en minúscula, por ejemplo abril, y la función retorna la cantidad de películas que se estrenaron en ese mes
    
        Formato de salida: En el mes de {mes} se estrenaron {cantidad} películas

- ```def cantidad_peliculas_dia(dia)```: Se ingresa el día en minúscula, por ejemplo sábado, y la función retorna la cantidad de películas que se estrenaron ese día
    

        Formato de salida: En el día {dia} se estrenaron {cantidad} películas

- ```def score_titulo(titulo)```: Se ingresa el título de una película, por ejemplo "Titanic", y se retorna el título, el año de estreno y el score.
    

        Formato de salida: "Título de la película": resultado['title'], "Año": resultado['release_year'], "Puntaje": resultado['vote_average']

- ```def votos_titulo(titulo)```: Se ingresa el título de una película, por ejemplo "Titanic", y se retorna el título, el año de estreno y el score.

        Formato de salida: {
                'Título de la película': titulo, 
                 'Año': year_es, 
                 'Voto total': voto_tot, 
                 'Voto promedio': voto_prom
                                  }

- ```def get_actor(nombre_actor)```: Se ingresa el nombre de un actor, por ejemplo "Tom Hanks" y se retorna su éxito medido a través del retorno, cantidad de películas y promedio de retorno.
    

        Formato de salida: {
        "Actor/Actriz": nombre_actor,
        "Cantidad de películas": cantidad_peliculas,
        "Retorno Total": total_retorno,
        "Retorno Promedio": promedio_retorno}

- ```def get_director(nombre_director)```: Se ingresa el nombre de un director y se retorna su éxito medido a través del retorno, nombre de cada película, fecha de lanzamiento, retorno individual, costo y ganancia.
    
        Formato de salida: {
        "Director": nombre_director,
        "Retorno Total": total_retorno,
        "Películas": resultado}
        {
            "Título de la película":   ,
            "Fecha de lanzamiento":    ,
            "Retorno":      ,
            "Presupuesto":   ,
            "Ganancia":    }

Estos endpoints permitirán que los empleados de la empresa puedan hacer solicitudes específicas a la API para obtener información valiosa o realizar acciones específicas.
- :three: ${\color{red} \textbf{Google Colaboratory}}$: Se utilizó esta plataforma para el desarrollo de los procesos ETL, EDA y Modelo de Machine Learning. 
    - **ETL:** se realizó limpieza y transformación de los datos para garantizar la calidad y consistencia de la información utilizada en el sistema de recomendación. El resultado del jupyter notebook (ETL_Garay.ipynb) desarrolado para esta etapa corresponde al conjunto de datos que se utilizó para alimentar a la Api, se lo descargó en formato parquet con el nombre  api_consult.parquet.
    - **EDA:** este análisis se realizó con la finalidad de identificar patrones, tendencias y relaciones en los datos, así como detectar posibles outliers y anomalías. Dicho análisis posibilitó decidir cuáles atributos eran los adecuados para aplicar el Modelo de Machine Learning. El resultado del jupyter notebook (EDA_Garay.ipynb) desarrolado para esta etapa corresponde al conjunto de datos que se utilizó para aplicar el modelo seleccionado.
    - **Modelo de Machine Learning (ML):** para el modelado se seleccionaron TF-IDF (Term Frequency-Inverse Document Frequency) y la similitud del coseno. Estas son dos técnicas fundamentales que se utilizan en procesamiento de lenguaje natural (NLP) para medir la relevancia de términos en documentos y para calcular la similitud entre ellos. Los distintos modelos aplicados se encuentran en el notebook ML_Garay.ipynb. Se eligió el modelo que responda al siguiente endpoint: 
       - def recomendacion(titulo)```: Se ingresa el título de una película, por ejemplo "Avatar", y devuelve 5 recomendaciones.
    

                Formato de salida: ['titulo_recomendado1', 'titulo_recomendado2', 'titulo_recomendado3', 'titulo_recomendado4', 'titulo_recomendado5']
    


Todas las tareas realizadas se encuentran en la carpeta ETL_EDA_ML_Garay. Para ejecutar cada notebook se sugiere descargarlo y luego subir cada uno a Google Colaboratory.

- :four: ${\color{red} \textbf{Github}}$: se usó esta plataforma para almacenar el proyecto. Se creó un repositorió con el nombre **Movies_Recomendation_System**. Este paso es imprescindible para deployar la Api en render, dado que se utiliza la dirección del repositorio para realizar el deploy. Cada cambio realizado a nivel local se iba actualizando en el repositorio

- :five: ${\color{red} \textbf{Render}}$: se utilizó este sitio para desplegar el proyecto. Primeramente se creó una cuenta en el sitio y luego se conectó con el repositorio de Github donde se encuentra alojado el proyecto. Se tuvo que tener mucho cuidado al elegir el ML ya que render tiene un límite de memoria de 512 Mb.




## :white_check_mark: :sparkles: ```Deployment de la Api``` :sparkles:
 Para realizar consultas y recomendaciones de películas dirigirse a la siguiente dirección: [carolina_Garay_Movies_Recomendation_System](https://movies-recomendation-system-2.onrender.com/docs)




## :white_check_mark: ```Video```
