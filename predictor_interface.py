<<<<<<< Updated upstream
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
=======
import streamlit as st
from PIL import Image
from freshness_predictor import predict
from consumers_info import get_consumers_for_label

labels = ["nice and tasty", "just tasty"]

st.set_page_config(page_title='Food Waste Challenge', page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)
st.title("REDUCE FOOD WASTE")
row1_1, row1_2 = st.columns([2, 3])
with row1_1:
    prediction = None
    uploaded_file = st.file_uploader("Choose an image...")
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image.resize((250, 250)), caption='Uploaded Image.', use_column_width=False)
        prediction = predict(image)
        st.subheader("***It looks {}!***".format(labels[prediction]))

with row1_2:
    if prediction is not None:
        st.subheader("There is someone willing to buy:")
        with st.container():
            consumers_list = get_consumers_for_label(prediction)
            for i in consumers_list:
                st.success("{}".format(i))
>>>>>>> Stashed changes
