import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(layout="wide")

st.title("📈 Deriv Trading Dashboard")

symbol = st.sidebar.selectbox(
    "Choose Market",
    ["EURUSD=X", "GBPUSD=X", "USDJPY=X"]
)

data = yf.download(symbol, period="1d", interval="1m")

st.subheader(f"Live Chart - {symbol}")

st.line_chart(data["Close"])

close = data["Close"]

ema5 = close.ewm(span=5).mean()
ema20 = close.ewm(span=20).mean()

if ema5.iloc[-1] > ema20.iloc[-1]:
    st.success("BUY SIGNAL")
else:
    st.error("SELL SIGNAL")

st.dataframe(data.tail())
