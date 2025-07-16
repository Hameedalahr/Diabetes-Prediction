# -*- coding: utf-8 -*-
"""
Created on Wed Jul 16 10:15:22 2025

@author: syeme
"""

import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open("trained_model.sav",'rb'))

def diabetes_prediction(input_data):
    
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    result = loaded_model.predict(input_data_reshaped)

    if(result[0] == 1):
      return "The Person have Diabetes"
    else:
      return "The Person dont have Diabetes"
  
    
  
def main():
    
    # Giving a title 
    st.title('Diabetes Prediction Web APP')
    
    # Getting the input data from User
    
    #Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age
    
    Pregnancies = st.text_input("Number of Pregnancies")
    Glucose = st.text_input("Glucose Level")
    BloodPressure = st.text_input("Blood Pressure Value")
    SkinThickness = st.text_input("Skin Thickness Value")
    Insulin = st.text_input("Insulin Value")
    BMI = st.text_input("Body Mass Index Value")
    DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function Value")
    Age = st.text_input("Age of the Person")
    
    diagnosis = ''
    
    # Creating a button
    
    if st.button("Diabetes Test Result"):
        diagnosis = diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
        
    
    st.success(diagnosis)
    


if __name__ == '__main__':
    main()
    
