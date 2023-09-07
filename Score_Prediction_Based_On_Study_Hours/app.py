import streamlit as st
import pickle

st.title("Student Score Prediction Based On Study Hours")
hours=st.text_input('Enter study hours')
st.markdown(f"My input is : {hours}")
if st.button('Predict'):
  if (len(hours)):
   model=pickle.load(open('model.sav', 'rb'))
   prediction=model.predict([[int(hours)]])
   st.header(f'Predicted Score:{prediction[0]}')
  else:
   st.header('Please Enter Valid Data')
