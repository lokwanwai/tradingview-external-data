from base_scraper import BaseScraper


class CryptoYouTuberViewScraper(BaseScraper):
    def __init__(self, crypto_name: str):
        super().__init__()
        self.crypto_name = crypto_name
        self.df_data = None

    def scrape_data(self):
        # Implement the scraping logic here
        pass

    def structuring_data(self):
        # Implement the data processing logic here
        pass
