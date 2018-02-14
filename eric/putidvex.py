# This is the IDV model for puts only.
# This is a modified version that calculates spreads like the call model.
# This accepts interest rates.
# Designed in Python 2.7.11 for Econ 136
# Dated February 16, 2016   Gary Evans
#

import math
import time
from datetime import date

stosym = "CSCO"
exmonth = int(2)
exday = int(17)
stopr = float(31.95)
strike = float(31.5)
putBid = float(0.35)
putAsk = float(0.36)
rfir = float (0.0025)

# Initialize key variables below
daystd = int(1)
pidv = float(0.0)
d1 = float(0.0)
durvol = float(0.0)
cumd1 = float(0.0)
cumd2 = float(0.0)
discount = float(0.0)
count = int(0.0)
newpp = float (0.0)
temppp = float(0.0)
timedecay = float (0.0)
tdprice = float (0.0)
putpr = float(0.0)

# Calculating strike value (PEG)
spread = putAsk - putBid
putpr = putBid + ((0.6)*spread)

# Calculating days to expiry:
#tnow = date.today()
tnow = date(2017, 2, 13)
expiry = date(tnow.year, exmonth, exday)
days2expiry = abs(expiry - tnow)
days = int(days2expiry.days)

#  This is how you calc the standard normal dist in Py for dval
def csnd(dval):
	return (1.0 + math.erf(dval/math.sqrt(2.0)))/2.0

# itteratively find put volatility
while temppp < putpr:
	pidv = pidv + 0.00001
	d1 = math.log(stopr/strike)+((rfir/365)+(pidv**2)/2)*days
	durvol = pidv*math.sqrt(days)
	cumd1 = csnd(-d1/durvol)
	cumd2 = csnd(-(d1/durvol - durvol))
	discount = math.exp(-rfir*days/365)
	temppp = -(stopr*cumd1)+(strike*discount*cumd2)

# Below we calculate one day time decay using our new value for volatility
# NOTE: This has a bug. If expiration is tomorrow, this tries to divide by zero!
days = days - daystd
d1 = math.log(stopr/strike)+((rfir/365)+(pidv**2)/2)*days
durvol = pidv*math.sqrt(days)
cumd1 = csnd(-d1/durvol)
cumd2 = csnd(-(d1/durvol - durvol))
discount = math.exp(-rfir*days/365)
newpp = -(stopr*cumd1)+(strike*discount*cumd2)
timedecay = putpr - newpp	


print ""
print "Date: ", tnow.strftime("%a %b %d %Y")
print "PUT" , stosym , expiry.strftime("%b %d")
print "Stock price: ", "%.3f" % stopr
print "Strike price: ", "%.2f" % strike
print "Days to expiry: ", days2expiry.days	
print "Put ASK: ", "%.3f" % putAsk
print "Put BID: ", "%.3f" % putBid
print "Put price (PEG): ", "%.3f" % putpr
print "The Delta:", "%.5f" % cumd1
print "One day time decay:", "%.3f" % timedecay
print "The put's implied probability: ", "%.5f" % pidv

#




