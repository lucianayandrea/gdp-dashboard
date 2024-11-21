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
if st.button("Transcribir a ARN"):
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
import streamlit as st

# Diccionario de codones de ARN a aminoácidos (simplificado)
codones_a_aminoacidos = {
    'AUG': 'Met', 'UUU': 'Phe', 'UUC': 'Phe', 'UUA': 'Leu', 'UUG': 'Leu',
    'CUU': 'Leu', 'CUC': 'Leu', 'CUA': 'Leu', 'CUG': 'Leu', 'AUU': 'Ile',
    'AUC': 'Ile', 'AUA': 'Ile', 'AUG': 'Met', 'GUU': 'Val', 'GUC': 'Val',
    'GUA': 'Val', 'GUG': 'Val', 'CCU': 'Pro', 'CCC': 'Pro', 'CCA': 'Pro',
    'CCG': 'Pro', 'ACU': 'Thr', 'ACC': 'Thr', 'ACA': 'Thr', 'ACG': 'Thr',
    'GCU': 'Ala', 'GCC': 'Ala', 'GCA': 'Ala', 'GCG': 'Ala', 'UAU': 'Tyr',
    'UAC': 'Tyr', 'UAA': 'Stop', 'UAG': 'Stop', 'UGA': 'Stop', 'CAU': 'His',
    'CAC': 'His', 'CAA': 'Gln', 'CAG': 'Gln', 'AAU': 'Asn', 'AAC': 'Asn',
    'AAA': 'Lys', 'AAG': 'Lys', 'GAU': 'Asp', 'GAC': 'Asp', 'GAA': 'Glu',
    'GAG': 'Glu', 'CGU': 'Arg', 'CGC': 'Arg', 'CGA': 'Arg', 'CGG': 'Arg',
    'AGU': 'Ser', 'AGC': 'Ser', 'AGA': 'Arg', 'AGG': 'Arg', 'GGU': 'Gly',
    'GGC': 'Gly', 'GGA': 'Gly', 'GGG': 'Gly'
}

# Función para traducir ARN a proteína
def transcribir_arn_a_proteina(arn):
    """
    Convierte una secuencia de ARN a una cadena de proteína
    usando el código genético.
    """
    # Inicializar la proteína
    proteina = []
    
    # Dividir el ARN en codones (cada 3 bases)
    for i in range(0, len(arn), 3):
        codon = arn[i:i+3]
        # Verificar si el codón es válido
        if len(codon) == 3:
            # Obtener el aminoácido correspondiente al codón
            aminoacido = codones_a_aminoacidos.get(codon, 'Stop')
            # Si el aminoácido es 'Stop', terminamos la traducción
            if aminoacido == 'Stop':
                break
            proteina.append(aminoacido)
    
    return ' - '.join(proteina)

# Título de la aplicación
st.title("Transcripción de ARN a Proteína")

# Descripción de la aplicación
st.write("""
    Esta aplicación convierte una secuencia de ARN mensajero (ARNm) en una cadena de proteína
    utilizando el código genético. Introduce una secuencia de ARN y obtén su secuencia de proteína correspondiente.
""")

# Entrada de texto para que el usuario ingrese una secuencia de ARN
arn = st.text_input("Introduce la secuencia de ARN:", "")

# Verifica si el usuario ha presionado el botón de transcripción
if st.button("Transcribir a proteina"):
    if arn:
        # Llamamos a la función para traducir el ARN a proteína
        proteina = transcribir_arn_a_proteina(arn)
        
        # Mostrar la secuencia de proteína resultante
        if proteina:
            st.success(f"Secuencia de proteína resultante: {proteina}")
        else:
            st.error("La secuencia de ARN no es válida o contiene caracteres no permitidos.")
    else:
        st.warning("Por favor, ingresa una secuencia de ARN.")
