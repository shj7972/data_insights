import streamlit as st
import pandas as pd
import requests
import plotly.express as px
from prophet import Prophet
import xml.etree.ElementTree as ET
from datetime import datetime

# Fetch data from the Seoul City API
def fetch_data(year, month, borough_code, service_key):
    all_data = []
    start = 1
    end = 1000
    max_records = 1000  # API limit

    while True:
        url = f"http://openapi.seoul.go.kr:8088/{service_key}/xml/tbLnOpendataRtmsV/{start}/{end}/{year}/{borough_code}"
        response = requests.get(url)

        if response.status_code == 200:
            # Parse XML
            root = ET.fromstring(response.content)
            response_data = []

            # Loop through each item in the XML and extract data
            for item in root.findall('.//row'):  # Adjust the path according to the XML structure
                deal_ymd = item.find('DEAL_YMD').text if item.find('DEAL_YMD') is not None else None
                obj_amt = item.find('OBJ_AMT').text if item.find('OBJ_AMT') is not None else None
                all_data.append({'DEAL_YMD': deal_ymd, 'OBJ_AMT': obj_amt})
                response_data.append({'DEAL_YMD': deal_ymd, 'OBJ_AMT': obj_amt})

            # If less than max_records, break the loop
            if len(response_data) < max_records:
                break

            # Update start and end for the next iteration
            start += max_records
            end += max_records
            # Convert list of dictionaries to DataFrame
            #return pd.DataFrame(data)
        else:
            print(f"Failed to fetch data: {response.status_code}")
            break

    return pd.DataFrame(all_data)


def run_real_estate_app():
    st.title("Seoul Real Estate Data and Forecasting")

    code_to_borough = {
    '11110': '종로구',
    '11140': '중구',
    '11170': '용산구',
    '11200': '성동구',
    '11215': '광진구',
    '11230': '동대문구',
    '11260': '중랑구',
    '11290': '성북구',
    '11305': '강북구',
    '11320': '도봉구',
    '11350': '노원구',
    '11380': '은평구',
    '11410': '서대문구',
    '11440': '마포구',
    '11470': '양천구',
    '11500': '강서구',
    '11530': '구로구',
    '11545': '금천구',
    '11560': '영등포구',
    '11590': '동작구',
    '11620': '관악구',
    '11650': '서초구',
    '11680': '강남구',
    '11710': '송파구',
    '11740': '강동구',
    '11410': '서대문구',
    '11410': '서대문구',
    '11410': '서대문구',
    }

    # Borough codes selection
    #borough_codes = ["11500", "11000", "11700"]  # Replace with actual codes
    borough_list = list(code_to_borough.keys())
    #selected_borough = st.selectbox("Select Borough Code", borough_codes)
    selected_borough = st.selectbox('Select a ticker', options=borough_list, format_func=lambda x: f"{x} - {code_to_borough[x]}")

    # Slider for forecast period
    forecast_period = st.slider("Select Forecast Period", 1, 12, 6)

    # Fetch and process data
    service_key = "6f6274765373686a37354158655944"
    #data_2022 = fetch_data("2022", selected_borough)
    #data_2023 = fetch_data("2023", selected_borough)
    # Fetch data from December 2022 to November 2023
    current_year = datetime.now().year
    current_month = datetime.now().month
    data = pd.DataFrame()

    for year in [current_year - 1, current_year]:
        for month in range(1, 13):
            if year == current_year - 1 and month < 12:
                continue
            if year == current_year and month > current_month:
                break
            month_data = fetch_data(year, month, selected_borough, service_key)
            data = pd.concat([data, month_data])

    # Now 'data' contains the combined data from Dec 2022 to Nov 2023

    # Assuming data_2022 and data_2023 are your DataFrames
    # Combine the data from 2022 and 2023
    #combined_data = pd.concat([data_2022, data_2023])
    combined_data = data

    # Ensure 'DEAL_YMD' is a datetime object
    combined_data['DEAL_YMD'] = pd.to_datetime(combined_data['DEAL_YMD'], format='%Y%m%d')

    # Extract year and month
    combined_data['Year'] = combined_data['DEAL_YMD'].dt.year
    combined_data['Month'] = combined_data['DEAL_YMD'].dt.month

    # Convert 'OBJ_AMT' to a numeric type for calculation, handling non-numeric values
    combined_data['OBJ_AMT'] = pd.to_numeric(combined_data['OBJ_AMT'], errors='coerce')

    # Group by year and month, then calculate the average
    monthly_averages = combined_data.groupby(['Year', 'Month'])['OBJ_AMT'].mean().reset_index()
    # Assuming 'monthly_averages' has a column 'OBJ_AMT' with average values
    monthly_averages['OBJ_AMT'] = monthly_averages['OBJ_AMT'].round(1)

    # Sort the DataFrame in descending order by 'Year' and 'Month'
    monthly_averages = monthly_averages.sort_values(by=['Year', 'Month'], ascending=[False, False])

    # Keep only the top 12 rows
    monthly_averages = monthly_averages.head(12)

    # Now, 'monthly_averages' contains the sorted and truncated data

    # Display the monthly averages
    #print(monthly_averages)

    # Visualization
    # Assuming 'monthly_averages' is your DataFrame with the required data
    # Ensure it's sorted and truncated as per your previous requirements

    # Create a line chart
    fig = px.line(
        monthly_averages, 
        x='Month', 
        y='OBJ_AMT', 
        color='Year', 
        title='Monthly Average Real Estate Transaction Prices',
        labels={'OBJ_AMT': 'Average Transaction Price', 'Month': 'Month', 'Year': 'Year'}
    )

    # Update x-axis to show month names or numbers as you prefer
    fig.update_xaxes(type='category')

    # Display the chart in Streamlit
    st.plotly_chart(fig)

    # Prophet forecasting
    # Assuming 'monthly_averages' is your DataFrame
    # Prepare the data for Prophet
    prophet_df = monthly_averages.rename(columns={'Month': 'ds', 'OBJ_AMT': 'y'})
    prophet_df['ds'] = prophet_df['Year'].astype(str) + '-' + prophet_df['ds'].astype(str) + '-01'  # Format as YYYY-MM-DD
    prophet_df['ds'] = pd.to_datetime(prophet_df['ds'])

    # Initialize and fit the model
    #model = Prophet()
    # Initialize the model with extra parameters for fine-tuning
    model = Prophet(
        changepoint_prior_scale=0.05,  # Adjust this for trend flexibility
        seasonality_prior_scale=10.0,  # Adjust this for seasonality flexibility
        yearly_seasonality=True,
        weekly_seasonality=False,
        daily_seasonality=False
    )
    # Add custom seasonality if applicable
    # model.add_seasonality(name='monthly', period=30.5, fourier_order=5)

    # Add holidays if they impact your data
    # model.add_country_holidays(country_name='KR')

    # Fit the model
    model.fit(prophet_df)

    # Create future DataFrame for the next N months
    # Assuming forecast_period is defined in your Streamlit app
    future = model.make_future_dataframe(periods=forecast_period, freq='M')

    # Predict
    forecast = model.predict(future)

    # Plot the forecast
    fig = model.plot(forecast)

    # Display the forecast in Streamlit
    st.plotly_chart(fig)

    # Display raw data
    st.write("Monthly Average Prices")
    st.dataframe(monthly_averages)
    #st.dataframe(data_2022)

if __name__ == "__main__":
    run_real_estate_app()
