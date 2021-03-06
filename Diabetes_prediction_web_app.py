import numpy as np
import joblib
import streamlit as st

loaded_model = joblib.load('trained_model.sav')

#let us create a function for the web app

def diabetes_prediction(input_data):
    input = [5,166,72,19,175,25.8,0.587,51]
    convert =np.asarray(input)
    convert_shaped = convert.reshape(1,-1)
    prediction = loaded_model.predict(convert_shaped)
    print(prediction)
    if(prediction[0]==0):
         return 'The person is not Diabetic'
    else:
        return 'This person totally got diabetes'    
   
                                       

def main():
    
    
    #Giving the title
    st.title("Diabetes Prediction App")
    
    #getting input data from the user
    
    
    Pregnancies=st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose level')
    BloodPressure = st.text_input('Blood Pressure Level')
    SkinThickness = st.text_input('Skin Thickness Value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI Value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    Age = st.text_input('Age of the Person')
    
    
    #Code for Prediction
    
    diagnosis = ''
    
    #Create Button for Prediction
    
    if st.button('Diabetes Test  Result'):
        diagnosis = diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
        
    st.success(diagnosis)    
     
                                           

if __name__ == '__main__':
    main()


