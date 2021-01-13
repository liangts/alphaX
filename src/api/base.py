import abc
import pandas as pd
from alpha_vantage.timeseries import TimeSeries

class BaseAPI(abc.ABC):
    """
    alpha vantage base API deletator
    """
    def __init__(self):
        self.api = "EBTAWY5OM01VMCW5"
        self.output_format = "pandas"

class TimeSeriesAPI(BaseAPI):
    def __init__(self):
        super(TimeSeriesAPI, self).__init__()
        self.ts = TimeSeries(key=self.api, output_format=self.output_format)

    def get_intraday(self, symbol):
        return self.ts.get_intraday(symbol)
        
    

if __name__ == "__main__":
    time_series = TimeSeriesAPI()
    aapl_data, aapl_metadata = time_series.get_intraday('AAPL')

    print(aapl_metadata)
    print(aapl_data)