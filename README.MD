# Turbo.az Car Price Predictor

An end-to-end Machine Learning pipeline and web scraping system designed to estimate second-hand automobile market values in Azerbaijan using data from [Turbo.az](https://turbo.az).

This project automates the entire workflow: from browser automation and data extraction using Playwright, to preprocessing, feature encoding, and model inference with `scikit-learn`.

---

## Key Features

* **Custom Web Scraper:** Built with Playwright to handle DOM interactions and bypass rate limits smoothly.
* **Structured Data Extraction:** Targets pre-cleaned HTML metadata (`#catfish` data attributes) for consistent feature extraction across different car makes and models.
* **Automated Data Pipeline:** Uses `ColumnTransformer` and `Pipeline` objects to execute numeric imputation and categorical encoding in a single pass.
* **Predictive AI Engine:** Implements a `RandomForestRegressor` tuned for non-linear depreciation curves and high-dimensional categorical features.
* **Robust Error Handling:** Prevents script crashes during scraping via `domcontentloaded` wait strategies and handles unseen test categories gracefully during model inference.

---

## Dataset & Features

The dataset is built by scraping active listings from Turbo.az and extracting structured properties:

| Feature Name | Type | Description |
| :--- | :--- | :--- |
| `price` | Target (Numeric) | Listing price in Azerbaijani Manat (AZN) |
| `make` | Categorical | Vehicle brand (e.g., Hyundai, Mercedes, Lexus) |
| `model` | Categorical | Specific model series (e.g., Santa Fe, E 220, CT 200h) |
| `year` | Numeric | Production year |
| `mileage` | Numeric | Total distance driven (in kilometers) |
| `engine_volume` | Numeric | Engine displacement (in cc, e.g., 2000 for 2.0L) |
| `category` | Categorical | Body type (e.g., Sedan, SUV, Hetçbek) |
| `fuel_type` | Categorical | Fuel system (e.g., Benzın, Dizel, Hibrid) |
| `transmission` | Categorical | Gearbox type (e.g., Avtomat, Mexaniki) |