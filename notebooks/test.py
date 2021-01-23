from alphax.src.api.base import TimeSeriesAPI, FundamentalDataAPI, ForeignExchangeAPI
import sys

print(sys.path)

ts = TimeSeriesAPI()
fd = FundamentalDataAPI()
fe = ForeignExchangeAPI()

# data = fd.get_earnings("BILI")

# fe_rate = fe.get_exchange_rate("USD", "CNY")


# ts.plot(symbol="AAPL")

usd_idx, meta_data = ts.get_daily_adjusted("^DXY")

print(usd_idx)
