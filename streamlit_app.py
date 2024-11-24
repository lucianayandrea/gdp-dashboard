import streamlit as st
import random
import pandas as pd
from collections import Counter

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
        "imagen": "https://globetechcdn.com/mobile_es_labmedica/images/stories/articles/article_images/2019-08-21/R3z42ndQ.jpeg"
    },
    {
        "nombre": "Quimotripsina",
        "descripcion": "La quimotripsina es una enzima digestiva que ayuda a descomponer proteínas en el intestino.",
        "imagen": "https://upload.wikimedia.org/wikipedia/commons/2/22/Chymotrypsin.png"
    },
    {
        "nombre": "Insulina",
        "descripcion": "La insulina es una hormona que produce el páncreas, ayuda al cuerpo a utilizar y almacenar la glucosa, o azúcar en la sangre, como fuente de energía.",
        "imagen": "https://guatequimica.com/bootstrap/bootstrap-proteina/diabetes/1trz-BU.png"
   },
    {
        "nombre": "Colágeno",
        "descripcion": "El colágeno es una proteína estructural que proporciona soporte a los tejidos conectivos.",
        "imagen": "https://lh5.googleusercontent.com/proxy/CaNMuLVw2ZVPJ_KFQjso1gAw5CF1QxuWVAOfkdrTO7IH71hYfJMgsb37_KH2PMShWUaAYIgYOEBCk2YuFNA-GdGynZCPy3bCIfSND0A64jaOWoS9_B3MsmnyENKIaY0E6L6lXRj57GUr1J0pzg"
   },
    {
        "nombre": "Actina",
        "descripcion": "La actina es una proteína involucrada en la contracción muscular y en la forma celular.",
        "imagen": "https://upload.wikimedia.org/wikipedia/commons/d/d3/Actin_with_ADP_highlighted.png"
    },
     {
        "nombre": "Mioglobina",
        "descripcion": "Es una proteína que se encarga de transportar y almacenar oxígeno en los músculos, especialmente en el cardíaco.",
        "imagen": "https://pymstatic.com/98662/conversions/mioglobina-wide_webp.webp"
    },
    {
        "nombre": "Queratina",
        "descripcion": "Es una proteína fundamental para la resistencia y durabilidad de la piel, el cabello y las uñas, y está presente en las células que recubren los órganos y las glándulas",
        "imagen": "https://www.kmax-espana.es/blog/wp-content/uploads/2017/08/queratina-300x225.jpg"
    },
    {
        "nombre": "Tripsina",
        "descripcion": "Es una enzima que se produce en el páncreas y que tiene un papel fundamental en la digestión y absorción de nutrientes.",
        "imagen": "https://st4.depositphotos.com/3802617/21578/v/950/depositphotos_215780520-stock-illustration-trypsin-molecular-chemical-formula-enzyme.jpg"
   },
    {
        "nombre": "Lisozima",
        "descripcion": "Es una enzima natural que tiene propiedades antibacterianas y que se encuentra en muchos fluidos corporales, como la saliva, las lágrimas, el moco, la leche materna, el plasma sanguíneo, etc.",
        "imagen": "https://i.blogs.es/ebd1f9/lisozima/1366_2000.png"
    },
    {
        "nombre": "Elastina",
        "descripcion": "Es una proteína que tiene como función  dar elasticidad y resistencia a los tejidos, y mantener su estructura.",
        "imagen": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS_ekmBuNv1L7ixWDm9y_aNdH3dVutWy9KMAQ&s"
    },
    {
        "nombre": "Pepsina",
        "descripcion": "Es una enzima digestiva que se encuentra en el jugo gástrico y que se encarga de descomponer las proteínas de los alimentos.",
        "imagen": "https://previews.123rf.com/images/lculig/lculig1207/lculig120700047/14568676-la-pepsina-modelo-3d-una-enzima-que-digiere-las-prote%C3%ADnas-de-los-alimentos-en-p%C3%A9ptidos.jpg"
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

# Función para transcribir ADN a ARN
def transcribir_adn_a_arn(adn):
    """
    Convierte una secuencia de ADN en ARN, reemplazando la Timina (T) por Uracilo (U).
    """
    transcripcion = {'A': 'U', 'T': 'A', 'G': 'C', 'C': 'G'}
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


# Entrada de texto para que SE ingrese su secuencia de ADN
adn_usuario = st.text_input("Introduce tu secuencia de ADN:", "")

# Verifica si se ha presionado el botón de transcripción
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
    "CAC": "His", "CAU": "His", "CAG": "Gln", "CAA": "Gln",
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
(Puedes utilizar la transcripción anterior de ARN para la transcripcion a aminoácidos en esta sección)
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
