# copm.py in PyGo\PyFTr
# This is the original call options pricing model based upon the Excel model.
# This requires that you provide the volatility and the model 
# calculates the options price. This model uses daily volatility.
# Designed in Python 2.7.11 for Econ 136
# Version P1.0 dated February 18, 2016   Gary Evans
# Tested briefly in early February 2017.
# Note to students: this version was only nominally tested when released.
# All time/date calculations have been disabled but they have been tested
# and do work.
# The default version of this takes today's date and the expiry and calculate
# days to maturity.
# That feature can be re-enabled by reinstating the commented lines affected
# below. It should work.

import math
import time
from datetime import date

stosym = "CSCO"
exmonth = int(2)
exday = int (17)
stopr = float(31.95)
strike = float(31.5)
dayvol = float(0.01037)
rfir = float (0.0025)

#  Initialize key variables below
daystd = int(1)
cipd = float(0.00)
d1 = float(0.0)
durvol = float(0.0)
cumd1 = float(0.0)
cumd2 = float(0.0)
newcp = float (0.0)
tdprice = float(0.0)
callpr = float(0.0)


# Calculating days to expiry (suspended for testing, this part already tested):
#tnow = date.today()
tnow = date(2017, 2, 13)
expiry = date(tnow.year, exmonth, exday)
days2expiry = abs(expiry - tnow)
days = int(days2expiry.days)
#  This is how you calc the standard normal dist in Py for dval
def csnd(dval):
	return (1.0 + math.erf(dval/math.sqrt(2.0)))/2.0
	
#   Below we calculate the call option price
d1 = math.log(stopr/strike)+((rfir/365)+(dayvol**2)/2)*days
durvol = dayvol*math.sqrt(days)
cumd1 = csnd(-d1/durvol)
cumd2 = csnd(-(d1/durvol - durvol))
discount = math.exp(-rfir*days/365)
callpr = -(stopr*cumd1) + (strike*discount*cumd2)

# Below we calculate one day time decay using our new value for volatility
# Not done in this version.
# Print output below
print ""
print "Date: ", tnow.strftime("%a %b %d %Y")
print "CALL" , stosym , expiry.strftime("%b %d")
print "Stock price: ", "%.3f" % stopr
print "Call strike price: ", "%.2f" % strike
print "Historical daily volatility: ", "%.5f" % dayvol
print "Duration volatility: ", "%.5f" % durvol
print "Days to expiry: ", days2expiry.days	
print "durvol:", "%.4f" % durvol
print "cumd2:", "%.4f" % cumd2
print "discount", "%.4f" % discount
print "The Delta:", "%.4f" % cumd1
print "Call option price: ", "%.2f" % callpr





