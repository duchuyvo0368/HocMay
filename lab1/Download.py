import yfinance as yf

symbol = 'AAPL'
start = '2010-01-01'
end = '2023-02-14'

df = yf.download(symbol, start=start, end=end)
df.to_csv("data.csv")
