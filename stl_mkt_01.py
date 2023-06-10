from email import header
import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

st.set_page_config(page_title='Intro', page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)

SCREEN_GRID_LAYER_DATA = (
    "https://raw.githubusercontent.com/visgl/deck.gl-data/master/website/sf-bike-parking.json"  # noqa
)
df = pd.read_json(SCREEN_GRID_LAYER_DATA)
from PIL import Image

image = Image.open('mkt_mapa.jpeg')

st.image(image, caption='Locations of bike parking within San Francisco. Aggregation level varies depending on the viewport of the user.', width=1200)
#st.image("./mkt_mapa.png")

st.markdown("## Introducción al Análisis de Datos con Streamlit de Python")

"""
¡Atención a todos los apasionados del análisis de datos y la visualización! 📊📈

¿Quieres llevar tus habilidades de análisis al siguiente nivel? ¡Tenemos el curso perfecto para ti! 

Únete a nuestro exclusivo curso de análisis de datos utilizando Python y Streamlit y descubre un mundo de posibilidades para visualizar tus datos de manera impactante y efectiva.

¿Por qué deberías elegir Python y Streamlit para tus proyectos de análisis de datos? ¡Déjame contarte todas las ventajas! 🚀

1️⃣ Python es uno de los lenguajes de programación más populares en el ámbito del análisis de datos. Con su sintaxis sencilla y poderosa, 
podrás manipular, limpiar y procesar tus conjuntos de datos de forma eficiente. Además, su amplia variedad de librerías especializadas, como Pandas, NumPy y Plotly, 
te permitirán realizar análisis estadísticos avanzados y generar visualizaciones de alta calidad.

2️⃣ Streamlit es una biblioteca de Python que facilita la creación de aplicaciones web interactivas para visualizar datos. 
¿Te imaginas tener un panel de control (*dashboard*) donde tus clientes o colegas puedan explorar y analizar los datos de manera intuitiva? 


### Visualización de datos.

Con Streamlit, podrás crear tableros interactivos y amigables en poco tiempo, sin necesidad de conocimientos avanzados de programación web.

En un mundo cada vez más inundado de información, saber comunicar tus hallazgos de manera clara y visualmente atractiva es fundamental. 

Con nuestro curso, aprenderás a generar gráficas de dispersión que revelen patrones ocultos, gráficas de sectores para resaltar proporciones, 
*heatmaps* para identificar correlaciones, *KPIs* para medir el rendimiento, tableros para presentar tus resultados de manera efectiva y mapas para visualizar datos geográficos.

Este curso ha sido diseñado para que puedas adquirir habilidades prácticas y aplicables de inmediato. 

Aprenderás de casos de estudio reales y recibirás retroalimentación personalizada para asegurarte de que obtengas el máximo provecho de tu experiencia de aprendizaje.

¡No pierdas la oportunidad de destacarte en el competitivo mundo del análisis de datos! Regístrate ahora en nuestro curso de análisis de datos utilizando Python y 
Streamlit y prepárate para convertirte en un experto en visualización de datos. ¡Asegura tu lugar hoy mismo y desata todo tu potencial!

Para más información y para inscribirte, envíame un correo a *randradedev@gmail.com* y te responderé con un documento que te explicará como inscribirte al curso. ¡Te espero para comenzar esta emocionante aventura juntos!

¡Los datos nunca han sido tan emocionantes! 📊✨
"""

"""
### Podrás generar un mapa como el que se muestra a continuación.

¡Arrastra el mapa con el *mouse* para interactuar con él!
"""
# Define a layer to display on a map
layer = pdk.Layer(
    "ScreenGridLayer",
    df,
    pickable=False,
    opacity=0.8,
    cell_size_pixels=30,
    color_range=[
        [0, 25, 0, 25],
        [0, 85, 0, 85],
        [0, 127, 0, 127],
        [0, 170, 0, 170],
        [0, 190, 0, 190],
        [0, 255, 0, 255],
    ],
    get_position="COORDINATES",
    get_weight="SPACES",
)

# Set the viewport location
view_state = pdk.ViewState(latitude=37.7749295, longitude=-122.4194155, zoom=12, bearing=0, pitch=0)
r = pdk.Deck(layers=[layer], initial_view_state=view_state)
# Render
st.pydeck_chart(pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v10",
        initial_view_state=view_state,
        layers=[layer]
    ))

"""
## *Chart Elements*

También podrás construir gráficos de varios tipos.

Por ejemplo, para crear el primer gráfico mostrado a continuación, tomamos datos al azar y sentencias de Python y Streamlit muy cortas y sencillas.
"""

body = """
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)
"""
st.code(body, language="python")


col1, col2, col3 = st.columns(3)

with col1:
    st.header("Gráfico de líneas")
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])
   
    st.line_chart(chart_data)

with col2:
    st.header("Gráfico de área")
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])
    st.area_chart(chart_data)

with col3:
    st.header("Gráfico de barras")
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=["a", "b", "c"])
    st.bar_chart(chart_data)

"""
### Temario
1. Introducción.
2. Creación del ambiente de desarrollo.
3. Funciones básicas de Streamlit.
4. ¿Qué es el análisis de datos?
5. Un poco de Pandas.
6. Tipos de gráficos.
7. Objetos de entrada (*input widgets*).
8. Visualización de datos geográficos.
9. *Outliers*, *boxplots*.
10. *Dashboard* sencillo.
11. Regresión lineal.
12. Análisis Exploratorio de Datos (*EDA*)
13. Análisis de ventas.
14. Mapas base de Mapbox.
15. Mapas interactivos con *pydeck library*.

### Conjuntos de datos a analizar
- Disturbios en Los Ángeles, Cal,
- Análisis de Accidentes de Tránsito en la CDMX
- *Marketing Data*
- Ventas al menudeo. Series de Tiempo.
- DENUE de INEGI
- AirBnB de la CDMX. Geodatos.

### Fecha y horario.
19 al 28 de junio de 2023

17 a 19 horas.

Vía Google Meet.

### Inversión
"""
new_title = '<p style="color:Brown; font-size: 17px;">$1,200 MX</p>'
st.markdown(new_title, unsafe_allow_html=True)

"""
### Informes para inscripción

Envía un correo electrónico a randradedev@gmail.com para obtener más detalles sobre el curso y 
la manera de inscribirte al curso.

### Herramientas
Para desarrollar este sitio web se usaron las siguientes bibliotecas de Python:
- Streamlit
- Pandas
- Plotly
- Numpy y
- pydeck.

### Datos
Se usó el conjunto de datos (*dataset*)de estacionamiento de bicicletas de San Francisco, Cal., USA., en formato JSON:

https://github.com/visgl/deck.gl/blob/master/examples/layer-browser/data/sf.bike.parking.json

### Ponente

**Roberto Andrade F.**
- Analista de Datos,
- DBA,
- Instructor de PostgreSQL,
- Profesor de la Maestría en Alta dirección de la FQ de la UNAM.

"""

