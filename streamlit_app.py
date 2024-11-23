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
import streamlit as st

import streamlit as st
import random


# Personalización de la página
st.markdown(
    """
    <style>
    body {
        background-color: #d4f7d4;  /* Fondo verde claro */
        font-family: 'Arial', sans-serif;
    }

    /* Estilos para los títulos */
    h1, h2, h3 {
        color: #2e8b57;  /* Verde oscuro */
        text-align: center;
    }

    /* Agregar decoración con imágenes de ADN */
    .dna-decoration {
        text-align: center;
        margin-top: 20px;
    }

    .dna-decoration img {
        width: 50%;
        max-width: 300px;
        margin: 10px;
    }

    .content {
        text-align: center;
        padding: 20px;
        background-color: #ffffff;  /* Fondo blanco para el contenido */
        border-radius: 10px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        margin-top: 30px;
    }

    .button {
        background-color: #2e8b57;
        color: white;
        padding: 10px 20px;
        border-radius: 5px;
        border: none;
        cursor: pointer;
        font-size: 18px;
    }

    .button:hover {
        background-color: #1f5e3f;
    }
    </style>
    """, unsafe_allow_html=True
)

# Título de la página
st.title("Dashboard de Bioinformática")

# Sección de bienvenida
st.write("""
Bienvenido al **Dashboard de Bioinformática**. Este es un entorno interactivo donde exploramos la ciencia de los datos biológicos.
Aquí podrás realizar diversos análisis y visualizar resultados de manera intuitiva. ¡Diviértete explorando el mundo de la genética y el ADN!
""")

# Decoración con imágenes de ADN
https://i.sstatic.net/GRxg2.png

# Lista de proteínas, sus descripciones y URLs de imágenes representativas
proteinas = [
    {
        "nombre": "Hemoglobina",
        "descripcion": "La hemoglobina es una proteína encargada de transportar oxígeno en la sangre.",
        "imagen": "https://lh5.googleusercontent.com/proxy/wyReeTVsruQXaURzd6CJhJOjXJu84_OLYd0qckp1Itge6VdPpg0l3eXNEB6krK7pOF5H1qWgqw5QlHXoTZLuE9gQPCluHw-Z5SsqoHyMl1ir31WQIZvyxZqjdFG27ZM"
    },
    {
        "nombre": "Quimotripsina",
        "descripcion": "La quimotripsina es una enzima digestiva que ayuda a descomponer proteínas en el intestino.",
        "imagen": "https://upload.wikimedia.org/wikipedia/commons/5/52/Chymotrypsin.svg"
    },
    {
        "nombre": "Dinamina",
        "descripcion": "La dinamina es una proteína involucrada en la fisión de vesículas intracelulares.",
        "imagen": "https://upload.wikimedia.org/wikipedia/commons/6/67/Dynamin.png"
    },
    {
        "nombre": "Colágeno",
        "descripcion": "El colágeno es una proteína estructural que proporciona soporte a los tejidos conectivos.",
        "imagen": "https://e7.pngegg.com/pngimages/1019/883/png-clipart-collagen-type-viii-alpha-1-collagen-type-viii-alpha-2-alpha-collagen-protein-alpha-viii.png"
    },
    {
        "nombre": "Actina",
        "descripcion": "La actina es una proteína involucrada en la contracción muscular y en la forma celular.",
        "imagen": "https://upload.wikimedia.org/wikipedia/commons/3/32/Actin_structure.png"
    }
]

# Función para mostrar la proteína aleatoria
def mostrar_proteina_aleatoria():
    proteina = random.choice(proteinas)
    st.markdown(f"### {proteina['nombre']}")
    st.write(proteina['descripcion'])
    st.image(proteina['imagen'], caption=proteina['nombre'], use_column_width=True)

# Sección para el botón de análisis
st.markdown("""
<div class="content">
    <h2>¡Explora el ADN y la Genética!</h2>
    <p>Haz clic en el siguiente botón para descubrir una nueva proteína y su información.</p>
</div>
""", unsafe_allow_html=True)

# Crear el botón para mostrar una proteína aleatoria
if st.button("Iniciar Análisis"):
    mostrar_proteina_aleatoria()

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
    transcripcion = {'A': 'A', 'T': 'U', 'G': 'C', 'C': 'G'}
    
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
    Aqui se convierte una secuencia de ADN a ARN.
    
    En el proceso de transcripción, la base Timina (T) del ADN se reemplaza por Uracilo (U) en el ARN.
""")

# Ejemplo de secuencia de ADN humana
adn_ejemplo = "ATGAGTGGCGTGGCGGTCCAGGAGGAGCTCAGGAGGAGGAGGAGGAGGAGGAGGAGGAGGAGGAGGAGGAGGAGGAGGAGGAGGA"
st.write("Ejemplo de secuencia de ADN:")
st.code(adn_ejemplo)

# Entrada de texto para que el usuario ingrese su propia secuencia de ADN
adn_usuario = st.text_input("Introduce tu secuencia de ADN:", "")

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

# Diccionario que mapea codones de ARN a sus respectivos códigos de tres letras de aminoácidos
codon_to_aminoacid = {
    "AUG": "Met", "UUU": "Phe", "UUC": "Phe", "UUA": "Leu", "UUG": "Leu",
    "CUU": "Leu", "CUC": "Leu", "CUA": "Leu", "CUG": "Leu", "AUU": "Iso",
    "AUC": "Iso", "AUA": "Iso", "ACU": "Thr", "ACC": "Thr", "ACA": "Thr",
    "ACG": "Thr", "GUU": "Val", "GUC": "Val", "GUA": "Val", "GUG": "Val",
    "GCU": "Ala", "GCC": "Ala", "GCA": "Ala", "GCG": "Ala", "AAU": "Asn",
    "AAC": "Asn", "AAA": "Lys", "AAG": "Lys", "GAU": "Asp", "GAC": "Asp",
    "GAA": "Glu", "GAG": "Glu", "UGU": "Cys", "UGC": "Cys", "UGA": "Stop",
    "UGG": "Trp", "CGU": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg",
    "AGU": "Ser", "AGC": "Ser", "AGA": "Arg", "AGG": "Arg", "GGU": "Gly",
    "GGC": "Gly", "GGA": "Gly", "GGG": "Gly"
}

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

# Función para traducir codones a códigos de tres letras de aminoácidos
def traducir_codones_a_codigo(codones):
    """
    Toma una lista de codones y los traduce a códigos de tres letras de aminoácidos utilizando el diccionario codon_to_aminoacid.
    """
    codigos = []
    for codon in codones:
        if codon in codon_to_aminoacid:
            codigos.append(codon_to_aminoacid[codon])
        else:
            codigos.append("Stop")  # Si el codón no es válido, consideramos "Stop"
    return codigos

# Título de la aplicación
st.title("Transcripción de ARN a Aminoácidos")

# Descripción de la aplicación
st.write("""Esta aplicación toma una secuencia de ARN, la divide en codones y luego la traduce a aminoácidos. Un codón es un conjunto de tres nucleótidos que codifica un aminoácido.
""")

# Entrada de texto para que el usuario ingrese una secuencia de ARN
arn = st.text_input("Introduce la secuencia de ARN (solo A, U, G, C):", "")

# Verifica si el usuario ha presionado el botón de transcripción
if st.button("Traducir ARN a Aminoácidos"):
    if arn:
        # Convertimos la secuencia de ARN a mayúsculas para evitar problemas de formato
        arn = arn.upper()

        # Comprobar que la secuencia solo contiene bases válidas de ARN (A, U, G, C)
        if all(base in 'AUGC' for base in arn):
            # Llamamos a la función para dividir el ARN en codones
            codones = dividir_en_codones(arn)
            
            # Llamamos a la función para traducir los codones a los códigos de aminoácidos
            codigos_aminoacidos = traducir_codones_a_codigo(codones)
            
            # Mostrar los resultados
            if codigos_aminoacidos:
                st.success(f"Códigos de aminoácidos obtenidos: {', '.join(codigos_aminoacidos)}")
            else:
                st.warning("La secuencia de ARN es demasiado corta para obtener aminoácidos válidos.")
        else:
            st.error("La secuencia de ARN contiene bases inválidas. Solo se permiten A, U, G y C.")
    else:
        st.warning("Por favor, ingresa una secuencia de ARN.")


