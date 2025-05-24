import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title = "Analisis de Anuncios de Coches",layour = "wide")
st.header("Analisis Exploratorio de Anuncios de Coches")     
car_data = pd.read_csv('vehicles_us.csv') # datos
hist_button = st.button('Construir histograma') #Boton

if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

build_scatter = st.checkbox("Construir Grafico de Dispersión")

if build_scatter:
    st.write("Creación de un gráfico de dispersión para odómetro vs precio")
    fig_scatter = px.scatter(car_data, x = "odometer", y = "price", title="Odómetro vs Precio")
    st.plotly_chart(fig_scatter, use_container_width=True)
