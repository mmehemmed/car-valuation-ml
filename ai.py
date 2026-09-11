import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error, r2_score


df = pd.read_csv("data.csv")


numeric_cols = ["price", "year", "mileage", "engine_volume"]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Drop rows missing the target variable
df = df.dropna(subset=["price"])


X = df[["category", "year", "make", "mileage", "model", "fuel_type", "transmission", "engine_volume"]]
y = df["price"]


categorical_features = ["category", "make", "model", "fuel_type", "transmission"]
numeric_features = ["year", "mileage", "engine_volume"]

numeric_transformer = SimpleImputer(strategy="median")
categorical_transformer = OneHotEncoder(handle_unknown="ignore", sparse_output=False)


preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features),
    ]
)


model_pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("regressor", RandomForestRegressor(n_estimators=100, random_state=42)),
    ]
)

# Train / Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42 # 80% of data used for training, 20% used for testing
)

model_pipeline.fit(X_train, y_train)
predictions = model_pipeline.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print(f"Average Price Error (MAE): {mae:.2f} AZN")
print(f"Model Accuracy (R² Score): {r2:.2f}")