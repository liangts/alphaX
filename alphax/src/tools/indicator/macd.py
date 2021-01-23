"""Get MACD indicator."""
import pandas as pd
import matplotlib.pyplot as plt
from pandas.core.frame import DataFrame
from alphax.src.api.base import BaseAPI, TimeSeriesAPI, TechIndicatorsAPI
from copy import copy, deepcopy

class MACD:
    """ Return the moving average convergence/divergence time series in two
    json objects as data and meta_data. It raises ValueError when problems
    arise

    Keyword Arguments:
        symbol:  the symbol for the equity we want to get its data
        interval:  time interval between two conscutive values,
            supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
            'weekly', 'monthly' (default 'daily'
        series_type:  The desired price type in the time series. Four types
            are supported: 'close', 'open', 'high', 'low' (default 'close')
        fastperiod:  Positive integers are accepted (default=None)
        slowperiod:  Positive integers are accepted (default=None)
        signalperiod:  Positive integers are accepted (default=None)
    """

    def __init__(self, symbol) -> None:
        # Attrs for alpha vantage api
        self.symbol = symbol
        self.interval = "daily"
        self.series_type = "close"
        self.fastperiod = None
        self.slowperiod = None
        self.signalperiod = None
        self.ti = TechIndicatorsAPI()

    def get_MACD(self):
        return self.ti.api_delegation("get_macd", symbol=self.symbol, interval=self.interval,
                                      series_type=self.series_type, fastperiod=self.fastperiod,
                                      slowperiod=self.slowperiod, signalperiod=self.signalperiod)

    def plot(self, df: DataFrame, **kwargs):
        time_start = kwargs.get("time_start")
        time_end = kwargs.get("time_end")
        title = kwargs.get("title")
        cols= kwargs.get("cols")

        if time_start:
            df = df[:time_start]
        if time_end:
            df = df[time_end:]
        if cols:
            df[cols].plot()
        else:
            df.plot()
        if title:
            plt.title(title)
        plt.show()

if __name__ == "__main__":
    macd = MACD("AAPL")
    df, metadata = macd.get_MACD()
    macd.plot(df)