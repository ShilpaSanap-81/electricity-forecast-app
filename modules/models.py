import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor

def train_and_forecast(X, y, model_type, forecast_days):
    if model_type == "Linear Regression":
        model = LinearRegression()
    elif model_type == "SVR":
        model = SVR()
    else:
        model = RandomForestRegressor(n_estimators=100)

    model.fit(X, y)
    future_X = X.iloc[-forecast_days:]
    preds = model.predict(future_X)
    forecast_df = pd.DataFrame({
        "Date": pd.date_range(start=pd.Timestamp.today(), periods=forecast_days),
        "Forecast": preds
    })
    return forecast_df
