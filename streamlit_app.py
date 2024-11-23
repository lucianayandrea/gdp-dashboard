import streamlit as st
import random

# Personalización de la página con CSS
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
st.title("🧬 ADN, ARN y Proteinas 🧬")

# Sección de bienvenida
st.write("""
Bienvenido al **Proyecto de Bioinformática**. Este es un entorno interactivo donde exploramos la ciencia de los datos biológicos.
Aquí podrás realizar diversos análisis y visualizar resultados de manera intuitiva. ¡Diviértete explorando el mundo de la genética y el ADN!
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
# Draw the actual page

# Set the title that appears at the top of the page.
'''
# 🦾 Transcriptor ADN, ARN.


La bioinformática es una disciplina interdisciplinaria que emplea técnicas computacionales y estadisticas 
para resolver problemas biologicos, especialmente aquellos relacionados con la biologia molecular y genética 
Una de las tareas fundamentales en el ámbito de la bioinformatica es la comprensión y manipulación de secuencias biológicas 
como las del ADN,ARN y proteinas. En este contexto, la traduccion de ADN representa un un proceso clave dento de la 
expresion genética contenida en el ADN es convertida en proteinas funcionales, a través de la intermediación del ARN mensajero.
'''

import streamlit as st
# -----------------------------------------------------------------------------
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

# Descripción de la aplicación
st.write("""
    Esta herramienta convierte una secuencia de ADN a ARN.
    
    En el proceso de transcripción, la base Timina (T) del ADN se reemplaza por Uracilo (U) en el ARN.
""")

# Ejemplo de secuencia de ADN humana
adn_ejemplo = "ATGAGTGGCGTGGCGGTCCAGGAGGAGCTCAGGAGGAGGAGGAGGAGGAGGAGGAGGAGGAGGAGGAGGAGGAGGAGGA"
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

# -----------------------------------------------------------------------------
