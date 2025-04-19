from abc import ABC, abstractmethod


class BaseScraper(ABC):
    df_data = None

    def __init__(self):
        pass

    @abstractmethod
    def scrape_data(self):
        pass

    @abstractmethod
    def structuring_data(self):
        pass
