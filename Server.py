import streamlit as st
import numpy as np

st.title("Blissful Mugs")
st.markdown("Upload an Imge and we will print it on your mug")

img_file_buffer = st.file_uploader("Upload a PNG image", type='png')

if img_file_buffer is not None:
  image = Image.open(img_file_buffer)
  img_array = np.array(Image)



