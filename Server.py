import streamlit as st
import numpy as np
from PIL import Image

st.title("Blissful Mugs")


img_file_buffer = st.file_uploader("Upload a PNG image", type='png')

if img_file_buffer is not None:
  image = Image.open(img_file_buffer)
  img_array = np.array(image)

st.markdown("This image will be printed on your mug")
