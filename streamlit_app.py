import streamlit as st
import pandas as pd
import math
from pathlib import Path
import pandas as pd
import streamlit as st

# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='Proyecto Bioinformatica',
    page_icon=':earth_world:', # This is an emoji shortcode. Could be a URL too.
)

# -----------------------------------------------------------------------------
# Declare some useful functions.

@st.cache_data
def get_gdp_data():
    """Grab GDP data from a CSV file.

    This uses caching to avoid having to read the file every time. If we were
    reading from an HTTP endpoint instead of a file, it's a good idea to set
    a maximum age to the cache with the TTL argument: @st.cache_data(ttl='1d')
    """

    # Instead of a CSV on disk, you could read from an HTTP endpoint here too.
    DATA_FILENAME = Path(__file__).parent/'data/gdp_data.csv'
    raw_gdp_df = pd.read_csv(DATA_FILENAME)

    MIN_YEAR = 1960
    MAX_YEAR = 2022

    # The data above has columns like:
    # - Country Name
    # - Country Code
    # - [Stuff I don't care about]
    # - GDP for 1960
    # - GDP for 1961
    # - GDP for 1962
    # - ...
    # - GDP for 2022
    #
    # ...but I want this instead:
    # - Country Name
    # - Country Code
    # - Year
    # - GDP
    #
    # So let's pivot all those year-columns into two: Year and GDP
    gdp_df = raw_gdp_df.melt(
        ['Country Code'],
        [str(x) for x in range(MIN_YEAR, MAX_YEAR + 1)],
        'Year',
        'GDP',
    )

    # Convert years from string to integers
    gdp_df['Year'] = pd.to_numeric(gdp_df['Year'])

    return gdp_df

gdp_df = get_gdp_data()

# -----------------------------------------------------------------------------
# Draw the actual page

# Set the title that appears at the top of the page.
'''
# 🦾🧬 Transcriptor ADN, ARN y Proteinas


La bioinformática es una disciplina interdisciplinaria que emplea técnicas computacionales y estadisticas 
para resolver problemas biologicos, especialmente aquellos relacionados con la biologia molecular y genética 
Una de las tareas fundamentales en el ámbito de la bioinformatica es la comprensión y manipulación de secuencias biológicas 
como las del ADN,ARN y proteinas. En este contexto, la traduccion de ADN representa un un proceso clave dento de la 
expresion genética contenida en el ADN es convertida en proteinas funcionales, a través de la intermediación del ARN mensajero.
'''

import streamlit as st

# Función para transcribir ADN a ARN
def transcribir_adn_a_arn(adn):
    """
    Transcribe una secuencia de ADN a ARN.
    Reemplaza las bases de ADN con las correspondientes bases de ARN:
    - A -> U
    - T -> A
    - C -> G
    - G -> C
    """
    # Diccionario que mapea las bases de ADN a ARN
    transcripcion = {'A': 'U', 'T': 'A', 'C': 'G', 'G': 'C'}
    
    # Se recorre la secuencia de ADN y se convierte a ARN
    arn = ''.join([transcripcion.get(base, '') for base in adn.upper()])
    
    # Retorna la secuencia de ARN
    return arn

# Título de la aplicación
st.title("Transcripción de ADN a ARN")

# Descripción breve de la aplicación
st.write("""
    Este es un sencillo transcriptor de ADN a ARN. 
    Introduce una secuencia de ADN (solo letras A, T, C, G) y obtén su secuencia de ARN correspondiente.
""")

# Entrada de texto para que el usuario introduzca una secuencia de ADN
adn = st.text_input("Introduce la secuencia de ADN:", "")

# Verifica si el usuario ha hecho clic en el botón de transcripción
if st.button("Transcribir"):
    # Si el usuario introdujo algo en el campo de texto
    if adn:
        # Llamamos a la función para transcribir ADN a ARN
        arn = transcribir_adn_a_arn(adn)
        
        # Si se obtuvo una secuencia de ARN válida, mostramos el resultado
        if arn:
            st.success(f"Secuencia de ARN resultante: {arn}")
        else:
            st.error("La secuencia de ADN contiene caracteres inválidos. Solo se permiten A, T, C, G.")
    else:
        st.warning("Por favor, introduce una secuencia de ADN.")
