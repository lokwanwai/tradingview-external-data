import yfinance as yf
from scraper.base_scraper import BaseScraper
import pandas as pd


class BTCVixRatioScraper(BaseScraper):
    """
    Source: Yahoo Finance
    BTCUSDT: UTC
    VIX: America/Chicago

    Transformed
    datetime: UTC 23:59:59(close of the day)
    BTCUSDT: close
    VIX: close
    """

    def __init__(self):
        super().__init__()

    def scrape_data(self, tickers):
        if self.is_full_run:
            df_raw = yf.download(tickers)['Close']
        else:
            df_raw = yf.download(tickers, period='30d')['Close']
        return df_raw

    def structuring_data(self):
        df = self.df_raw.ffill().copy()
        df_formatted = df.dropna().copy()
        df_formatted.index.rename('datetime', inplace=True)
        df_formatted.index = df_formatted.index.tz_localize('UTC')
        df_formatted.index = df_formatted.index + pd.Timedelta('23:59:59')
        df_formatted.reset_index(inplace=True)
        df_formatted.rename(
            columns={'BTC-USD': 'BTCUSDT', '^VIX': 'VIX'}, inplace=True)

        # filter data and get data only before self.today_utc
        df_formatted = df_formatted[df_formatted['datetime'] < self.today_utc]
        return df_formatted

    def run(self, full_run=False):
        if full_run:
            self.is_full_run = True
        self.df_raw = self.scrape_data(
            ['BTC-USD', '^VIX'])
        self.df_formatted = self.structuring_data()
        return self.df_formatted


if __name__ == "__main__":
    scraper = BTCVixRatioScraper()
    btc_vix_data = scraper.run()
    btc_vix_data
