import pandas as pd
import yfinance as yf
import config


def fetch_data():
    tickers = ["XLB", "XLE", "XLF", "XLI", "XLK", "XLP", "XLU", "XLV", "XLY"]
    df = yf.download(tickers, start="2020-06-09", end="2021-06-09")
    df = df["Adj Close"]
    df = df.pct_change()[1:]

    if df.isnull().values.any() == False:
        df.to_csv(config.TRAINING_FILE, index_label=False)
        print('No Null values found')
    else:
        print('Null values Found, clean data')


if __name__ == '__main__':
    fetch_data()