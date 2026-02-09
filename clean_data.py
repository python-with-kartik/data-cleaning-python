import pandas as pd
import numpy as np

def word_to_number(text):
    words = text.lower().split()

    numbers = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
        "ten": 10, "eleven": 11, "twelve": 12
    }

    multipliers = {
        "hundred": 100,
        "thousand": 1000
    }

    total = 0
    current = 0

    for word in words:
        if word in numbers:
            current += numbers[word]
        elif word in multipliers:
            current *= multipliers[word]
            total += current
            current = 0
        else:
            return None  # unclear word → reject

    return total + current

#Load raw data
df = pd.read_csv('raw_data/sales_messy.csv')

# ------------------ Cleaning Steps ------------------

# 1.Standardize Column names
df.columns = (df.columns.str.strip()).str.lower().str.replace(' ', '_').str.replace('-', '_')

# 2. Removed rows which contained empty in order_id, customer_name, order_date and sales_amount columns
df.dropna(subset=['order_id','customer_name','order_date','sales_amount'], inplace=True,ignore_index=True)

# 3. Standardize date format to YYYY-MM-DD format
df['order_date'] = df.order_date.apply(lambda x:pd.to_datetime(x,dayfirst=True, errors='coerce'))

# 4. Clean text columns
df['city'] = df['city'].str.strip().str.title()
df['customer_name'] = df['customer_name'].str.strip().str.title().str.strip('$').str.replace(r"\s+"," ",regex=True)
df['payment_mode'] = df['payment_mode'].str.strip().str.lower()
df['remarks'] = df['remarks'].str.strip().str.lower()

# 5. Removed extra spaces, commas and ₹ sign and standardize amount
df['sales_amount'] = df['sales_amount'].str.strip('₹$INR').str.replace(',', '').str.strip()

# 6. Converting amount in words to amount in numbers
for index, row in df.iterrows():
    if word_to_number(row['sales_amount']) is None:
        pass
    else:
        a = word_to_number(row['sales_amount'])
        if a > 0:
            df.loc[index, 'sales_amount'] = str(a)
        else:
            df.loc[index, 'sales_amount'] = np.nan

# 7. Removed duplicate rows
df.drop_duplicates(inplace=True,ignore_index=True)

# 8. Drop rows which holds sales amount less than or equal to 0
df.dropna(subset=['sales_amount'], inplace=True)

# 9. Filling empty items with 'Unknown' in payment_mode and city and with 'no remarks' in remark column
df.fillna({'remarks': 'no remarks', 'payment_mode': 'Unknown', 'city': 'Unknown'}, inplace=True)

# 10. Fix data types
df['order_id'] = df['order_id'].astype(int)
df['sales_amount'] = df['sales_amount'].astype(int)
print(df.to_string())

# 11. Information about the cleaned data set
print(df.info())

# ------------------ Save Cleaned Data ------------------

# Save cleaned data
df.to_csv('cleaned_data/cleaned_data.csv', index=False)
print("Data cleaning completed successfully ✅")