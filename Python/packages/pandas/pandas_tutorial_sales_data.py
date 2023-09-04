import pandas as pd
# Load data into a Pandas DataFrame
df = pd.read_csv('sales_data.csv')
# Drop rows with missing values
df.dropna(inplace=True)
# Convert 'Revenue' to float
df['Revenue'] = df['Revenue'].astype(float)
# Group data by 'Month' and sum 'Revenue'
monthly_sales = df.groupby('Month')['Revenue'].sum()

# Find the most profitable month
most_profitable_month = monthly_sales.idxmax()
print(f"The most profitable month is {most_profitable_month}.")

# Group data by 'Product' and sum 'Revenue'
product_sales = df.groupby(by='Product')['Revenue'].sum()

# Find the best-selling product
best_selling_product = product_sales.idxmax()
print(f"The best-selling product is {best_selling_product}.")
import matplotlib.pyplot as plt

# Plotting
plt.bar(monthly_sales.index, monthly_sales)
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.title('Monthly Sales Data')
plt.show()
