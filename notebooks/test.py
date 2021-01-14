from alphax.src.api.base import TimeSeriesAPI, FundamentalDataAPI
import sys

print(sys.path)

ts = TimeSeriesAPI()
fd = FundamentalDataAPI()

data = fd.get_earnings("BILI")

print(data)
# ts.plot(symbol="AAPL")