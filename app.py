import os
import pickle
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

    
# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models

diabetes_model = pickle.load(open(f'{working_dir}/saved_models/Breast_Cancer_model.sav', 'rb'))


# creating a function for Prediction

def diabetes_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = diabetes_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person is not diabetic'
    else:
      return 'The person is diabetic'
  
    
  
def main():
    
    
     
    # giving a title
    st.title('Breast Cancer Web App')
    
    
    # getting the input data from the user
    
    
    radius_mean = st.text_input('Your radius_mean')
    texture_mean= st.text_input('texture_mean')
    perimeter_mean = st.text_input('perimeter_mean')
    area_mean = st.text_input('area_mean')
    smoothness_mean = st.text_input('smoothness_mean')
    compactness_mean = st.text_input('BMI value')
    concavity_mean = st.text_input('Diabetes Pedigree Function value')
    concave_points_mean = st.text_input('Age of the Person')
    symmetry_mean = st.text_input('Your radius_mean')
    fractal_dimension_mean = st.text_input('texture_mean')
    radius_se = st.text_input('perimeter_mean')
    texture_se = st.text_input('area_mean')
    perimeter_se = st.text_input('smoothness_mean')
    area_se = st.text_input('BMI value')
    smoothness_se = st.text_input('Diabetes Pedigree Function value')
    compactness_se = st.text_input('Age of the Person')
    concavity_se = st.text_input('smoothness_mean')
    concave_points_se = st.text_input('Your radius_mean')
    symmetry_se = st.text_input('texture_mean')
    fractal_dimension_se = st.text_input('perimeter_mean')
    radius_worst = st.text_input('Your radius_mean')
    texture_worst = st.text_input('area_mean')


    perimeter_worst = st.text_input('area_mean')
    area_worst = st.text_input('area_mean')
    smoothness_worst = st.text_input('area_mean')

    compactness_worst = st.text_input('area_mean')
    concavity_worst = st.text_input('area_mean')
    concave_points_worst = st.text_input('area_mean')
    symmetry_worst = st.text_input('area_mean')
    fractal_dimension_worst = st.text_input('area_mean')


    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Breast Cancer Test Result'):
        diagnosis = diabetes_prediction([radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean, concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean, radius_se, texture_se, perimeter_se, area_se, smoothness_se, compactness_se, concavity_se, concave_points_se, symmetry_se, fractal_dimension_se, radius_worst, texture_worst, perimeter_worst, area_worst, smoothness_worst, compactness_worst, concavity_worst, concave_points_worst, symmetry_worst, fractal_dimension_worst
])
        
        
    st.success(diagnosis)
    
    
    
    
    
if __name__ == '__main__':
    main()
    