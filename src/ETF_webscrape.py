from bs4 import BeautifulSoup
import requests
import yfinance as yf
import pandas as pd
import config


class SPYScraper:
    """
    WebScrape the SP500 WikiTable using BeautifulSoup module
    Create an empty list and append all assets
    """

    def fetch(self, url):
        return requests.get(url)

    def parse(self, html):
        """
        Fetch the URL html code from Wikipedia
        Extract the ticker from the table and append to tickers empty list
        Use the yfinance package to get price data and save to csv file
        """
        soup = BeautifulSoup(html, "lxml")
        table = soup.find("table", {"class": "wikitable sortable"})

        tickers = []
        for row in table.findAll("tr")[1:]:
            ticker = row.findAll("td")[0].text
            tickers.append(ticker)

        tickers = [s.replace("\n", "") for s in tickers]
        df = yf.download(tickers, start="2019-01-01", end="2021-05-27")
        df.to_csv(config.SPY_DATA)

    def run(self):
        resonse = self.fetch(config.URL)
        self.parse(resonse.text)


if __name__ == "__main__":
    scraper = SPYScraper()
    scraper.run()
