import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st


data = pd.read_csv('C:/Users/USER/Desktop/Business Analyst Certificate/TRIPLE TEN/PROY 4/vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
            # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
    fig = px.histogram(data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True) 