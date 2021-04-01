import pandas as pd
from PIL import Image
import streamlit as st
from streamlit_drawable_canvas import st_canvas
import qrcode

URL = 'https://share.streamlit.io/malo21st/st_canvas/main/app_canvas.py'

# Create a canvas component
canvas_result = st_canvas(
    stroke_width=15,
    stroke_color="black",
    background_color="lightblue",
    update_streamlit=True,
    height=200,
    width =200,
    drawing_mode="freedraw",
    key="canvas",
)

qrcode.make(URL)
