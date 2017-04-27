# rolldice.py  in PyGo\PyFTR
# This is the experimental model for integrating a stock distribution, designed as 
# a basis for our own version of an options pricing model, including the Aruba model.
# Code is arranged here in order to teach or explain the logical steps taken.
# Designed in Python 2.7.11 for Econ 136
# First edition dated March 1, 2017   Professor Gary R. Evans
# This is version 1.3, dated March 8, 2017
#
import math
import numpy as np
import matplotlib.pyplot as plt
#
# Establish the testing values of our stock price (stp), strike price (strike), drift (alpha)
# and volatility (sigma). 
#
stp = float(80.0)
days = float(1.0)
alpha = float(0.00)
sigma = float(0.10)
#
# Normally we would call our SN cumulative density function from our library, but it is written 
# here so others can see what we are doing. We are using the version that draws upon the Gaussian
# error function, which is an unusual but fruitful approach. This will be used below.
# 
def csnd(point):
	return (1.0 + math.erf(point/math.sqrt(2.0)))/2.0
#
# An elementary function for calculating the stock price adjusted for drift (alpha).
#
def drift(alpha,time):
	return 1.0*math.exp(alpha*time)
#
# An elementary multiplier function for converting daily volatility to duration volatility.
#
def durvol(time):
	return 1.0*math.sqrt(time)
#
# An elementary price expected-mean-value adjustment multiplier for log distributed prices.
# The mean of a log-distributed pdf is adjusted by minus one-half variance.
#
def lnmeanshift(sigma):
	return 1.0*math.exp(-1.0*(sigma*sigma/2))
#
# Adjust the stock price for drift. If drift is not desired, set the alpha above to zero, don't override this.
#
print "Stock price before drift:", stp
stp = stp*drift(alpha,days)
print "Stock price adjusted for drift: ", stp
#
# Adjust the daily volatility for duration volatility. If the adjustment is unneccesary, set days to zero.
#
print "Sigma before adjustment: ", sigma
sigma = sigma*durvol(days)
print "Sigma after duration adjustment: ", sigma
#
# Establish the array of Bin values as a series of multiples of standard deviations
# The centered-on-zero load array is appropriate (although it doesn't really matter).
# Assuming symmetry, the binnumbers (num) will equal 2 X abs(deviation) X # of intervals + 1 e.g.(4.25*2*2+1)= 18
#
binborder = np.linspace(-4.25, 4.25, num=18, dtype=float)
size = len(binborder)
#print "Number of bins:", size - 1
#
# Given the stock price (stp) and sigma above, establish an array to associate a stock 
# value (binprice) with each binborder. Then establish an array of integrated probabilities 
# for each bin edge (binedgeprob) integrating from minus infinity to the sigma multiples. 
#
binprice = np.zeros(size)
binedgeprob = np.zeros(size) 
for i in range(0,size):
	binprice[i] = stp*math.exp(binborder[i]*sigma)
	binedgeprob[i] = csnd(binborder[i])
#
# Now calculate the bin (spread) probabilities.
# Then calculate a mid-price bin value for each bin (COMPLICATED - source of major error if done wrong).
# Look carefully at the adjusted binmidprice formula and see that we are not using the average of the two edge prices.
# Then multiply binmidprice times the equivalent binprob to get the value of each bin.
# Check/debug results by summing stepwise and in total.
#
size = size - 1
binprob = np.zeros(size)
binmidprice = np.zeros(size)
binvalue = np.zeros(size)
#
for i in range(0,size):
	#print
        # probability that the stock price lands in this bin at expiry
	binprob[i] = binedgeprob[i+1] - binedgeprob[i]

        # price that this bin represents
	binmidprice[i] = stp*math.exp(((binborder[i+1]+binborder[i])/2.0)*sigma)
	#print "Probability range:", binborder[i], "to" , binborder[i+1]
	#print "Bin edge prices (no adjustment): ", "%.3f" % binprice[i], "to ", "%.4f" % binprice[i+1]
	#print "Binmidprice unadjusted: ", "%.4f" % binmidprice[i]

        # adjust for non-linearity
	binmidprice[i] = (stp*math.exp(((binborder[i+1]+binborder[i])/2.0)*sigma))*lnmeanshift(sigma)
	#print "Binmidprice adjusted for half variance:", "%.3f" % binmidprice [i]

        # calculate bin values
	binvalue[i] = binmidprice[i]*binprob[i]
	#print "Probability of being in this range: ", "%.5f" % binprob[i]
	#print "Sum of probabilities to here:", "%.5f" % np.sum(binprob[0:(i+1)])
	#print "Binvalue:", binvalue[i]
	#print "Sum (itergration) to this point:", np.sum(binvalue[0:(i+1)])

# estimate price of call with this price
callstrike = 84.0
callpr = 0.0
itm_value = 0.0
for i in range(size):
    if binprice[i+1] > callstrike:
        mul = 1.0
        if binprice[i] < callstrike:
            mul = (binprice[i+1] - callstrike)/(binprice[i+1] - binprice[i])
        callpr += mul * (binvalue[i] - callstrike * binprob[i])
        itm_value += mul * binvalue[i]

print
print "Estimated value of a",callstrike,"call:",callpr
print "Value of ITM portion of stock distribution (call):",itm_value
print "Value of OTM portion of stock distribution (call):",stp - itm_value

# estimate the value of a put with this strike price
putstrike = 77.0
putpr = 0.0
itm_value = 0.0
for i in range(size)[::-1]:
    if binprice[i] < putstrike:
        mul = 1.0
        if binprice[i+1] > putstrike:
            mul = (putstrike - binprice[i])/(binprice[i+1] - binprice[i])
        putpr += mul * (putstrike * binprob[i] - binvalue[i])
        itm_value += mul * binvalue[i]

print
print "Estimated value a",putstrike,"put:",putpr
print "Value of ITM portion of stock distribution (put):",itm_value
print "Value of OTM portion of stock distribution (put):",stp - itm_value
