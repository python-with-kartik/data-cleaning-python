import pandas as pd

#Load raw data
df = pd.read_csv('raw_data/sales_messy.csv')
print(df.to_string())

# # ------------------ Cleaning Steps ------------------
#
# # 1.Removed Remark column as clint did not want this column
# df.drop(columns=['Remarks'], inplace=True)
#
# # 2. Changed column names as clint wanted
# df.columns = ['name', 'amount', 'city', 'date']
#
# # 3. Removed rows which contained empty in name and city columns as clint asked
# df.dropna(subset=['name','city'], inplace=True,ignore_index=True)
#
# # 4. Standardize date format
# df['date'] = df.date.apply(lambda x:pd.to_datetime(x).strftime("%y-%m-%d"))
#
# # 5. Remove extra spaces and standardize text
# df['city'] = df['city'].str.strip().str.title()
# df['name'] = df['name'].str.strip().str.title()
#
# # 6. Removed extra spaces, commas and ₹ sign and standardize amount
# df['amount'] = df['amount'].str.strip('₹').str.replace(',', '').str.strip()
#
#
# # 7. Converting amount in words to amount in numbers
# def word_to_number(text):
#     words = text.lower().split()
#
#     numbers = {
#         "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
#         "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
#         "ten": 10, "eleven": 11, "twelve": 12
#     }
#
#     multipliers = {
#         "hundred": 100,
#         "thousand": 1000
#     }
#
#     total = 0
#     current = 0
#
#     for word in words:
#         if word in numbers:
#             current += numbers[word]
#         elif word in multipliers:
#             current *= multipliers[word]
#             total += current
#             current = 0
#         else:
#             return None  # unclear word → reject
#
#     return total + current
#
# for index, row in df.iterrows():
#     if word_to_number(row['amount']) is None:
#         pass
#     else:
#         a = word_to_number(row['amount'])
#         df.loc[index, 'amount'] = str(a)
#
# # 8. Removed duplicate rows
# df.drop_duplicates(inplace=True,ignore_index=True)
#
# # 9. Removed rows with typo in names but amount, city and date columns are same
# df.drop_duplicates(subset=['amount', 'city', 'date'],inplace=True,ignore_index=True)
#
#
# # 10. Converting amount column to integer form from string form
# df['amount'] = df['amount'].astype(int)
# print(df.to_string())
#
# # 11. Information about the cleaned data set
# print(df.info())
#
# # ------------------ Save Cleaned Data ------------------
#
# df.to_csv('cleaned_data/cleaned_data.csv', index=False)
# print("Data cleaning completed successfully ✅")