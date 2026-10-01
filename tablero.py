import streamlit as st
from streamlit_drawable_canvas import st_canvas

# Título fucsia con CSS
st.markdown(
    """
    <style>
    h1.titulo-fucsia { color: #FF00FF !important; }
    </style>
    <h1 class="titulo-fucsia">Tablero para dibujo</h1>
    """,
    unsafe_allow_html=True,
)

# Imagen debajo del título + texto
st.image("gatodibujon.jpg", width=300)
st.write("Ahora dibuja abajo 👇")

with st.sidebar:
    st.subheader("Propiedades del Tablero")

    st.subheader("Dimensiones del Tablero")
    canvas_width = st.slider("Ancho del tablero", 300, 700, 500, 50)
    canvas_height = st.slider("Alto del tablero", 200, 600, 300, 50)

    drawing_mode = st.selectbox(
        "Herramienta de Dibujo:",
        ("freedraw", "line", "rect", "circle", "transform", "polygon", "point"),
    )

    stroke_width = st.slider("Selecciona el ancho de línea", 1, 30, 15)

    stroke_color = st.color_picker("Color de trazo", "#FF00FF", key="color_trazo_fucsia")

    bg_color = st.color_picker("Color de fondo", "#000000")

canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=canvas_height,
    width=canvas_width,
    drawing_mode=drawing_mode,
    key=f"canvas_{canvas_width}_{canvas_height}_{stroke_color}",
)
