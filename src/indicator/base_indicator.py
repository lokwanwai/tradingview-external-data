from abc import ABC


class BaseIndicator(ABC):
    """
    Base class for all indicators.
    """

    def __init__(self):
        pass

    def calculate(self, data):
        """
        Run the indicator.
        """
        pass
