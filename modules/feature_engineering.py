def prepare_features(df):
    features = df[['Temp', 'Humidity', 'GDP', 'is_holiday', 'is_weekend']]
    target = df['Demand']
    return features, target
