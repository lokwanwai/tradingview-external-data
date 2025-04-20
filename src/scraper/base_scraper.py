from abc import ABC, abstractmethod
import datetime


class BaseScraper(ABC):
    def __init__(self):
        self.df_raw = None
        self.df_formatted = None
        self.is_full_run = False
        self.today_utc = datetime.datetime.now(tz=datetime.timezone.utc)
        pass

    @abstractmethod
    def scrape_data(self):
        pass

    @abstractmethod
    def structuring_data(self):
        pass

    @abstractmethod
    def run(self, full_run=False):
        pass
