import streamlit as st
import pandas as pd
import pandas_datareader.data as web
import numpy as np
import plotly.graph_objects as go
#from plotly.subplots import make_subplot
from datetime import datetime 
import yfinance as yf
yf.pdr_override()

st.sidebar.title('Mercado de ações')

companies = ['AMAR3.SA','PETR4.SA', 'AMER3.SA', 'VALE3.SA', 'MGLU3.SA']
# companiess = {
#     'name': 'Marisa',
#     'symbol': 'AMAR3.SA'
# }
seelect = st.sidebar.selectbox('Selecione a empresa: ', companies)
rannge = st.sidebar.slider('Período em meses', 0, 12, 3, key='selection_bar')
range_selected = str(rannge) + 'mo'


#col1, col2 = st.columns([0.9, 0.1])
header = f'Análise econômica {str(seelect)} 💰'
st.title(header)

data = web.get_data_yahoo(seelect, period=range_selected)

graph_candle = go.Figure(
    data = [
        go.Candlestick(
            x = data.index,
            open = data.Open,
            high = data.High,
            low = data.Low,
            close = data.Close
        )
    ]
).update_layout(
    xaxis_rangeslider_visible = False,
    title = 'Análise das ações',
    yaxis_title = 'preço'
)

# mostrar o gráfico do plotly no streamlit
st.plotly_chart(graph_candle)

if st.checkbox('Mostrar os dados na tabela'):
    st.subheader('Tabela de registros')
    st.write(data)

