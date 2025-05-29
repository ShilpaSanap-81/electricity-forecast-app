import streamlit as st
import pandas as pd
from modules.data_loader import load_all_data
from modules.feature_engineering import prepare_features
from modules.models import train_and_forecast
import plotly.express as px

st.title("⚡ Electricity Demand Forecasting - Maharashtra")

model_type = st.selectbox("Select a Model", ["Linear Regression", "SVR", "Random Forest"])
days = st.slider("Forecast Horizon (Days)", 1, 30, 7)

df = load_all_data()
features, target = prepare_features(df)
forecast_df = train_and_forecast(features, target, model_type, days)

st.subheader("Forecast")
st.dataframe(forecast_df)
fig = px.line(forecast_df, x='Date', y='Forecast')
st.plotly_chart(fig)
