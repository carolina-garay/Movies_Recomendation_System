

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


## 💡```Metodología de trabajo```

Para llevar a cabo los objetivos, se ejecutaron los siguientes procedimientos utilizando diversas herramientas:

-  :one: <font color='green'>Google Drive: se utilizó la cuenta de quien les escribe para almacenar el conjunto de datos de los datasets, ambos conjuntos se descargaron en el notebook ETL_Garay.ipynb

- :two: <font color='green'>Visual Studio Code: se utilizó este editor de código para crear un directorio con el nombre del proyecto y se implementó un entorno virtual de forma local. En este entorno se procedió a crear la API junto a los end point ‘/’.
- :three: <font color='green'>Google Colaboratory: Se utilizó esta plataforma para el desarrollo de los procesos ETL, EDA y Modelo de Machine Learning. 
    - **ETL:** se realizó limpieza y transformación de los datos para garantizar la calidad y consistencia de la información utilizada en el sistema de recomendación. El resultado del jupyter notebook (ETL_Garay.ipynb) desarrolado para esta etapa corresponde al conjunto de datos que se utilizó para alimentar a la Api, se lo descargó en formato parquet con el nombre  api_consult.parquet.
    - **EDA:** este análisis se realizó con la finalidad de identificar patrones, tendencias y relaciones en los datos, así como detectar posibles outliers y anomalías. Dicho análisis posibilitó decidir cuáles atributos eran los adecuados para aplicar el Modelo de Machine Learning. El resultado del jupyter notebook (EDA_Garay.ipynb) desarrolado para esta etapa corresponde al conjunto de datos que se utilizó para aplicar el modelo seleccionado.
    - **Modelo de Machine Learning:** para el modelado se seleccionaron TF-IDF (Term Frequency-Inverse Document Frequency) y la similitud del coseno. Estas son dos técnicas fundamentales que se utilizan en procesamiento de lenguaje natural (NLP) para medir la relevancia de términos en documentos y para calcular la similitud entre ellos. Los distintos modelos aplicados se encuentran en el notebook ML_Garay.ipynb

Todas las tareas realizadas se encuentran en la carpeta ETL_EDA_ML_Garay. Para ejecutar cada notebook se sugiere descargarlo y luego subir cada uno a Google Colaboratory.

- :four: <font color='green'>Github: se usó esta plataforma para almacenar el proyecto. Se creó un repositorió con el nombre **Movies_Recomendation_System**. Este paso es imprescindible para deployar la Api en render, dado que se utiliza la dirección del repositorio para realizar el deploy.

- :five: <font color='green'>Render: se utilizó este sitio para desplegar el proyecto. Primeramente se creó una cuenta en el sitio <p style="color: red;">Esta es una oración coloreada en rojo.</p>


