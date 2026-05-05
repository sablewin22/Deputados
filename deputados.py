import streamlit as st
import pandas as pd 
df = pd.read_csv('deputados_2022.csv')
st.dataframe(df)

opcao = selectbox(
  'Escolha o partido que deseja ver os deputados que fazemn parte',
  ['deputados_2022.csv(partido)']
)
