import pandas as pd
import streamlit as st
import plotly.express as px

#confinguração da página
st.markdown("""
            <style>
            #dashboard-de-analise-de-roupas{
            color:#000
            }
            </style>
            """,unsafe_allow_html=True)


st.set_page_config(page_title="Dashboard da ZARA",
                   layout='wide')

st.title("Dashboard de Análise de Roupas")
st.markdown("**Explore** os dados de produtos da Zara")

@st.cache_data
def load_data():
    df=pd.read_csv('zara.csv',sep=";")
    return df

df= load_data()

section=st.sidebar.multiselect('Selecione a Seção', options=df['section'].unique(),default=df['section'].unique())

promotion=st.sidebar.multiselect('Selecione se quer itens promocionais', options=df['Promotion'].unique(),default=df['Promotion'].unique())


df_filtered=df[df['section'].isin(section) & df['Promotion'].isin(promotion)]

st.subheader('Principais Métricas: ')
col1,col2,col3=st.columns(3)
col1.metric("Total de Produtos",len(df_filtered))
#col2.metric("Soma de Todos os Produtos",sum(df_filtered['price']))
col2.metric("Soma de Todos os Produtos", round(df_filtered['price'].sum(),2))
col3.metric("Média dos Produtos",round(df_filtered['price'].mean(),2))

price_distribution = px.histogram(df_filtered,x='price',nbins=50,title='Distribuição de Preços',template='plotly_white')

st.plotly_chart(price_distribution)



st.dataframe(df_filtered)