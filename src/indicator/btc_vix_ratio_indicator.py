from indicator.base_indicator import BaseIndicator


class BTCVixRatioIndicator(BaseIndicator):
    """
    BTC VIX Ratio Indicator
    """

    def __init__(self):
        super().__init__()

    def calculate(self, data):
        """
        Calculate the BTC VIX Ratio.
        :return: DataFrame with the calculated indicators
        """
        df = data.copy()
        df['BTC_VIX_Ratio'] = df['BTCUSDT'] / df['VIX']
        df['BTC_VIX_Ratio_MA'] = df['BTC_VIX_Ratio'].rolling(
            window=30).mean().ffill()
        self.df_calculated = df
        print(df)
        return self.df_calculated
