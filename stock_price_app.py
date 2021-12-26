import yfinance as yf
import streamlit as st
import pandas as pd

tickerSymbol = 'GOOGL'
st.markdown("""
# Simple Stock Price App

Shown are the ***stock closing price*** and ***volume*** 
* **Python libraries:** yfinance, pandas, streamlit
* **Data Source:** yfinance.
""")

st.subheader('Enter tickerSymbol')
tickerSymbol = st.text_area('for example tickerSymbol of Google is GOOGL', tickerSymbol, height = 50)
#Define the ticker symbol


# get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#get the historical prices for this ticker
tickerOf = tickerData.history(period = '1d', start = '2010-5-31', end = '2021-5-31')
#Open High Low Close Volume Dividents Stock Splits
st.write("""
### Closing Price
""")
st.line_chart(tickerOf.Close)
st.write("""
### Volume Price
""")
st.line_chart(tickerOf.Volume)