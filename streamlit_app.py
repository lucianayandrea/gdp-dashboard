import streamlit as st
import random

# Personalización de la página con CSS

import streamlit as st

# Personalización de la página con CSS
st.markdown(
    """
    <style>
    body {
        background-color: #b3cde0;  /* Azul bebé */
        color: #333333;  /* Color de texto oscuro para contraste */
    }
    </style>
    """, unsafe_allow_html=True
)

    # Personalización de la página con CSS
st.markdown(
    """
    <style>
    body {
        background-color: #ffffff;  /* Cambia el valor aquí por cualquier color que desees */
    }
    </style>
    """, unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    body {
        background-color: #2e8b57;  /* Fondo verde claro */
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
        background-color: #b3cde0;
    }
    </style>
    """, unsafe_allow_html=True
)

# Título de la página
st.title("🧬 Cadenas de ADN, ARN y Proteinas")

# Sección de bienvenida
st.write("""
Bienvenido al **Proyecto de Bioinformática**. Este es un entorno interactivo donde exploramos la ciencia de los datos biológicos.
""")

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
        "imagen": "data:image/jpeg;base64,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"
    },
    {
        "nombre": "Dinamina",
        "descripcion": "La dinamina es una proteína involucrada en la fisión de vesículas intracelulares.",
        "imagen": "https://upload.wikimedia.org/wikipedia/commons/6/67/Dynamin.png"
    },
    {
        "nombre": "Colágeno",
        "descripcion": "El colágeno es una proteína estructural que proporciona soporte a los tejidos conectivos.",
        "imagen": "https://w7.pngwing.com/pngs/319/346/png-transparent-type-i-collagen-collagen-type-iii-alpha-1-collagen-type-i-alpha-1-type-ii-collagen-metal-pattern.png"
    },
    {
        "nombre": "Actina",
        "descripcion": "La actina es una proteína involucrada en la contracción muscular y en la forma celular.",
        "imagen": "https://upload.wikimedia.org/wikipedia/commons/3/32/Actin_structure.png"
    }
]

# Función para mostrar una proteína aleatoria
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
import streamlit as st

# Personalización de la página con CSS
st.markdown(
    """
    <style>
    body {
        background-color: #f0f8ff;  /* Fondo azul claro */
        font-family: 'Arial', sans-serif;
    }

    h1 {
        color: #2e8b57;  /* Verde oscuro */
        text-align: center;  /* Centrado del título */
    }

    .description {
        color: #333333;  /* Texto en gris oscuro */
        font-size: 18px;
        text-align: center;  /* Centrado del texto */
        max-width: 800px;  /* Controlar el ancho del texto */
        margin: 20px auto;  /* Centrar el texto con margen */
    }
    </style>
    """, unsafe_allow_html=True
)

# Título de la página
st.markdown("<h1>🦾 Transcriptor de ADN, ARN y Aminoácidos </h1>", unsafe_allow_html=True)

# Texto descriptivo centrado debajo del título
st.markdown("""
<div class="description">
La bioinformática es una disciplina interdisciplinaria que emplea técnicas computacionales y estadísticas 
para resolver problemas biológicos, especialmente aquellos relacionados con la biología molecular y genética.
Una de las tareas fundamentales en el ámbito de la bioinformática es la comprensión y manipulación de secuencias biológicas 
como las del ADN, ARN, aminoácidos y proteínas. En este contexto, la traducción de ADN representa un proceso clave dentro de la 
expresión genética, donde el ADN es convertido en proteínas funcionales, a través de la intermediación del ARN mensajero a aminoácidos.
</div>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------

import streamlit as st

# Función para transcribir ADN a ARN
def transcribir_adn_a_arn(adn):
    """
    Convierte una secuencia de ADN en ARN, reemplazando la Timina (T) por Uracilo (U).
    """
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

# Ejemplo de secuencia de ADN humana
adn_ejemplo = "CGACACATAAGAACAACGAGAGTAGAAATATGAAGACTTCTCCCAGGGAAAATACTTTTACTTCAAAAACAGTTACTTGTTACAACGACGCCACTCATATGAGGCAGACTTGTAAAAATACAAGATGGGAAATTAACAGTTGTCCTCCTCCCAAGAACG"
st.write("Ejemplo de secuencia de ADN:")
st.code(adn_ejemplo)

# Descripción de la aplicación
st.write("""
    Esta herramienta convierte una secuencia de ADN a ARN.
    En el proceso de transcripción, la base Timina (T) del ADN se reemplaza por Uracilo (U) en el ARN.
    Ingrese la cadena sin espacios, comas o guión.
""")


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

# -----------------------------------------------------------------------------

# Diccionario que mapea codones de ARN a sus respectivos códigos de tres letras de aminoácidos
codon_to_aminoacid = {
    "AUG": "Met", "UUU": "Phe", "UUC": "Phe", "UUA": "Leu", "UUG": "Leu",
    "CUU": "Leu", "CUC": "Leu", "CUA": "Leu", "CUG": "Leu", "AUU": "Ile",
    "AUC": "Ile", "AUA": "Ile", "ACU": "Thr", "ACC": "Thr", "ACA": "Thr",
    "ACG": "Thr", "GUU": "Val", "GUC": "Val", "GUA": "Val", "GUG": "Val",
    "GCU": "Ala", "GCC": "Ala", "GCA": "Ala", "GCG": "Ala", "AAU": "Asn",
    "AAC": "Asn", "AAA": "Lys", "AAG": "Lys", "GAU": "Asp", "GAC": "Asp",
    "GAA": "Glu", "GAG": "Glu", "UGU": "Cys", "UGC": "Cys", "UGA": "Stop",
    "UGG": "Trp", "CGU": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg",
    "AGU": "Ser", "AGC": "Ser", "AGA": "Arg", "AGG": "Arg", "GGU": "Gly",
    "GGC": "Gly", "GGA": "Gly", "GGG": "Gly", "UCU": "Ser", "UCC": "Ser", 
    "UCA": "Ser", "UCG": "Ser", "CCU": "Pro", "CCC": "Pro", "CCA": "Pro", 
    "CCG": "Pro", "UAU": "Tyr", "UAC": "Tyr", "UAA": "Stop", "UAG": "Stop",
    "CAC": "His", "CAU": "His", "CAG": "Gln", 
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
            codigos.append("Error")  # Si el codón no es válido, consideramos "Stop"
    return codigos

# Título de la aplicación
st.title("Transcripción de ARN a Aminoácidos")

# Descripción de la aplicación
st.write("""En esta sección se toma una secuencia de ARN, la divide en codones y luego la traduce a aminoácidos. 
Un codón es un conjunto de tres nucleótidos que codifica un aminoácido.
Ingrese la cadena sin espacios, comas o guión.
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

# -----------------------------------------------------------------------------
import streamlit as st
import pandas as pd
from collections import Counter

# Definir los aminoácidos de "stop"
STOP_CODES = ["TAG", "TAA", "TGA"]

# Función para calcular los porcentajes de aminoácidos
def calcular_porcentajes(aminoacidos):
    """
    Calcula la frecuencia de cada aminoácido en una cadena y devuelve un DataFrame con los porcentajes.
    Incluye los códigos de "stop".
    """
    # Contar la frecuencia de cada aminoácido
    contador = Counter(aminoacidos)
    
    # Total de aminoácidos en la secuencia
    total = sum(contador.values())
    
    # Crear una lista con los aminoácidos y sus porcentajes
    porcentaje_aminoacidos = [(aminoacido, count, (count / total) * 100) for aminoacido, count in contador.items()]
    
    # Crear un DataFrame con la información
    df = pd.DataFrame(porcentaje_aminoacidos, columns=["Aminoácido", "Frecuencia", "Porcentaje"])
    
    # Ordenar el DataFrame por frecuencia (de mayor a menor)
    df = df.sort_values(by="Frecuencia", ascending=False)
    
    return df

# Título de la aplicación
st.title("Cuantificador de aminoácidos en una cadena")

# Descripción de la aplicación
st.write("""
    En esta sección permite ingresar una secuencia de aminoácidos de tres letras y calcula los porcentajes de frecuencia de cada aminoácido en una cadena.
""")

# Entrada de texto para que el usuario ingrese la secuencia de aminoácidos
aminoacidos_input = st.text_input("Introduce la secuencia de aminoácidos (separados por comas):", "")

# Verifica si el usuario ha presionado el botón de análisis
if st.button("Calcular Porcentajes"):
    if aminoacidos_input:
        # Convertimos la entrada en una lista de aminoácidos, separando por comas
        aminoacidos = aminoacidos_input.split(",")
        
        # Verificamos que no haya espacios innecesarios
        aminoacidos = [aa.strip() for aa in aminoacidos]
        
        # Validamos que los aminoácidos sean de tres letras o "STOP"
        validos = all(len(aa) == 3 or aa == "Stop" for aa in aminoacidos)
        
        if validos:
            # Agregamos los códigos de "stop" como aminoácidos válidos
            aminoacidos = [aa if aa in STOP_CODES else aa for aa in aminoacidos]
            
            # Calculamos los porcentajes
            df_resultado = calcular_porcentajes(aminoacidos)
            
            # Mostrar la tabla de resultados
            st.write("### Tabla de Porcentajes de Aminoácidos:")
            st.dataframe(df_resultado)
        else:
            st.error("La secuencia debe contener aminoácidos de tres letras válidos o el código 'Stop'.")
    else:
        st.warning("Por favor, ingresa una secuencia de aminoácidos.")
