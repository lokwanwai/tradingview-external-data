from src.scraper.base_scraper import BaseScraper


class DataHandler:
    def __init__(self, scraper: BaseScraper, config: dict):
        self.scraper = scraper
        self.config = config
        self.old_data = None
        self.new_data = None
        self.script = None

    def append_data(self, new_data):
        pass

    def save_data_csv(self, file_path):
        with open(file_path, 'w') as file:
            file.write(self.data)
        print(f"Data saved to {file_path}")

    def load_data_csv(self, file_path):
        with open(file_path, 'r') as file:
            self.data = file.read()
        print(f"Data loaded from {file_path}")

    def generate_pinescript():
        pass

    def save_pinescript():
        pass
