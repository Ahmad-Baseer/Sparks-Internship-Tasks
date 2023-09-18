import streamlit as st
import requests as req
from streamlit_lottie import st_lottie
from prediction_helper import predict_class_way1, predict_class_way2

st.set_page_config(page_title="Welcome to Iris Classifier",page_icon=":blossom:")

with st.container():
    st.title("Welcome to Iris Classifier :blossom:")
    st.subheader("Author: Ahmad Baseer")
    st.write("You can find the code [here](https://github.com/Ahmad-Baseer/AI-Projects)")

st.write("---")

def load_lottieurl(url):
    r=req.get(url)
    if r.status_code !=200:
        None
    return r.json()

lottie_flower=load_lottieurl("https://lottie.host/db599348-de9d-44a3-9e66-6490a4920520/jiH4zhQwAD.json")

left_col, right_col = st.columns(2)

with left_col:
    # Create four input fields.
    sepal_length = st.number_input("Sepal length (cm)", min_value=0.0, max_value=100.0)
    sepal_width = st.number_input("Sepal width (cm)", min_value=0.0, max_value=100.0)
    petal_length = st.number_input("Petal length (cm)", min_value=0.0, max_value=100.0)
    petal_width = st.number_input("Petal width (cm)", min_value=0.0, max_value=100.0)

    datapoint = [sepal_length,sepal_width,petal_length,petal_width]

    # Display the input fields.
    st.write("Sepal length:", sepal_length)
    st.write("Sepal width:", sepal_width)
    st.write("Petal length:", petal_length)
    st.write("Petal width:", petal_width)
    st.write(" **This model got accuracy of:** ", 0.8933)

if(sepal_length!=0 and sepal_width!=0 and petal_length!=0 and petal_width!=0):
    st.write("---")
    result_1=predict_class_way1(datapoint)
    result_2=predict_class_way2(datapoint)

    st.write(f" I guess 🤔 it belongs to (using method 1): **{result_1.capitalize()}** ")
    st.write(f" I guess 🤔 it belongs to (using method 2): **{result_2.capitalize()}** ")

    if result_1==result_2:
        st.write(" **Hurray :partying_face: we got same results from both techniques!**")

with right_col:
    st_lottie(lottie_flower,height=250,key="flower")

st.caption("Made with :heart: by Ahmad")

#using local css to design contact form
def local_css_for_contact_form(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
        
local_css_for_contact_form("style.css")