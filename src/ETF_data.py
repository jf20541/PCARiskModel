import pandas as pd
import yfinance as yf
import config
from webscrape import SPYScraper


def fetch_data():
    """
    Collect all the SP500 Equities to a list
    Set index to Date and extract Adj Closing price
    """
    # tickers = ["SPY", "XLB", "XLE", "XLF", "XLI", "XLK", "XLP", "XLU", "XLV", "XLY"]
    tickers = SPYScraper.run()
    tickers = tickers.drop(["BF.B", "BRK.B"], axis=1)
    df = yf.download(tickers, start="2019-01-01", end="2021-05-27")
    df = df["Adj Close"]
    df.to_csv(config.TRAINING_FILE, index_label="Date")


if __name__ == "__main__":
    fetch_data()
