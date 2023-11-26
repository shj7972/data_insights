import yfinance as yf
import plotly
from prophet import Prophet
from prophet.plot import plot_plotly
import pandas as pd
import streamlit as st

# Function to fetch stock data using yfinance
def fetch_stock_data(ticker):
    stock_data = yf.download(ticker, period="1y")  # Fetch 1 year of historical data
    stock_data.reset_index(inplace=True)  # Reset index to turn the Date index into a column
    return stock_data

# Function to predict stock price using Prophet
def predict_stock_price(data, days):
    # Prepare the data for Prophet
    df_for_prophet = data[['Date', 'Close']].rename(columns={'Date': 'ds', 'Close': 'y'})
    
    # Initialize Prophet model
    model = Prophet(daily_seasonality=True)
    model.fit(df_for_prophet)
    
    # Create a dataframe for future predictions
    future = model.make_future_dataframe(periods=days)
    
    # Make predictions
    forecast = model.predict(future)
    
    return model, forecast, future

# Streamlit UI (you would call this in your main function)
def run_k_stocks_app():
    st.title("Korean Stock Predictions")

    ticker_to_name = {
    '005930.KS': '삼성전자',
    '373220.KS': 'LG에너지솔루션',
    '000660.KS': 'SK하이닉스',
    '207940.KS': '삼성바이오로직스',
    '005935.KS': '삼성전자우',
    '005490.KS': 'POSCO홀딩스',
    '005380.KS': '현대차',
    '051910.KS': 'LG화학',
    '035420.KS': 'NAVER',
    '000270.KS': '기아'
    }

    # Selection box for tickers
    #ticker_list = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'FB', 'TSLA', 'BRK-A', 'V', 'JNJ', 'WMT']
    #selected_ticker = st.selectbox('Select a ticker', ticker_list)
    ticker_list = list(ticker_to_name.keys())
    selected_ticker = st.selectbox('Select a ticker', options=ticker_list, format_func=lambda x: f"{x} - {ticker_to_name[x]}")

    # Slider for forecast period
    forecast_period = st.slider('Select forecast period (days)', 1, 30, 1)

    # Fetch and display stock data
    if st.button('Show Data and Prediction'):
        data = fetch_stock_data(selected_ticker)
        st.write('Historical Stock Data')

        #st.line_chart(data['Close'])
        # Make sure the Date is in datetime format for proper plotting
        data['Date'] = pd.to_datetime(data['Date'])
        fig = plotly.graph_objs.Figure()
        fig.add_trace(plotly.graph_objs.Scatter(x=data['Date'], y=data['Close'], mode='lines', name='Close Price'))
        fig.update_layout(title='Historical Stock Prices', xaxis_title='Date', yaxis_title='Price', xaxis=dict(type='date'))
        st.plotly_chart(fig)

        # Predict and display future stock prices
        model, prediction, future = predict_stock_price(data, forecast_period)
        st.write('Stock Price Prediction')
        fig1 = plot_plotly(model, prediction)  # This plots the forecast
        st.plotly_chart(fig1)

        # Display predicted raw data
        st.write('Forecasted Raw Data')
        # Only show the 'ds' (date) and 'yhat' (predicted value) columns
        #forecasted_data = prediction[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(Date)
        st.dataframe(prediction)

# This would be placed in your main app function
# show_predictions()

if __name__ == '__main__':
    run_k_stocks_app()