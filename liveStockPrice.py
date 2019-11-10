# we import the Twilio client from the dependency we just installed
from twilio.rest import Client
from yahoo_fin.stock_info import *
from datetime import datetime

nowPrice = (round(get_live_price('nio'), 2))

# the following line needs your Twilio Account SID and Auth Token
client = Client("AC304a451807ceb0e80b56526c2505957e", "ebb4c1fd3a8b95e18df02c31d96d37de")

output = ("current price: " + str(nowPrice))
print(output)
# to = my number | from_ = twilio number
client.messages.create(to="+18477906048",
                       from_="+18706690817",
                       body=output)

print(datetime.now())



