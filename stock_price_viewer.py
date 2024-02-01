import yfinance as yf
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

try:
    df = pd.DataFrame({
        'first column': ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "FB", "JPM", "V", "PYPL", "NFLX", "DIS", "BA", "IBM", "KO", "PFE", "GM", "XOM", "CSCO", "INTC", "AMD", "NVDA", "GS", "VZ", "T", "PEP", "JNJ", "WMT", "HD", "MCD", "NKE", "CAT", "ADBE", "CRM", "ORCL", "SBUX", "CVX", "PDD", "BABA", "JD", "TSM", "WFC", "BAC", "GE", "LMT", "RTX", "SPG", "AMT", "VLO", "UPS", "FDX", "AXP", "MA", "MELI", "TMUS", "SQ", "CRM", "ABT", "MRK", "ABNB", "ZM", "DOCU", "SHOP", "SNOW", "CRM", "TDOC", "ROKU", "WORK", "TWLO", "CRWD", "NET", "FSLY", "ZS", "NOW", "IBM", "ATVI", "EA", "AMD", "MU", "AMAT", "TSM", "TXN", "PYPL", "SQ", "ADBE", "CRM", "WMT", "AMZN", "SHOP", "TSLA", "AAPL", "GOOGL", "MSFT", "NFLX", "DIS", "V", "MA", "JPM", "BAC", "GS", "XOM", "CVX", "IBM", "CSCO", "INTC", "AMD", "NVDA", "PFE", "MRK", "JNJ", "KO", "PEP", "MCD", "WMT", "HD"]
    })
    
    st.write("### Which Stock chart do you want to see?")
    
    tickerSymbol = st.selectbox(
        '  ',
        df['first column'])
    tickerData = yf.Ticker(tickerSymbol)
    info = tickerData.info
    st.write(f"# Chart of {info['longName']} ({tickerSymbol})")
    st.write(f"**Sector:** {info['sector']}")
    st.write(f"**Market Cap:** {info['marketCap']}")
    timeframe_options = ['1d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']
    selected_timeframe = st.selectbox('Select Timeframe', timeframe_options, index=4)

    tickerdf = tickerData.history(period=selected_timeframe)
    
    fig = go.Figure(data=[go.Candlestick(x=tickerdf.index,
                                         open=tickerdf['Open'],
                                         high=tickerdf['High'],
                                         low=tickerdf['Low'],
                                         close=tickerdf['Close'])])

    st.plotly_chart(fig)
    
    recommendations = tickerData.recommendations
    st.write("## Analyst Recommendations")
    st.dataframe(recommendations)

    st.write("## Stock Volume")
    st.line_chart(tickerdf.Volume)

    dividends = tickerData.dividends
    st.write("## Dividends")
    st.dataframe(dividends)

except Exception as e:
    st.write(f"Error fetching data for {tickerSymbol}: {e}")
