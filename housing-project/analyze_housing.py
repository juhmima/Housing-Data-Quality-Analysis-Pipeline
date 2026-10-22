import pandas as pd
import sys

# Load csv file
csv_file=sys.argv[1] if len(sys.argv) > 1 else "housing.csv"
df = pd.read_csv(csv_file)

# Print rows + columns
# print(df.shape)
# Print rows + columns  nicely formatted
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

# Calculate mean, median  price
average_price = df['price'].mean()
print(f"Average housing price: ${average_price:,.2f}")
median_price = df['price'].median()
print(f"Median housing price: ${median_price:,.2f}")

# Find the most expensive house
highest_price = df['price'].max()
print(f"Highest value: ${highest_price:,.2f}")

# Find the average area
average_area = df['area'].mean()
print(f"Average area: {average_area:,.2f}")

# Calculate correlation between area and price
area_price_corr = df["area"].corr(df["price"])
print(f"Correlation between area and price: {area_price_corr}")
