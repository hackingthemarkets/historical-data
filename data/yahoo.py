import yfinance as yf

work = yf.Ticker("WORK")

# get historical market data
history = work.history(period="max")

# show pandas dataframe
print(history)

# show csv
print(history.to_csv())