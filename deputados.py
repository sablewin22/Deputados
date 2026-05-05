import streamlit as st
import pandas as pd 
df = pd.read_csv('deputados_2022.csv')
st.dataframe(df)

partidos = st.text_input.('Digite o partido que você queira ver os deputados:')

if partidos:
    st.dataframe(df[df['partido'].str.lower() == partidos.lower()])
