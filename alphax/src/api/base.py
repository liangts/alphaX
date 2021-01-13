import abc
import pandas as pd
import matplotlib.pyplot as plt
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.foreignexchange import ForeignExchange
from alpha_vantage.fundamentaldata import FundamentalData
from alpha_vantage.techindicators import TechIndicators

class BaseAPI(abc.ABC):
    """
    alpha vantage base API deletator
    """
    def __init__(self):
        self.api = "EBTAWY5OM01VMCW5"
        self.output_format = "pandas"

    @abc.abstractmethod
    def plot(self, **kwargs):
        raise NotImplementedError

class TimeSeriesAPI(BaseAPI):
    """
    This TimeSeries API is for demo use only.
    """
    def __init__(self):
        super(TimeSeriesAPI, self).__init__()
        self.ts = TimeSeries(key=self.api, output_format=self.output_format)

    def get_intraday(self, symbol, interval="15min", outputsize="full"):
        return self.ts.get_intraday(symbol, interval=interval, outputsize=outputsize)

    def plot(self, **kwargs):
        symbol = kwargs.get('symbol')
        data, meta_data = self.get_intraday(symbol)
        data['4. close'].plot()
        plt.title('Intraday Times Series for the AAPL stock (15 min)')
        plt.show()


class TechIndicatorsAPI(BaseAPI):
    """
    aaa
    """
    def __init__(self):
        super(TechIndicatorsAPI, self).__init__()
        self.ti = TechIndicators(key=self.api, output_format=self.output_format)

    def get_sma(self, symbol, interval="daily", time_period=20, series_type="close"):
        return self.ti.get_sma(symbol, interval=interval, time_period=time_period, series_type=series_type)

    def plot(self, **kwargs):
        symbol = kwargs.get('symbol')
        data, meta_data = self.get_sma(symbol)
        data.plot()
        plt.title('SMA for the AAPL stock (15 min)')
        plt.show()
        

if __name__ == "__main__":
    time_series = TimeSeriesAPI()
    time_series.plot(symbol="AAPL")