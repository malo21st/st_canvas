import pandas as pd
from PIL import Image
import streamlit as st
from streamlit_drawable_canvas import st_canvas

# Create a canvas component
canvas_result = st_canvas(
#     fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
    stroke_width=10,
    stroke_color="black",
    background_color="lightblue",
    update_streamlit=True,
    height=200,
    width =200,
    drawing_mode="freedraw",
    key="canvas",
)
