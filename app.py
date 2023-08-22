import streamlit as st
import pandas as pd
import numpy as np
import pickle


pickle_in = open('model.pkl', 'rb')
model = pickle.load(pickle_in)
pickle_in.close()

st.title("Iris Flower Classification")
st.write("Developed by: Khallidah Idris")



sepal_length = st.number_input("Sepal Length") 
sepal_width = st.number_input("Sepal Width") 
petal_length = st.number_input("Petal Length") 
petal_width = st.number_input("Petal Width") 


button = st.button("Classify")


if button:
    predictions = model.predict([[sepal_length,sepal_width,petal_length,petal_width]])
if predictions == 0:
    st.write("The flower is Setosa.")
elif predictions == 1:
    st.write("The flower is Versicolor.")
else:
    st.write("The flower is Virginica.")