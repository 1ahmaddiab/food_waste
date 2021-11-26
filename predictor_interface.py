import streamlit as st
from PIL import Image
from freshness_predictor import predict
st.set_page_config(page_title='Food Waste Challenge', page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)
st.title("Reducing Food Waste")

row1_1, row1_2 = st.columns((2, 3))

with row1_1:
    uploaded_file = st.file_uploader("Choose an image...", type="jpg")
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image.resize((200, 200)), caption='Uploaded Image.', use_column_width=True)

with row1_2:
    if uploaded_file is not None:
        st.write("")
        st.write("Classifying...")
        label = predict(image)
        st.write("***It looks {}!***".format(label))
