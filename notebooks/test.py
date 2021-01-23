from alphax.src.api.base import BaseAPI, TimeSeriesAPI, FundamentalDataAPI, ForeignExchangeAPI
import sys

print(sys.path)

ts = TimeSeriesAPI()
# fd = FundamentalDataAPI()
# fe = ForeignExchangeAPI()


aapl_daily_ts = ts.api_delegation("get_intraday", symbol="AAPL")
print(aapl_daily_ts)