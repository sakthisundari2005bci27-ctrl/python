import yfinance as yf
import matplotlib.pyplot as plt

def plot_stock(ticker):
    data = yf.download(ticker, start="2023-01-01", end="2023-12-31")
    data['Close'].plot(title=f"{ticker} Stock Price")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.show()

# plot_stock("AAPL")
