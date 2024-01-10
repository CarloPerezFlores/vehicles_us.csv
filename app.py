import streamlit as st
import pandas as pd
import plotly.express as px

# se llama el dataset y se guarda
try:
  data = pd.read_csv('C:/Users/USER/Desktop/Business Analyst Certificate/TRIPLE TEN/PROY 4/vehicles_us.csv')
except FileNotFoundError:
  st.error('El archivo "vehicles_us.csv" no se encuentra.')

st.header('Anuncios de venta de autos')

# crear casillas de verificación
hist_check = st.checkbox('Construir histograma')
scatter_check = st.checkbox('Construir gráfico de dispersión')

# al hacer clic en el botón
if hist_check:
  try:
    st.write(
      'Creación de un histograma para la columna de precios del conjunto de datos de anuncios de venta de autos')
    # se crea un histogrma
    fig = px.histogram(data, x='price')
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
  except Exception as e:
    st.error(e)

if scatter_check:
  try:
    st.write(
      'Creación de gráfico de dispersión del precio y año del modelo, para el conjunto de datos de anuncios de venta de autos')
    # se crea gráfico de dispersión
    fig = px.scatter(data, x='model_year', y='price')
    # mostrar un gráfico Plotly interactivo de gráfico de dispersión
    st.plotly_chart(fig, use_container_width=True)
  except Exception as e:
    st.error(e)


