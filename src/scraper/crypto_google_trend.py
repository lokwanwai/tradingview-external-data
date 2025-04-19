from src.scraper.base_scraper import BaseScraper


class CryptoGoogleTrendScraper(BaseScraper):
    def __init__(self, crypto_name: str):
        super().__init__()
        self.crypto_name = crypto_name
        self.df_data = None

    def scrape_data(self):
        pass

    def structuring_data(self):
        # Implement the data processing logic here
        pass
