import pandas as pd 
import sys

# Title
print("===== HOUSING DATA QUALITY REPORT =====")

# Read file
csv_file = sys.argv[1] if len(sys.argv) > 1 else "housing.csv"
df = pd.read_csv(csv_file)

# Missing rows check
if len(df) == 0:
    print('The file has zero rows')
    sys.exit(1)
else:
    print(f'The file has {len(df)} rows.')

validation_passed = True

# Check to see if price and area columns exist
required_columns = {'price', 'area'}

if required_columns.issubset(df.columns):
    print("Required columns: PASS")
else:
    print("Required columns: FAIL")
    print("Required column(s) are missing") 
    sys.exit(1)

# Count missing cells
total_missing = df.isnull().sum().sum()
print(f"Total missing cells:{total_missing}")
if total_missing > 0:
    validation_passed = False
# Count total duplicate rows
duplicate_count = df.duplicated().sum()
print(f"\nTotal duplicate rows:{duplicate_count}")
if duplicate_count > 0:
    validation_passed = False 

# Detect invalid data
invalid_price_count = (df["price"] <= 0).sum()
print(f"Invalid prices: {invalid_price_count}")
if invalid_price_count > 0:
    validation_passed = False
invalid_area_count = (df["area"] <= 0).sum()
print(f"Invalid areas: {invalid_area_count}")
if invalid_area_count > 0:
    validation_passed = False 

# Validate categorical values
categorical_columns = [
    "mainroad",
    "guestroom",
    "basement",
    "hotwaterheating",
    "airconditioning",
    "prefarea"
]

for column in categorical_columns:
    unexpected_count = (~df[column].isin(["yes", "no"])).sum() 
    print(f"{column}: {unexpected_count} unexpected values")
    if unexpected_count > 0:
        validation_passed = False 
    
# Adding an overall PASS / FAIL result
if validation_passed:
    print("OVERALL RESULT: PASS")
    sys.exit(0)
else: 
    print("OVERALL RESULT: FAIL")
    sys.exit(1)


