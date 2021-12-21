import math
import re
import sys
from collections import defaultdict
import copy
import requests
import datetime
from datetime import datetime, timedelta
import pickle
from dateutil.relativedelta import relativedelta


SVK_URL = 'http://www.svk.se/ControlRoom/GetProductionHistory/?productionDate={date}&countryCode={zoneKey}'

STATTNET_TIMESTAMP_URL = 'https://driftsdata.statnett.no/restapi/physicalflowmap/gettimestamp?price=1'
STATTNET_PRICE_URL = 'https://driftsdata.statnett.no/restapi/physicalflowmap/getprice?ticks={timestamp}'
def main():

    url_ts = STATTNET_TIMESTAMP_URL
    ts_data = requests.get(url_ts).json()
    url_price = STATTNET_PRICE_URL.format(timestamp=ts_data)
    price_data = requests.get(url_price).json()

    prices={}
    for price in price_data:
        prices[price["elspot"]]=price["price"]

    print(ts_data)
    print(prices)

    start_time = datetime.strptime("2020-08-01", "%Y-%m-%d")
    cur_time=start_time

    MAPPING = {
        2: 'nuclear',
        4: 'unknown',
        5: 'wind',
        6: 'unknown',
        1: None,
        7: None,
        3: 'hydro'
    }

    for m in range(3):
        all_days=[]
        while (cur_time)<(start_time + relativedelta(months=m+1)):
            print(cur_time)
            timestr=cur_time.strftime("%Y-%m-%d")
            url = SVK_URL.format(date=timestr, zoneKey='SE')
            data = requests.get(url).json()
            named_data={}
            for d in data:
                name=MAPPING[d["name"]]
                named_data[name]=d["data"]
            all_days.append((timestr,named_data))
            cur_time+=timedelta(days=1)

        month_str=(cur_time-relativedelta(months=1)).strftime("%Y-%m")
        print("finnished month:"+month_str)
        PIK = "el_dataslack/production%s.dat"%month_str
        with open(PIK, "wb") as f:
            pickle.dump(all_days, f)


if __name__ =="__main__":
    main()
