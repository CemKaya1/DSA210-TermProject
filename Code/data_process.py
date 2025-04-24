import pandas as pd
import numpy as np

# Load datasets
df1 = pd.read_csv("used_cars_data.csv")
df2 = pd.read_csv("train.csv") 

# Working on df1
df = df1.copy()

# Feature engineering: Creating car age from manufacture year (current year: 2025)
df['car_age'] = 2025 - df['year']

# Changing the names and cleaning price and mileage columns
df.rename(columns={'price (eur)': 'price', 'mileage (kms)': 'mileage'}, inplace=True)
df['price'] = pd.to_numeric(df['price'], errors='coerce')
df['mileage'] = pd.to_numeric(df['mileage'], errors='coerce')

# Feature engineering: Building price per km feature
df['price_per_km'] = df['price'] / df['mileage']

# Future engineering: Classifying brands into economy, luxury, performance
luxury_brands = ['BMW', 'Mercedes-Benz', 'Audi', 'Lexus']
performance_brands = ['Porsche', 'Tesla', 'Alfa Romeo']
economy_brands = ['Toyota', 'Honda', 'Ford', 'Hyundai', 'Kia', 'Opel', 'SEAT', 'Volkswagen', 'Renault', 'Peugeot']

def classify_brand(brand):
    if brand in luxury_brands:
        return 'luxury'
    elif brand in performance_brands:
        return 'performance'
    elif brand in economy_brands:
        return 'economy'
    else:
        return 'unknown'

df['brand_classification'] = df['brand'].apply(classify_brand)

# Data Cleaning: Drop rows with unknown brand classifications
df = df[df['brand_classification'] != 'unknown']

# Feature Engineering: Apply log transformation to price and mileage
df['log_price'] = np.log1p(df['price'])
df['log_mileage'] = np.log1p(df['mileage'])

# Save to CSV
df.to_csv("processed_used_cars.csv", index=False)
