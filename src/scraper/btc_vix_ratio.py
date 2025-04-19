from base_scraper import BaseScraper
import pandas as pd
import yfinance as yf


class BTCVixRatioScraper(BaseScraper):
    def __init__(self):
        super().__init__()

    def scrape_data(self, tickers):
        """
        從 Yahoo Finance 抓取多個資產的歷史收盤價。
        :param tickers: 例如 ['BTC-USD', '^VIX']
        :param start: 'YYYY-MM-DD'
        :param end: 'YYYY-MM-DD'
        :return: DataFrame，每列為日期，每欄為收盤價
        """
        df_bronze = yf.download(tickers)['Close']
        return df_bronze

    def structuring_data(self):
        df = self.df_bronze.ffill()
        df_silver = df.dropna()
        return df_silver

    def calculate_btc_vix_ratio(self):
        """
        計算BTC/VIX比值
        :param df: 含BTC-USD與^VIX兩欄的DataFrame
        :return: 新DataFrame，新增一欄'BTC_VIX_Ratio'
        """
        gold_data = self.df_silver.copy()
        gold_data['BTC_VIX_Ratio'] = gold_data['BTC-USD'] / gold_data['^VIX']
        return gold_data

    def run(self):
        self.df_bronze = self.scrape_data(['BTC-USD', '^VIX'])
        self.df_silver = self.structuring_data()
        self.df_gold = self.calculate_btc_vix_ratio()
        return self.df_gold


if __name__ == "__main__":
    scraper = BTCVixRatioScraper()
    btc_vix_data = scraper.run()
    print(btc_vix_data)
