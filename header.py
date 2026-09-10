import csv

fieldnames = [
    "price",
    "category",
    "year",
    "make",
    "mileage",
    "model",
    "fuel_type",
    "transmission",
    "engine_volume"
]

with open("data.csv", mode = "w",newline="", encoding="utf-8") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()