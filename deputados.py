import streamlit as st
import pandas as pd 
df = pd.read_csv('deputados_2022.csv')
st.dataframe(df)

opcao = st.text_input(
    'Digite o partido que deseja ver os deputados que fazem parte:'
)
if opcao:
    filtrado = df[df['partido'].str.contains(opcao, case=False, na=False)]
    
    st.write(f'Deputados do partido "{opcao}":')
    st.dataframe(filtrado)
