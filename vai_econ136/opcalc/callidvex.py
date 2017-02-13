# callidvex.py (modified from callidv) in PyGo\PyFi
# This is the IDV model for calls only, modified on Feb 2 2016 to calculate days to expiry.
# This accepts interest rates.
# Designed in Python 2.7.11 for Econ 136
# Dated February 16, 2016   Gary Evans
#
import math
import time
from datetime import date
stosym = "FB"
exmonth = int(2)
exday = int (3)
stopr = float(131.88)
strike = float(133.00)
callBid = float(2.81)
callAsk = float(2.84)
rfir = float (0.0025)
#
#  Initialize key variables below
daystd = int(1)
cipd = float(0.00)
d1 = float(0.0)
durvol = float(0.0)
cumd1 = float(0.0)
cumd2 = float(0.0)
newcp = float (0.0)
tempcp = float(0.0)
timedecay = float (0.0)
tdprice = float (0.0)
callpr = float(0.0)
#
# Calculating strike value (PEG)
spread = callAsk - callBid
callpr = callBid + ((0.6)*spread)
# Calculating days to expiry:
tnow = date.today()
expiry = date(tnow.year, exmonth, exday)
days2expiry = abs(expiry - tnow)
days = int(days2expiry.days)
#  This is how you calc the standard normal dist in Py for dval
def csnd(dval):
	return (1.0 + math.erf(dval/math.sqrt(2.0)))/2.0
#
#   Below we calculate implied daily volatility
#
while tempcp < callpr:
	cipd = cipd + 0.00001
	d1 = math.log(stopr/strike)+((rfir/365)+(cipd**2)/2)*days
	durvol = cipd*math.sqrt(days)
	cumd1 = csnd(d1/durvol)
	cumd2 = csnd((d1/durvol) - durvol)
	discount = math.exp(-rfir*days/365)
	tempcp = (stopr*cumd1)-(strike*discount*cumd2)
#
#	Below we calculate one day time decay using our new value for volatility
#   BUG: This won't work if there is only one day left!! Found this on the MSFT call!!
#
days = days - daystd
d1 = math.log(stopr/strike)+((rfir/365)+(cipd**2)/2)*days
durvol = cipd*math.sqrt(days)
cumd1 = csnd(d1/durvol)
cumd2 = csnd((d1/durvol) - durvol)
discount = math.exp(-rfir*days/365)
newcp = (stopr*cumd1)-(strike*discount*cumd2)
timedecay = callpr - newcp
#
#	Print output below
#
print ""
print "Date: ", tnow.strftime("%a %b %d %Y")
# print "Date: ", str(tnow)
print "CALL" , stosym , expiry.strftime("%b %d")
print "Stock price: ", "%.3f" % stopr
print "Strike price: ", "%.2f" % strike
# print "Expiry date; :", expiry
print "Days to expiry: ", days2expiry.days
print "Call ASK: ", "%.3f" % callAsk
print "Call BID: ", "%.3f" % callBid
print "Call price (PEG): ", "%.3f" % callpr
# print "durvol:", "%.4f" % durvol
# print "cumd2:", "%.4f" % cumd2
# print "discount", "%.4f" % discount
# print "tempcp:", "%.4f" % tempcp
print "The Delta:", "%.4f" % cumd1
print "One day time decay:", "%.3f" % timedecay
print "The call's implied probability: ", "%.5f" % cipd
