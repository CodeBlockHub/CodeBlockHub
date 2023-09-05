import pandas as pd
import sys
from os.path import dirname
sys.path.append(dirname(__file__))

# Read the stock data
df = pd.read_csv('stock_data.csv', parse_dates=['Date'])
import matplotlib.pyplot as plt

# Basic Line Plot
plt.plot(df['Date'], df['Close'])
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.title('Stock Closing Prices')
plt.show()
# Multiple Line Plots
plt.plot(df['Date'], df['High'], label='High Price')
plt.plot(df['Date'], df['Low'], label='Low Price')
plt.plot(df['Date'], df['Close'], label='Close Price')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Stock Prices')
plt.legend()
plt.show()
# Calculate Moving Averages
df['20_day_avg'] = df['Close'].rolling(window=20).mean()
df['50_day_avg'] = df['Close'].rolling(window=50).mean()

# Plot Moving Averages
plt.plot(df['Date'], df['Close'], label='Close Price')
plt.plot(df['Date'], df['20_day_avg'], label='20-Day Avg')
plt.plot(df['Date'], df['50_day_avg'], label='50-Day Avg')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Stock Prices with Moving Averages')
plt.legend()
plt.show()
# Find Maximum Close Price
max_close = df['Close'].max()
date_max_close = df[df['Close'] == max_close]['Date'].iloc[0]

# Annotations
plt.plot(df['Date'], df['Close'], label='Close Price')
plt.annotate(f'Max: {max_close}', xy=(date_max_close, max_close), xytext=(date_max_close, max_close+10),
             arrowprops=dict(facecolor='red', arrowstyle='->'),
             fontsize=9, color='red')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Stock Closing Prices with Annotation')
plt.show()
