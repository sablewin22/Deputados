import streamlit as st
import pandas as pd 
df = pd.read_csv('deputados_2022.csv')

st.title('Veja a lista dos deputados de 2022!')

partidos = st.text_input('Digite o partido que você queira ver os deputados:')

if partidos:
    st.dataframe(df[df['partido'] == partidos.upper()])
