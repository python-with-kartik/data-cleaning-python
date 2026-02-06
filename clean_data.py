import pandas as pd

# Load raw data
df = pd.read_csv("raw_data/same_messy.csv")

# ------------------ Cleaning Steps ------------------

# 1. Remove extra spaces and standardize text
df['name'] = df['name'].str.strip().str.title()
df['city'] = df['city'].str.strip().str.title()

# 2. Convert amount to numeric
df['amount'] = (
    df['amount']
    .astype(str)
    .str.replace('₹', '', regex=False)
    .str.replace(',', '', regex=False)
    .astype(int)
)

# 3. Standardize date format
df['date'] = pd.to_datetime(df['date'], errors='coerce').dt.strftime('%Y-%m-%d')

# 4. Remove duplicate rows
df = df.drop_duplicates()

# ------------------ Save Cleaned Data ------------------
df.to_csv("cleaned_data/cleaned_data.csv", index=False)

print("Data cleaning completed successfully ✅")
