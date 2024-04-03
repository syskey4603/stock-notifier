import time
import yfinance as yf
import warnings
from plyer import notification


averageprice = 0
warnings.filterwarnings('ignore', category=FutureWarning)

while True:
    reliance_stock = yf.Ticker("RELIANCE.NS")
    for x in range(10):
        price = reliance_stock.history(period="10d")["Close"][x]
        print(f"The 10d price of Reliance stock is: {price}")
        averageprice += price
    averageprice += price/10
    print(f"the average price of reliance in the past 10 days is " + str(averageprice))
    currentprice = reliance_stock.history(period="1d")["Close"][0]
    if(currentprice < 2930):
        notification.notify(
        title = "Reliance price",
        message = "Reliance price is currently " + str(currentprice),
        timeout = 10
        )
    time.sleep(300)
