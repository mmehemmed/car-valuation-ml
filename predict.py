from ai import model_pipeline
import pandas as pd


def predict_price(car_specs):
    df = pd.DataFrame([car_specs])

    price_prediction = model_pipeline.predict(df)[0]
    return price_prediction

sample_car = {
    "category": "Sedan",
    "year": 2013,
    "make": "mercedes",
    "mileage": 120000,
    "model": "c-250",
    "fuel_type": "Benzin",
    "transmission": "Avtomat (AT)",
    "engine_volume": 1800
}

print(predict_price(sample_car))