import streamlit as st
import pandas as pd

#Llamar el csv de la carpeta static
data = pd.read_csv('./static/integrador.csv')
df = pd.DataFrame(data)




#------------------------------------------------------------------------------

st.header("Peliculas con mayor nota entre las fechas seleccionadas")

FechaInicial = st.date_input("Ingrese la fecha inicial",value=None)

FechaFinal = st.date_input("Ingrese la fecha Final",value=None)

#------------------------------------------------------------------------------

st.header("Peliculas con mayor puntuación segun la categoría seleccionada")

def categorias_peliculas():

    CategoriasP = df['Categoria'].unique()
    opcion = st.selectbox("Categorias", CategoriasP)
    opcion_seleccionada = df[df['Categoria']==opcion]
    #Crea la grafica
    data = opcion_seleccionada[['Titulo','Puntuacion']]
    df_grafico = pd.DataFrame(data)
    st.bar_chart(df_grafico.set_index('Titulo'))
    #Crea la tabla
    st.table(opcion_seleccionada)

    

categorias_peliculas()