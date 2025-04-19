from abc import ABC, abstractmethod


class BaseScraper(ABC):
    def __init__(self):
        self.df_raw = None
        self.df_formatted = None
        pass

    @abstractmethod
    def scrape_data(self):
        pass

    @abstractmethod
    def structuring_data(self):
        pass

    @abstractmethod
    def run(self):
        pass
