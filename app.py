import streamlit as st
import pandas as pd
import plotly.express as px


st.title("Análise de Dados de Veículos")


df = pd.read_csv("vehicles.csv")


st.subheader("Pré-visualização dos dados")
st.write(df.head())


if st.checkbox("Criar histograma"):
    st.subheader("Distribuição da quilometragem")
    fig = px.histogram(df, x="odometer", title="Distribuição da Quilometragem")
    st.plotly_chart(fig, use_container_width=True)


if st.checkbox("Criar gráfico de dispersão"):
    st.subheader("Dispersão entre preço e quilometragem")
    fig2 = px.scatter(df, x="odometer", y="price", title="Preço x Quilometragem")
    st.plotly_chart(fig2, use_container_width=True)