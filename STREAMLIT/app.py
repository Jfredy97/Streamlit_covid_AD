import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.write("Hello world")

st.title('Este es el Titulo')
st.header('Este es el encabezado')
st.subheader('Este es el encabezado')
st.text('Este es un texto')
st.markdown("<p style='color:red;'>Esto es un parrafo - st.markdown</p>", unsafe_allow_html=True)
st.html("<p style='color:blue;'>st.html</p>")

df = pd.DataFrame({
    'fruta': ['manzana', 'fresa', 'banano'],
    'cantidad': [10,15,8]
})
#df.set_index('fruta', inplace=True)
st.write(df)
st.pyplot(df.plot(kind='pie', y='cantidad',autopct='%1.1f%%', legend=False).figure)
st.line_chart(df, x='fruta', y='cantidad')

