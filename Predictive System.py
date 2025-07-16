# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pickle
import numpy as np


loaded_model = pickle.load(open("C:/Users/syeme/Downloads/Machine Learning/Project 2 - Diabetes Prediction/trained_model.sav",'rb'))

input_data = (6,148,72,35,0,33.6,0.627,50)

input_data_as_numpy_array = np.asarray(input_data)
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
result = loaded_model.predict(input_data_reshaped)

if(result[0] == 1):
  print("The Person have Diabetes")
else:
  print("The Person dont have Diabetes")