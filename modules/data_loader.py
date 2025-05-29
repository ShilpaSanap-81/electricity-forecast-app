import pandas as pd
import requests
import holidays

def load_demand_data():
    return pd.read_csv("data/electricity_demand.csv", parse_dates=['Date'])

def load_gdp_data():
    return pd.read_csv("data/maharashtra_gdp.csv")

def load_weather_data():
    api_key = "your_openweather_api_key"  # Replace with st.secrets["OPENWEATHER_API_KEY"]
    url = f"http://api.openweathermap.org/data/2.5/weather?q=Mumbai&appid={api_key}&units=metric"
    response = requests.get(url).json()
    return {
        'temp': response['main']['temp'],
        'humidity': response['main']['humidity'],
        'weather': response['weather'][0]['main']
    }

def load_calendar_features(dates):
    holiday_set = holidays.India()
    return dates.apply(lambda d: {
        "is_holiday": d in holiday_set,
        "is_weekend": d.weekday() >= 5
    }).apply(pd.Series)

def load_all_data():
    df = load_demand_data()
    gdp = load_gdp_data()
    weather = load_weather_data()
    cal = load_calendar_features(df['Date'])

    df = pd.concat([df, cal], axis=1)
    df['GDP'] = gdp['GDP'].iloc[-1]
    df['Temp'] = weather['temp']
    df['Humidity'] = weather['humidity']
    return df
