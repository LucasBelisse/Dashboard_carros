import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Dashboard de Carros')
st.header('Visualizações Interativas')

# Carregar os dados
car_data = pd.read_csv('vehicles.csv')

# Criar as caixas de seleção
build_histogram = st.checkbox('Criar um histograma de odometer')
build_scatter = st.checkbox('Criar um gráfico de dispersão entre odometer e price')

# Mostrar histograma se selecionado
if build_histogram:
    st.write('Histograma da quilometragem (odometer)')
    fig_hist = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig_hist, use_container_width=True)

# Mostrar gráfico de dispersão se selecionado
if build_scatter:
    st.write('Gráfico de dispersão entre quilometragem (odometer) e preço (price)')
    fig_scatter = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig_scatter, use_container_width=True)