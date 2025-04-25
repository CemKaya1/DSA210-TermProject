import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from scipy.stats import ttest_ind, sem, pearsonr

# Load dataset
df = pd.read_csv("aaa.csv")

# --- 1. Univariate Analysis ---
plt.figure(figsize=(14, 6))

# Log Price Distribution
plt.subplot(1, 2, 1)
sns.histplot(df['log_price'], kde=True).set(title='Distribution of Log Price')
mean_price = df['log_price'].mean()
median_price = df['log_price'].median()
plt.figtext(0.15, 0.85, f"Mean: {mean_price:.2f}\nMedian: {median_price:.2f}", fontsize=12)

# Log Mileage Distribution
plt.subplot(1, 2, 2)
sns.histplot(df['log_mileage'], kde=True).set(title='Distribution of Log Mileage')
mean_mileage = df['log_mileage'].mean()
median_mileage = df['log_mileage'].median()
plt.figtext(0.65, 0.85, f"Mean: {mean_mileage:.2f}\nMedian: {median_mileage:.2f}", fontsize=12)

plt.tight_layout()
plt.show()

# --- 2. Price by Brand Classification ---
plt.figure(figsize=(8, 5))
sns.boxplot(x='brand_classification', y='price', data=df)
plt.title("Price by Brand Classification")
plt.yscale('log')  # For visibility
mean_price_brand = df.groupby('brand_classification')['price'].mean()
median_price_brand = df.groupby('brand_classification')['price'].median()
plt.figtext(0.15, 0.85, f"Mean: {mean_price_brand.mean():.2f}\nMedian: {median_price_brand.mean():.2f}", fontsize=12)
plt.show()

# --- 3. Scatter & Regression Plot: Price vs. Mileage ---
plt.figure(figsize=(10, 6))
sns.lmplot(x='mileage', y='price', hue='brand_classification', data=df, 
           height=6, aspect=1.5, scatter_kws={'alpha':0.5}, lowess=True)
plt.title("Price vs. Mileage with Regression by Brand Classification")
plt.yscale('log')
plt.xscale('log')

# Loop through each brand and calculate Pearson correlation coefficient
for brand in df['brand_classification'].unique():
    sub_df = df[df['brand_classification'] == brand]
    corr, p_value = pearsonr(sub_df['mileage'], sub_df['price'])
    
    # Annotate the plot with the correlation coefficient for each brand
    plt.annotate(f'{brand}: Pearson={corr:.2f}, p-value={p_value:.2e}', 
                 xy=(0.5, 0.9 - 0.05 * np.arange(len(df['brand_classification'].unique()))[list(df['brand_classification'].unique()).index(brand)]), 
                 xycoords='axes fraction', fontsize=12, ha='center')

plt.show()

# --- 4. Correlation Matrix (What affects price the most?) ---
corr = df[['price', 'mileage', 'car_age', 'price_per_km']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

# --- 5. Price Sensitivity Regression by Brand ---
brand_slopes = {}
for brand in df['brand'].unique():
    sub_df = df[df['brand'] == brand]
    if len(sub_df) > 10:  # avoid tiny sample bias
        X = sm.add_constant(sub_df['mileage'])
        model = sm.OLS(sub_df['price'], X).fit()
        brand_slopes[brand] = model.params['mileage']

slopes_df = pd.DataFrame(brand_slopes.items(), columns=['brand', 'price_mileage_slope'])
slopes_df['abs_slope'] = slopes_df['price_mileage_slope'].abs()
slopes_df.sort_values('abs_slope', inplace=True)

plt.figure(figsize=(12, 6))
sns.barplot(data=slopes_df, x='brand', y='price_mileage_slope')
plt.xticks(rotation=45)
plt.title("Price Sensitivity to Mileage by Brand (Slope of Price ~ Mileage)")
plt.axhline(0, color='gray', linestyle='--')

# Display brand-specific slope statistics
mean_slope = slopes_df['price_mileage_slope'].mean()
median_slope = slopes_df['price_mileage_slope'].median()
plt.figtext(0.15, 0.85, f"Mean Slope: {mean_slope:.2f}\nMedian Slope: {median_slope:.2f}", fontsize=12)

plt.tight_layout()
plt.show()

# --- 6. Fair Price Estimator Using Key Attributes ---
features = ['mileage', 'car_age']
X = df[features]
y = df['price']

model = LinearRegression().fit(X, y)
df['predicted_price'] = model.predict(X)
df['residual'] = df['price'] - df['predicted_price']

# --- 7. Visual: Actual vs Predicted ---
plt.figure(figsize=(8, 5))
sns.scatterplot(x=df['predicted_price'], y=df['price'], alpha=0.6)
plt.plot([df['price'].min(), df['price'].max()], [df['price'].min(), df['price'].max()], 'r--')
plt.xlabel("Predicted Price")
plt.ylabel("Actual Price")
plt.title("Actual vs Predicted Prices")

# Calculate R2 score and Mean Squared Error
r2 = r2_score(df['price'], df['predicted_price'])
mse = mean_squared_error(df['price'], df['predicted_price'])
plt.figtext(0.15, 0.85, f"R2 Score: {r2:.2f}\nMSE: {mse:.2f}", fontsize=12)

plt.show()

# --- 8. Overpriced / Underpriced Detection ---
plt.figure(figsize=(12, 5))
sns.histplot(df['residual'], kde=True)
plt.title("Residual Distribution (Underpriced vs Overpriced)")
plt.axvline(0, color='red', linestyle='--')

# Show residual stats
mean_residual = df['residual'].mean()
median_residual = df['residual'].median()
plt.figtext(0.15, 0.85, f"Mean Residual: {mean_residual:.2f}\nMedian Residual: {median_residual:.2f}", fontsize=12)

plt.show()

# Flag listings
df['pricing_status'] = df['residual'].apply(
    lambda x: 'underpriced' if x > 3000 else ('overpriced' if x < -3000 else 'fair'))

print(df['pricing_status'].value_counts())

# --- 9. Price Sensitivity t-test and Pearson Correlation ---
# Create price sensitivity slope for each brand
brand_slopes = {}
for brand in df['brand'].unique():
    sub_df = df[df['brand'] == brand]
    if len(sub_df) > 10:
        X = sm.add_constant(sub_df['mileage'])
        model = sm.OLS(sub_df['price'], X).fit()
        brand_slopes[brand] = model.params['mileage']

slope_df = pd.DataFrame(brand_slopes.items(), columns=['brand', 'price_sensitivity'])

# Merge with brand classification info
merged_df = pd.merge(slope_df, df[['brand', 'brand_classification']].drop_duplicates(), on='brand')

# Add price sensitivity for each car
df = pd.merge(df, merged_df[['brand', 'price_sensitivity']], on='brand', how='left')

# Group data for luxury and economy cars
luxury_df = df[df['brand_classification'] == 'luxury']
economy_df = df[df['brand_classification'] == 'economy']

# --- Check for NaN or constant values ---
luxury_sensitivity = luxury_df['price_sensitivity']
economy_sensitivity = economy_df['price_sensitivity']

luxury_prices = luxury_df['price']
economy_prices = economy_df['price']

# Check for NaN values in price sensitivity
if luxury_sensitivity.isnull().any() or economy_sensitivity.isnull().any():
    print("Warning: NaN values found in price sensitivity data. Removing rows with NaN values.")
    luxury_df = luxury_df.dropna(subset=['price_sensitivity'])
    economy_df = economy_df.dropna(subset=['price_sensitivity'])

    luxury_sensitivity = luxury_df['price_sensitivity']
    economy_sensitivity = economy_df['price_sensitivity']
    luxury_prices = luxury_df['price']
    economy_prices = economy_df['price']

# Check if the price sensitivity values are constant
if luxury_sensitivity.nunique() <= 1 or economy_sensitivity.nunique() <= 1:
    print("Warning: Constant values found in price sensitivity data. Adjusting calculations.")
    # Handle the case where price sensitivity is constant (e.g., you might want to skip correlation or modify hypothesis)
    luxury_corr, luxury_p_val = None, None
    economy_corr, economy_p_val = None, None
else:
    # --- Perform One-Sided t-Test ---
    t_stat, p_value = ttest_ind(luxury_sensitivity, economy_sensitivity, alternative='less', equal_var=False)

    # --- Pearson Correlation for Price Sensitivity and Price ---
    luxury_corr, luxury_p_val = pearsonr(luxury_prices, luxury_sensitivity)
    economy_corr, economy_p_val = pearsonr(economy_prices, economy_sensitivity)

# --- Summary and Plotting ---
summary_df = pd.DataFrame({
    'Brand Classification': ['Luxury', 'Economy'],
    'Mean Sensitivity': [luxury_sensitivity.mean(), economy_sensitivity.mean()],
    'Standard Error': [sem(luxury_sensitivity), sem(economy_sensitivity)]
})

plt.figure(figsize=(8, 5))
barplot = sns.barplot(x='Brand Classification', y='Mean Sensitivity',
                      data=summary_df, palette='Set2')

# Add error bars manually
for i, row in summary_df.iterrows():
    plt.errorbar(x=i,
                 y=row['Mean Sensitivity'],
                 yerr=row['Standard Error'],
                 fmt='none',
                 ecolor='black',
                 capsize=5)

# Annotate p-value for t-test
plt.text(0.5, max(summary_df['Mean Sensitivity']) + 0.0001,
         f"p-value = {p_value:.4f}" if p_value is not None else "p-value = N/A",
         ha='center', fontsize=10, color='black')

plt.axhline(0, color='gray', linestyle='--')
plt.title("Brand Classification Price Sensitivity (Mean and Standard Error)")
plt.show()

