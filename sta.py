import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Define the stock ticker and the time period
ticker = "AAPL"
start_date = "2020-01-01"
end_date = "2023-01-01"

# Fetch the stock data
stock_data = yf.download(ticker, start=start_date, end=end_date)

# Display the first few rows of the data
print("Stock data:")
print(stock_data.head())

# Calculate the moving averages
stock_data['MA50'] = stock_data['Close'].rolling(window=50).mean()
stock_data['MA200'] = stock_data['Close'].rolling(window=200).mean()

# Display the first few rows to see the new columns
print("\nStock data with moving averages:")
print(stock_data.head())

# Plot the closing price and the moving averages
plt.figure(figsize=(14, 7))
plt.plot(stock_data['Close'], label='Closing Price')
plt.plot(stock_data['MA50'], label='50-Day MA')
plt.plot(stock_data['MA200'], label='200-Day MA')
plt.title(f'{ticker} Stock Price and Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()

# Calculate Bollinger Bands
stock_data['20 Day MA'] = stock_data['Close'].rolling(window=20).mean()
stock_data['20 Day STD'] = stock_data['Close'].rolling(window=20).std()
stock_data['Upper Band'] = stock_data['20 Day MA'] + (stock_data['20 Day STD'] * 2)
stock_data['Lower Band'] = stock_data['20 Day MA'] - (stock_data['20 Day STD'] * 2)

# Plot Bollinger Bands
plt.figure(figsize=(14, 7))
plt.plot(stock_data['Close'], label='Closing Price')
plt.plot(stock_data['Upper Band'], label='Upper Bollinger Band', linestyle='--')
plt.plot(stock_data['Lower Band'], label='Lower Bollinger Band', linestyle='--')
plt.title(f'{ticker} Bollinger Bands')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")