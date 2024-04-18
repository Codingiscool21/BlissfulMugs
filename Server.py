import streamlit as st
import numpy as np

img_file_buffer = st.file_uploader("Upload a PNG image", type='png')

if img_file_buffer is not None:
  image = Image.open(img_file_buffer)
  img_array = np.array(Image)




st.markdown(page_bg_color, unsafe-allow-html=True)
st.title("Blissful Mugs")
