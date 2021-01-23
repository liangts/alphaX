import abc
from numpy.lib.arraysetops import isin
import pandas as pd
import matplotlib.pyplot as plt
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.foreignexchange import ForeignExchange
from alpha_vantage.fundamentaldata import FundamentalData
from alpha_vantage.techindicators import TechIndicators

class APICollections:
    """
    Save all APIs here.
    """

    def __init__(self) -> None:
        self.alpha_vantage_api = "EBTAWY5OM01VMCW5"

class BaseAPI(abc.ABC):
    """
    alpha vantage base API deletator
    """
    def __init__(self):
        self.api = "EBTAWY5OM01VMCW5"
        self.output_format = "pandas"

    @abc.abstractmethod
    def plot(self, **kwargs):
        title = kwargs.get('title')
        df = kwargs.get('df')
        cols = kwargs.get('cols')
        df[cols].plot()
        plt.title(title)
        plt.show()

    @abc.abstractmethod
    def api_delegation(self, func_name, **kwargs):
        """Pass the original API func to execute."""
        if isinstance(self, TimeSeriesAPI):
            obj = TimeSeries(key=self.api, output_format=self.output_format)
            func = getattr(obj, func_name)
            return func(**kwargs)
        if isinstance(self, ForeignExchangeAPI):
            obj = ForeignExchange(key=self.api, output_format=self.output_format)
            func = getattr(obj, func_name)
            return func(**kwargs)
        if isinstance(self, FundamentalDataAPI):
            obj = FundamentalData(key=self.api, output_format=self.output_format)
            func = getattr(obj, func_name)
            return func(**kwargs)
        if isinstance(self, TechIndicatorsAPI):
            obj = TechIndicators(key=self.api, output_format=self.output_format)
            func = getattr(obj, func_name)
            return func(**kwargs)

class TimeSeriesAPI(BaseAPI):
    """
    This TimeSeries API is for demo use only.
    """
    def __init__(self):
        super(TimeSeriesAPI, self).__init__()
        self.ts = TimeSeries(key=self.api, output_format=self.output_format)

    def get_intraday(self, symbol, interval="15min", outputsize="full"):
        return self.ts.get_intraday(symbol, interval=interval, outputsize=outputsize)

    def get_daily(self, symbol):
        return self.ts.get_daily(symbol=symbol)

    def get_daily_adjusted(self, symbol):
        return self.ts.get_daily_adjusted(symbol=symbol)

    def plot(self, **kwargs):
        symbol = kwargs.get('symbol')
        data, meta_data = self.get_intraday(symbol)
        data['4. close'].plot()
        plt.title('Intraday Times Series for the AAPL stock (15 min)')
        plt.show()

    def api_delegation(self, func_name, **kwargs):
        return super().api_delegation(func_name, **kwargs)

class FundamentalDataAPI(BaseAPI):
    """

    xxx
    """
    def __init__(self):
        super(FundamentalDataAPI, self).__init__()
        self.fd = FundamentalData(key=self.api, output_format=self.output_format)

    def get_company_overview(self, symbol):
        return self.fd.get_company_overview(symbol)

    def get_earnings(self, symbol):
        return self.fd.get_income_statement_quarterly(symbol)

    def plot(self, **kwargs):
        return super().plot(**kwargs)

    def api_delegation(self, func_name, **kwargs):
        return super().api_delegation(func_name, **kwargs)


class TechIndicatorsAPI(BaseAPI):
    """
    Get Technical indicator.

    Keyword Arguments:
        symbol:  the symbol for the equity we want to get its data
        interval:  time interval between two conscutive values,
            supported values are '1min', '5min', '15min', '30min', '60min', 'daily',
            'weekly', 'monthly' (default 'daily')
        time_period:  How many data points to average (default 20)
        series_type:  The desired price type in the time series. Four types
            are supported: 'close', 'open', 'high', 'low' (default 'close')
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

    def api_delegation(self, func_name, **kwargs):
        return super().api_delegation(func_name, **kwargs)

class ForeignExchangeAPI(BaseAPI):
    """
    API for ForeignExchange Data
    """
    def __init__(self):
        super(ForeignExchangeAPI, self).__init__()
        self.fe = ForeignExchange(key=self.api, output_format=self.output_format)

    def get_intraday(self, from_symbol, to_symbol, interval='15min', outputsize='compact'):
        return self.fe.get_currency_exchange_intraday(from_symbol, to_symbol, interval=interval, outputsize=outputsize)

    def get_exchange_rate(self, from_currency, to_currency):
        return self.fe.get_currency_exchange_rate(from_currency, to_currency)

    def plot(self, **kwargs):
        from_symbol = kwargs.get('from_symbol')
        to_symbol = kwargs.get('to_symbol')
        data, meta_data = self.get_intraday(from_symbol, to_symbol)
        data['4. close'].plot()
        plt.show()

    def api_delegation(self, func_name, **kwargs):
        return super().api_delegation(func_name, **kwargs)

        

if __name__ == "__main__":
    time_series = TimeSeriesAPI()
    time_series.plot(symbol="AAPL")