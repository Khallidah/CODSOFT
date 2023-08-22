import streamlit as st
import pandas as pd
import numpy as np
import pickle


pickle_in = open('model.pkl', 'rb')
model = pickle.load(pickle_in)
pickle_in.close()

st.title("Titanic Survival Prediction")
st.write("Developed by: Khallidah Idris")
### inputing variables

name = st.text_input("Name of the individual") 
Pclass = st.number_input("Passenger Class (1=FirstClass, 2=SecondClass, 3=ThirdClass)")
Sex = st.number_input("Sex (0=Male, 1=Female)") 
Age = st.number_input("Age") 
SibSp = st.number_input("Number of Siblings and Spouses") 
Parch = st.number_input("Number of Parents and Children") 
Fare = st.number_input("Fare") 
Cabin = st.number_input("Cabin Number")
Embarked_Q = st.checkbox("Embarked from Queens")
Embarked_S = st.checkbox("Embarked from Southampton")
Embarked_C = st.checkbox("Embarked from Cherbourg")

button = st.button("Predict")

### making predictions
if button:
    predictions = model.predict([[Pclass,Sex,Age,SibSp,Parch,Fare,Cabin,Embarked_Q,Embarked_S,Embarked_C]])
if predictions == 0:
    st.write("Unfortunately",name,"did not survive.")
else:
    st.write(name,"survived.")
    