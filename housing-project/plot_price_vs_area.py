import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import sys 

csv_file=sys.argv[1] if len(sys.argv) > 1 else "housing.csv"
df = pd.read_csv(csv_file)

# Define x and y
x = df['area']
y = df['price']

# Calculate line of best fit
slope, intercept = np.polyfit(x, y, deg=1)

# Generate x-values for a smooth, straight line
x_line = np.linspace(x.min(), x.max(), 100)

# Calculate predicted prices for those x-values
best_fit_line = slope * x_line + intercept

# Create scatterplot
ax = df.plot.scatter(x='area', y='price', color='blue', grid=True)

# Plot best fit line on top + correlation
ax.plot(x_line, best_fit_line, color='red', linewidth=2,
        label=f'Best Fit: y = {slope:.2f}x + {intercept:.2f}')
correlation = x.corr(y)
ax.text(0.05, 0.95, f'Correlation: {correlation:.3f}',
        transform=ax.transAxes, va='top')

# Display scatterplot
plt.title('House Prices vs. Area')
plt.xlabel('Area (square feet)')
plt.ylabel('Price ($)')
ax.legend()
plt.savefig('housing_price_vs_area.png')
plt.show()
