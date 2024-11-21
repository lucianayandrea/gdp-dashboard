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
    Convierte una secuencia de ADN en ARN, reemplazando la Timina (T) por Uracilo (U).
    """
    # Diccionario de sustituciones de ADN a ARN
    transcripcion = {'A': 'A', 'T': 'U', 'G': 'G', 'C': 'C'}
    
    arn = ''
    for base in adn:
        if base in transcripcion:
            arn += transcripcion[base]
        else:
            return None  # Si hay un carácter no válido, retornamos None
    
    return arn

# Título de la aplicación
st.title("Transcripción de ADN a ARN")

# Descripción de la aplicación
st.write("""
    Esta aplicación convierte una secuencia de ADN en ARN mensajero (ARNm).
    En el proceso de transcripción, la base Timina (T) del ADN se reemplaza por Uracilo (U) en el ARN.
    Si introduces un carácter no válido, te mostraremos un mensaje de error.
""")

# Ejemplo de secuencia de ADN humana
adn_ejemplo = "ATGAGTGGCGTGGCGGTCCAGGAGGAGCTCAGGAGGAGGAGGAGGAGGAGGAGGAGGAGGAGGAGGAGGAGGAGGAGGAGGAGGA"
st.write("Ejemplo de secuencia de ADN:")
st.code(adn_ejemplo)

# Entrada de texto para que el usuario ingrese su propia secuencia de ADN
adn_usuario = st.text_input("Introduce tu secuencia de ADN (solo A, T, G, C):", "")

# Verifica si el usuario ha presionado el botón de transcripción
if st.button("Transcribir ADN a ARN"):
    if adn_usuario:
        # Convertimos la secuencia de ADN a mayúsculas para evitar problemas de formato
        adn_usuario = adn_usuario.upper()

        # Validar que la secuencia contiene solo caracteres válidos
        if all(base in 'ATGC' for base in adn_usuario):
            # Llamamos a la función de transcripción
            arn_resultado = transcribir_adn_a_arn(adn_usuario)
            
            if arn_resultado:
                st.success(f"La secuencia de ARN transcrita es: {arn_resultado}")
            else:
                st.error("Hubo un error en la transcripción. Asegúrate de que la secuencia de ADN esté correcta.")
        else:
            st.error("La secuencia de ADN contiene caracteres no válidos. Solo se permiten A, T, G y C.")
    else:
        st.warning("Por favor, ingresa una secuencia de ADN.")


import streamlit as st

# Función para dividir la secuencia de ARN en codones (tripletas de bases)
def dividir_en_codones(arn):
    """
    Toma una secuencia de ARN y la divide en codones (tripletas de bases).
    Devuelve una lista de codones.
    """
    codones = []
    for i in range(0, len(arn), 3):  # Dividimos el ARN en fragmentos de 3 bases
        codon = arn[i:i+3]
        # Aseguramos que cada codón tenga exactamente 3 bases
        if len(codon) == 3:
            codones.append(codon)
    return codones

# Título de la aplicación
st.title("Transcripción de ARN a Codones")

# Descripción de la aplicación
st.write("""
    Esta aplicación toma una secuencia de ARN y la divide en codones (tripletas de bases).
    Un codón es un conjunto de tres nucleótidos que codifica un aminoácido.
    Si introduces un carácter no válido, te mostraremos un mensaje de error.
""")

# Entrada de texto para que el usuario ingrese una secuencia de ARN
arn = st.text_input("Introduce la secuencia de ARN (solo A, U, G, C):", "")

# Verifica si el usuario ha presionado el botón de transcripción
if st.button("Dividir en Codones"):
    if arn:
        # Convertimos la secuencia de ARN a mayúsculas para evitar problemas de formato
        arn = arn.upper()

        # Comprobar que la secuencia solo contiene bases válidas de ARN (A, U, C, G)
        if all(base in 'AUGC' for base in arn):
            # Llamamos a la función para dividir el ARN en codones
            codones = dividir_en_codones(arn)
            
            # Mostrar la lista de codones
            if codones:
                st.success(f"Codones obtenidos: {', '.join(codones)}")
            else:
                st.warning("La secuencia de ARN es demasiado corta para obtener codones válidos.")
        else:
            st.error("La secuencia de ARN contiene bases inválidas. Solo se permiten A, U, G y C.")
    else:
        st.warning("Por favor, ingresa una secuencia de ARN.")

  


