from alphax.src.api.base import TimeSeriesAPI, FundamentalDataAPI, ForeignExchangeAPI
import sys

print(sys.path)

ts = TimeSeriesAPI()
fd = FundamentalDataAPI()
fe = ForeignExchangeAPI()

#data = fd.get_earnings("BILI")

fe_rate = fe.get_exchange_rate("USD", "CNY")

print(fe_rate)
# ts.plot(symbol="AAPL")