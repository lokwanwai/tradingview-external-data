import yfinance as yf
from scraper.base_scraper import BaseScraper


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
        df_raw = yf.download(tickers)['Close']
        return df_raw

    def structuring_data(self):
        df = self.df_raw.ffill()
        df_formatted = df.dropna()
        df_formatted.index.rename('datetime', inplace=True)
        df_formatted.reset_index(inplace=True)
        df_formatted.rename(
            columns={'BTC-USD': 'BTCUSDT', '^VIX': 'VIX'}, inplace=True)
        return df_formatted

    def run(self):
        self.df_raw = self.scrape_data(['BTC-USD', '^VIX'])
        self.df_formatted = self.structuring_data()
        return self.df_formatted


if __name__ == "__main__":
    scraper = BTCVixRatioScraper()
    btc_vix_data = scraper.run()
    print(btc_vix_data)
