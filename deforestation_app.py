# -*- coding: utf-8 -*-
"""
Created on Tues July 06 15:20:31 2021

@author: Abdoul Wahab Diallo
"""

# -*- coding: utf-8 -*-
"""
Created on Tues July 06 02:20:31 2021

@author: Abdoul Wahab Diallo
"""


import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(TU = 10,SA = 100,SP = 100):
    
   
    prediction=classifier.predict([[TU,SA,SP]])
    print(prediction)
    return prediction



def main():
    st.title("AIMS-GPSDD FELLOWSHIP")
    html_temp = """
    <div style="background-color:#EACF4C;padding:10px">
    <h2 style="color:white;text-align:center;">Détection d'une région menacée par la déforestation</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True) 
    TU = st.text_input("Taux d'urbanisation (%)","")
    SA = st.text_input("Superficie agricole (ha)","")
    SP = st.text_input("Superficie perdue (ha)","")
    result=""
    if st.button("Prédire"):
        result=predict_note_authentication(TU,SA,SP)
    st.success('Le résultat est {}'.format(result))

    st.text("[1] : la région est fortement menacée par la déforestation")
    st.text("[0] : la région est faiblement menacée par la déforestation")

    if st.button("A propos"):
       st.markdown("Ce projet a été piloté par IPAR en collaboration avec AIMS, GPSDD, ANSD et DPVE. L'objectif \
                   de ce projet etait de mettre en place un modèle de machine learning qui permettrait de prédire la menace \
                   de déforestation dans une zone donnée en utilisant des données relatives au développement de l’agriculture et de l’urbanisation.")
      


    Col1, Col2 = st.columns(2)

    with Col1:
       # st.header("A cat")
       st.image("aims.png")

    with Col2:
       # st.header("A dog")
       st.image("GPSDD.png") 


    col1, col2, col3 = st.columns(3)
    with col1:
       # st.header("A cat")
       st.image("ipar.png")

    with col2:
       # st.header("A dog")
       st.image("ANSD.png")
 
    with col3:
       # st.header("An owl")
       st.image("dpve.jpg")
if __name__=='__main__':
    main()
    
    
    
