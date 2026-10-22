import pandas as pd
import matplotlib.pyplot as plt
import sys

csv_file=sys.argv[1] if len(sys.argv) > 1 else "housing.csv"
df = pd.read_csv(csv_file)

# Create histogram
df['price'].hist(bins=20, edgecolor='black')
# Add titles / labels
plt.title('Distribution of Prices') 
plt.xlabel('House Price ($)')
plt.ylabel('Number of Houses') 
# Display the plot 
plt.savefig('housing_price_distribution.png')
plt.show()
# Print confirmation message
print("Histogram saved successfully!")
